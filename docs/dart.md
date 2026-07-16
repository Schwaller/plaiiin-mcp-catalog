Dart AI Model Context Protocol (MCP) server.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/dart](https://hub.docker.com/repository/docker/mcp/dart)
**Author**|[its-dart](https://github.com/its-dart)
**Repository**|https://github.com/its-dart/dart-mcp-server

## Available Tools (16)
Tools provided by this Server|Short Description
-|-
`add_task_comment`|Add a comment to an existing task without modifying the task description.|
`create_doc`|Create a new doc in Dart.|
`create_task`|Create a new task in Dart.|
`delete_doc`|Move an existing doc to the trash, where it can be recovered if needed.|
`delete_task`|Move an existing task to the trash, where it can be recovered if needed.|
`get_config`|Get information about the user's space, including all of the possible values that can be provided to other endpoints.|
`get_dartboard`|Retrieve an existing dartboard by its ID.|
`get_doc`|Retrieve an existing doc by its ID.|
`get_folder`|Retrieve an existing folder by its ID.|
`get_task`|Retrieve an existing task by its ID.|
`get_view`|Retrieve an existing view by its ID.|
`list_docs`|List docs from Dart with optional filtering parameters.|
`list_task_comments`|List comments from Dart with optional filtering parameters.|
`list_tasks`|List tasks from Dart with optional filtering parameters.|
`update_doc`|Update an existing doc.|
`update_task`|Update an existing task.|

---
## Tools Details

#### Tool: **`add_task_comment`**
Add a comment to an existing task without modifying the task description. Comments support markdown formatting.
Parameters|Type|Description
-|-|-
`taskId`|`string`|The 12-character alphanumeric ID of the task
`text`|`string`|The full content of the comment, which can include markdown formatting.

---
#### Tool: **`create_doc`**
Create a new doc in Dart. You can specify title, text content, and folder.
Parameters|Type|Description
-|-|-
`title`|`string`|The title of the doc (required)
`folder`|`string` *optional*|The title of the folder to place the doc in
`text`|`string` *optional*|The text content of the doc, which can include markdown formatting

---
#### Tool: **`create_task`**
Create a new task in Dart. You can specify title, description, status, priority, size, dates, dartboard, assignees, tags, parent task, custom properties, and task relationships.
Parameters|Type|Description
-|-|-
`title`|`string`|The title of the task (required)
`assignee`|`string` *optional*|Single assignee name or email (if workspace doesn't allow multiple assignees)
`assignees`|`array` *optional*|Array of assignee names or emails (if workspace allows multiple assignees)
`customProperties`|`object` *optional*|Custom properties to apply to the task. Use the property names from the config. Examples: { 'customCheckboxProperty': true, 'customTextProperty': 'Some text', 'customNumberProperty': 5, 'customSelectProperty': 'Option Name', 'customDatesProperty': '2025-05-10', 'customDatesPropertyWithRange': ['2025-05-01', '2025-05-30'], 'customMultiselectProperty': ['option1', 'option2'], 'customUserProperty': 'user@example.com', 'customMultipleUserProperty': ['user1@example.com', 'user2@example.com'], 'customTimeTrackingProperty': '1:30:00' }
`dartboard`|`string` *optional*|The title of the dartboard (project or list of tasks)
`description`|`string` *optional*|A longer description of the task, which can include markdown formatting
`dueAt`|`string` *optional*|The due date in ISO format (should be at 9:00am in user's timezone)
`parentId`|`string` *optional*|The ID of the parent task
`priority`|`string` *optional*|The priority (Critical, High, Medium, or Low)
`size`|`string` *optional*|The size which represents the amount of work needed
`startAt`|`string` *optional*|The start date in ISO format (should be at 9:00am in user's timezone)
`status`|`string` *optional*|The status from the list of available statuses
`tags`|`array` *optional*|Array of tags to apply to the task
`taskRelationships`|`object` *optional*|Task relationships including subtasks, blockers, duplicates, and related tasks
`type`|`string` *optional*|The type of the task from the list of available types

---
#### Tool: **`delete_doc`**
Move an existing doc to the trash, where it can be recovered if needed. Nothing else about the doc will be changed.
Parameters|Type|Description
-|-|-
`id`|`string`|The 12-character alphanumeric ID of the doc

---
#### Tool: **`delete_task`**
Move an existing task to the trash, where it can be recovered if needed. Nothing else about the task will be changed.
Parameters|Type|Description
-|-|-
`id`|`string`|The 12-character alphanumeric ID of the task

---
#### Tool: **`get_config`**
Get information about the user's space, including all of the possible values that can be provided to other endpoints. This includes available assignees, dartboards, folders, statuses, tags, priorities, sizes, and all custom property definitions.
#### Tool: **`get_dartboard`**
Retrieve an existing dartboard by its ID. Returns the dartboard's information including title, description, and all tasks within it.
Parameters|Type|Description
-|-|-
`id`|`string`|The 12-character alphanumeric ID of the dartboard

---
#### Tool: **`get_doc`**
Retrieve an existing doc by its ID. Returns the doc's information including title, text content, folder, and more.
Parameters|Type|Description
-|-|-
`id`|`string`|The 12-character alphanumeric ID of the doc

---
#### Tool: **`get_folder`**
Retrieve an existing folder by its ID. Returns the folder's information including title, description, and all docs within it.
Parameters|Type|Description
-|-|-
`id`|`string`|The 12-character alphanumeric ID of the folder

---
#### Tool: **`get_task`**
Retrieve an existing task by its ID. Returns the task's information including title, description, status, priority, dates, custom properties, and more.
Parameters|Type|Description
-|-|-
`id`|`string`|The 12-character alphanumeric ID of the task

---
#### Tool: **`get_view`**
Retrieve an existing view by its ID. Returns the view's information including title, description, and all tasks within it.
Parameters|Type|Description
-|-|-
`id`|`string`|The 12-character alphanumeric ID of the view

---
#### Tool: **`list_docs`**
List docs from Dart with optional filtering parameters. You can filter by folder, title, text content, and more.
Parameters|Type|Description
-|-|-
`folder`|`string` *optional*|Filter by folder title
`folderId`|`string` *optional*|Filter by folder ID
`ids`|`string` *optional*|Filter by IDs
`inTrash`|`boolean` *optional*|Filter by trash status
`limit`|`number` *optional*|Number of results per page
`o`|`array` *optional*|Ordering options (use - prefix for descending)
`offset`|`number` *optional*|Initial index for pagination
`s`|`string` *optional*|Search by title, text, or folder title
`text`|`string` *optional*|Filter by text content
`title`|`string` *optional*|Filter by title

---
#### Tool: **`list_task_comments`**
List comments from Dart with optional filtering parameters. You can filter by author, task, text content, dates, and more.
Parameters|Type|Description
-|-|-
`taskId`|`string`|Filter by task ID
`author`|`string` *optional*|Filter by author name or email
`authorId`|`string` *optional*|Filter by author ID
`ids`|`string` *optional*|Filter by comment IDs
`limit`|`number` *optional*|Number of results per page
`offset`|`number` *optional*|Initial index for pagination
`parentId`|`string` *optional*|Filter by parent comment ID
`publishedAtAfter`|`string` *optional*|Filter by published date after (ISO format)
`publishedAtBefore`|`string` *optional*|Filter by published date before (ISO format)
`task`|`string` *optional*|Filter by task title
`text`|`string` *optional*|Filter by comment text content

---
#### Tool: **`list_tasks`**
List tasks from Dart with optional filtering parameters. You can filter by assignee, status, dartboard, priority, due date, and more.
Parameters|Type|Description
-|-|-
`assignee`|`string` *optional*|Filter by assignee name or email
`assigneeId`|`string` *optional*|Filter by assignee ID
`dartboard`|`string` *optional*|Filter by dartboard title
`dartboardId`|`string` *optional*|Filter by dartboard ID
`description`|`string` *optional*|Filter by description content
`dueAtAfter`|`string` *optional*|Filter by due date after (ISO format)
`dueAtBefore`|`string` *optional*|Filter by due date before (ISO format)
`ids`|`string` *optional*|Filter by IDs
`inTrash`|`boolean` *optional*|Filter by trash status
`isCompleted`|`boolean` *optional*|Filter by completion status
`limit`|`number` *optional*|Number of results per page
`offset`|`number` *optional*|Initial index for pagination
`parentId`|`string` *optional*|Filter by parent task ID
`priority`|`string` *optional*|Filter by priority
`size`|`number` *optional*|Filter by task size
`startAtAfter`|`string` *optional*|Filter by start date after (ISO format)
`startAtBefore`|`string` *optional*|Filter by start date before (ISO format)
`status`|`string` *optional*|Filter by status
`statusId`|`string` *optional*|Filter by status ID
`tag`|`string` *optional*|Filter by tag
`tagId`|`string` *optional*|Filter by tag ID
`title`|`string` *optional*|Filter by title
`type`|`string` *optional*|Filter by task type
`typeId`|`string` *optional*|Filter by task type ID

---
#### Tool: **`update_doc`**
Update an existing doc. You can modify its title, text content, and folder.
Parameters|Type|Description
-|-|-
`id`|`string`|The 12-character alphanumeric ID of the doc
`folder`|`string` *optional*|The title of the folder to place the doc in
`text`|`string` *optional*|The text content of the doc, which can include markdown formatting
`title`|`string` *optional*|The title of the doc

---
#### Tool: **`update_task`**
Update an existing task. You can modify any of its properties including title, description, status, priority, dates, assignees, tags, custom properties, and task relationships.
Parameters|Type|Description
-|-|-
`id`|`string`|The 12-character alphanumeric ID of the task
`assignee`|`string` *optional*|Single assignee name or email (if workspace doesn't allow multiple assignees)
`assignees`|`array` *optional*|Array of assignee names or emails (if workspace allows multiple assignees)
`customProperties`|`object` *optional*|Custom properties to apply to the task. Use the property names from the config. Examples: { 'customCheckboxProperty': true, 'customTextProperty': 'Some text', 'customNumberProperty': 5, 'customSelectProperty': 'Option Name', 'customDatesProperty': '2025-05-10', 'customDatesPropertyWithRange': ['2025-05-01', '2025-05-30'], 'customMultiselectProperty': ['option1', 'option2'], 'customUserProperty': 'user@example.com', 'customMultipleUserProperty': ['user1@example.com', 'user2@example.com'], 'customTimeTrackingProperty': '1:30:00' }
`dartboard`|`string` *optional*|The title of the dartboard (project or list of tasks)
`description`|`string` *optional*|A longer description of the task, which can include markdown formatting
`dueAt`|`string` *optional*|The due date in ISO format (should be at 9:00am in user's timezone)
`parentId`|`string` *optional*|The ID of the parent task
`priority`|`string` *optional*|The priority (Critical, High, Medium, or Low)
`size`|`string` *optional*|The size which represents the amount of work needed
`startAt`|`string` *optional*|The start date in ISO format (should be at 9:00am in user's timezone)
`status`|`string` *optional*|The status from the list of available statuses
`tags`|`array` *optional*|Array of tags to apply to the task
`taskRelationships`|`object` *optional*|Task relationships including subtasks, blockers, duplicates, and related tasks
`title`|`string` *optional*|The title of the task
`type`|`string` *optional*|The type of the task from the list of available types

---
