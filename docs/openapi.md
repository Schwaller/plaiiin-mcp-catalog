Fetch, validate, and generate code or curl from any OpenAPI or Swagger spec - all from a single URL.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/openapi](https://hub.docker.com/repository/docker/mcp/openapi)
**Author**|[lepoco](https://github.com/lepoco)
**Repository**|https://github.com/lepoco/openapi.client

## Available Tools (5)
Tools provided by this Server|Short Description
-|-
`create_csharp_snippet`|Generate a C# code snippet for a given operation ID from a URL OR a raw JSON string or file contents pointing to an OpenAPI or Swagger JSON document.|
`generate_curl_command`|Generate a cURL command for a given operation ID from a URL OR a raw JSON string or file contents pointing to an OpenAPI or Swagger JSON document.|
`get_known_responses`|Analyze an OpenAPI or Swagger document provided as a URL OR a raw JSON string or file contents, and list possible HTTP responses (status codes and descriptions) for the specified operation ID.|
`get_list_of_operations`|Retrieve a list of operations (endpoints) from a URL OR a raw JSON string or file contents pointing to an OpenAPI or Swagger JSON document.|
`validate_document`|Analyze and validate an OpenAPI or Swagger document provided as a URL OR a raw JSON string or file contents, and list possible errors, issues and problems with specification for the specified operation ID.|

---
## Tools Details

#### Tool: **`create_csharp_snippet`**
Generate a C# code snippet for a given operation ID from a URL OR a raw JSON string or file contents pointing to an OpenAPI or Swagger JSON document.
Parameters|Type|Description
-|-|-
`addressOrFileContents`|`string`|URL address of the OpenAPI or Swagger JSON document OR raw JSON contents of the OpenAPI or Swagger specification. Can be provided as text or from a file.
`baseAddress`|`string`|Optional base URL to be used in the generated cURL command.
`operationId`|`string`|Operation ID for which to create a snippet.

---
#### Tool: **`generate_curl_command`**
Generate a cURL command for a given operation ID from a URL OR a raw JSON string or file contents pointing to an OpenAPI or Swagger JSON document.
Parameters|Type|Description
-|-|-
`addressOrFileContents`|`string`|URL address of the OpenAPI or Swagger JSON document OR raw JSON contents of the OpenAPI or Swagger specification. Can be provided as text or from a file.
`baseAddress`|`string`|Optional base URL to be used in the generated cURL command.
`operationId`|`string`|Operation ID for which to generate the cURL command.

---
#### Tool: **`get_known_responses`**
Analyze an OpenAPI or Swagger document provided as a URL OR a raw JSON string or file contents, and list possible HTTP responses (status codes and descriptions) for the specified operation ID.
Parameters|Type|Description
-|-|-
`addressOrFileContents`|`string`|URL address of the OpenAPI or Swagger JSON document OR raw JSON contents of the OpenAPI or Swagger specification. Can be provided as text or from a file.
`operationId`|`string`|Operation ID for which to retrieve known responses.

---
#### Tool: **`get_list_of_operations`**
Retrieve a list of operations (endpoints) from a URL OR a raw JSON string or file contents pointing to an OpenAPI or Swagger JSON document.
Parameters|Type|Description
-|-|-
`addressOrFileContents`|`string`|URL address of the OpenAPI or Swagger JSON document OR raw JSON contents of the OpenAPI or Swagger specification. Can be provided as text or from a file.

---
#### Tool: **`validate_document`**
Analyze and validate an OpenAPI or Swagger document provided as a URL OR a raw JSON string or file contents, and list possible errors, issues and problems with specification for the specified operation ID.
Parameters|Type|Description
-|-|-
`addressOrFileContents`|`string`|URL address of the OpenAPI or Swagger JSON document OR raw JSON contents of the OpenAPI or Swagger specification. Can be provided as text or from a file.

---
