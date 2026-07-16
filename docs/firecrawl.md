🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/firecrawl](https://hub.docker.com/repository/docker/mcp/firecrawl)
**Author**|[firecrawl](https://github.com/firecrawl)
**Repository**|https://github.com/mendableai/firecrawl-mcp-server

## Available Tools (26)
Tools provided by this Server|Short Description
-|-
`firecrawl_agent`|Start a research agent|
`firecrawl_agent_status`|Get agent job status|
`firecrawl_check_crawl_status`|Get crawl status|
`firecrawl_crawl`|Run a site crawl|
`firecrawl_extract`|Extract structured data|
`firecrawl_feedback`|Send feedback on a Firecrawl job|
`firecrawl_interact`|Interact with a scraped page|
`firecrawl_interact_stop`|Stop interact session|
`firecrawl_map`|Map a website|
`firecrawl_monitor_check`|Get monitor check|
`firecrawl_monitor_checks`|List monitor checks|
`firecrawl_monitor_create`|Create monitor|
`firecrawl_monitor_delete`|Delete monitor|
`firecrawl_monitor_get`|Get monitor|
`firecrawl_monitor_list`|List monitors|
`firecrawl_monitor_run`|Run monitor now|
`firecrawl_monitor_update`|Update monitor|
`firecrawl_parse`|Parse a local file|
`firecrawl_research_inspect_paper`|Inspect a paper|
`firecrawl_research_read_paper`|Read a paper|
`firecrawl_research_related_papers`|Find related arXiv papers|
`firecrawl_research_search_github`|Search GitHub history|
`firecrawl_research_search_papers`|Search research papers|
`firecrawl_scrape`|Scrape a URL|
`firecrawl_search`|Search the web|
`firecrawl_search_feedback`|Send feedback on a search result|

---
## Tools Details

#### Tool: **`firecrawl_agent`**
Autonomous web research agent. This is a separate AI agent layer that independently browses the internet, searches for information, navigates through pages, and extracts structured data based on your query. You describe what you need, and the agent figures out where to find it.

**How it works:** The agent performs web searches, follows links, reads pages, and gathers data autonomously. This runs **asynchronously** - it returns a job ID immediately, and you poll `firecrawl_agent_status` to check when complete and retrieve results.

**IMPORTANT - Async workflow with patient polling:**
1. Call `firecrawl_agent` with your prompt/schema → returns job ID immediately
2. Poll `firecrawl_agent_status` with the job ID to check progress
3. **Keep polling for at least 2-3 minutes** - agent research typically takes 1-5 minutes for complex queries
4. Poll every 15-30 seconds until status is "completed" or "failed"
5. Do NOT give up after just a few polling attempts - the agent needs time to research

**Expected wait times:**
- Simple queries with provided URLs: 30 seconds - 1 minute
- Complex research across multiple sites: 2-5 minutes
- Deep research tasks: 5+ minutes

**Best for:** Complex research tasks where you don't know the exact URLs; multi-source data gathering; finding information scattered across the web; extracting data from JavaScript-heavy SPAs that fail with regular scrape.
**Not recommended for:**
- Single-page extraction when you have a URL (use firecrawl_scrape, faster and cheaper)
- Web search (use firecrawl_search first)
- Interactive page tasks like clicking, filling forms, login, or navigating JS-heavy SPAs (use firecrawl_scrape + firecrawl_interact)
- Extracting specific data from a known page (use firecrawl_scrape with JSON format)

**Arguments:**
- prompt: Natural language description of the data you want (required, max 10,000 characters)
- urls: Optional array of URLs to focus the agent on specific pages
- schema: Optional JSON schema for structured output

**Prompt Example:** "Find the founders of Firecrawl and their backgrounds"
**Usage Example (start agent, then poll patiently for results):**
```json
{
  "name": "firecrawl_agent",
  "arguments": {
    "prompt": "Find the top 5 AI startups founded in 2024 and their funding amounts",
    "schema": {
      "type": "object",
      "properties": {
        "startups": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string" },
              "funding": { "type": "string" },
              "founded": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
```
Then poll with `firecrawl_agent_status` every 15-30 seconds for at least 2-3 minutes.

**Usage Example (with URLs - agent focuses on specific pages):**
```json
{
  "name": "firecrawl_agent",
  "arguments": {
    "urls": ["https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"],
    "prompt": "Compare the features and pricing information from these pages"
  }
}
```
**Returns:** Job ID for status checking. Use `firecrawl_agent_status` to poll for results.
Parameters|Type|Description
-|-|-
`prompt`|`string`|
`schema`|`object` *optional*|
`urls`|`array` *optional*|

*This tool interacts with external entities.*

---
#### Tool: **`firecrawl_agent_status`**
Check the status of an agent job and retrieve results when complete. Use this to poll for results after starting an agent with `firecrawl_agent`.

**IMPORTANT - Be patient with polling:**
- Poll every 15-30 seconds
- **Keep polling for at least 2-3 minutes** before considering the request failed
- Complex research can take 5+ minutes - do not give up early
- Only stop polling when status is "completed" or "failed"

**Usage Example:**
```json
{
  "name": "firecrawl_agent_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```
**Possible statuses:**
- processing: Agent is still researching - keep polling, do not give up
- completed: Research finished - response includes the extracted data
- failed: An error occurred (only stop polling on this status)

**Returns:** Status, progress, and results (if completed) of the agent job.
Parameters|Type|Description
-|-|-
`id`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`firecrawl_check_crawl_status`**
Check the status of a crawl job.

**Usage Example:**
```json
{
  "name": "firecrawl_check_crawl_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```
**Returns:** Status and progress of the crawl job, including results if available.
Parameters|Type|Description
-|-|-
`id`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`firecrawl_crawl`**
Starts a crawl job on a website, polls until it reaches a terminal state, and returns the final crawl status/data.

 **Best for:** Extracting content from multiple related pages, when you need comprehensive coverage.
 **Not recommended for:** Extracting content from a single page (use scrape); when token limits are a concern (use map + scrape for tighter control); when you need fast results (crawling can be slow).
 **Warning:** Crawl responses can be very large and may exceed token limits. Limit the crawl depth and number of pages, or use map + scrape for tighter control.
 **Common mistakes:** Setting limit or maxDiscoveryDepth too high (causes token overflow) or too low (causes missing pages); using crawl for a single page (use scrape instead). Using a /* wildcard is not recommended.
 **Prompt Example:** "Get all blog posts from the first two levels of example.com/blog."
 **Usage Example:**
 ```json
 {
   "name": "firecrawl_crawl",
   "arguments": {
     "url": "https://example.com/blog/*",
     "maxDiscoveryDepth": 5,
     "limit": 20,
     "allowExternalLinks": false,
     "deduplicateSimilarURLs": true,
     "sitemap": "include"
   }
 }
 ```
 **Returns:** Final crawl status and data after internal polling, including the crawl id. Use firecrawl_check_crawl_status only when you need to re-check an existing crawl ID later.
Parameters|Type|Description
-|-|-
`url`|`string`|
`allowExternalLinks`|`boolean` *optional*|
`allowSubdomains`|`boolean` *optional*|
`crawlEntireDomain`|`boolean` *optional*|
`deduplicateSimilarURLs`|`boolean` *optional*|
`delay`|`number` *optional*|
`excludePaths`|`array` *optional*|
`ignoreQueryParameters`|`boolean` *optional*|
`includePaths`|`array` *optional*|
`limit`|`number` *optional*|
`maxConcurrency`|`number` *optional*|
`maxDiscoveryDepth`|`number` *optional*|
`prompt`|`string` *optional*|
`scrapeOptions`|`object` *optional*|
`sitemap`|`string` *optional*|
`webhook`|`string` *optional*|
`webhookHeaders`|`object` *optional*|

*This tool interacts with external entities.*

---
#### Tool: **`firecrawl_extract`**
Extract structured information from web pages using LLM capabilities. Supports both cloud AI and self-hosted LLM extraction.

**Best for:** Extracting specific structured data like prices, names, details from web pages.
**Not recommended for:** When you need the full content of a page (use scrape); when you're not looking for specific structured data.
**Arguments:**
- urls: Array of URLs to extract information from
- prompt: Custom prompt for the LLM extraction
- schema: JSON schema for structured data extraction
- allowExternalLinks: Allow extraction from external links
- enableWebSearch: Enable web search for additional context
- includeSubdomains: Include subdomains in extraction
**Prompt Example:** "Extract the product name, price, and description from these product pages."
**Usage Example:**
```json
{
  "name": "firecrawl_extract",
  "arguments": {
    "urls": ["https://example.com/page1", "https://example.com/page2"],
    "prompt": "Extract product information including name, price, and description",
    "schema": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "price": { "type": "number" },
        "description": { "type": "string" }
      },
      "required": ["name", "price"]
    },
    "allowExternalLinks": false,
    "enableWebSearch": false,
    "includeSubdomains": false
  }
}
```
**Returns:** Extracted structured data as defined by your schema.
Parameters|Type|Description
-|-|-
`urls`|`array`|
`allowExternalLinks`|`boolean` *optional*|
`enableWebSearch`|`boolean` *optional*|
`includeSubdomains`|`boolean` *optional*|
`prompt`|`string` *optional*|
`schema`|`object` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`firecrawl_feedback`**
Send structured feedback for a completed Firecrawl v2 job. Use this for endpoint-level feedback on `scrape`, `parse`, `map`, or `search` jobs when the job result was useful, partially useful, or failed to meet expectations.

For search-result quality specifically, prefer `firecrawl_search_feedback` when available because it has search-focused guidance. This generic tool posts to `/v2/feedback` and accepts endpoint-wide signals:

- **endpoint** — one of `search`, `scrape`, `parse`, or `map`.
- **jobId** — the id returned by that endpoint.
- **rating** — overall result quality: `good`, `partial`, or `bad`.
- **issues** — stable lowercase issue codes such as `missing_markdown`, `bad_pdf_parse`, or `wrong_links`.
- **tags** — optional lowercase tags for grouping feedback.
- **note** — short human-readable context. Do not include huge page contents or raw scrape results.
- **url**, **pageNumbers**, and **metadata** — small contextual fields that identify what the feedback refers to.

Do not store multi-MB outputs in feedback. Use concise notes, issue codes, URLs, and page numbers.

**Returns:** `{ success, feedbackId, creditsRefunded, creditsRefundedToday?, dailyRefundCap?, dailyCapReached?, alreadySubmitted?, warning? }` JSON.
Parameters|Type|Description
-|-|-
`endpoint`|`string`|
`jobId`|`string`|
`rating`|`string`|
`issues`|`array` *optional*|
`metadata`|`object` *optional*|
`missingContent`|`array` *optional*|
`note`|`string` *optional*|
`pageNumbers`|`array` *optional*|
`querySuggestions`|`string` *optional*|
`tags`|`array` *optional*|
`url`|`string` *optional*|
`valuableSources`|`array` *optional*|

*This tool interacts with external entities.*

---
#### Tool: **`firecrawl_interact`**
Interact with a page in a live browser session: click buttons, fill forms, extract dynamic content, or navigate deeper.

**Best for:** Multi-step workflows on a single page — searching a site, clicking through results, filling forms, extracting data that requires interaction.
**Two ways to target a page:**
- Pass a `url` to interact directly. The session is opened for you in one call (use this for a fresh page).
- Pass a `scrapeId` from a previous firecrawl_scrape to reuse that already-loaded page (cheaper when you just scraped it).

**Arguments:**
- url: Page to interact with; opens a session for you (use this OR scrapeId)
- scrapeId: Scrape job ID from a previous scrape, found in its metadata (use this OR url)
- prompt: Natural language instruction describing the action to take (use this OR code)
- code: Code to execute in the browser session (use this OR prompt)
- language: "bash", "python", or "node" (optional, defaults to "node", only used with code)
- timeout: Interact execution timeout in seconds, 1-300 (optional, defaults to 30)
- scrapeOptions: Optional scrape controls used only with url mode, such as waitFor, maxAge, proxy, or zeroDataRetention

**Usage Example (prompt, direct via url):**
```json
{
  "name": "firecrawl_interact",
  "arguments": {
    "url": "https://example.com/products",
    "prompt": "Click on the first product and tell me its price"
  }
}
```

**Usage Example (code):**
```json
{
  "name": "firecrawl_interact",
  "arguments": {
    "scrapeId": "scrape-id-from-previous-scrape",
    "code": "agent-browser click @e5",
    "language": "bash"
  }
}
```
**Returns:** Execution result including output, stdout, stderr, exit code, and live view URLs.
Parameters|Type|Description
-|-|-
`code`|`string` *optional*|
`language`|`string` *optional*|
`prompt`|`string` *optional*|
`scrapeId`|`string` *optional*|
`scrapeOptions`|`object` *optional*|
`timeout`|`number` *optional*|
`url`|`string` *optional*|

*This tool interacts with external entities.*

---
#### Tool: **`firecrawl_interact_stop`**
Stop an interact session for a scraped page. Call this when you are done interacting to free resources.

**Usage Example:**
```json
{
  "name": "firecrawl_interact_stop",
  "arguments": {
    "scrapeId": "scrape-id-here"
  }
}
```
**Returns:** Success confirmation.
Parameters|Type|Description
-|-|-
`scrapeId`|`string`|

*This tool may perform destructive updates.*

---
#### Tool: **`firecrawl_map`**
Map a website to discover all indexed URLs on the site.

**Best for:** Discovering URLs on a website before deciding what to scrape; finding specific sections or pages within a large site; locating the correct page when scrape returns empty or incomplete results.
**Not recommended for:** When you already know which specific URL you need (use scrape); when you need the content of the pages (use scrape after mapping).
**Common mistakes:** Using crawl to discover URLs instead of map; jumping straight to firecrawl_agent when scrape fails instead of using map first to find the right page.

**IMPORTANT - Use map before agent:** If `firecrawl_scrape` returns empty, minimal, or irrelevant content, use `firecrawl_map` with the `search` parameter to find the specific page URL containing your target content. This is faster and cheaper than using `firecrawl_agent`. Only use the agent as a last resort after map+scrape fails.

**Prompt Example:** "Find the webhook documentation page on this API docs site."
**Usage Example (discover all URLs):**
```json
{
  "name": "firecrawl_map",
  "arguments": {
    "url": "https://example.com"
  }
}
```
**Usage Example (search for specific content - RECOMMENDED when scrape fails):**
```json
{
  "name": "firecrawl_map",
  "arguments": {
    "url": "https://docs.example.com/api",
    "search": "webhook events"
  }
}
```
**Returns:** Array of URLs found on the site, filtered by search query if provided.
Parameters|Type|Description
-|-|-
`url`|`string`|
`ignoreQueryParameters`|`boolean` *optional*|
`includeSubdomains`|`boolean` *optional*|
`limit`|`number` *optional*|
`search`|`string` *optional*|
`sitemap`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`firecrawl_monitor_check`**
Get a single check with page-level diff results. Filter `pageStatus` to surface only the pages that changed (or were new, removed, etc.).

Each entry in `data.pages[]` has `url`, `status` (`same` | `new` | `changed` | `removed` | `error`), optional `judgment` when goal-based judging ran, and — when changed — a `diff` and possibly a `snapshot`. The shape of `diff` depends on the monitor's `formats` configuration:

- **Markdown mode (default).** `diff.text` is the unified markdown diff; `diff.json` is a parse-diff AST (`{ files: [...] }`). No `snapshot`.
- **JSON mode** (`changeTracking` with `modes: ["json"]`). `diff.json` is a per-field map keyed by JSON path into the extraction, e.g. `plans[0].price`, with each value being `{ previous, current }`. `snapshot.json` is the full current extraction. No `diff.text`.
- **Mixed mode** (`modes: ["json", "git-diff"]`). Both `diff.text` (markdown sidecar) AND `diff.json` (per-field map) are present, plus `snapshot.json`.

**Example JSON-mode response `pages[]` entry:**

```json
{
  "url": "https://example.com/pricing",
  "status": "changed",
  "diff": {
    "json": {
      "plans[0].price":       { "previous": "$19/mo",        "current": "$24/mo" },
      "plans[1].features[2]": { "previous": "10 GB storage", "current": "25 GB storage" }
    }
  },
  "snapshot": { "json": { "plans": [/* current full extraction matching the monitor's schema */] } },
  "judgment": {
    "meaningful": true,
    "confidence": "high",
    "reason": "The pricing changed, which matches the monitor goal.",
    "meaningfulChanges": [
      {
        "type": "changed",
        "before": "$19/mo",
        "after": "$24/mo",
        "reason": "The tracked plan price changed."
      }
    ]
  }
}
```

When summarizing a check for the user, prefer `diff.json` paths (e.g. "plans[0].price changed from $19/mo to $24/mo") over re-printing the markdown diff — it's more concise and grounded in the schema fields they asked for.

When `judgment` is present, use it to decide what to surface. `judgment.meaningful: false` means the change was classified as noise for the monitor's goal. When `judgment.meaningfulChanges` is present, prefer those goal-relevant changes over raw diff hunks; each item includes `type`, `before`, `after`, and `reason`.

The endpoint paginates via a top-level `next` URL; this tool returns one page at a time. Increase `limit` (max 100) to fetch fewer pages.

**Usage Example:**
```json
{
  "name": "firecrawl_monitor_check",
  "arguments": {
    "id": "mon_abc123",
    "checkId": "chk_xyz",
    "pageStatus": "changed"
  }
}
```
Parameters|Type|Description
-|-|-
`checkId`|`string`|
`id`|`string`|
`limit`|`integer` *optional*|
`pageStatus`|`string` *optional*|
`skip`|`integer` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`firecrawl_monitor_checks`**
List historical checks for a monitor.

**Usage Example:**
```json
{ "name": "firecrawl_monitor_checks", "arguments": { "id": "mon_abc123", "limit": 10, "status": "completed" } }
```
Parameters|Type|Description
-|-|-
`id`|`string`|
`limit`|`integer` *optional*|
`offset`|`integer` *optional*|
`status`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`firecrawl_monitor_create`**
Create a Firecrawl monitor — a recurring scrape, crawl, or search that diffs each result against the last retained snapshot.

Prefer the simple path: pass `page` or `pages` plus `goal` to monitor specific URLs, OR pass `queries` plus `goal` to monitor web search results for new/changed hits. The tool will create the monitor with a 30-minute schedule and meaningful-change judging enabled by the API. Use `body` only for advanced requests such as crawl targets, JSON change tracking, custom retention, or manual `judgeEnabled` control.

Meaningful-change judge: set `goal` to a plain-language description of what the user actually cares about. `judgeEnabled` defaults to true when `goal` is set, so providing `goal` is enough. Page webhooks expose `isMeaningful` and `judgment` on `monitor.page` events.

Simple fields:
- `page`: one page URL to monitor.
- `pages`: multiple page URLs to monitor.
- `queries`: one or more search queries (1-12) to monitor instead of fixed URLs. Each check runs the searches and diffs the result set, so you get alerted when new or changed results appear. Mutually exclusive with `page`/`pages` in the simple path.
- `searchWindow`: optional recency window for search targets — one of `5m`, `15m`, `1h`, `6h`, `24h`, `7d` (default `24h`).
- `maxResults`: optional max results per search, 1-50 (default 10).
- `includeDomains` / `excludeDomains`: optional domain allow/deny lists for search targets.
- `goal`: plain-English instruction for what changes matter. Required for the simple path (and always required when `queries` are set — web monitors must have a goal).
- `scheduleText`: optional natural-language schedule, default `every 30 minutes`.
- `email`: optional email recipient for summaries.
- `webhookUrl`: optional webhook URL. Configures `monitor.page` and `monitor.check.completed`.

**Search-mode example:**

```json
{
  "name": "firecrawl_monitor_create",
  "arguments": {
    "queries": ["new LLM release", "frontier model launch"],
    "goal": "Notify me about major new LLM model releases.",
    "searchWindow": "24h",
    "maxResults": 10
  }
}
```

Goal guidance:
- Expand the user's one-line monitoring intent into a concise 2-3 sentence monitor goal.
- State what should trigger an alert, restate any scope the user gave, and include intent-specific exclusions only when obvious from the user's request.
- Generic noise such as whitespace, formatting-only changes, request IDs, tracking params, generic metadata, and unrelated page chrome is already handled by the judge; do not repeat it in every goal.
- If the user is vague, keep the goal broad rather than guessing exclusions. If the user asks for broad monitoring or "any change", preserve that and do not add exclusions that hide changes.
- If the user says they do not care about something, include that explicitly. It is okay to ask whether they want to ignore specific noise when it is likely to matter.
- Do not invent page-specific sections, thresholds, entities, or business rules unless the user mentioned them.

Query guidance (web monitors): `queries` control recall (what search retrieves) and `goal` controls precision (which results alert) — tune both.
- Write keywords, not sentences: `OpenAI new model release`, not `tell me when OpenAI releases a new model`.
- Quote multi-word entities (`"Llama 4"`); group synonyms with `OR` (`launch OR release OR announcement`).
- Keep each query tight (~2-6 terms). One broad query usually beats several narrow ones — extra queries split the `maxResults` budget. Use one query per distinct entity; do not emit one per facet of a single subject.
- Keep `site:` operators out of queries — use `includeDomains` / `excludeDomains`.
- A healthy web monitor mostly returns `new: 0` and alerts only on genuinely new, on-goal results. Many `ignored` results ⇒ queries too broad (tighten them); nothing for long stretches ⇒ queries too narrow or window too tight (broaden); dismissed alerts ⇒ goal too broad (add an intent-specific Ignore). Aim for high precision with enough recall.

Full `body` requests require: `name`, `schedule` (with `cron` or `text`), and `targets` (one or more `{ type: 'scrape', urls: [...] }`, `{ type: 'crawl', url: '...' }`, or `{ type: 'search', queries: [...], searchWindow?, maxResults?, includeDomains?, excludeDomains? }`). Optional: `goal` (required when any search target is present), `judgeEnabled`, `webhook`, `notification`, `retentionDays`.

**Markdown-mode (default):** Each check produces a unified text diff of the page's markdown. No extra configuration needed.

```json
{
  "name": "fir

[...]

## Screenshots

![Firecrawl screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/firecrawl-1.png)
