An MCP server implementation for retrieving information from the AWS Knowledge Base using the Bedrock Agent Runtime.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-kb-retrieval-server](https://hub.docker.com/repository/docker/mcp/aws-kb-retrieval-server)
**Author**|[modelcontextprotocol](https://github.com/modelcontextprotocol)
**Repository**|https://github.com/modelcontextprotocol/servers

## Available Tools (1)
Tools provided by this Server|Short Description
-|-
`retrieve_from_aws_kb`|Performs retrieval from the AWS Knowledge Base using the provided query and Knowledge Base ID.|

---
## Tools Details

#### Tool: **`retrieve_from_aws_kb`**
Performs retrieval from the AWS Knowledge Base using the provided query and Knowledge Base ID.
Parameters|Type|Description
-|-|-
`knowledgeBaseId`|`string`|The ID of the AWS Knowledge Base
`query`|`string`|The query to perform retrieval on
`n`|`number` *optional*|Number of results to retrieve

---
