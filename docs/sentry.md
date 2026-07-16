A Model Context Protocol server for retrieving and analyzing issues from Sentry.io. This server provides tools to inspect error reports, stacktraces, and other debugging information from your Sentry account.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/sentry](https://hub.docker.com/repository/docker/mcp/sentry)
**Author**|[modelcontextprotocol](https://github.com/modelcontextprotocol)
**Repository**|https://github.com/modelcontextprotocol/servers

## Available Tools (1)
Tools provided by this Server|Short Description
-|-
`get_sentry_issue`|Retrieve and analyze a Sentry issue by ID or URL.|

---
## Tools Details

#### Tool: **`get_sentry_issue`**
Retrieve and analyze a Sentry issue by ID or URL. Use this tool when you need to:
                - Investigate production errors and crashes
                - Access detailed stacktraces from Sentry
                - Analyze error patterns and frequencies
                - Get information about when issues first/last occurred
                - Review error counts and status
Parameters|Type|Description
-|-|-
`issue_id_or_url`|`string`|Sentry issue ID or URL to analyze

---
