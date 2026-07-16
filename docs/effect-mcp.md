Tools and resources for writing Effect code in Typescript.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/effect-mcp](https://hub.docker.com/repository/docker/mcp/effect-mcp)
**Author**|[tim-smart](https://github.com/tim-smart)
**Repository**|https://github.com/tim-smart/effect-mcp

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`effect_docs_search`|Searches the Effect documentation.|
`get_effect_doc`|Get the Effect documentation for a documentId.|

---
## Tools Details

#### Tool: **`effect_docs_search`**
Searches the Effect documentation. Result content can be accessed with the `get_effect_doc` tool.
Parameters|Type|Description
-|-|-
`query`|`string`|The search query to look for in the documentation.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`get_effect_doc`**
Get the Effect documentation for a documentId. The content might be paginated. Use the `page` parameter to specify which page to retrieve.
Parameters|Type|Description
-|-|-
`documentId`|`number`|The unique identifier for the Effect documentation entry.
`page`|`number` *optional*|The page number to retrieve for the document content.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
