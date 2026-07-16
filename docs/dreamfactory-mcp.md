DreamFactory is a REST API generation platform with support for hundreds of data sources, including Microsoft SQL Server, MySQL, PostgreSQL, and MongoDB. The DreamFactory MCP Server makes it easy for users to securely interact with their data sources via an MCP client.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/df-mcp](https://hub.docker.com/repository/docker/mcp/df-mcp)
**Author**|[dreamfactorysoftware](https://github.com/dreamfactorysoftware)
**Repository**|https://github.com/dreamfactorysoftware/df-mcp

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`call-stored-function`|Call a stored function|
`call-stored-procedure`|Call a stored procedure|
`get-stored-functions`|Get stored functions available in the database|
`get-stored-procedures`|Get stored procedures available in the database|
`get-table-data`|Retrieve the data of a specific table|
`get-table-schema`|Retrieve the schema of a specific table|
`get-tables`|Get tables available in the database|
`list-tools`|List available tools|

---
## Tools Details

#### Tool: **`call-stored-function`**
Call a stored function
Parameters|Type|Description
-|-|-
`functionName`|`string`|

---
#### Tool: **`call-stored-procedure`**
Call a stored procedure
Parameters|Type|Description
-|-|-
`procedureName`|`string`|

---
#### Tool: **`get-stored-functions`**
Get stored functions available in the database
#### Tool: **`get-stored-procedures`**
Get stored procedures available in the database
#### Tool: **`get-table-data`**
Retrieve the data of a specific table
Parameters|Type|Description
-|-|-
`tableName`|`string`|
`continue`|`boolean` *optional*|In batch scenarios where supported, continue processing even after one action fails. Default behavior is to halt and return results up to the first point of failure.
`fields`|`array` *optional*|
`filter`|`string` *optional*|SQL-like filter to limit the records to retrieve.
`group`|`string` *optional*|Comma-delimited list of the fields used for grouping of filter results.
`limit`|`number` *optional*|Limit for pagination.
`offset`|`number` *optional*|Offset for pagination.
`order`|`string` *optional*|SQL-like order containing field and direction for filter results.
`related`|`string` *optional*|Comma-delimited list of related names to retrieve for each resource. (it will be found in the related field of the schema)

---
#### Tool: **`get-table-schema`**
Retrieve the schema of a specific table
Parameters|Type|Description
-|-|-
`tableName`|`string`|

---
#### Tool: **`get-tables`**
Get tables available in the database
#### Tool: **`list-tools`**
List available tools

## Screenshots

![DreamFactory screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/dreamfactory-mcp-1.png)

![DreamFactory screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/dreamfactory-mcp-2.png)

![DreamFactory screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/dreamfactory-mcp-3.png)
