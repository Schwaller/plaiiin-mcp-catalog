MCP support for Temporal. A comprehensive set of tools for interacting with workflows and their adjacent configurations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/temporal](https://hub.docker.com/repository/docker/mcp/temporal)
**Author**|[GethosTheWalrus](https://github.com/GethosTheWalrus)
**Repository**|https://github.com/GethosTheWalrus/temporal-mcp

## Available Tools (29)
Tools provided by this Server|Short Description
-|-
`batch_cancel`|Cancel multiple workflows matching a query with concurrent processing for speed.|
`batch_cancel_activities`|Cancel multiple standalone activities matching a query with concurrent processing for speed.|
`batch_signal`|Send a signal to multiple workflows matching a query.|
`batch_terminate`|Terminate multiple workflows matching a query.|
`batch_terminate_activities`|Terminate multiple standalone activities matching a query.|
`cancel_activity`|Cancel a running standalone activity execution|
`cancel_workflow`|Cancel a running workflow execution|
`continue_as_new`|Signal a workflow to continue as new (restart with new inputs while preserving history link)|
`count_activities`|Count standalone activity executions matching a query|
`create_schedule`|Create a new schedule for periodic workflow execution|
`delete_schedule`|Delete a schedule|
`describe_activity`|Get detailed information about a standalone activity execution|
`describe_workflow`|Get detailed information about a workflow execution|
`execute_activity`|Execute a standalone Temporal activity and wait for result|
`get_activity_result`|Get the result of a standalone activity|
`get_workflow_history`|Get the complete event history of a workflow execution.|
`get_workflow_result`|Get the result of a completed workflow|
`list_activities`|List standalone activity executions based on a query.|
`list_schedules`|List all schedules.|
`list_workflows`|List workflow executions based on a query.|
`pause_schedule`|Pause a schedule|
`query_workflow`|Query a running workflow for its current state|
`signal_workflow`|Send a signal to a running workflow|
`start_activity`|Start a new standalone Temporal activity execution|
`start_workflow`|Start a new Temporal workflow execution|
`terminate_activity`|Forcefully terminate a standalone activity execution|
`terminate_workflow`|Forcefully terminate a workflow execution|
`trigger_schedule`|Manually trigger a scheduled workflow immediately|
`unpause_schedule`|Resume a paused schedule|

---
## Tools Details

#### Tool: **`batch_cancel`**
Cancel multiple workflows matching a query with concurrent processing for speed. Use 'concurrency' to control parallel operations (default: 50).
Parameters|Type|Description
-|-|-
`query`|`string`|Query to select workflows to cancel
`concurrency`|`number` *optional*|Number of workflows to cancel concurrently for faster processing (default: 50, max recommended: 100)
`limit`|`number` *optional*|Maximum number of workflows to cancel (default: 100)

---
#### Tool: **`batch_cancel_activities`**
Cancel multiple standalone activities matching a query with concurrent processing for speed. Use 'concurrency' to control parallel operations (default: 50).
Parameters|Type|Description
-|-|-
`query`|`string`|Query to select activities to cancel
`concurrency`|`number` *optional*|Number of activities to cancel concurrently (default: 50)
`limit`|`number` *optional*|Maximum number of activities to cancel (default: 100)

---
#### Tool: **`batch_signal`**
Send a signal to multiple workflows matching a query. Specify 'limit' to control batch size (default: 100).
Parameters|Type|Description
-|-|-
`query`|`string`|Query to select workflows
`signal_name`|`string`|The signal name to send
`args`|`object` *optional*|Arguments for the signal
`limit`|`number` *optional*|Maximum number of workflows to signal (default: 100)

---
#### Tool: **`batch_terminate`**
Terminate multiple workflows matching a query. Specify 'limit' to control batch size (default: 100).
Parameters|Type|Description
-|-|-
`query`|`string`|Query to select workflows to terminate
`limit`|`number` *optional*|Maximum number of workflows to terminate (default: 100)
`reason`|`string` *optional*|Reason for termination

---
#### Tool: **`batch_terminate_activities`**
Terminate multiple standalone activities matching a query. Specify 'limit' to control batch size (default: 100).
Parameters|Type|Description
-|-|-
`query`|`string`|Query to select activities to terminate
`concurrency`|`number` *optional*|Number of activities to terminate concurrently (default: 50)
`limit`|`number` *optional*|Maximum number of activities to terminate (default: 100)
`reason`|`string` *optional*|Reason for termination

---
#### Tool: **`cancel_activity`**
Cancel a running standalone activity execution
Parameters|Type|Description
-|-|-
`activity_id`|`string`|Standalone activity execution ID
`run_id`|`string` *optional*|Run ID for the standalone activity execution

---
#### Tool: **`cancel_workflow`**
Cancel a running workflow execution
Parameters|Type|Description
-|-|-
`workflow_id`|`string`|The workflow execution ID to cancel

---
#### Tool: **`continue_as_new`**
Signal a workflow to continue as new (restart with new inputs while preserving history link)
Parameters|Type|Description
-|-|-
`signal_name`|`string`|The signal name to send (must be handled by the workflow to trigger continue-as-new)
`workflow_id`|`string`|The workflow ID to continue as new
`signal_args`|`object` *optional*|Arguments for the signal that will trigger continue-as-new

---
#### Tool: **`count_activities`**
Count standalone activity executions matching a query
Parameters|Type|Description
-|-|-
`query`|`string` *optional*|List filter query (e.g., 'TaskQueue = "my-task-queue"')

---
#### Tool: **`create_schedule`**
Create a new schedule for periodic workflow execution
Parameters|Type|Description
-|-|-
`cron`|`string`|Cron expression (e.g., '0 12 * * *')
`schedule_id`|`string`|Unique identifier for the schedule
`task_queue`|`string`|Task queue for the workflow
`workflow_name`|`string`|Name of the workflow to schedule
`args`|`object` *optional*|Arguments for the workflow

---
#### Tool: **`delete_schedule`**
Delete a schedule
Parameters|Type|Description
-|-|-
`schedule_id`|`string`|The schedule ID to delete

---
#### Tool: **`describe_activity`**
Get detailed information about a standalone activity execution
Parameters|Type|Description
-|-|-
`activity_id`|`string`|Standalone activity execution ID
`run_id`|`string` *optional*|Run ID for the standalone activity execution

---
#### Tool: **`describe_workflow`**
Get detailed information about a workflow execution
Parameters|Type|Description
-|-|-
`workflow_id`|`string`|The workflow execution ID to describe

---
#### Tool: **`execute_activity`**
Execute a standalone Temporal activity and wait for result
Parameters|Type|Description
-|-|-
`activity`|`string`|Activity type name to execute
`activity_id`|`string`|Unique identifier for the activity execution
`task_queue`|`string`|Task queue for this activity
`args`|`object` *optional*|Arguments to pass to the activity
`start_to_close_timeout_seconds`|`number` *optional*|Activity start-to-close timeout in seconds

---
#### Tool: **`get_activity_result`**
Get the result of a standalone activity
Parameters|Type|Description
-|-|-
`activity_id`|`string`|Standalone activity execution ID
`run_id`|`string` *optional*|Run ID for the standalone activity execution
`timeout`|`number` *optional*|Optional timeout in seconds while waiting for result

---
#### Tool: **`get_workflow_history`**
Get the complete event history of a workflow execution. Specify 'limit' to control the number of events (default: 1000).
Parameters|Type|Description
-|-|-
`workflow_id`|`string`|The workflow execution ID
`limit`|`number` *optional*|Maximum number of history events to return (default: 1000)

---
#### Tool: **`get_workflow_result`**
Get the result of a completed workflow
Parameters|Type|Description
-|-|-
`workflow_id`|`string`|The workflow execution ID

---
#### Tool: **`list_activities`**
List standalone activity executions based on a query. Specify 'limit' to control results and 'skip' for pagination.
Parameters|Type|Description
-|-|-
`limit`|`number` *optional*|Maximum number of results to return (default: 100)
`query`|`string` *optional*|List filter query (e.g., 'TaskQueue = "my-task-queue"')
`skip`|`number` *optional*|Number of results to skip for pagination (default: 0)

---
#### Tool: **`list_schedules`**
List all schedules. Specify 'limit' to control the number of results (default: 100). Use 'skip' to paginate through results.
Parameters|Type|Description
-|-|-
`limit`|`number` *optional*|Maximum number of schedules to return (default: 100)
`skip`|`number` *optional*|Number of results to skip for pagination (default: 0)

---
#### Tool: **`list_workflows`**
List workflow executions based on a query. Specify 'limit' to control the number of results (default: 100, max recommended: 1000). Use 'skip' to paginate through results.
Parameters|Type|Description
-|-|-
`limit`|`number` *optional*|Maximum number of results to return (default: 100, increase for more results)
`query`|`string` *optional*|List filter query (e.g., 'WorkflowType="MyWorkflow"')
`skip`|`number` *optional*|Number of results to skip for pagination (default: 0)

---
#### Tool: **`pause_schedule`**
Pause a schedule
Parameters|Type|Description
-|-|-
`schedule_id`|`string`|The schedule ID to pause
`note`|`string` *optional*|Note explaining why the schedule was paused

---
#### Tool: **`query_workflow`**
Query a running workflow for its current state
Parameters|Type|Description
-|-|-
`query_name`|`string`|The name of the query to execute
`workflow_id`|`string`|The workflow execution ID to query
`args`|`object` *optional*|Arguments for the query (as JSON object)

---
#### Tool: **`signal_workflow`**
Send a signal to a running workflow
Parameters|Type|Description
-|-|-
`signal_name`|`string`|The name of the signal to send
`workflow_id`|`string`|The workflow execution ID to signal
`args`|`object` *optional*|Arguments for the signal (as JSON object)

---
#### Tool: **`start_activity`**
Start a new standalone Temporal activity execution
Parameters|Type|Description
-|-|-
`activity`|`string`|Activity type name to start
`activity_id`|`string`|Unique identifier for the activity execution
`task_queue`|`string`|Task queue for this activity
`args`|`object` *optional*|Arguments to pass to the activity
`start_to_close_timeout_seconds`|`number` *optional*|Activity start-to-close timeout in seconds

---
#### Tool: **`start_workflow`**
Start a new Temporal workflow execution
Parameters|Type|Description
-|-|-
`task_queue`|`string`|The task queue to use for this workflow
`workflow_id`|`string`|Unique identifier for the workflow execution
`workflow_name`|`string`|The name of the workflow to start
`args`|`object` *optional*|Arguments to pass to the workflow (as JSON object)

---
#### Tool: **`terminate_activity`**
Forcefully terminate a standalone activity execution
Parameters|Type|Description
-|-|-
`activity_id`|`string`|Standalone activity execution ID
`reason`|`string` *optional*|Reason for termination
`run_id`|`string` *optional*|Run ID for the standalone activity execution

---
#### Tool: **`terminate_workflow`**
Forcefully terminate a workflow execution
Parameters|Type|Description
-|-|-
`workflow_id`|`string`|The workflow execution ID to terminate
`reason`|`string` *optional*|Reason for termination

---
#### Tool: **`trigger_schedule`**
Manually trigger a scheduled workflow immediately
Parameters|Type|Description
-|-|-
`schedule_id`|`string`|The schedule ID to trigger

---
#### Tool: **`unpause_schedule`**
Resume a paused schedule
Parameters|Type|Description
-|-|-
`schedule_id`|`string`|The schedule ID to unpause
`note`|`string` *optional*|Note explaining why the schedule was resumed

---
