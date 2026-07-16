#!/usr/bin/env python3
"""Generate per-service detail docs (docs/<id>.md) for the plaiiin MCP catalog.

Content: Docker Hub's generated markdown per mcp/<name> image (intro, MCP info,
full tool list with per-tool parameter tables), cleaned of Hub boilerplate,
plus up to 3 screenshots scraped from each project's GitHub README (downloaded
into docs/img/, referenced by absolute raw URL). Also stamps index.json with a
detailURL per entry, and can emit bundled docs for the Bridge app's built-in
catalog (--builtin/--builtin-out).

Usage:
  python3 tools/generate_docs.py
  python3 tools/generate_docs.py --builtin <service-catalog.json> --builtin-out <dir>
"""
import argparse
import json
import pathlib
import re
import urllib.request

RAW_BASE = "https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/"
HUB_API = "https://hub.docker.com/v2/repositories/"
IMG_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".webp")
BADGE_HINTS = ("shields.io", "badge", "codecov", "travis", "opencollective", "colab")
DROP_SECTIONS = ("use this mcp server", "image building info")
MAX_SHOTS = 3
IMG_MD = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
IMG_HTML = re.compile(r"<img[^>]+src=[\"']([^\"']+)[\"']", re.I)

# Built-in ids whose image is NOT mcp/<x> (npm-wrapped or ghcr) -> Docker Hub doc name.
BUILTIN_HUB = {
    "filesystem": "filesystem",
    "memory": "memory",
    "sequential-thinking": "sequentialthinking",
    "github": "github",
    "tavily": "tavily",
    "firecrawl": "firecrawl",
    "context7": "context7",
}


def get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "plaiiin-mcp-catalog-gen"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def hub_description(hub_name):
    try:
        data = json.loads(get(HUB_API + f"mcp/{hub_name}/"))
    except Exception:
        return None
    desc = (data.get("full_description") or "").strip()
    return desc or None


def clean(md):
    """Drop the leading H1 (the sheet header owns the title), the Hub's
    'What is an MCP Server?' plug, and boilerplate sections."""
    out, skipping, seen_body = [], False, False
    for line in md.splitlines():
        s = line.strip()
        if s.startswith("# ") and not seen_body:
            continue
        if "[what is an mcp server?]" in s.lower():
            continue
        if s.startswith("## "):
            title = s[3:].strip().lower()
            skipping = any(title.startswith(d) for d in DROP_SECTIONS)
            if skipping:
                continue
        if skipping:
            continue
        if s:
            seen_body = True
        out.append(line)
    text = "\n".join(out).strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def github_slug(docs_url):
    m = re.match(r"https?://github\.com/([^/]+/[^/#?]+)", docs_url or "")
    return m.group(1).removesuffix(".git") if m else None


def readme_screenshots(slug):
    try:
        md = get(f"https://raw.githubusercontent.com/{slug}/HEAD/README.md").decode("utf-8", "replace")
    except Exception:
        return []
    shots = []
    for u in IMG_MD.findall(md) + IMG_HTML.findall(md):
        if not u.startswith("http"):
            u = f"https://raw.githubusercontent.com/{slug}/HEAD/" + u.lstrip("./")
        low = u.lower().split("?")[0]
        if not low.endswith(IMG_EXTS):
            continue
        if any(h in low for h in BADGE_HINTS):
            continue
        if u not in shots:
            shots.append(u)
        if len(shots) == MAX_SHOTS:
            break
    return shots


def fallback_doc(entry):
    """No Hub doc: a minimal but honest page from the catalog entry itself."""
    lines = [entry["description"], ""]
    if entry.get("secretKeys"):
        keys = ", ".join(f"`{k}`" for k in entry["secretKeys"])
        lines += ["## Setup", "", f"Requires: {keys}", ""]
    if entry.get("docsURL"):
        lines += [f"[Project documentation]({entry['docsURL']})", ""]
    return "\n".join(lines).strip()


def build_doc(entry, md_dir, img_dir):
    """Write <md_dir>/<id>.md. Returns 'hub' or 'fallback'."""
    image = entry.get("image") or ""
    hub_name = None
    if image.startswith("mcp/"):
        hub_name = image.split("/", 1)[1].split(":")[0]
    else:
        hub_name = BUILTIN_HUB.get(entry["id"])
    body = hub_description(hub_name) if hub_name else None
    kind = "hub" if body else "fallback"
    body = clean(body) if body else fallback_doc(entry)

    slug = github_slug(entry.get("docsURL"))
    shots = readme_screenshots(slug) if slug else []
    section = []
    for i, u in enumerate(shots, 1):
        ext = pathlib.Path(u.split("?")[0]).suffix or ".png"
        name = f"{entry['id']}-{i}{ext}"
        try:
            (img_dir / name).write_bytes(get(u))
        except Exception:
            continue
        section.append(f"![{entry['name']} screenshot {i}]({RAW_BASE}docs/img/{name})")
        section.append("")
    if section:
        body = body.rstrip() + "\n\n## Screenshots\n\n" + "\n".join(section)

    (md_dir / f"{entry['id']}.md").write_text(body.rstrip() + "\n", encoding="utf-8")
    return kind


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--builtin", help="path to the app's service-catalog.json")
    ap.add_argument("--builtin-out", help="output dir for bundled built-in docs")
    args = ap.parse_args()

    repo = pathlib.Path(__file__).resolve().parent.parent
    docs_dir = repo / "docs"
    img_dir = docs_dir / "img"
    docs_dir.mkdir(exist_ok=True)
    img_dir.mkdir(exist_ok=True)

    index_path = repo / "index.json"
    index = json.loads(index_path.read_text())
    fallbacks = []
    for entry in index:
        kind = build_doc(entry, docs_dir, img_dir)
        if kind == "fallback":
            fallbacks.append(entry["id"])
        entry["detailURL"] = f"{RAW_BASE}docs/{entry['id']}.md"
        print(f"  {entry['id']}: {kind}", flush=True)
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")
    print(f"remote: {len(index)} docs, {len(fallbacks)} fallbacks: {fallbacks}")

    if args.builtin and args.builtin_out:
        out = pathlib.Path(args.builtin_out)
        out.mkdir(parents=True, exist_ok=True)
        builtin = json.loads(pathlib.Path(args.builtin).read_text())
        bfall = []
        for entry in builtin:
            if build_doc(entry, out, img_dir) == "fallback":
                bfall.append(entry["id"])
            print(f"  [builtin] {entry['id']}", flush=True)
        print(f"builtin: {len(builtin)} docs, {len(bfall)} fallbacks: {bfall}")


if __name__ == "__main__":
    main()
