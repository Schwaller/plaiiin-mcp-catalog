Bridges n8n's workflow automation platform with AI models, providing access to 543 n8n nodes, workflow templates, and AI-capable automation tools.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/n8n](https://hub.docker.com/repository/docker/mcp/n8n)
**Author**|[czlonkowski](https://github.com/czlonkowski)
**Repository**|https://github.com/czlonkowski/n8n-mcp

## Available Tools (42)
Tools provided by this Server|Short Description
-|-
`get_database_statistics`|Node stats: 525 total, 263 AI tools, 104 triggers, 87% docs coverage.|
`get_node_as_tool_info`|How to use ANY node as AI tool.|
`get_node_documentation`|Get readable docs with examples/auth/patterns.|
`get_node_essentials`|Get node essential info with optional real-world examples from templates.|
`get_node_info`|Get full node documentation.|
`get_property_dependencies`|Shows property dependencies and visibility rules.|
`get_template`|Get template by ID.|
`get_templates_for_task`|Curated templates by task.|
`list_ai_tools`|List 263 AI-optimized nodes.|
`list_node_templates`|Find templates using specific nodes.|
`list_nodes`|List n8n nodes.|
`list_tasks`|List task templates by category: HTTP/API, Webhooks, Database, AI, Data Processing, Communication.|
`list_templates`|List all templates with minimal data (id, name, description, views, node count).|
`n8n_autofix_workflow`|Automatically fix common workflow validation errors.|
`n8n_create_workflow`|Create workflow.|
`n8n_delete_execution`|Delete an execution record.|
`n8n_delete_workflow`|Permanently delete a workflow.|
`n8n_diagnostic`|Diagnose n8n API config.|
`n8n_get_execution`|Get execution details with smart filtering.|
`n8n_get_workflow`|Get a workflow by ID.|
`n8n_get_workflow_details`|Get workflow details with metadata, version, execution stats.|
`n8n_get_workflow_minimal`|Get minimal info: ID, name, active status, tags.|
`n8n_get_workflow_structure`|Get workflow structure: nodes and connections only.|
`n8n_health_check`|Check n8n instance health and API connectivity.|
`n8n_list_available_tools`|List available n8n tools and capabilities.|
`n8n_list_executions`|List workflow executions (returns up to limit).|
`n8n_list_workflows`|List workflows (minimal metadata only).|
`n8n_trigger_webhook_workflow`|Trigger workflow via webhook.|
`n8n_update_full_workflow`|Full workflow update.|
`n8n_update_partial_workflow`|Update workflow incrementally with diff operations.|
`n8n_validate_workflow`|Validate workflow by ID.|
`n8n_workflow_versions`|Manage workflow version history, rollback, and cleanup.|
`search_node_properties`|Find specific properties in a node (auth, headers, body, etc).|
`search_nodes`|Search n8n nodes by keyword with optional real-world examples.|
`search_templates`|Search templates by name/description keywords.|
`search_templates_by_metadata`|Search templates by AI-generated metadata.|
`tools_documentation`|Get documentation for n8n MCP tools.|
`validate_node_minimal`|Check n8n node required fields.|
`validate_node_operation`|Validate n8n node configuration.|
`validate_workflow`|Full workflow validation: structure, connections, expressions, AI tools.|
`validate_workflow_connections`|Check workflow connections only: valid nodes, no cycles, proper triggers, AI tool links.|
`validate_workflow_expressions`|Validate n8n expressions: syntax {{}}, variables ($json/$node), references.|

---
## Tools Details

#### Tool: **`get_database_statistics`**
Node stats: 525 total, 263 AI tools, 104 triggers, 87% docs coverage. Verifies MCP working.
#### Tool: **`get_node_as_tool_info`**
How to use ANY node as AI tool. Shows requirements, use cases, examples. Works for all nodes, not just AI-marked ones.
Parameters|Type|Description
-|-|-
`nodeType`|`string`|Full node type WITH prefix: "nodes-base.slack", "nodes-base.googleSheets", etc.

---
#### Tool: **`get_node_documentation`**
Get readable docs with examples/auth/patterns. Better than raw schema! 87% coverage. Format: "nodes-base.slack"
Parameters|Type|Description
-|-|-
`nodeType`|`string`|Full type with prefix: "nodes-base.slack"

---
#### Tool: **`get_node_essentials`**
Get node essential info with optional real-world examples from templates. Pass nodeType as string with prefix. Example: nodeType="nodes-base.slack". Use includeExamples=true to get top 3 template configs.
Parameters|Type|Description
-|-|-
`nodeType`|`string`|Full type: "nodes-base.httpRequest"
`includeExamples`|`boolean` *optional*|Include top 3 real-world configuration examples from popular templates (default: false)

---
#### Tool: **`get_node_info`**
Get full node documentation. Pass nodeType as string with prefix. Example: nodeType="nodes-base.webhook"
Parameters|Type|Description
-|-|-
`nodeType`|`string`|Full type: "nodes-base.{name}" or "nodes-langchain.{name}". Examples: nodes-base.httpRequest, nodes-base.webhook, nodes-base.slack

---
#### Tool: **`get_property_dependencies`**
Shows property dependencies and visibility rules. Example: sendBody=true reveals body fields. Test visibility with optional config.
Parameters|Type|Description
-|-|-
`nodeType`|`string`|The node type to analyze (e.g., "nodes-base.httpRequest")
`config`|`object` *optional*|Optional partial configuration to check visibility impact

---
#### Tool: **`get_template`**
Get template by ID. Use mode to control response size: nodes_only (minimal), structure (nodes+connections), full (complete workflow).
Parameters|Type|Description
-|-|-
`templateId`|`number`|The template ID to retrieve
`mode`|`string` *optional*|Response detail level. nodes_only: just node list, structure: nodes+connections, full: complete workflow JSON.

---
#### Tool: **`get_templates_for_task`**
Curated templates by task. Returns paginated results sorted by popularity.
Parameters|Type|Description
-|-|-
`task`|`string`|The type of task to get templates for
`limit`|`number` *optional*|Maximum number of results. Default 10.
`offset`|`number` *optional*|Pagination offset. Default 0.

---
#### Tool: **`list_ai_tools`**
List 263 AI-optimized nodes. Note: ANY node can be AI tool! Connect any node to AI Agent's tool port. Community nodes need N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true.
#### Tool: **`list_node_templates`**
Find templates using specific nodes. Returns paginated results. Use FULL types: "n8n-nodes-base.httpRequest".
Parameters|Type|Description
-|-|-
`nodeTypes`|`array`|Array of node types to search for (e.g., ["n8n-nodes-base.httpRequest", "n8n-nodes-base.openAi"])
`limit`|`number` *optional*|Maximum number of templates to return. Default 10.
`offset`|`number` *optional*|Pagination offset. Default 0.

---
#### Tool: **`list_nodes`**
List n8n nodes. Common: list_nodes({limit:200}) for all, list_nodes({category:'trigger'}) for triggers. Package: "n8n-nodes-base" or "@n8n/n8n-nodes-langchain". Categories: trigger/transform/output/input.
Parameters|Type|Description
-|-|-
`category`|`string` *optional*|trigger|transform|output|input|AI
`developmentStyle`|`string` *optional*|Usually "programmatic"
`isAITool`|`boolean` *optional*|Filter AI-capable nodes
`limit`|`number` *optional*|Max results (default 50, use 200+ for all)
`package`|`string` *optional*|"n8n-nodes-base" (core) or "@n8n/n8n-nodes-langchain" (AI)

---
#### Tool: **`list_tasks`**
List task templates by category: HTTP/API, Webhooks, Database, AI, Data Processing, Communication.
Parameters|Type|Description
-|-|-
`category`|`string` *optional*|Filter by category (optional)

---
#### Tool: **`list_templates`**
List all templates with minimal data (id, name, description, views, node count). Optionally include AI-generated metadata for smart filtering.
Parameters|Type|Description
-|-|-
`includeMetadata`|`boolean` *optional*|Include AI-generated metadata (categories, complexity, setup time, etc.). Default false.
`limit`|`number` *optional*|Number of results (1-100). Default 10.
`offset`|`number` *optional*|Pagination offset. Default 0.
`sortBy`|`string` *optional*|Sort field. Default: views (popularity).

---
#### Tool: **`n8n_autofix_workflow`**
Automatically fix common workflow validation errors. Preview fixes or apply them. Fixes expression format, typeVersion, error output config, webhook paths.
Parameters|Type|Description
-|-|-
`id`|`string`|Workflow ID to fix
`applyFixes`|`boolean` *optional*|Apply fixes to workflow (default: false - preview mode)
`confidenceThreshold`|`string` *optional*|Minimum confidence level for fixes (default: medium)
`fixTypes`|`array` *optional*|Types of fixes to apply (default: all)
`maxFixes`|`number` *optional*|Maximum number of fixes to apply (default: 50)

---
#### Tool: **`n8n_create_workflow`**
Create workflow. Requires: name, nodes[], connections{}. Created inactive. Returns workflow with ID.
Parameters|Type|Description
-|-|-
`connections`|`object`|Workflow connections object. Keys are source node IDs, values define output connections
`name`|`string`|Workflow name (required)
`nodes`|`array`|Array of workflow nodes. Each node must have: id, name, type, typeVersion, position, and parameters
`settings`|`object` *optional*|Optional workflow settings (execution order, timezone, error handling)

---
#### Tool: **`n8n_delete_execution`**
Delete an execution record. This only removes the execution history, not any data processed.
Parameters|Type|Description
-|-|-
`id`|`string`|Execution ID to delete

---
#### Tool: **`n8n_delete_workflow`**
Permanently delete a workflow. This action cannot be undone.
Parameters|Type|Description
-|-|-
`id`|`string`|Workflow ID to delete

---
#### Tool: **`n8n_diagnostic`**
Diagnose n8n API config. Shows tool status, API connectivity, env vars. Helps troubleshoot missing tools.
Parameters|Type|Description
-|-|-
`verbose`|`boolean` *optional*|Include detailed debug information (default: false)

---
#### Tool: **`n8n_get_execution`**
Get execution details with smart filtering. RECOMMENDED: Use mode='preview' first to assess data size.
Examples:
- {id, mode:'preview'} - Structure & counts (fast, no data)
- {id, mode:'summary'} - 2 samples per node (default)
- {id, mode:'filtered', itemsLimit:5} - 5 items per node
- {id, nodeNames:['HTTP Request']} - Specific node only
- {id, mode:'full'} - Complete data (use with caution)
Parameters|Type|Description
-|-|-
`id`|`string`|Execution ID
`includeData`|`boolean` *optional*|Legacy: Include execution data. Maps to mode=summary if true (deprecated, use mode instead)
`includeInputData`|`boolean` *optional*|Include input data in addition to output (default: false)
`itemsLimit`|`number` *optional*|Items per node: 0=structure only, 2=default, -1=unlimited (for filtered mode)
`mode`|`string` *optional*|Data retrieval mode: preview=structure only, summary=2 items, filtered=custom, full=all data
`nodeNames`|`array` *optional*|Filter to specific nodes by name (for filtered mode)

---
#### Tool: **`n8n_get_workflow`**
Get a workflow by ID. Returns the complete workflow including nodes, connections, and settings.
Parameters|Type|Description
-|-|-
`id`|`string`|Workflow ID

---
#### Tool: **`n8n_get_workflow_details`**
Get workflow details with metadata, version, execution stats. More info than get_workflow.
Parameters|Type|Description
-|-|-
`id`|`string`|Workflow ID

---
#### Tool: **`n8n_get_workflow_minimal`**
Get minimal info: ID, name, active status, tags. Fast for listings.
Parameters|Type|Description
-|-|-
`id`|`string`|Workflow ID

---
#### Tool: **`n8n_get_workflow_structure`**
Get workflow structure: nodes and connections only. No parameter details.
Parameters|Type|Description
-|-|-
`id`|`string`|Workflow ID

---
#### Tool: **`n8n_health_check`**
Check n8n instance health and API connectivity. Returns status and available features.
#### Tool: **`n8n_list_available_tools`**
List available n8n tools and capabilities.
#### Tool: **`n8n_list_executions`**
List workflow executions (returns up to limit). Check hasMore/nextCursor for pagination.
Parameters|Type|Description
-|-|-
`cursor`|`string` *optional*|Pagination cursor from previous response
`includeData`|`boolean` *optional*|Include execution data (default: false)
`limit`|`number` *optional*|Number of executions to return (1-100, default: 100)
`projectId`|`string` *optional*|Filter by project ID (enterprise feature)
`status`|`string` *optional*|Filter by execution status
`workflowId`|`string` *optional*|Filter by workflow ID

---
#### Tool: **`n8n_list_workflows`**
List workflows (minimal metadata only). Returns id/name/active/dates/tags. Check hasMore/nextCursor for pagination.
Parameters|Type|Description
-|-|-
`active`|`boolean` *optional*|Filter by active status
`cursor`|`string` *optional*|Pagination cursor from previous response
`excludePinnedData`|`boolean` *optional*|Exclude pinned data from response (default: true)
`limit`|`number` *optional*|Number of workflows to return (1-100, default: 100)
`projectId`|`string` *optional*|Filter by project ID (enterprise feature)
`tags`|`array` *optional*|Filter by tags (exact match)

---
#### Tool: **`n8n_trigger_webhook_workflow`**
Trigger workflow via webhook. Must be ACTIVE with Webhook node. Method must match config.
Parameters|Type|Description
-|-|-
`webhookUrl`|`string`|Full webhook URL from n8n workflow (e.g., https://n8n.example.com/webhook/abc-def-ghi)
`data`|`object` *optional*|Data to send with the webhook request
`headers`|`object` *optional*|Additional HTTP headers
`httpMethod`|`string` *optional*|HTTP method (must match webhook configuration, often GET)
`waitForResponse`|`boolean` *optional*|Wait for workflow completion (default: true)

---
#### Tool: **`n8n_update_full_workflow`**
Full workflow update. Requires complete nodes[] and connections{}. For incremental use n8n_update_partial_workflow.
Parameters|Type|Description
-|-|-
`id`|`string`|Workflow ID to update
`connections`|`object` *optional*|Complete connections object (required if modifying workflow structure)
`name`|`string` *optional*|New workflow name
`nodes`|`array` *optional*|Complete array of workflow nodes (required if modifying workflow structure)
`settings`|`object` *optional*|Workflow settings to update

---
#### Tool: **`n8n_update_partial_workflow`**
Update workflow incrementally with diff operations. Types: addNode, removeNode, updateNode, moveNode, enable/disableNode, addConnection, removeConnection, updateSettings, updateName, add/removeTag. See tools_documentation("n8n_update_partial_workflow", "full") for details.
Parameters|Type|Description
-|-|-
`id`|`string`|Workflow ID to update
`operations`|`array`|Array of diff operations to apply. Each operation must have a "type" field and relevant properties for that operation type.
`continueOnError`|`boolean` *optional*|If true, apply valid operations even if some fail (best-effort mode). Returns applied and failed operation indices. Default: false (atomic)
`validateOnly`|`boolean` *optional*|If true, only validate operations without applying them

---
#### Tool: **`n8n_validate_workflow`**
Validate workflow by ID. Checks nodes, connections, expressions. Returns errors/warnings/suggestions.
Parameters|Type|Description
-|-|-
`id`|`string`|Workflow ID to validate
`options`|`object` *optional*|Validation options

---
#### Tool: **`n8n_workflow_versions`**
Manage workflow version history, rollback, and cleanup. Six modes:
- list: Show version history for a workflow
- get: Get details of specific version
- rollback: Restore workflow to previous version (creates backup first)
- delete: Delete specific version or all versions for a workflow
- prune: Manually trigger pruning to keep N most recent versions
- truncate: Delete ALL versions for ALL workflows (requires confirmation)
Parameters|Type|Description
-|-|-
`mode`|`string`|Operation mode
`confirmTruncate`|`boolean` *optional*|REQUIRED: Must be true to truncate all versions (truncate mode only)
`deleteAll`|`boolean` *optional*|Delete all versions for workflow (delete mode only)
`limit`|`number` *optional*|Max versions to return in list mode
`maxVersions`|`number` *optional*|Keep N most recent versions (prune mode only)
`validateBefore`|`boolean` *optional*|Validate workflow structure before rollback
`versionId`|`number` *optional*|Version ID (required for get mode and single version delete, optional for rollback)
`workflowId`|`string` *optional*|Workflow ID (required for list, rollback, delete, prune)

---
#### Tool: **`search_node_properties`**
Find specific properties in a node (auth, headers, body, etc). Returns paths and descriptions.
Parameters|Type|Description
-|-|-
`nodeType`|`string`|Full type with prefix
`query`|`string`|Property to find: "auth", "header", "body", "json"
`maxResults`|`number` *optional*|Max results (default 20)

---
#### Tool: **`search_nodes`**
Search n8n nodes by keyword with optional real-world examples. Pass query as string. Example: query="webhook" or query="database". Returns max 20 results. Use includeExamples=true to get top 2 template configs per node.
Parameters|Type|Description
-|-|-
`query`|`string`|Search terms. Use quotes for exact phrase.
`includeExamples`|`boolean` *optional*|Include top 2 real-world configuration examples from popular templates (default: false)
`limit`|`number` *optional*|Max results (default 20)
`mode`|`string` *optional*|OR=any word, AND=all words, FUZZY=typo-tolerant

---
#### Tool: **`search_templates`**
Search templates by name/description keywords. Returns paginated results. NOT for node types! For nodes use list_node_templates.
Parameters|Type|Description
-|-|-
`query`|`string`|Search keyword as string. Example: "chatbot"
`fields`|`array` *optional*|Fields to include in response. Default: all fields. Example: ["id", "name"] for minimal response.
`limit`|`number` *optional*|Maximum number of results. Default 20.
`offset`|`number` *optional*|Pagination offset. Default 0.

---
#### Tool: **`search_templates_by_metadata`**
Search templates by AI-generated metadata. Filter by category, complexity, setup time, services, or audience. Returns rich metadata for smart template discovery.
Parameters|Type|Description
-|-|-
`category`|`string` *optional*|Filter by category (e.g., "automation", "integration", "data processing")
`complexity`|`string` *optional*|Filter by complexity level
`limit`|`number` *optional*|Maximum number of results. Default 20.
`maxSetupMinutes`|`number` *optional*|Maximum setup time in minutes
`minSetupMinutes`|`number` *optional*|Minimum setup time in minutes
`offset`|`number` *optional*|Pagination offset. Default 0.
`requiredService`|`string` *optional*|Filter by required service (e.g., "openai", "slack", "google")
`targetAudience`|`string` *optional*|Filter by target audience (e.g., "developers", "marketers", "analysts")

---
#### Tool: **`tools_documentation`**
Get documentation for n8n MCP tools. Call without parameters for quick start guide. Use topic parameter to get documentation for specific tools. Use depth='full' for comprehensive documentation.
Parameters|Type|Description
-|-|-
`depth`|`string` *optional*|Level of detail. "essentials" (default) for quick reference, "full" for comprehensive docs.
`topic`|`string` *optional*|Tool name (e.g., "search_nodes") or "overview" for general guide. Leave empty for quick reference.

---
#### Tool: **`validate_node_minimal`**
Check n8n node required fields. Pass nodeType as string and config as empty object {}. Example: nodeType="nodes-base.webhook", config={}
Parameters|Type|Description
-|-|-
`config`|`object`|Configuration object. Always pass {} for empty config
`nodeType`|`string`|Node type as string. Example: "nodes-base.slack"

---
#### Tool: **`validate_node_operation`**
Validate n8n node configuration. Pass nodeType as string and config as object. Example: nodeType="nodes-base.slack", config={resource:"channel",operation:"create"}
Parameters|Type|Description
-|-|-
`config`|`object`|Configuration as object. For simple nodes use {}. For complex nodes include fields like {resource:"channel",operation:"create"}
`nodeType`|`string`|Node type as string. Example: "nodes-base.slack"
`profile`|`string` *optional*|Profile string: "minimal", "runtime", "ai-friendly", or "strict". Default is "ai-friendly"

---
#### Tool: **`validate_workflow`**
Full workflow validation: structure, connections, expressions, AI tools. Returns errors/warnings/fixes. Essential before deploy.
Parameters|Type|Description
-|-|-
`workflow`|`object`|The complete workflow JSON to validate. Must include nodes array and connections object.
`options`|`object` *optional*|Optional validation settings

---
#### Tool: **`validate_workflow_connections`**
Check workflow connections only: valid nodes, no cycles, proper triggers, AI tool links. Fast structure validation.
Parameters|Type|Description
-|-|-
`workflow`|`object`|The workflow JSON with nodes array and connections object.

---
#### Tool: **`validate_workflow_expressions`**
Validate n8n expressions: syntax {{}}, variables ($json/$node), references. Returns errors with locations.
Parameters|Type|Description
-|-|-
`workflow`|`object`|The workflow JSON to check for expression errors.

---

## Screenshots

![n8n screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/n8n-1.png)
