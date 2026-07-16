Provides tools to search and retrieve Google Gemini API documentation.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/gemini-api-docs-mcp](https://hub.docker.com/repository/docker/mcp/gemini-api-docs-mcp)
**Author**|[kgprs](https://github.com/kgprs)
**Repository**|https://github.com/kgprs/gemini-api-docs-mcp

## Available Tools (3)
Tools provided by this Server|Short Description
-|-
`get_capability_page`|Retrieves the full content of a specific documentation page by its exact title.|
`get_current_model`|Shortcut tool to explicitly retrieve the canonical 'Gemini Models' documentation page.|
`search_documentation`|Performs a standard keyword search on Gemini API documentation.|

---
## Tools Details

#### Tool: **`get_capability_page`**
Retrieves the full content of a specific documentation page by its exact title.
You can call can this tool WITHOUT arguments first to see a master list of all available page titles.
Then, call it again with the exact title you need.
Parameters|Type|Description
-|-|-
`capability`|`string`|The EXACT title of the documentation page to retrieve (case-sensitive). If you do not know the exact title, OMIT this argument to receive a master list of all available titles.

---
#### Tool: **`get_current_model`**
Shortcut tool to explicitly retrieve the canonical 'Gemini Models' documentation page. Use this to fast-track finding details about available model variants (Pro, Flash, etc.), their capabilities, versioning, and context window sizes.
#### Tool: **`search_documentation`**
Performs a standard keyword search on Gemini API documentation.
CRITICAL: This is a naive keyword search, NOT semantic. Long queries will FAIL.
You MUST use VERY SHORT keyword based queries (max 1-3 keywords) focusing only on the most unique terms.
Break complex questions into separate, simple queries. It will return the full documentation page for a capability or feature.
Parameters|Type|Description
-|-|-
`queries`|`array`|List of up to 3 SHORT keyword queries. Keep each query under 3 words.
BAD: 'google genai python generate image save bytes' (too specific, will fail).
GOOD: ['function calling', 'imagen parameters', 'save bytes'] (broad, likely to hit).

---
