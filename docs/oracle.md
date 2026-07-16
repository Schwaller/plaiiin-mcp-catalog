Connect to Oracle databases via MCP, providing secure read-only access with support for schema exploration, query execution, and metadata inspection.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/oracle](https://hub.docker.com/repository/docker/mcp/oracle)
**Author**|[git-scarrow](https://github.com/git-scarrow)
**Repository**|https://github.com/samscarrow/oracle-mcp-server

## Available Tools (13)
Tools provided by this Server|Short Description
-|-
`build_dispatch_packet`|Validate a Lab work item and build an execution packet for an external execution plane.|
`check_gates`|Check Pre-Flight Mode and cascade-depth gates for a work item in the backend-owned Lab mirror.|
`describe_table`|Describe columns for a table|
`dispatch_scene`|Create a scene-item row and fire the writers-room entry signal.|
`execute_query`|Execute a SQL query on the Oracle database|
`fail_dispatch_preflight`|Record a preflight failure and restore the work item to a dispatch-ready state.|
`get_dispatchable_items`|List backend-owned Lab work items ready for dispatch.|
`get_table_constraints`|List constraints for a table|
`get_table_indexes`|List indexes for a table|
`handle_final_return`|Ingest a structured execution-plane return payload into the backend-owned Lab mirror.|
`list_schemas`|List all accessible schemas in the Oracle database|
`list_tables`|List database tables from a schema or all accessible schemas|
`stamp_dispatch_consumed`|Accept dispatch start, stamp consumption, and move a work item to In Progress.|

---
## Tools Details

#### Tool: **`build_dispatch_packet`**
Validate a Lab work item and build an execution packet for an external execution plane.
Parameters|Type|Description
-|-|-
`work_item_id`|`string`|Work item UUID

---
#### Tool: **`check_gates`**
Check Pre-Flight Mode and cascade-depth gates for a work item in the backend-owned Lab mirror.
Parameters|Type|Description
-|-|-
`work_item_id`|`string`|Work item UUID

---
#### Tool: **`describe_table`**
Describe columns for a table
Parameters|Type|Description
-|-|-
`table_name`|`string`|Table name
`schema`|`string` *optional*|Schema name (optional)

---
#### Tool: **`dispatch_scene`**
Create a scene-item row and fire the writers-room entry signal.
Parameters|Type|Description
-|-|-
`creative_brief`|`string`|
`scene_name`|`string`|
`season`|`number`|
`task_type`|`string`|
`character_list`|`string` *optional*|
`episode`|`number` *optional*|
`prompt_notes`|`string` *optional*|
`work_item_id`|`string` *optional*|

---
#### Tool: **`execute_query`**
Execute a SQL query on the Oracle database
Parameters|Type|Description
-|-|-
`query`|`string`|SQL query to execute
`maxRows`|`number` *optional*|Maximum number of rows to return (default: 1000)
`params`|`array` *optional*|Query parameters (optional)

---
#### Tool: **`fail_dispatch_preflight`**
Record a preflight failure and restore the work item to a dispatch-ready state.
Parameters|Type|Description
-|-|-
`reason`|`string`|Blocking reason
`run_id`|`string`|Dispatch run UUID
`work_item_id`|`string`|Work item UUID

---
#### Tool: **`get_dispatchable_items`**
List backend-owned Lab work items ready for dispatch.
Parameters|Type|Description
-|-|-
`limit`|`number` *optional*|Maximum items to return (default 25)

---
#### Tool: **`get_table_constraints`**
List constraints for a table
Parameters|Type|Description
-|-|-
`table_name`|`string`|Table name
`schema`|`string` *optional*|Schema name (optional)

---
#### Tool: **`get_table_indexes`**
List indexes for a table
Parameters|Type|Description
-|-|-
`table_name`|`string`|Table name
`schema`|`string` *optional*|Schema name (optional)

---
#### Tool: **`handle_final_return`**
Ingest a structured execution-plane return payload into the backend-owned Lab mirror.
Parameters|Type|Description
-|-|-
`duration_ms`|`number`|
`lane`|`string`|
`model`|`string`|
`raw_output`|`string`|
`run_id`|`string`|
`status`|`string`|
`summary`|`string`|
`work_item_id`|`string`|
`artifacts`|`string` *optional*|
`commit_sha`|`string` *optional*|
`error`|`string` *optional*|
`files_changed`|`string` *optional*|
`metrics`|`string` *optional*|
`pr_url`|`string` *optional*|
`tool_calls`|`string` *optional*|
`verdict`|`string` *optional*|

---
#### Tool: **`list_schemas`**
List all accessible schemas in the Oracle database
#### Tool: **`list_tables`**
List database tables from a schema or all accessible schemas
Parameters|Type|Description
-|-|-
`pattern`|`string` *optional*|Table name pattern with % wildcards (optional)
`schema`|`string` *optional*|Schema name (optional)

---
#### Tool: **`stamp_dispatch_consumed`**
Accept dispatch start, stamp consumption, and move a work item to In Progress.
Parameters|Type|Description
-|-|-
`run_id`|`string`|Dispatch run UUID
`work_item_id`|`string`|Work item UUID

---
