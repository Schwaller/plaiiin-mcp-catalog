Ref powerful search tool connets your coding tools with documentation context. It includes an up-to-date index of public documentation and it can ingest your private documentation (eg. GitHub repos, PDFs) as well.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/ref-tools-mcp](https://hub.docker.com/repository/docker/mcp/ref-tools-mcp)
**Author**|[ref-tools](https://github.com/ref-tools)
**Repository**|https://github.com/ref-tools/ref-tools-mcp

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`ref_read_url`|A tool that fetches content from a URL and converts it to markdown for easy reading with Ref.|
`ref_search_documentation`|A powerful search tool to check technical documentation.|

---
## Tools Details

#### Tool: **`ref_read_url`**
A tool that fetches content from a URL and converts it to markdown for easy reading with Ref. 

This is powerful when used in conjunction with the ref_search_documentation or ref_search_web tool that return urls of relevant content.
Parameters|Type|Description
-|-|-
`url`|`string`|The URL of the webpage to read.

---
#### Tool: **`ref_search_documentation`**
A powerful search tool to check technical documentation. Great for finding facts or code snippets. Can be used to search for public documentation on the web or github as well from private resources like repos and pdfs.
Parameters|Type|Description
-|-|-
`query`|`string`|Query to search for relevant documentation. This should be a full sentence or question.
`keyWords`|`array` *optional*|A list of keywords to use for the search like you would use for grep
`source`|`string` *optional*|Defaults to 'all'. 'public' is used when the user is asking about a public API or library. 'private' is used when the user is asking about their own private repo or pdfs. 'web' is use only as a fallback when 'public' has failed.

---

## Screenshots

![Ref - Up-To-Date Docs screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/ref-1.png)
