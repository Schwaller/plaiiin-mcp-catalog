Pinecone Assistant MCP server.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/pinecone](https://hub.docker.com/repository/docker/mcp/pinecone)
**Author**|[pinecone-io](https://github.com/pinecone-io)
**Repository**|https://github.com/pinecone-io/assistant-mcp

## Available Tools (1)
Tools provided by this Server|Short Description
-|-
`assistant_context`|Retrieves relevant document snippets from your Pinecone Assistant knowledge base.|

---
## Tools Details

#### Tool: **`assistant_context`**
Retrieves relevant document snippets from your Pinecone Assistant knowledge base. Returns an array of text snippets from the most relevant documents. You can use the 'top_k' parameter to control result count (default: 15). Recommended top_k: a few (5-8) for simple/narrow queries, 10-20 for complex/broad topics.
Parameters|Type|Description
-|-|-
`assistant_name`|`string`|Name of an existing Pinecone assistant
`query`|`string`|The query to retrieve context for.
`top_k`|`integer` *optional*|The number of context snippets to retrieve. Defaults to 15.

---
