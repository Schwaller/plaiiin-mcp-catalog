A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/github-chat](https://hub.docker.com/repository/docker/mcp/github-chat)
**Author**|[AsyncFuncAI](https://github.com/AsyncFuncAI)
**Repository**|https://github.com/AsyncFuncAI/github-chat-mcp

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`index_repository`|Index a GitHub repository to analyze its codebase.|
`query_repository`|Ask questions about a GitHub repository and receive detailed AI responses.|

---
## Tools Details

#### Tool: **`index_repository`**
Index a GitHub repository to analyze its codebase. This must be done before asking questions about the repository.
Parameters|Type|Description
-|-|-
`repo_url`|`string`|The GitHub repository URL to index (format: https://github.com/username/repo).

---
#### Tool: **`query_repository`**
Ask questions about a GitHub repository and receive detailed AI responses. The repository must be indexed first.
Parameters|Type|Description
-|-|-
`question`|`string`|The question to ask about the repository.
`repo_url`|`string`|The GitHub repository URL to query (format: https://github.com/username/repo).
`conversation_history`|`string` *optional*|Previous conversation history for multi-turn conversations.

---
