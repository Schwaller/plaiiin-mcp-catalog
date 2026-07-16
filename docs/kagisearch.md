The Official Model Context Protocol (MCP) server for Kagi search & other tools.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/kagisearch](https://hub.docker.com/repository/docker/mcp/kagisearch)
**Author**|[kagisearch](https://github.com/kagisearch)
**Repository**|https://github.com/kagisearch/kagimcp

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`kagi_search_fetch`|Fetch web results based on one or more queries using the Kagi Search API.|
`kagi_summarizer`|Summarize content from a URL using the Kagi Summarizer API.|

---
## Tools Details

#### Tool: **`kagi_search_fetch`**
Fetch web results based on one or more queries using the Kagi Search API. Use for general search and when the user explicitly tells you to 'fetch' results/information. Results are from all queries given. They are numbered continuously, so that a user may be able to refer to a result by a specific number.
Parameters|Type|Description
-|-|-
`queries`|`array`|One or more concise, keyword-focused search queries. Include essential context within each query for standalone use.

---
#### Tool: **`kagi_summarizer`**
Summarize content from a URL using the Kagi Summarizer API. The Summarizer can summarize any document type (text webpage, video, audio, etc.)
Parameters|Type|Description
-|-|-
`url`|`string`|A URL to a document to summarize.
`summary_type`|`string` *optional*|Type of summary to produce. Options are 'summary' for paragraph prose and 'takeaway' for a bulleted list of key points.
`target_language`|`string` *optional*|Desired output language using language codes (e.g., 'EN' for English). If not specified, the document's original language influences the output.

---
