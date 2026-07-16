MCP server to deploy apps to Cloud Run.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/cloud-run-mcp](https://hub.docker.com/repository/docker/mcp/cloud-run-mcp)
**Author**|[GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
**Repository**|https://github.com/GoogleCloudPlatform/cloud-run-mcp

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`create_project`|Creates a new GCP project and attempts to attach it to the first available billing account.|
`deploy_container_image`|Deploys a container image to Cloud Run.|
`deploy_file_contents`|Deploy files to Cloud Run by providing their contents directly.|
`deploy_local_folder`|Deploy a local folder to Cloud Run.|
`get_service`|Gets details for a specific Cloud Run service.|
`get_service_log`|Gets Logs and Error Messages for a specific Cloud Run service.|
`list_projects`|Lists available GCP projects|
`list_services`|Lists all Cloud Run services in a given project.|

---
## Tools Details

#### Tool: **`create_project`**
Creates a new GCP project and attempts to attach it to the first available billing account. A project ID can be optionally specified; otherwise it will be automatically generated.
Parameters|Type|Description
-|-|-
`projectId`|`string` *optional*|Optional. The desired ID for the new GCP project. If not provided, an ID will be auto-generated.

---
#### Tool: **`deploy_container_image`**
Deploys a container image to Cloud Run. Use this tool if the user provides a container image URL.
Parameters|Type|Description
-|-|-
`imageUrl`|`string`|The URL of the container image to deploy (e.g. "gcr.io/cloudrun/hello")
`project`|`string`|Google Cloud project ID. Do not select it yourself, make sure the user provides or confirms the project ID.
`region`|`string` *optional*|Region to deploy the service to
`service`|`string` *optional*|Name of the Cloud Run service to deploy to

---
#### Tool: **`deploy_file_contents`**
Deploy files to Cloud Run by providing their contents directly. Takes an array of file objects containing filename and content. Use this tool if the files only exist in the current chat context.
Parameters|Type|Description
-|-|-
`files`|`array`|Array of file objects containing filename and content
`project`|`string`|Google Cloud project ID. Leave unset for the app to be deployed in a new project. If provided, make sure the user confirms the project ID they want to deploy to.
`region`|`string` *optional*|Region to deploy the service to
`service`|`string` *optional*|Name of the Cloud Run service to deploy to

---
#### Tool: **`deploy_local_folder`**
Deploy a local folder to Cloud Run. Takes an absolute folder path from the local filesystem that will be deployed. Use this tool if the entire folder content needs to be deployed.
Parameters|Type|Description
-|-|-
`folderPath`|`string`|Absolute path to the folder to deploy (e.g. "/home/user/project/src")
`project`|`string`|Google Cloud project ID. Do not select it yourself, make sure the user provides or confirms the project ID.
`region`|`string` *optional*|Region to deploy the service to
`service`|`string` *optional*|Name of the Cloud Run service to deploy to. If not provided, it will be inferred.

---
#### Tool: **`get_service`**
Gets details for a specific Cloud Run service.
Parameters|Type|Description
-|-|-
`project`|`string`|Google Cloud project ID containing the service
`service`|`string`|Name of the Cloud Run service
`region`|`string` *optional*|Region where the service is located

---
#### Tool: **`get_service_log`**
Gets Logs and Error Messages for a specific Cloud Run service.
Parameters|Type|Description
-|-|-
`project`|`string`|Google Cloud project ID containing the service
`service`|`string`|Name of the Cloud Run service
`region`|`string` *optional*|Region where the service is located

---
#### Tool: **`list_projects`**
Lists available GCP projects
#### Tool: **`list_services`**
Lists all Cloud Run services in a given project.
Parameters|Type|Description
-|-|-
`project`|`string`|Google Cloud project ID

---

## Screenshots

![Cloud Run screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/cloud-run-mcp-1.gif)

![Cloud Run screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/cloud-run-mcp-2.gif)

![Cloud Run screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/cloud-run-mcp-3.gif)
