A Model Context Protocol server for Omi interaction and automation. This server provides tools to read, search, and manipulate Memories and Conversations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/omi](https://hub.docker.com/repository/docker/mcp/omi)
**Author**|[BasedHardware](https://github.com/BasedHardware)
**Repository**|https://github.com/BasedHardware/omi

## Available Tools (6)
Tools provided by this Server|Short Description
-|-
`create_memory`|Create a new memory.|
`delete_memory`|Delete a memory by ID.|
`edit_memory`|Edit a memory's content.|
`get_conversation_by_id`|Retrieve a conversation by ID including each segment of the transcript.|
`get_conversations`|Retrieve a list of conversation metadata.|
`get_memories`|Retrieve a list of memories.|

---
## Tools Details

#### Tool: **`create_memory`**
Create a new memory. A memory is a known fact about the user across multiple domains.
Parameters|Type|Description
-|-|-
`category`|`string`|The category of the memory to create.
`content`|`string`|The content of the memory.
`api_key`|`string` *optional*|The user's MCP API key. If not provided, it will be read from the OMI_API_KEY environment variable. For more details, see https://docs.omi.me/doc/developer/MCP

---
#### Tool: **`delete_memory`**
Delete a memory by ID. A memory is a known fact about the user across multiple domains.
Parameters|Type|Description
-|-|-
`memory_id`|`string`|The ID of the memory to delete.
`api_key`|`string` *optional*|The user's MCP API key. If not provided, it will be read from the OMI_API_KEY environment variable. For more details, see https://docs.omi.me/doc/developer/MCP

---
#### Tool: **`edit_memory`**
Edit a memory's content. A memory is a known fact about the user across multiple domains.
Parameters|Type|Description
-|-|-
`content`|`string`|The new content for the memory.
`memory_id`|`string`|The ID of the memory to edit.
`api_key`|`string` *optional*|The user's MCP API key. If not provided, it will be read from the OMI_API_KEY environment variable. For more details, see https://docs.omi.me/doc/developer/MCP

---
#### Tool: **`get_conversation_by_id`**
Retrieve a conversation by ID including each segment of the transcript.
Parameters|Type|Description
-|-|-
`conversation_id`|`string`|The ID of the conversation to retrieve.
`api_key`|`string` *optional*|The user's MCP API key. If not provided, it will be read from the OMI_API_KEY environment variable. For more details, see https://docs.omi.me/doc/developer/MCP

---
#### Tool: **`get_conversations`**
Retrieve a list of conversation metadata. To get full transcripts, use get_conversation_by_id.
Parameters|Type|Description
-|-|-
`api_key`|`string` *optional*|The user's MCP API key. If not provided, it will be read from the OMI_API_KEY environment variable. For more details, see https://docs.omi.me/doc/developer/MCP
`categories`|`array` *optional*|Filter by conversation categories.
`end_date`|`string` *optional*|Filter conversations before this date (yyyy-mm-dd)
`limit`|`integer` *optional*|The number of conversations to retrieve.
`offset`|`integer` *optional*|The offset of the conversations to retrieve.
`start_date`|`string` *optional*|Filter conversations after this date (yyyy-mm-dd)

---
#### Tool: **`get_memories`**
Retrieve a list of memories. A memory is a known fact about the user across multiple domains.
Parameters|Type|Description
-|-|-
`api_key`|`string` *optional*|The user's MCP API key. If not provided, it will be read from the OMI_API_KEY environment variable. For more details, see https://docs.omi.me/doc/developer/MCP
`categories`|`array` *optional*|The categories of memories to filter by.
`limit`|`integer` *optional*|The number of memories to retrieve.
`offset`|`integer` *optional*|The offset of the memories to retrieve.

---
