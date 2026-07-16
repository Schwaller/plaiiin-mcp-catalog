Connector for Perplexity API, to enable real-time, web-wide research.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/perplexity-ask](https://hub.docker.com/repository/docker/mcp/perplexity-ask)
**Author**|[perplexityai](https://github.com/perplexityai)
**Repository**|https://github.com/ppl-ai/modelcontextprotocol

## Available Tools (3)
Tools provided by this Server|Short Description
-|-
`perplexity_ask`|Engages in a conversation using the Sonar API.|
`perplexity_reason`|Performs reasoning tasks using the Perplexity API.|
`perplexity_research`|Performs deep research using the Perplexity API.|

---
## Tools Details

#### Tool: **`perplexity_ask`**
Engages in a conversation using the Sonar API. Accepts an array of messages (each with a role and content) and returns a ask completion response from the Perplexity model.
Parameters|Type|Description
-|-|-
`messages`|`array`|Array of conversation messages

---
#### Tool: **`perplexity_reason`**
Performs reasoning tasks using the Perplexity API. Accepts an array of messages (each with a role and content) and returns a well-reasoned response using the sonar-reasoning-pro model.
Parameters|Type|Description
-|-|-
`messages`|`array`|Array of conversation messages

---
#### Tool: **`perplexity_research`**
Performs deep research using the Perplexity API. Accepts an array of messages (each with a role and content) and returns a comprehensive research response with citations.
Parameters|Type|Description
-|-|-
`messages`|`array`|Array of conversation messages

---
