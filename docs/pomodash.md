Connect your AI assistant to PomoDash for seamless task and project management.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/pomodash](https://hub.docker.com/repository/docker/mcp/pomodash)
**Author**|[DannyyTv](https://github.com/DannyyTv)
**Repository**|https://github.com/dannyytv/pomodash-mcp-server

## Available Tools (14)
Tools provided by this Server|Short Description
-|-
`create_category`|Create a new category or project|
`create_note`|Create a new note in PomoDash|
`create_note_for_project`|Create a note linked to a specific project|
`create_note_for_task`|Create a note linked to a specific task|
`create_task`|Create a new task in PomoDash|
`create_task_for_project`|Create a task linked to a specific project|
`delete_note`|Delete a note|
`delete_task`|Delete a task|
`list_categories`|List all categories and projects|
`list_note_references`|List available tasks and projects for note linking|
`list_notes`|List all notes|
`list_tasks`|List all tasks|
`update_note`|Update an existing note|
`update_task`|Update an existing task|

---
## Tools Details

#### Tool: **`create_category`**
Create a new category or project
Parameters|Type|Description
-|-|-
`name`|`string`|Category/Project name (required)
`color`|`string` *optional*|Category color (default: #3b82f6)
`is_project`|`boolean` *optional*|Whether this is a project (default: false)

---
#### Tool: **`create_note`**
Create a new note in PomoDash
Parameters|Type|Description
-|-|-
`content`|`string`|Note content (required)
`reference_id`|`string` *optional*|Reference ID (default: general)
`reference_type`|`string` *optional*|Type of reference (default: general)

---
#### Tool: **`create_note_for_project`**
Create a note linked to a specific project
Parameters|Type|Description
-|-|-
`content`|`string`|Note content (required)
`project_id`|`string`|ID of the project to link the note to (required)

---
#### Tool: **`create_note_for_task`**
Create a note linked to a specific task
Parameters|Type|Description
-|-|-
`content`|`string`|Note content (required)
`task_id`|`string`|ID of the task to link the note to (required)

---
#### Tool: **`create_task`**
Create a new task in PomoDash
Parameters|Type|Description
-|-|-
`title`|`string`|Task title (required)
`description`|`string` *optional*|Task description (optional)
`due_date`|`string` *optional*|Due date in ISO format (optional)
`end_time`|`string` *optional*|End time for timeboxing (optional)
`priority`|`string` *optional*|Task priority (default: medium)
`start_time`|`string` *optional*|Start time for timeboxing (optional)

---
#### Tool: **`create_task_for_project`**
Create a task linked to a specific project
Parameters|Type|Description
-|-|-
`project_id`|`string`|Project ID to link task to (required)
`title`|`string`|Task title (required)
`description`|`string` *optional*|Task description (optional)
`due_date`|`string` *optional*|Due date in ISO format (optional)
`priority`|`string` *optional*|Task priority (optional)

---
#### Tool: **`delete_note`**
Delete a note
Parameters|Type|Description
-|-|-
`note_id`|`string`|Note ID to delete (required)

---
#### Tool: **`delete_task`**
Delete a task
Parameters|Type|Description
-|-|-
`task_id`|`string`|Task ID to delete (required)

---
#### Tool: **`list_categories`**
List all categories and projects
#### Tool: **`list_note_references`**
List available tasks and projects for note linking
#### Tool: **`list_notes`**
List all notes
#### Tool: **`list_tasks`**
List all tasks
#### Tool: **`update_note`**
Update an existing note
Parameters|Type|Description
-|-|-
`note_id`|`string`|Note ID to update (required)
`content`|`string` *optional*|New note content (optional)

---
#### Tool: **`update_task`**
Update an existing task
Parameters|Type|Description
-|-|-
`task_id`|`string`|Task ID to update (required)
`description`|`string` *optional*|New task description (optional)
`priority`|`string` *optional*|New task priority (optional)
`status`|`string` *optional*|New task status (optional)
`title`|`string` *optional*|New task title (optional)

---
