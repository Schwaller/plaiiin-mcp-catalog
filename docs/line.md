MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/line](https://hub.docker.com/repository/docker/mcp/line)
**Author**|[line](https://github.com/line)
**Repository**|https://github.com/line/line-bot-mcp-server

## Available Tools (12)
Tools provided by this Server|Short Description
-|-
`broadcast_flex_message`|Broadcast a highly customizable flex message via LINE to all users who have added your LINE Official Account.|
`broadcast_text_message`|Broadcast a simple text message via LINE to all users who have followed your LINE Official Account.|
`cancel_rich_menu_default`|Cancel the default rich menu.|
`create_rich_menu`|Create a rich menu based on the given actions.|
`delete_rich_menu`|Delete a rich menu from your LINE Official Account.|
`get_follower_ids`|Get a list of user IDs of users who have added the LINE Official Account as a friend.|
`get_message_quota`|Get the message quota and consumption of the LINE Official Account.|
`get_profile`|Get detailed profile information of a LINE user including display name, profile picture URL, status message and language.|
`get_rich_menu_list`|Get the list of rich menus associated with your LINE Official Account.|
`push_flex_message`|Push a highly customizable flex message to a user via LINE.|
`push_text_message`|Push a simple text message to a user via LINE.|
`set_rich_menu_default`|Set a rich menu as the default rich menu.|

---
## Tools Details

#### Tool: **`broadcast_flex_message`**
Broadcast a highly customizable flex message via LINE to all users who have added your LINE Official Account. Supports both bubble (single container) and carousel (multiple swipeable bubbles) layouts. Please be aware that this message will be sent to all users.
Parameters|Type|Description
-|-|-
`message`|`object`|

*This tool may perform destructive updates.*

---
#### Tool: **`broadcast_text_message`**
Broadcast a simple text message via LINE to all users who have followed your LINE Official Account. Use this for sending plain text messages without formatting. Please be aware that this message will be sent to all users.
Parameters|Type|Description
-|-|-
`message`|`object`|

*This tool may perform destructive updates.*

---
#### Tool: **`cancel_rich_menu_default`**
Cancel the default rich menu.
#### Tool: **`create_rich_menu`**
Create a rich menu based on the given actions. Generate and upload a rich menu image based on the given action. This rich menu will be registered as the default.
Parameters|Type|Description
-|-|-
`actions`|`array`|The actions of the rich menu.
`chatBarText`|`string`|Text displayed in the chat bar and this is also used as name of the rich menu to create

*This tool may perform destructive updates.*

---
#### Tool: **`delete_rich_menu`**
Delete a rich menu from your LINE Official Account.
Parameters|Type|Description
-|-|-
`richMenuId`|`string`|The ID of the rich menu to delete.

*This tool may perform destructive updates.*

---
#### Tool: **`get_follower_ids`**
Get a list of user IDs of users who have added the LINE Official Account as a friend. This allows you to obtain user IDs for sending messages without manually preparing them.
Parameters|Type|Description
-|-|-
`limit`|`number` *optional*|The maximum number of user IDs to retrieve in a single request.
`start`|`string` *optional*|Continuation token to get the next array of user IDs. Returned in the 'next' property of a previous response.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_message_quota`**
Get the message quota and consumption of the LINE Official Account. This shows the monthly message limit and current usage.
#### Tool: **`get_profile`**
Get detailed profile information of a LINE user including display name, profile picture URL, status message and language.
Parameters|Type|Description
-|-|-
`userId`|`string` *optional*|The user ID to get a profile. Defaults to DESTINATION_USER_ID.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_rich_menu_list`**
Get the list of rich menus associated with your LINE Official Account.
#### Tool: **`push_flex_message`**
Push a highly customizable flex message to a user via LINE. Supports both bubble (single container) and carousel (multiple swipeable bubbles) layouts.
Parameters|Type|Description
-|-|-
`message`|`object`|
`userId`|`string` *optional*|The user ID to receive a message. Defaults to DESTINATION_USER_ID.

*This tool may perform destructive updates.*

---
#### Tool: **`push_text_message`**
Push a simple text message to a user via LINE. Use this for sending plain text messages without formatting.
Parameters|Type|Description
-|-|-
`message`|`object`|
`userId`|`string` *optional*|The user ID to receive a message. Defaults to DESTINATION_USER_ID.

*This tool may perform destructive updates.*

---
#### Tool: **`set_rich_menu_default`**
Set a rich menu as the default rich menu.
Parameters|Type|Description
-|-|-
`richMenuId`|`string`|The ID of the rich menu to set as default.

*This tool may perform destructive updates.*

---

## Screenshots

![LINE screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/line-1.png)
