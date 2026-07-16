Transform natural language queries into GraphQL queries using an AI agent. Provides schema management, query validation, execution, and history tracking.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/text-to-graphql](https://hub.docker.com/repository/docker/mcp/text-to-graphql)
**Author**|[Arize-ai](https://github.com/Arize-ai)
**Repository**|https://github.com/Arize-ai/text-to-graphql-mcp

## Available Tools (5)
Tools provided by this Server|Short Description
-|-
`execute_graphql_query`|Execute a GraphQL query and optionally visualize the results|
`generate_graphql_query`|Generate a GraphQL query from natural language description|
`get_query_examples`|Get example queries to help users understand what they can ask for|
`get_query_history`|Retrieve the history of all queries|
`validate_graphql_query`|Validate and update a GraphQL query|

---
## Tools Details

#### Tool: **`execute_graphql_query`**
Execute a GraphQL query and optionally visualize the results
Parameters|Type|Description
-|-|-
`graphql_query`|`string`|The GraphQL query to execute
`history_id`|`string` *optional*|Optional history ID to update
`natural_language_query`|`string` *optional*|The original natural language query for context
`variables`|`string` *optional*|Optional variables for the GraphQL query

---
#### Tool: **`generate_graphql_query`**
Generate a GraphQL query from natural language description
Parameters|Type|Description
-|-|-
`query`|`string`|Natural language description of the desired GraphQL query
`history_id`|`string` *optional*|Optional history ID to associate with this query

---
#### Tool: **`get_query_examples`**
Get example queries to help users understand what they can ask for

Returns:
    JSON string containing example queries
#### Tool: **`get_query_history`**
Retrieve the history of all queries

Returns:
    JSON string containing all query history
#### Tool: **`validate_graphql_query`**
Validate and update a GraphQL query
Parameters|Type|Description
-|-|-
`graphql_query`|`string`|The GraphQL query to validate
`history_id`|`string` *optional*|Optional history ID to update
`natural_language_query`|`string` *optional*|The original natural language query for context

---

## Screenshots

![Text-to-GraphQL screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/text-to-graphql-1.gif)
