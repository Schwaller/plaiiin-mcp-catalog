A Python-based execution tool that mimics a Jupyter notebook environment. It accepts code snippets, executes them, and maintains state across sessions — preserving variables, imports, and past results. Ideal for iterative development, debugging, or code execution.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/mcp-code-interpreter](https://hub.docker.com/repository/docker/mcp/mcp-code-interpreter)
**Author**|[akuadane](https://github.com/akuadane)
**Repository**|https://github.com/akuadane/mcp-code-interpreter

## Available Tools (1)
Tools provided by this Server|Short Description
-|-
`execute_code`|Executes Python code within a persistent session, retaining past results (e.g., variables, imports).|

---
## Tools Details

#### Tool: **`execute_code`**
Executes Python code within a persistent session, retaining past results (e.g., variables, imports). Similar to a Jupyter notebook. A session_id is returned on first use and must be included in subsequent requests to maintain context.
Parameters|Type|Description
-|-|-
`code`|`string`|
`session_id`|`integer` *optional*|

---
