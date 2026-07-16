Connects with the Beagle Security backend using a user token to manage applications, run automated security tests, track vulnerabilities across environments, and gain intelligence from Application and API vulnerability data.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/beagle-security-mcp-server](https://hub.docker.com/repository/docker/mcp/beagle-security-mcp-server)
**Author**|[beaglesecurity](https://github.com/beaglesecurity)
**Repository**|https://github.com/beaglesecurity/beagle-security-mcp-server

## Available Tools (17)
Tools provided by this Server|Short Description
-|-
`beagle_create_application`|Create a new application in a project|
`beagle_create_project`|Create a new project in Beagle Security|
`beagle_delete_application`|Delete an application|
`beagle_delete_project`|Delete a project|
`beagle_get_application`|Get application details by token|
`beagle_get_domain_signature`|Get domain verification signature|
`beagle_get_test_result`|Get detailed test results in JSON format|
`beagle_get_test_status`|Get the status of a running test|
`beagle_list_applications`|List all applications under a project|
`beagle_list_projects`|List all projects and applications|
`beagle_list_running_tests`|List all running tests for user or team|
`beagle_list_test_sessions`|List all test sessions for an application|
`beagle_modify_application`|Modify an existing application|
`beagle_modify_project`|Modify an existing project|
`beagle_start_test`|Start an automated penetration test|
`beagle_stop_test`|Stop a running test|
`beagle_verify_domain`|Complete domain verification|

---
## Tools Details

#### Tool: **`beagle_create_application`**
Create a new application in a project
Parameters|Type|Description
-|-|-
`name`|`string`|Application name
`projectKey`|`string`|Project key
`type`|`string`|Application type
`url`|`string`|Application URL

---
#### Tool: **`beagle_create_project`**
Create a new project in Beagle Security
Parameters|Type|Description
-|-|-
`name`|`string`|Project name
`description`|`string` *optional*|Project description
`teamId`|`string` *optional*|Team ID (optional)

---
#### Tool: **`beagle_delete_application`**
Delete an application
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token

---
#### Tool: **`beagle_delete_project`**
Delete a project
Parameters|Type|Description
-|-|-
`projectKey`|`string`|Project key to delete

---
#### Tool: **`beagle_get_application`**
Get application details by token
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token

---
#### Tool: **`beagle_get_domain_signature`**
Get domain verification signature
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token

---
#### Tool: **`beagle_get_test_result`**
Get detailed test results in JSON format
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token
`resultToken`|`string`|Result token from test start

---
#### Tool: **`beagle_get_test_status`**
Get the status of a running test
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token
`resultToken`|`string`|Result token from test start

---
#### Tool: **`beagle_list_applications`**
List all applications under a project
Parameters|Type|Description
-|-|-
`projectKey`|`string`|Project key

---
#### Tool: **`beagle_list_projects`**
List all projects and applications
Parameters|Type|Description
-|-|-
`includeTeam`|`boolean` *optional*|Include team projects

---
#### Tool: **`beagle_list_running_tests`**
List all running tests for user or team
Parameters|Type|Description
-|-|-
`teamId`|`string` *optional*|Team ID (optional, for team tests)

---
#### Tool: **`beagle_list_test_sessions`**
List all test sessions for an application
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token
`count`|`number` *optional*|Number of sessions to retrieve

---
#### Tool: **`beagle_modify_application`**
Modify an existing application
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token
`name`|`string`|Application name
`url`|`string`|Application URL

---
#### Tool: **`beagle_modify_project`**
Modify an existing project
Parameters|Type|Description
-|-|-
`description`|`string`|Project description
`name`|`string`|Project name
`projectKey`|`string`|Project key

---
#### Tool: **`beagle_start_test`**
Start an automated penetration test
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token

---
#### Tool: **`beagle_stop_test`**
Stop a running test
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token

---
#### Tool: **`beagle_verify_domain`**
Complete domain verification
Parameters|Type|Description
-|-|-
`applicationToken`|`string`|Application token
`signatureType`|`string`|Type of signature verification
`pluginType`|`string` *optional*|Plugin type (optional)

---
