Official ClickHouse MCP Server.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/clickhouse](https://hub.docker.com/repository/docker/mcp/clickhouse)
**Author**|[ClickHouse](https://github.com/ClickHouse)
**Repository**|https://github.com/ClickHouse/mcp-clickhouse

## Available Tools (3)
Tools provided by this Server|Short Description
-|-
`list_databases`|List available ClickHouse databases|
`list_tables`|List available ClickHouse tables in a database, including schema, comment, row count, and column count.|
`run_select_query`|Run a SELECT query in a ClickHouse database|

---
## Tools Details

#### Tool: **`list_databases`**
List available ClickHouse databases
#### Tool: **`list_tables`**
List available ClickHouse tables in a database, including schema, comment,
row count, and column count.
Parameters|Type|Description
-|-|-
`database`|`string`|
`like`|`string` *optional*|
`not_like`|`string` *optional*|

---
#### Tool: **`run_select_query`**
Run a SELECT query in a ClickHouse database
Parameters|Type|Description
-|-|-
`query`|`string`|

---

## Screenshots

![Official ClickHouse screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/clickhouse-1.jpg)
