Send emails directly from Cursor with this email sending MCP server.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/resend](https://hub.docker.com/repository/docker/mcp/resend)
**Author**|[resend](https://github.com/resend)
**Repository**|https://github.com/resend/mcp-send-email

## Available Tools (1)
Tools provided by this Server|Short Description
-|-
`send-email`|Send an email using Resend|

---
## Tools Details

#### Tool: **`send-email`**
Send an email using Resend
Parameters|Type|Description
-|-|-
`subject`|`string`|Email subject line
`text`|`string`|Plain text email content
`to`|`string`|Recipient email address
`bcc`|`array` *optional*|Optional array of BCC email addresses. You MUST ask the user for this parameter. Under no circumstance provide it yourself
`cc`|`array` *optional*|Optional array of CC email addresses. You MUST ask the user for this parameter. Under no circumstance provide it yourself
`html`|`string` *optional*|HTML email content. When provided, the plain text argument MUST be provided as well.
`scheduledAt`|`string` *optional*|Optional parameter to schedule the email. This uses natural language. Examples would be 'tomorrow at 10am' or 'in 2 hours' or 'next day at 9am PST' or 'Friday at 3pm ET'.

---
