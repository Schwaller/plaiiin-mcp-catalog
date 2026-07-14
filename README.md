# plaiiin MCP catalog

A catalog of Dockerized [Model Context Protocol](https://modelcontextprotocol.io) servers
for the **plaiiin AI Bridge**.

Each entry is generated from Docker's official
[`docker/mcp-registry`](https://github.com/docker/mcp-registry), and only servers whose
configuration fits the Bridge cleanly are included:

- **one-click** servers that need no configuration, and
- servers that need only **secret tokens** (each modelled as a Keychain-backed field).

Servers that require templated env/parameters, volumes, or that are remote-only are
intentionally excluded, so nothing here ships broken.

Every image was verified to exist on Docker Hub at generation time.

## Use it

In the Bridge: **Services → Add a Service → Sources… → Add**, then point it at this
repo's URL. The Bridge fetches this `index.json`, and its entries appear in the catalog
browser alongside the built-in ones.

Remote catalog content is untrusted by design: entries are never auto-enabled, any folder
mount is forced read-only, and every add is re-validated locally before it can run.
