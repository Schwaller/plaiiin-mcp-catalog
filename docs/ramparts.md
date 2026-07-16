A comprehensive security scanner for MCP servers with YARA rules and static analysis capabilities.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/ramparts](https://hub.docker.com/repository/docker/mcp/ramparts)
**Author**|[getjavelin](https://github.com/getjavelin)
**Repository**|https://github.com/getjavelin/ramparts

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`scan`|Scan an MCP server URL and return security findings as JSON|
`scan-config`|Scan MCP servers from IDE configuration files and return results as JSON|

---
## Tools Details

#### Tool: **`scan`**
Scan an MCP server URL and return security findings as JSON
Parameters|Type|Description
-|-|-
`url`|`string`|
`auth_headers`|`object` *optional*|
`detailed`|`boolean` *optional*|
`format`|`string` *optional*|
`httpTimeout`|`integer` *optional*|
`returnPrompts`|`boolean` *optional*|If true, do not call the LLM; return prompts instead
`timeout`|`integer` *optional*|

---
#### Tool: **`scan-config`**
Scan MCP servers from IDE configuration files and return results as JSON
Parameters|Type|Description
-|-|-
`auth_headers`|`object` *optional*|
`detailed`|`boolean` *optional*|
`format`|`string` *optional*|
`httpTimeout`|`integer` *optional*|
`returnPrompts`|`boolean` *optional*|If true, do not call the LLM; return prompts instead
`timeout`|`integer` *optional*|

---

## Screenshots

![Ramparts Security Scanner screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/ramparts-1.png)
