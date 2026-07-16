Provides access to Pica's integrations, actions, execution, and code generation capabilities.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/pica-mcp-server](https://hub.docker.com/repository/docker/mcp/pica-mcp-server)
**Author**|[picahq](https://github.com/picahq)
**Repository**|https://github.com/picahq/mcp

## Available Tools (4)
Tools provided by this Server|Short Description
-|-
`execute_pica_action`|Execute a Pica action to perform actual operations on third-party platforms.|
`get_pica_action_knowledge`|Get comprehensive documentation for a specific action including parameters, requirements, and usage examples.|
`list_pica_integrations`|List all available Pica integrations and platforms.|
`search_pica_platform_actions`|Search for relevant actions on a specific platform using a query.|

---
## Tools Details

#### Tool: **`execute_pica_action`**
Execute a Pica action to perform actual operations on third-party platforms. CRITICAL: Only call this when the user's intent is to EXECUTE an action (e.g., 'read my last Gmail email', 'fetch 5 contacts from HubSpot', 'create a task in Asana'). DO NOT call this when the user wants to BUILD or CREATE code/forms/applications - in those cases, stop after get_pica_action_knowledge and provide implementation guidance instead. REQUIRED WORKFLOW: Must call get_pica_action_knowledge first. If uncertain about execution intent or parameters, ask for confirmation before proceeding.
Parameters|Type|Description
-|-|-
`actionId`|`string`|Action ID from search_pica_platform_actions
`connectionKey`|`string`|Key of the connection to use
`platform`|`string`|Platform name
`data`|`string` *optional*|Request data (for POST, PUT, etc.)
`headers`|`object` *optional*|Additional headers
`isFormData`|`boolean` *optional*|Whether to send data as multipart/form-data
`isFormUrlEncoded`|`boolean` *optional*|Whether to send data as application/x-www-form-urlencoded
`pathVariables`|`object` *optional*|Variables to replace in the path
`queryParams`|`object` *optional*|Query parameters

---
#### Tool: **`get_pica_action_knowledge`**
Get comprehensive documentation for a specific action including parameters, requirements, and usage examples. MANDATORY: You MUST call this tool before execute_pica_action to understand the action's requirements, parameter structure, caveats, and proper usage. This loads the action documentation into context and is required for successful execution.
Parameters|Type|Description
-|-|-
`actionId`|`string`|The action ID to get knowledge for (from the actions list returned by search_pica_platform_actions). REQUIRED: This tool must be called before execute_pica_action to load the action's documentation into context.
`platform`|`string`|The platform name to get knowledge for (e.g., 'ship-station', 'shopify'). This is the kebab-case version of the platform name that comes from the list_pica_integrations tool AVAILABLE PLATFORMS section.

---
#### Tool: **`list_pica_integrations`**
List all available Pica integrations and platforms. ALWAYS call this tool first in any workflow to discover what platforms and connections are available. This returns the connections that the user has and all available Pica platforms in kebab-case format (e.g., 'ship-station', 'shopify') which you'll need for subsequent tool calls.
#### Tool: **`search_pica_platform_actions`**
Search for relevant actions on a specific platform using a query. Call this after list_pica_integrations to find actions that match your intent. Returns the top 5 most relevant actions based on your search query. Use the exact kebab-case platform name from the integrations list.
Parameters|Type|Description
-|-|-
`platform`|`string`|The platform name to search actions for (e.g., 'ship-station', 'shopify'). This is the kebab-case version of the platform name that comes from the list_pica_integrations tool AVAILABLE PLATFORMS section.
`query`|`string`|The search query to find relevant actions (e.g., 'search contacts', 'create customer', 'send email'). Be specific about what you want to do.
`agentType`|`string` *optional*|The type of agent context: 'execute' if the user wants to execute an action, 'knowledge' if they want to get information or write code. Defaults to 'knowledge' if not specified.

---
