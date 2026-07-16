A Model Context Protocol (MCP) server for integrating with StackHawk's security scanning platform. Provides security analytics, YAML configuration management, sensitive data/threat surface analysis, and anti-hallucination tools for LLMs.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/stackhawk](https://hub.docker.com/repository/docker/mcp/stackhawk)
**Author**|[stackhawk](https://github.com/stackhawk)
**Repository**|https://github.com/stackhawk/stackhawk-mcp

## Available Tools (7)
Tools provided by this Server|Short Description
-|-
`get_app_findings_for_triage`|Get triage-worthy findings for a project or application at or above the configured failureThreshold (or High/Medium if not set).|
`get_organization_info`|Get information about a StackHawk organization|
`list_applications`|List applications in a StackHawk organization|
`run_stackhawk_scan`|Run a StackHawk scan using the CLI and stream results back to the chat.|
`setup_stackhawk_for_project`|Set up StackHawk for a new project.|
`validate_field_exists`|Validate that a field path exists in the StackHawk schema|
`validate_stackhawk_config`|Validate a StackHawk YAML configuration file|

---
## Tools Details

#### Tool: **`get_app_findings_for_triage`**
Get triage-worthy findings for a project or application at or above the configured failureThreshold (or High/Medium if not set). Accepts app_id, config_path, or config_content.
Parameters|Type|Description
-|-|-
`app_id`|`string` *optional*|StackHawk application ID (optional)
`config_content`|`string` *optional*|YAML content of the StackHawk config file (optional, takes precedence over config_path)
`config_path`|`string` *optional*|Path to StackHawk config file (optional, default: stackhawk.yml)

---
#### Tool: **`get_organization_info`**
Get information about a StackHawk organization
Parameters|Type|Description
-|-|-
`org_id`|`string`|Organization ID

---
#### Tool: **`list_applications`**
List applications in a StackHawk organization
Parameters|Type|Description
-|-|-
`org_id`|`string`|Organization ID
`page_size`|`integer` *optional*|Page size (optional)

---
#### Tool: **`run_stackhawk_scan`**
Run a StackHawk scan using the CLI and stream results back to the chat. Optionally specify a config path (default: stackhawk.yml).
Parameters|Type|Description
-|-|-
`config_path`|`string` *optional*|Path to StackHawk config file (default: stackhawk.yml)

---
#### Tool: **`setup_stackhawk_for_project`**
Set up StackHawk for a new project. Finds or creates the application and generates a complete stackhawk.yml configuration file ready for scanning.
Parameters|Type|Description
-|-|-
`host`|`string`|Target URL to scan (e.g., https://localhost:3000, https://ginandjuice.shop)
`app_name`|`string` *optional*|Application name (optional, defaults to current directory name)
`environment`|`string` *optional*|Environment name (default: dev)
`org_id`|`string` *optional*|Organization ID (optional, auto-detected if omitted)

---
#### Tool: **`validate_field_exists`**
Validate that a field path exists in the StackHawk schema
Parameters|Type|Description
-|-|-
`field_path`|`string`|Field path to validate

---
#### Tool: **`validate_stackhawk_config`**
Validate a StackHawk YAML configuration file
Parameters|Type|Description
-|-|-
`yaml_content`|`string`|YAML content to validate

---
