MCP Server to interact with a SuzieQ network observability instance via its REST API.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/suzieq-mcp](https://hub.docker.com/repository/docker/mcp/suzieq-mcp)
**Author**|[PovedaAqui](https://github.com/PovedaAqui)
**Repository**|https://github.com/PovedaAqui/suzieq-mcp

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`run_suzieq_show`|Runs a SuzieQ 'show' query via its REST API.|
`run_suzieq_summarize`|Runs a SuzieQ 'summarize' query via its REST API.|

---
## Tools Details

#### Tool: **`run_suzieq_show`**
Runs a SuzieQ 'show' query via its REST API.
Parameters|Type|Description
-|-|-
`table`|`string`|The name of the SuzieQ table to query (e.g., 'device', 'bgp', 'interface', 'route').
`filters`|`string` *optional*|An optional dictionary of filter parameters for the SuzieQ query

---
#### Tool: **`run_suzieq_summarize`**
Runs a SuzieQ 'summarize' query via its REST API.
Parameters|Type|Description
-|-|-
`table`|`string`|The name of the SuzieQ table to summarize (e.g., 'device', 'bgp', 'interface', 'route').
`filters`|`string` *optional*|An optional dictionary of filter parameters for the SuzieQ query

---
