Documentation on AgentCore platform services.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/amazon-bedrock-agentcore-mcp-server](https://hub.docker.com/repository/docker/mcp/amazon-bedrock-agentcore-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (122)
Tools provided by this Server|Short Description
-|-
`browser_click`|Click an element identified by its accessibility ref.|
`browser_close`|Close the current page.|
`browser_console_messages`|Get recent browser console messages.|
`browser_evaluate`|Execute a JavaScript expression in the page context.|
`browser_fill_form`|Fill multiple form fields in one action.|
`browser_handle_dialog`|Configure how JavaScript dialogs are handled for a session.|
`browser_hover`|Hover over an element identified by its accessibility ref.|
`browser_mouse_wheel`|Scroll the page by the specified pixel amounts.|
`browser_navigate`|Navigate to a URL in the browser.|
`browser_navigate_back`|Navigate back in browser history.|
`browser_navigate_forward`|Navigate forward in browser history.|
`browser_network_requests`|List recent network requests and their status.|
`browser_press_key`|Press a keyboard key or key combination.|
`browser_resize`|Resize the browser viewport.|
`browser_select_option`|Select an option from a dropdown or combobox.|
`browser_snapshot`|Capture an accessibility tree snapshot of the current page.|
`browser_tabs`|Manage browser tabs: list, create, select, or close tabs.|
`browser_take_screenshot`|Capture a visual screenshot of the page.|
`browser_type`|Type text into an element identified by its accessibility ref.|
`browser_upload_file`|Upload files to a file input element identified by its ref.|
`browser_wait_for`|Wait for text to appear or an element to become visible.|
`create_agent_runtime`|Create a new AgentCore Runtime to host an agent or tool.|
`create_agent_runtime_endpoint`|Create a custom endpoint for an AgentCore Runtime.|
`delete_agent_runtime`|Delete an AgentCore Runtime and all its versions.|
`delete_agent_runtime_endpoint`|Delete a runtime endpoint.|
`download_file`|Download a file from the sandboxed code interpreter session.|
`execute_code`|Execute code in a sandboxed code interpreter session.|
`execute_command`|Execute a shell command in a sandboxed code interpreter session.|
`fetch_agentcore_doc`|Fetch full document content by URL.|
`gateway_create`|Create a new AgentCore Gateway resource.|
`gateway_delete`|Delete an AgentCore Gateway.|
`gateway_get`|Get details of an AgentCore Gateway.|
`gateway_list`|List all AgentCore Gateways in the account.|
`gateway_resource_policy_delete`|Delete the resource-based policy attached to a gateway.|
`gateway_resource_policy_get`|Get the resource-based policy attached to a gateway.|
`gateway_resource_policy_put`|Create or update a resource-based policy on a gateway.|
`gateway_target_create`|Create a new gateway target to expose tools through a gateway.|
`gateway_target_delete`|Delete a gateway target.|
`gateway_target_get`|Get details of a gateway target.|
`gateway_target_list`|List all targets attached to a gateway.|
`gateway_target_synchronize`|Explicitly synchronize gateway targets with their upstream tool catalog.|
`gateway_target_update`|Update an existing gateway target.|
`gateway_update`|Update an AgentCore Gateway.|
`get_agent_runtime`|Get details of an AgentCore Runtime including its configuration.|
`get_agent_runtime_endpoint`|Get details of a specific runtime endpoint.|
`get_browser_session`|Get the status and metadata of a browser session.|
`get_code_interpreter_session`|Get the status and details of a code interpreter session.|
`get_gateway_guide`|Get the comprehensive AgentCore Gateway guide.|
`get_identity_guide`|Get the comprehensive AgentCore Identity guide.|
`get_memory_guide`|Get the comprehensive AgentCore Memory guide.|
`get_policy_guide`|Get the comprehensive AgentCore Policy guide.|
`get_runtime_guide`|Get a comprehensive reference guide for AgentCore Runtime.|
`identity_create_api_key_provider`|Create an API key credential provider in AgentCore Identity.|
`identity_create_oauth2_provider`|Create an OAuth2 credential provider in AgentCore Identity.|
`identity_create_workload_identity`|Create a new AgentCore workload identity.|
`identity_delete_api_key_provider`|Permanently delete an API key credential provider.|
`identity_delete_oauth2_provider`|Permanently delete an OAuth2 credential provider.|
`identity_delete_resource_policy`|Permanently delete the resource-based policy on an AgentCore resource.|
`identity_delete_workload_identity`|Permanently delete an AgentCore workload identity.|
`identity_get_api_key_provider`|Get metadata for an API key credential provider.|
`identity_get_oauth2_provider`|Get metadata for an OAuth2 credential provider.|
`identity_get_resource_policy`|Get the resource-based policy attached to an AgentCore resource.|
`identity_get_token_vault`|Get details of an AgentCore Identity token vault.|
`identity_get_workload_identity`|Get details of an AgentCore workload identity.|
`identity_list_api_key_providers`|List API key credential providers in the account.|
`identity_list_oauth2_providers`|List OAuth2 credential providers in the account.|
`identity_list_workload_identities`|List AgentCore workload identities in the account.|
`identity_put_resource_policy`|Create or replace the resource-based policy on an AgentCore resource.|
`identity_set_token_vault_cmk`|Set the customer master key (CMK) for an AgentCore Identity token vault.|
`identity_update_api_key_provider`|Update the API key stored in an existing credential provider.|
`identity_update_oauth2_provider`|Update an OAuth2 credential provider's configuration.|
`identity_update_workload_identity`|Update an AgentCore workload identity.|
`install_packages`|Install Python packages in a sandboxed code interpreter session.|
`invoke_agent_runtime`|Invoke an agent hosted in AgentCore Runtime.|
`list_agent_runtime_endpoints`|List all endpoints for an AgentCore Runtime.|
`list_agent_runtime_versions`|List all versions of a specific AgentCore Runtime.|
`list_agent_runtimes`|List all AgentCore Runtimes in the account.|
`list_browser_sessions`|List active browser sessions.|
`list_code_interpreter_sessions`|List code interpreter sessions with optional filtering.|
`memory_batch_create_records`|Batch create memory records in an AgentCore Memory resource.|
`memory_batch_delete_records`|Batch delete memory records from an AgentCore Memory resource.|
`memory_batch_update_records`|Batch update memory records in an AgentCore Memory resource.|
`memory_create`|Create a new AgentCore Memory resource.|
`memory_create_event`|Create an event in an AgentCore Memory resource (short-term memory).|
`memory_delete`|Delete an AgentCore Memory resource.|
`memory_delete_event`|Permanently delete an event from an AgentCore Memory resource.|
`memory_delete_record`|Permanently delete a memory record from an AgentCore Memory resource.|
`memory_get`|Get details of an AgentCore Memory resource.|
`memory_get_event`|Get a specific event from an AgentCore Memory resource.|
`memory_get_record`|Get a specific memory record from an AgentCore Memory resource.|
`memory_list`|List all AgentCore Memory resources in the account.|
`memory_list_actors`|List all actors in an AgentCore Memory resource.|
`memory_list_events`|List events in an AgentCore Memory resource.|
`memory_list_extraction_jobs`|List memory extraction jobs for an AgentCore Memory resource.|
`memory_list_records`|List memory records in an AgentCore Memory resource.|
`memory_list_sessions`|List sessions for an actor in an AgentCore Memory resource.|
`memory_retrieve_records`|Semantic search for memory records in an AgentCore Memory resource.|
`memory_start_extraction_job`|Start (or restart) a memory extraction job.|
`memory_update`|Update an AgentCore Memory resource.|
`policy_create`|Create a Cedar policy within an AgentCore Policy Engine.|
`policy_delete`|Delete a Cedar policy.|
`policy_engine_create`|Create a new AgentCore Policy Engine.|
`policy_engine_delete`|Delete an AgentCore Policy Engine.|
`policy_engine_get`|Get details of an AgentCore Policy Engine.|
`policy_engine_list`|List AgentCore Policy Engines in the account.|
`policy_engine_update`|Update an AgentCore Policy Engine.|
`policy_generation_get`|Get details of an AgentCore Policy Generation.|
`policy_generation_list`|List policy generations within a Policy Engine.|
`policy_generation_list_assets`|List Cedar policies and findings produced by policy generation.|
`policy_generation_start`|Start an AI-powered Cedar policy generation from natural language.|
`policy_get`|Get details of a Cedar policy.|
`policy_list`|List Cedar policies within a Policy Engine.|
`policy_update`|Update a Cedar policy.|
`search_agentcore_docs`|Search curated AgentCore documentation and return ranked results with snippets.|
`start_browser_session`|Start a cloud browser session via Amazon Bedrock AgentCore.|
`start_code_interpreter_session`|Start a new sandboxed code interpreter session.|
`stop_browser_session`|Stop a browser session and release resources.|
`stop_code_interpreter_session`|Stop a running code interpreter session and release its resources.|
`stop_runtime_session`|Stop a running runtime session to release its microVM.|
`update_agent_runtime`|Update an AgentCore Runtime, creating a new immutable version.|
`update_agent_runtime_endpoint`|Update an endpoint to point to a different runtime version.|
`upload_file`|Upload a file to the sandboxed code interpreter session.|

---
## Tools Details

#### Tool: **`browser_click`**
Click an element identified by its accessibility ref.

Use refs from the most recent browser_snapshot or navigation result.
If the ref is not found, returns an error with the current page
snapshot so you can retry with a correct ref.
Parameters|Type|Description
-|-|-
`ref`|`string`|Element ref from snapshot (e.g., "e4")
`session_id`|`string`|Browser session identifier
`button`|`string` *optional*|Mouse button: "left", "right", or "middle"
`double_click`|`boolean` *optional*|Double-click instead of single click

---
#### Tool: **`browser_close`**
Close the current page.

Closes the active page in the browser session. If multiple tabs
are open, subsequent tools will use the remaining tab. Use
stop_browser_session to fully terminate the session.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier

---
#### Tool: **`browser_console_messages`**
Get recent browser console messages.

Returns console log, warning, and error messages captured since
the Playwright connection was established. Useful for debugging
JavaScript errors or inspecting application logging.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier

---
#### Tool: **`browser_evaluate`**
Execute a JavaScript expression in the page context.

The expression is evaluated in the browser and its return value
is serialized to JSON. Use this for extracting data, reading
page state, or performing custom interactions. You can use
fetch() to make HTTP requests from the browser's origin and cookies.
Parameters|Type|Description
-|-|-
`expression`|`string`|JavaScript expression to evaluate in the page context. Use for inspecting state, extracting data, or performing actions not covered by other tools.
`session_id`|`string`|Browser session identifier

---
#### Tool: **`browser_fill_form`**
Fill multiple form fields in one action.

Clears each field before filling. Optionally clicks a submit button
after all fields are filled. Returns the page snapshot after completion.
Parameters|Type|Description
-|-|-
`fields`|`array`|List of form fields to fill. Each entry has "ref" (element ref) and "value" (text to enter). Example: [{"ref": "e2", "value": "user@example.com"}]
`session_id`|`string`|Browser session identifier
`submit_ref`|`string` *optional*|Ref of the submit button to click after filling all fields

---
#### Tool: **`browser_handle_dialog`**
Configure how JavaScript dialogs are handled for a session.

Sets a persistent handler for JavaScript dialogs (alert, confirm,
prompt, beforeunload). Once set, all subsequent dialogs in the
session are automatically accepted or dismissed. Call again to
change the behavior.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier
`action`|`string` *optional*|How to handle dialogs: "accept" or "dismiss"
`prompt_text`|`string` *optional*|Text to enter for prompt dialogs (only used with accept)

---
#### Tool: **`browser_hover`**
Hover over an element identified by its accessibility ref.

Useful for triggering tooltips, dropdown menus, or hover states.
Returns the page snapshot after hovering.
Parameters|Type|Description
-|-|-
`ref`|`string`|Element ref to hover over
`session_id`|`string`|Browser session identifier

---
#### Tool: **`browser_mouse_wheel`**
Scroll the page by the specified pixel amounts.

Default scrolls down by 500px (roughly half a viewport). Use negative
delta_y to scroll up. Returns the page snapshot after scrolling.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier
`delta_x`|`integer` *optional*|Horizontal scroll amount in pixels (positive = right)
`delta_y`|`integer` *optional*|Vertical scroll amount in pixels (positive = down, negative = up)

---
#### Tool: **`browser_navigate`**
Navigate to a URL in the browser.

Loads the specified URL and returns an accessibility tree snapshot
of the loaded page. Use the element refs in the snapshot for
subsequent interaction tools.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier
`url`|`string`|URL to navigate to

---
#### Tool: **`browser_navigate_back`**
Navigate back in browser history.

Returns an accessibility tree snapshot of the previous page.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier

---
#### Tool: **`browser_navigate_forward`**
Navigate forward in browser history.

Returns an accessibility tree snapshot of the next page.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier

---
#### Tool: **`browser_network_requests`**
List recent network requests and their status.

Returns a summary of network requests made by the page, including
URL, HTTP method, status code, and resource type. Useful for
debugging API calls or monitoring page loading.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier

---
#### Tool: **`browser_press_key`**
Press a keyboard key or key combination.

Simulates a key press on the page (not a specific element).
Supports modifier combinations like "Control+a" or "Meta+c".
Returns the page snapshot after the key press.
Parameters|Type|Description
-|-|-
`key`|`string`|Key to press. Examples: "Enter", "Tab", "Escape", "ArrowDown", "Control+a", "Meta+c". See Playwright keyboard API for key names.
`session_id`|`string`|Browser session identifier

---
#### Tool: **`browser_resize`**
Resize the browser viewport.

Changes the viewport dimensions of the active page. Useful for
testing responsive layouts or viewing content at different sizes.
Returns the page snapshot at the new size.
Parameters|Type|Description
-|-|-
`height`|`integer`|New viewport height in pixels
`session_id`|`string`|Browser session identifier
`width`|`integer`|New viewport width in pixels

---
#### Tool: **`browser_select_option`**
Select an option from a dropdown or combobox.

Provide one of: value (option value attribute), label (visible text),
or index (zero-based position). Returns the page snapshot after selection.
Parameters|Type|Description
-|-|-
`ref`|`string`|Element ref of the select/combobox element
`session_id`|`string`|Browser session identifier
`index`|`string` *optional*|Zero-based index of the option to select
`label`|`string` *optional*|Visible text label of the option to select
`value`|`string` *optional*|Option value attribute to select

---
#### Tool: **`browser_snapshot`**
Capture an accessibility tree snapshot of the current page.

Returns a structured text view of the page with element refs.
Use the refs (e.g., e1, e2) in interaction tools like browser_click
and browser_type to target specific elements.

Example output:
  - heading "Sign In" [ref=e1]
  - textbox "Email" [ref=e2]
  - textbox "Password" [ref=e3]
  - button "Sign In" [ref=e4]
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier
`selector`|`string` *optional*|Optional CSS selector to scope the snapshot to a specific section of the page (e.g., "main", "[role=main]", "#content"). If omitted, captures the full page.

---
#### Tool: **`browser_tabs`**
Manage browser tabs: list, create, select, or close tabs.

Actions:
- "list": Show all open tabs with their titles and URLs.
- "new": Open a new tab, optionally navigating to a URL.
- "select": Switch the active tab (subsequent tools use this tab).
- "close": Close a tab by its index.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier
`action`|`string` *optional*|Tab action to perform: "list" to show all tabs, "new" to open a new tab, "select" to switch to a tab by index, "close" to close a tab by index.
`tab_index`|`string` *optional*|Zero-based tab index for "select" and "close" actions
`url`|`string` *optional*|URL to open in a new tab (for "new" action)

---
#### Tool: **`browser_take_screenshot`**
Capture a visual screenshot of the page.

Returns the screenshot as a base64-encoded PNG image.
Use this when you need to visually inspect the page rather
than reading the accessibility tree.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier
`full_page`|`boolean` *optional*|Capture the full scrollable page instead of just the viewport

---
#### Tool: **`browser_type`**
Type text into an element identified by its accessibility ref.

By default, clears the existing content before typing. Set
clear_first=False to append to existing text. Set submit=True
to press Enter after typing.
Parameters|Type|Description
-|-|-
`ref`|`string`|Element ref from snapshot (e.g., "e2")
`session_id`|`string`|Browser session identifier
`text`|`string`|Text to type into the element
`clear_first`|`boolean` *optional*|Clear existing content before typing
`submit`|`boolean` *optional*|Press Enter after typing to submit

---
#### Tool: **`browser_upload_file`**
Upload files to a file input element identified by its ref.

Resolves the ref to a file input locator and sets the specified
file paths. For cloud AgentCore sessions, paths refer to files
on the remote VM. For local Playwright connections, paths refer
to files on the local filesystem.
Parameters|Type|Description
-|-|-
`paths`|`array`|List of file paths to upload
`ref`|`string`|Element ref of the file input (e.g., "e5")
`session_id`|`string`|Browser session identifier

---
#### Tool: **`browser_wait_for`**
Wait for text to appear or an element to become visible.

Provide either text or selector. Returns the page snapshot after
the condition is met. Raises an error if the timeout is exceeded.
Parameters|Type|Description
-|-|-
`session_id`|`string`|Browser session identifier
`selector`|`string` *optional*|CSS selector to wait for
`text`|`string` *optional*|Wait for this text to appear on the page
`timeout`|`integer` *optional*|Maximum wait time in milliseconds (default: 10000)

---
#### Tool: **`create_agent_runtime`**
Create a new AgentCore Runtime to host an agent or tool.

This is a one-time setup operation that creates AWS infrastructure
(IAM role binding, container deployment, endpoint). The DEFAULT
endpoint is created automatically. Subsequent updates create new
immutable versions.

**Cost note:** Creating a runtime provisions infrastructure.
You are not billed until sessions are invoked, but the runtime
definition and its resources persist until deleted.
Parameters|Type|Description
-|-|-
`agent_runtime_name`|`string`|Name for the runtime. Must match [a-zA-Z][a-zA-Z0-9_]{0,47}.
`role_arn`|`string`|IAM execution role ARN for the runtime.
`code_entry_point`|`string` *optional*|Entry point command as comma-separated values, e.g. "main.py" or "opentelemetry-instrument,main.py".
`code_runtime`|`string` *optional*|Python runtime identifier for direct code deploy, e.g. PYTHON_3_13.
`code_s3_bucket`|`string` *optional*|S3 bucket for direct code deployment.
`code_s3_prefix`|`string` *optional*|S3 key/prefix for the code zip.
`container_uri`|`string` *optional*|ECR container URI. Provide either container_uri or the s3 code fields, not both.
`description`|`string` *optional*|Description (max 4096 chars).
`idle_timeout`|`string` *optional*|Idle session timeout in seconds (60-28800). Default 900.
`max_lifetime`|`string` *optional*|Max session lifetime in seconds (60-28800). Default 28800.
`network_mode`|`string` *optional*|Network mode: "PUBLIC" or "VPC".
`security_groups`|`string` *optional*|Comma-separated security group IDs (required for VPC mode).
`server_protocol`|`string` *optional*|Protocol: "HTTP", "MCP", or "A2A".
`subnets`|`string` *optional*|Comma-separated subnet IDs (required for VPC mode).

---
#### Tool: **`create_agent_runtime_endpoint`**
Create a custom endpoint for an AgentCore Runtime.

Endpoints provide stable access points to specific runtime
versions. The DEFAULT endpoint is created automatically;
use this for additional environments (dev, staging, prod).

This is a configuration operation with no per-use cost.
Parameters|Type|Description
-|-|-
`agent_runtime_id`|`string`|Runtime ID to create the endpoint for.
`name`|`string`|Endpoint name. Must match [a-zA-Z][a-zA-Z0-9_]{0,47}.
`agent_runtime_version`|`string` *optional*|Version to point to. Omit to use latest.
`description`|`string` *optional*|Endpoint description (max 256 chars).

---
#### Tool: **`delete_agent_runtime`**
Delete an AgentCore Runtime and all its versions.

All endpoints must be deleted first. Active sessions will be
terminated. This operation cannot be undone.
Parameters|Type|Description
-|-|-
`agent_runtime_id`|`string`|Runtime ID to delete.

---
#### Tool: **`delete_agent_runtime_endpoint`**
Delete a runtime endpoint. Cannot delete the DEFAULT endpoint.

This operation cannot be undone.
Parameters|Type|Description
-|-|-
`agent_runtime_id`|`string`|Runtime ID.
`endpoint_name`|`string`|Endpoint name to delete.

---
#### Tool: **`download_file`**
Download a file from the sandboxed code interpreter session.

Reads the content of a file at the specified path in the session's sandbox.
Parameters|Type|Description
-|-|-
`path`|`string`|Relative file path in the sandbox to download (e.g. 'output/result.csv').
`session_id`|`string`|The session ID to download the file from.
`region`|`string` *optional*|AWS region.

---
#### Tool: **`execute_code`**
Execute code in a sandboxed code interpreter session.

Runs Python, JavaScript, or TypeScript code in the session's sandbox.
The execution context (variables, imports) persists across calls within
the same session unless clear_context is True.
Parameters|Type|Description
-|-|-
`code`|`string`|The source code to execute.
`session_id`|`string`|The session ID to execute code in. Must be a started session.
`clear_context`|`string` *optional*|If True, reset the execution context before running.
`language`|`string` *optional*|Programming language ('python', 'javascript', 'typescript').
`region`|`string` *optional*|AWS region.

---
#### Tool: **`execute_command`**
Execute a shell command in a sandboxed code interpreter session.

Runs a shell command in the session's sandbox environment.
Parameters|Type|Description
-|-|-
`command`|`string`|The shell command to execute.
`session_id`|`string`|The session ID to execute the command in.
`region`|`string` *optional*|AWS region.

---
#### Tool: **`fetch_agentcore_doc`**
Fetch full document content by URL.

Retrieves complete AgentCore documentation content from URLs found via search_agentcore_docs
or provided directly. Use this to get full documentation pages including:

- Complete platform overview and service documentation
- Detailed getting started guides with step-by-step instruc

[...]

## Screenshots

![AWS Bedrock AgentCore screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/amazon-bedrock-agentcore-1.png)

![AWS Bedrock AgentCore screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/amazon-bedrock-agentcore-2.png)

![AWS Bedrock AgentCore screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/amazon-bedrock-agentcore-3.png)
