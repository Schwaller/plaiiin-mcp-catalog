OpenAPI Schema Model Context Protocol Server.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/openapi-schema](https://hub.docker.com/repository/docker/mcp/openapi-schema)
**Author**|[hannesj](https://github.com/hannesj)
**Repository**|https://github.com/hannesj/mcp-openapi-schema

## Available Tools (10)
Tools provided by this Server|Short Description
-|-
`get-component`|Gets detailed definition for a specific component|
`get-endpoint`|Gets detailed information about a specific API endpoint|
`get-examples`|Gets examples for a specific component or endpoint|
`get-path-parameters`|Gets the parameters for a specific path|
`get-request-body`|Gets the request body schema for a specific endpoint|
`get-response-schema`|Gets the response schema for a specific endpoint, method, and status code|
`list-components`|Lists all schema components (schemas, parameters, responses, etc.)|
`list-endpoints`|Lists all API paths and their HTTP methods with summaries, organized by path|
`list-security-schemes`|Lists all available security schemes|
`search-schema`|Searches across paths, operations, and schemas|

---
## Tools Details

#### Tool: **`get-component`**
Gets detailed definition for a specific component
Parameters|Type|Description
-|-|-
`name`|`string`|Component name
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file
`type`|`string`|Component type (e.g., schemas, parameters, responses)

---
#### Tool: **`get-endpoint`**
Gets detailed information about a specific API endpoint
Parameters|Type|Description
-|-|-
`method`|`string`|
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file
`path`|`string`|

---
#### Tool: **`get-examples`**
Gets examples for a specific component or endpoint
Parameters|Type|Description
-|-|-
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file
`type`|`string`|Type of example to retrieve
`componentName`|`string` *optional*|Component name (required for component examples)
`componentType`|`string` *optional*|Component type (required for component examples)
`method`|`string` *optional*|HTTP method (required for request/response examples)
`path`|`string` *optional*|API path (required for request/response examples)
`statusCode`|`string` *optional*|Status code (for response examples)

---
#### Tool: **`get-path-parameters`**
Gets the parameters for a specific path
Parameters|Type|Description
-|-|-
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file
`path`|`string`|
`method`|`string` *optional*|

---
#### Tool: **`get-request-body`**
Gets the request body schema for a specific endpoint
Parameters|Type|Description
-|-|-
`method`|`string`|
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file
`path`|`string`|

---
#### Tool: **`get-response-schema`**
Gets the response schema for a specific endpoint, method, and status code
Parameters|Type|Description
-|-|-
`method`|`string`|
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file
`path`|`string`|
`statusCode`|`string` *optional*|

---
#### Tool: **`list-components`**
Lists all schema components (schemas, parameters, responses, etc.)
Parameters|Type|Description
-|-|-
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file

---
#### Tool: **`list-endpoints`**
Lists all API paths and their HTTP methods with summaries, organized by path
Parameters|Type|Description
-|-|-
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file

---
#### Tool: **`list-security-schemes`**
Lists all available security schemes
Parameters|Type|Description
-|-|-
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file

---
#### Tool: **`search-schema`**
Searches across paths, operations, and schemas
Parameters|Type|Description
-|-|-
`openapiSchemaPath`|`string`|Path to the OpenAPI schema file
`pattern`|`string`|Search pattern (case-insensitive)

---
