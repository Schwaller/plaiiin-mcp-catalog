A unified MCP proxy that aggregates multiple MCP servers into one interface, enabling seamless tool discovery and management across all your AI interactions. Manage all your MCP servers from a single connection point with RAG capabilities and real-time notifications.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/pluggedin-mcp-proxy](https://hub.docker.com/repository/docker/mcp/pluggedin-mcp-proxy)
**Author**|[VeriTeknik](https://github.com/VeriTeknik)
**Repository**|https://github.com/VeriTeknik/pluggedin-mcp-proxy

## Available Tools (6)
Tools provided by this Server|Short Description
-|-
`pluggedin_ask_knowledge_base`|Ask questions and get AI-generated answers from your knowledge base.|
`pluggedin_delete_notification`|Delete a notification from the Plugged.in system|
`pluggedin_discover_tools`|Triggers discovery of tools (and resources/templates) for configured MCP servers in the Pluggedin App.|
`pluggedin_list_notifications`|List notifications from the Plugged.in system with optional filters for unread only and result limit|
`pluggedin_mark_notification_done`|Mark a notification as done in the Plugged.in system|
`pluggedin_send_notification`|Send custom notifications through the Plugged.in system with optional email delivery.|

---
## Tools Details

#### Tool: **`pluggedin_ask_knowledge_base`**
Ask questions and get AI-generated answers from your knowledge base. Returns structured JSON with answer, document sources, and metadata.
Parameters|Type|Description
-|-|-
`query`|`string`|Your question or query to get AI-generated answers from the knowledge base.

---
#### Tool: **`pluggedin_delete_notification`**
Delete a notification from the Plugged.in system
Parameters|Type|Description
-|-|-
`notificationId`|`string`|The ID of the notification to delete

---
#### Tool: **`pluggedin_discover_tools`**
Triggers discovery of tools (and resources/templates) for configured MCP servers in the Pluggedin App.
Parameters|Type|Description
-|-|-
`force_refresh`|`boolean` *optional*|Set to true to bypass cache and force a fresh discovery. Defaults to false.
`server_uuid`|`string` *optional*|Optional UUID of a specific server to discover. If omitted, attempts to discover all.

---
#### Tool: **`pluggedin_list_notifications`**
List notifications from the Plugged.in system with optional filters for unread only and result limit
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|Limit the number of notifications returned (1-100)
`onlyUnread`|`boolean` *optional*|Filter to show only unread notifications

---
#### Tool: **`pluggedin_mark_notification_done`**
Mark a notification as done in the Plugged.in system
Parameters|Type|Description
-|-|-
`notificationId`|`string`|The ID of the notification to mark as read

---
#### Tool: **`pluggedin_send_notification`**
Send custom notifications through the Plugged.in system with optional email delivery. You can provide a custom title or let the system use a localized default.
Parameters|Type|Description
-|-|-
`message`|`string`|The notification message content
`sendEmail`|`boolean` *optional*|Whether to also send the notification via email
`severity`|`string` *optional*|The severity level of the notification (defaults to INFO)
`title`|`string` *optional*|Optional notification title. If not provided, a localized default will be used. Consider generating a descriptive title based on the message content.

---
