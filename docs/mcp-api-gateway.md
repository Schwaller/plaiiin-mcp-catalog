A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/api-gateway](https://hub.docker.com/repository/docker/mcp/api-gateway)
**Author**|[rflpazini](https://github.com/rflpazini)
**Repository**|https://github.com/rflpazini/mcp-api-gateway

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`execute_api`|Execute any API endpoint with custom parameters|
`get_api_info`|Get information about available APIs and their endpoints|

---
## Tools Details

#### Tool: **`execute_api`**
Execute any API endpoint with custom parameters
Parameters|Type|Description
-|-|-
`api_name`|`string`|Name of the API
`method`|`string`|
`path`|`string`|API endpoint path
`data`|`object` *optional*|Request body data
`headers`|`object` *optional*|Additional headers
`params`|`object` *optional*|Query parameters

---
#### Tool: **`get_api_info`**
Get information about available APIs and their endpoints
Parameters|Type|Description
-|-|-
`api_name`|`string` *optional*|Name of the API (optional, shows all if not provided)

---
