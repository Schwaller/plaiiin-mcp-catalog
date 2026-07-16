Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. .

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/opik](https://hub.docker.com/repository/docker/mcp/opik)
**Author**|[comet-ml](https://github.com/comet-ml)
**Repository**|https://github.com/comet-ml/opik-mcp

## Available Tools (13)
Tools provided by this Server|Short Description
-|-
`add-trace-feedback`|Add feedback scores to a trace for quality evaluation and monitoring.|
`create-project`|Create a new project|
`create-prompt`|Create a new prompt|
`get-prompt-version`|Retrieve a specific version of a prompt|
`get-prompts`|Get a list of prompts with optional filtering|
`get-trace-by-id`|Get detailed information about a specific trace including input, output, metadata, and timing information|
`get-trace-stats`|Get aggregated statistics for traces including counts, costs, token usage, and performance metrics over time|
`get-trace-threads`|Get trace threads (conversation groupings) to view related traces that belong to the same conversation or session|
`list-projects`|Get a list of projects with optional filtering|
`list-traces`|Get a list of traces from a project.|
`opik-integration-docs`|Provides detailed documentation on how to integrate Opik with your LLM application|
`save-prompt-version`|Save a new version of a prompt|
`search-traces`|Advanced search for traces with complex filtering and query capabilities|

---
## Tools Details

#### Tool: **`add-trace-feedback`**
Add feedback scores to a trace for quality evaluation and monitoring. Useful for rating trace quality, relevance, or custom metrics
Parameters|Type|Description
-|-|-
`scores`|`array`|Array of feedback scores to add. Each score should have a name and value between 0-1
`traceId`|`string`|ID of the trace to add feedback to
`workspaceName`|`string` *optional*|Workspace name to use instead of the default

---
#### Tool: **`create-project`**
Create a new project
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the project
`description`|`string` *optional*|Description of the project
`workspaceName`|`string` *optional*|Workspace name to use instead of the default

---
#### Tool: **`create-prompt`**
Create a new prompt
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the prompt
`description`|`string` *optional*|Description of the prompt
`tags`|`array` *optional*|List of tags for the prompt

---
#### Tool: **`get-prompt-version`**
Retrieve a specific version of a prompt
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the prompt
`commit`|`string` *optional*|Specific commit/version to retrieve

---
#### Tool: **`get-prompts`**
Get a list of prompts with optional filtering
Parameters|Type|Description
-|-|-
`name`|`string` *optional*|Filter by prompt name
`page`|`number` *optional*|Page number for pagination
`size`|`number` *optional*|Number of items per page

---
#### Tool: **`get-trace-by-id`**
Get detailed information about a specific trace including input, output, metadata, and timing information
Parameters|Type|Description
-|-|-
`traceId`|`string`|ID of the trace to fetch (UUID format, e.g. "123e4567-e89b-12d3-a456-426614174000")
`workspaceName`|`string` *optional*|Workspace name to use instead of the default workspace

---
#### Tool: **`get-trace-stats`**
Get aggregated statistics for traces including counts, costs, token usage, and performance metrics over time
Parameters|Type|Description
-|-|-
`endDate`|`string` *optional*|End date in ISO format (YYYY-MM-DD). Example: "2024-01-31"
`projectId`|`string` *optional*|Project ID to filter traces. If not provided, will use the first available project
`projectName`|`string` *optional*|Project name to filter traces (alternative to projectId)
`startDate`|`string` *optional*|Start date in ISO format (YYYY-MM-DD). Example: "2024-01-01"
`workspaceName`|`string` *optional*|Workspace name to use instead of the default workspace

---
#### Tool: **`get-trace-threads`**
Get trace threads (conversation groupings) to view related traces that belong to the same conversation or session
Parameters|Type|Description
-|-|-
`page`|`number` *optional*|Page number for pagination
`projectId`|`string` *optional*|Project ID to filter threads
`projectName`|`string` *optional*|Project name to filter threads
`size`|`number` *optional*|Number of threads per page
`threadId`|`string` *optional*|Specific thread ID to retrieve (useful for getting all traces in a conversation)
`workspaceName`|`string` *optional*|Workspace name to use instead of the default

---
#### Tool: **`list-projects`**
Get a list of projects with optional filtering
Parameters|Type|Description
-|-|-
`page`|`number` *optional*|Page number for pagination
`size`|`number` *optional*|Number of items per page
`workspaceName`|`string` *optional*|Workspace name to use instead of the default

---
#### Tool: **`list-traces`**
Get a list of traces from a project. Use this for basic trace retrieval and overview
Parameters|Type|Description
-|-|-
`page`|`number` *optional*|Page number for pagination (starts at 1)
`projectId`|`string` *optional*|Project ID to filter traces. If not provided, will use the first available project
`projectName`|`string` *optional*|Project name to filter traces (alternative to projectId). Example: "My AI Assistant"
`size`|`number` *optional*|Number of traces per page (1-100, default 10)
`workspaceName`|`string` *optional*|Workspace name to use instead of the default workspace

---
#### Tool: **`opik-integration-docs`**
Provides detailed documentation on how to integrate Opik with your LLM application
#### Tool: **`save-prompt-version`**
Save a new version of a prompt
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the prompt
`template`|`string`|Template content for the prompt version
`change_description`|`string` *optional*|Description of changes in this version
`metadata`|`object` *optional*|Additional metadata for the prompt version
`type`|`string` *optional*|Template type

---
#### Tool: **`search-traces`**
Advanced search for traces with complex filtering and query capabilities
Parameters|Type|Description
-|-|-
`filters`|`object` *optional*|Advanced filters as key-value pairs. Examples: {"status": "error"}, {"model": "gpt-4"}, {"duration_ms": {"$gt": 1000}}
`page`|`number` *optional*|Page number for pagination
`projectId`|`string` *optional*|Project ID to search within
`projectName`|`string` *optional*|Project name to search within
`query`|`string` *optional*|Text query to search in trace names, inputs, outputs, and metadata. Example: "error" or "user_query:hello"
`size`|`number` *optional*|Number of traces per page (max 100)
`sortBy`|`string` *optional*|Field to sort by. Options: "created_at", "duration", "name", "status"
`sortOrder`|`string` *optional*|Sort order: ascending or descending
`workspaceName`|`string` *optional*|Workspace name to use instead of the default

---
