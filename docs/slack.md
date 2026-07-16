Interact with Slack Workspaces over the Slack API.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/slack](https://hub.docker.com/repository/docker/mcp/slack)
**Author**|[modelcontextprotocol](https://github.com/modelcontextprotocol)
**Repository**|https://github.com/modelcontextprotocol/servers

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`slack_add_reaction`|Add a reaction emoji to a message|
`slack_get_channel_history`|Get recent messages from a channel|
`slack_get_thread_replies`|Get all replies in a message thread|
`slack_get_user_profile`|Get detailed profile information for a specific user|
`slack_get_users`|Get a list of all users in the workspace with their basic profile information|
`slack_list_channels`|List public or pre-defined channels in the workspace with pagination|
`slack_post_message`|Post a new message to a Slack channel|
`slack_reply_to_thread`|Reply to a specific message thread in Slack|

---
## Tools Details

#### Tool: **`slack_add_reaction`**
Add a reaction emoji to a message
Parameters|Type|Description
-|-|-
`channel_id`|`string`|The ID of the channel containing the message
`reaction`|`string`|The name of the emoji reaction (without ::)
`timestamp`|`string`|The timestamp of the message to react to

---
#### Tool: **`slack_get_channel_history`**
Get recent messages from a channel
Parameters|Type|Description
-|-|-
`channel_id`|`string`|The ID of the channel
`limit`|`number` *optional*|Number of messages to retrieve (default 10)

---
#### Tool: **`slack_get_thread_replies`**
Get all replies in a message thread
Parameters|Type|Description
-|-|-
`channel_id`|`string`|The ID of the channel containing the thread
`thread_ts`|`string`|The timestamp of the parent message in the format '1234567890.123456'. Timestamps in the format without the period can be converted by adding the period such that 6 numbers come after it.

---
#### Tool: **`slack_get_user_profile`**
Get detailed profile information for a specific user
Parameters|Type|Description
-|-|-
`user_id`|`string`|The ID of the user

---
#### Tool: **`slack_get_users`**
Get a list of all users in the workspace with their basic profile information
Parameters|Type|Description
-|-|-
`cursor`|`string` *optional*|Pagination cursor for next page of results
`limit`|`number` *optional*|Maximum number of users to return (default 100, max 200)

---
#### Tool: **`slack_list_channels`**
List public or pre-defined channels in the workspace with pagination
Parameters|Type|Description
-|-|-
`cursor`|`string` *optional*|Pagination cursor for next page of results
`limit`|`number` *optional*|Maximum number of channels to return (default 100, max 200)

---
#### Tool: **`slack_post_message`**
Post a new message to a Slack channel
Parameters|Type|Description
-|-|-
`channel_id`|`string`|The ID of the channel to post to
`text`|`string`|The message text to post

---
#### Tool: **`slack_reply_to_thread`**
Reply to a specific message thread in Slack
Parameters|Type|Description
-|-|-
`channel_id`|`string`|The ID of the channel containing the thread
`text`|`string`|The reply text
`thread_ts`|`string`|The timestamp of the parent message in the format '1234567890.123456'. Timestamps in the format without the period can be converted by adding the period such that 6 numbers come after it.

---
