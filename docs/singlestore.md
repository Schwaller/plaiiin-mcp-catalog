MCP server for interacting with SingleStore Management API and services.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/singlestore](https://hub.docker.com/repository/docker/mcp/singlestore)
**Author**|[singlestore-labs](https://github.com/singlestore-labs)
**Repository**|https://github.com/singlestore-labs/mcp-server-singlestore

## Available Tools (28)
Tools provided by this Server|Short Description
-|-
`create_cloud_function`|Deploy a notebook as a cloud function.|
`create_job_from_notebook`|Create a scheduled job to run a notebook (uploaded to shared space).|
`create_notebook_file`|Create a Jupyter notebook file in the correct singlestore format and saves it to a temporary location.|
`create_starter_workspace`|Create a new starter workspace using the SingleStore SDK.|
`delete_cloud_function`|Delete a cloud function by its ID.|
`delete_job`|Delete a scheduled job by its ID.|
`get_cloud_function`|Get detailed information about a specific cloud function including its status, endpoint, and configuration.|
`get_cloud_function_token`|Get an authentication token for invoking a cloud function.|
`get_job`|Retrieve details of a scheduled job by its ID.|
`get_user_info`|Retrieve all information about the current user.|
`list_cloud_functions`|List all cloud functions in the current organization.|
`list_regions`|List all available deployment regions where SingleStore workspaces can be deployed by the user.|
`list_sharedtier_regions`|List all regions where shared tier workspaces can be created.|
`list_starter_workspaces`|List all starter (virtual) workspaces available to the user in SingleStore.|
`organization_info`|Retrieve information about the current user's organization in SingleStore.|
`resume_workspace`|Resume a workspace within a specified workspace group in SingleStore.|
`run_sql`|Use this tool to execute a single SQL statement against a SingleStore database.|
`stage_create_folder`|Create a folder in Stage.|
`stage_delete`|Delete a file or folder from Stage.|
`stage_get_file`|Get a file from Stage by path.|
`stage_list_files`|List files and folders in a Stage deployment's file system.|
`stage_move`|Move or rename a file or folder in Stage.|
`stage_upload_file`|Upload a file to Stage from text content or a local file path.|
`terminate_starter_workspace`|Permanently delete a starter workspace in SingleStore with safety confirmations.|
`update_cloud_function`|Update a cloud function's configuration.|
`upload_notebook_file`|Upload a notebook file from a local local_path to SingleStore shared or personal space.|
`workspace_groups_info`|List all workspace groups accessible to the user in SingleStore.|
`workspaces_info`|List all workspaces within a specified workspace group in SingleStore.|

---
## Tools Details

#### Tool: **`create_cloud_function`**
Deploy a notebook as a cloud function.

    The notebook must already exist in the Stage file system shared space. Use
    stage_upload_file to upload a notebook first, then deploy it as a cloud function.

    The notebook must define a FastAPI app, and initialize it using a singlestore tool.
    Base example:
        from fastapi import FastAPI
        import singlestoredb.apps as apps
        app = FastAPI()
        @app.get("/")
        async def root():
            return {"message": "hello world"}
        await apps.run_function_app(app)

    Target_type is optional, but if it specifies a virtual workspace, it must also specify a database_name.
Parameters|Type|Description
-|-|-
`name`|`string`|Name for the cloud function.
`notebook_path`|`string`|Path to the notebook in Stage (e.g. "my_notebook.ipynb").
`target_id`|`string`|ID of the workspace, cluster, or virtual workspace to deploy to.
`database_name`|`string` *optional*|Optional database name to attach to the function.
`description`|`string` *optional*|Optional description of the cloud function.
`idle_timeout_seconds`|`string` *optional*|Optional idle timeout in seconds before scaling down.
`target_type`|`string` *optional*|Type of target - "Workspace", "Cluster", or "VirtualWorkspace".

---
#### Tool: **`create_job_from_notebook`**
Create a scheduled job to run a notebook (uploaded to shared space).
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the job
`notebook_path`|`string`|Remote path to the shared notebook file
`execution_interval_in_minutes`|`string` *optional*|Optional interval in minutes for recurring jobs
`mode`|`string` *optional*|Job mode (options: "Once", "Recurring")

---
#### Tool: **`create_notebook_file`**
Create a Jupyter notebook file in the correct singlestore format and saves it to a temporary location.

    This tool validates the provided content against the Jupyter notebook schema and creates a properly
    formatted .ipynb file in a temporary location. The content is converted from the simplified format
    to the full Jupyter notebook format.

    Each code cell MUST include a "language" field in its metadata for SingleStore to
    properly recognize the cell. If not provided or empty, it defaults to "python".
    Supported languages are "python" and "sql"; other values are rejected.
Parameters|Type|Description
-|-|-
`content`|`object`|Notebook content in the format: {

---
#### Tool: **`create_starter_workspace`**
Create a new starter workspace using the SingleStore SDK.

    This tool provides a modern SDK-based approach to creating starter workspaces,
    offering improved reliability and better error handling compared to direct API calls.
Parameters|Type|Description
-|-|-
`database_name`|`string`|Name of the database to create in the starter workspace
`name`|`string`|Unique name for the new starter workspace
`provider`|`string` *optional*|Cloud provider for the workspace (e.g., "AWS", "GCP", "Azure")
`region_name`|`string` *optional*|Region where the workspace should be deployed (e.g., "us-west-2", "europe-west1")

---
#### Tool: **`delete_cloud_function`**
Delete a cloud function by its ID.
Parameters|Type|Description
-|-|-
`cloud_function_id`|`string`|The unique identifier (UUID) of the cloud function to delete.

---
#### Tool: **`delete_job`**
Delete a scheduled job by its ID.
Parameters|Type|Description
-|-|-
`job_id`|`string`|ID of the job to delete

---
#### Tool: **`get_cloud_function`**
Get detailed information about a specific cloud function including its
    status, endpoint, and configuration.
Parameters|Type|Description
-|-|-
`cloud_function_id`|`string`|The unique identifier (UUID) of the cloud function.

---
#### Tool: **`get_cloud_function_token`**
Get an authentication token for invoking a cloud function.

    Returns a JWT token and its expiration time. Use this token in the
    Authorization header when making HTTP requests to the cloud function's
    endpoint.
Parameters|Type|Description
-|-|-
`cloud_function_id`|`string`|The unique identifier (UUID) of the cloud function.

---
#### Tool: **`get_job`**
Retrieve details of a scheduled job by its ID.
Parameters|Type|Description
-|-|-
`job_id`|`string`|ID of the job to retrieve

---
#### Tool: **`get_user_info`**
Retrieve all information about the current user.

    Returns:
        dict: User information including userID, email, firstName, lastName.

    Performance Tip:
    Cache the returned info when making multiple API calls.
#### Tool: **`list_cloud_functions`**
List all cloud functions in the current organization.

    Returns name, status, endpoint, and description for each cloud function.
Parameters|Type|Description
-|-|-
`limit`|`string` *optional*|Optional maximum number of cloud functions to return.
`offset_id`|`string` *optional*|ID of the last cloud function from the previous page, used to

---
#### Tool: **`list_regions`**
List all available deployment regions where SingleStore workspaces can be deployed by the user.

    Returns region information including:
    - regionID: Unique identifier for the region
    - provider: Cloud provider (AWS, GCP, or Azure)
    - name: Human-readable region name (e.g., Europe West 2 (London), US West 2 (Oregon))

    Use this tool to:
    1. Select optimal deployment regions based on:
       - Geographic proximity to users
       - Compliance requirements
       - Cost considerations
       - Available cloud providers
    2. Plan multi-region deployments
#### Tool: **`list_sharedtier_regions`**
List all regions where shared tier workspaces can be created.

    This tool provides information about available regions for creating starter workspaces,
    including region names and cloud providers.
#### Tool: **`list_starter_workspaces`**
List all starter (virtual) workspaces available to the user in SingleStore.

    Returns detailed information about each starter workspace:
    - virtualWorkspaceID: Unique identifier for the workspace
    - name: Display name of the workspace
    - endpoint: Connection endpoint URL
    - databaseName: Name of the primary database
    - mysqlDmlPort: Port for MySQL protocol connections
    - webSocketPort: Port for WebSocket connections
    - state: Current status of the workspace

    Use this tool to:
    1. Get starter workspace IDs for other operations
    2. Check starter workspace availability and status
    3. Obtain connection details for database access
#### Tool: **`organization_info`**
Retrieve information about the current user's organization in SingleStore.

    Returns organization details including:
    - orgID: Unique identifier for the organization
    - name: Organization display name
#### Tool: **`resume_workspace`**
Resume a workspace within a specified workspace group in SingleStore.
Parameters|Type|Description
-|-|-
`workspace_id`|`string`|Unique identifier of the workspace to resume

---
#### Tool: **`run_sql`**
Use this tool to execute a single SQL statement against a SingleStore database.

    Generally you should *NOT* specify the username and password when calling this tool.
    You must only use those parameters if a previous attempt to call this method failed and
    indicated that the `username` and `password` must be specified.
    Credentials for a specific workspace and database combination will be cached.

    Returns:
    - Query results with column names and typed values
    - Row count and metadata
    - Execution status
    - Workspace type ("shared" for starter workspaces, "dedicated" for regular workspaces)
    - Workspace name
Parameters|Type|Description
-|-|-
`id`|`string`|Workspace or starter workspace ID
`sql_query`|`string`|The SQL query to execute
`database`|`string` *optional*|(optional) Database name to use
`password`|`string` *optional*|
`username`|`string` *optional*|

---
#### Tool: **`stage_create_folder`**
Create a folder in Stage.
Parameters|Type|Description
-|-|-
`deployment_id`|`string`|The workspace group ID or starter workspace ID.
`path`|`string`|Folder path to create.

---
#### Tool: **`stage_delete`**
Delete a file or folder from Stage.

    For folders, ensure the path ends with '/'.
    For files, the path must not end with '/'.
Parameters|Type|Description
-|-|-
`deployment_id`|`string`|The workspace group ID or starter workspace ID.
`path`|`string`|Path of the file or folder to delete.

---
#### Tool: **`stage_get_file`**
Get a file from Stage by path. Returns metadata, a download URL, or text content.

    Recommended workflow: first call with return_type='metadata' to check file size
    and type, then decide whether to fetch the full content or just the URL.
Parameters|Type|Description
-|-|-
`deployment_id`|`string`|The workspace group ID or starter workspace ID.
`path`|`string`|Path to the file in Stage.
`return_type`|`string` *optional*|What to return. One of:

---
#### Tool: **`stage_list_files`**
List files and folders in a Stage deployment's file system.

    Lists the contents of the root folder or a specific subfolder in the Stage
    file system attached to a SingleStore deployment (workspace group or starter
    workspace).
Parameters|Type|Description
-|-|-
`deployment_id`|`string`|The workspace group ID or starter workspace ID.
`path`|`string` *optional*|Optional folder path to list. Defaults to root. Must refer to a

---
#### Tool: **`stage_move`**
Move or rename a file or folder in Stage.
    For folders, ensure the path ends with '/'.
    For files, the path must not end with '/'.

    Works like the `mv` command - can rename and/or move into a different folder.
Parameters|Type|Description
-|-|-
`deployment_id`|`string`|The workspace group ID or starter workspace ID.
`destination_path`|`string`|New path for the file or folder.
`source_path`|`string`|Current path of the file or folder.

---
#### Tool: **`stage_upload_file`**
Upload a file to Stage from text content or a local file path.

    Provide exactly one of `content` or `local_path`:
    - content: Text content to upload as the file body.
    - local_path: Absolute path to a local file to upload.
Parameters|Type|Description
-|-|-
`deployment_id`|`string`|The workspace group ID or starter workspace ID.
`path`|`string`|Destination file path in Stage.
`content`|`string` *optional*|Text content to upload as the file body.
`local_path`|`string` *optional*|Absolute path to a local file to upload.

---
#### Tool: **`terminate_starter_workspace`**
Permanently delete a starter workspace in SingleStore with safety confirmations.

    ⚠️  WARNING: This action CANNOT be undone. All workspace data will be permanently lost.
    Make sure to backup important data before proceeding.

    Safety Features:
    - Requires explicit user confirmation (if elicitation is supported)
    - Validates workspace existence
    - Provides warning messages
    - Includes error handling
Parameters|Type|Description
-|-|-
`workspace_id`|`string`|Workspace identifier (format: "ws-" followed by alphanumeric chars)

---
#### Tool: **`update_cloud_function`**
Update a cloud function's configuration. Only provided fields are updated.
Parameters|Type|Description
-|-|-
`cloud_function_id`|`string`|The unique identifier (UUID) of the cloud function.
`database_name`|`string` *optional*|New database name to attach.
`description`|`string` *optional*|New description.
`idle_timeout_seconds`|`string` *optional*|New idle timeout in seconds.
`name`|`string` *optional*|New name for the cloud function.
`notebook_path`|`string` *optional*|New notebook path in Stage.
`target_id`|`string` *optional*|New target workspace/cluster/virtual workspace ID.
`target_type`|`string` *optional*|New target type - "Workspace", "Cluster", or "VirtualWorkspace".
`update_notebook_snapshot`|`string` *optional*|Whether to update the notebook snapshot after updating.

---
#### Tool: **`upload_notebook_file`**
Upload a notebook file from a local local_path to SingleStore shared or personal space.

    This tool validates the notebook schema before uploading. If upload_name or upload_location
    are not provided, the user will be prompted through elicitation.
Parameters|Type|Description
-|-|-
`local_path`|`string`|Local file system path to the notebook file (.ipynb)
`upload_location`|`string` *optional*|Optional. Either "shared" or "personal". If not provided, user will be prompted.
`upload_name`|`string` *optional*|Optional. Name of the file after upload (with or without .ipynb extension).

---
#### Tool: **`workspace_groups_info`**
List all workspace groups accessible to the user in SingleStore.

    Returns detailed information for each group:
    - workspaceGroupID: Unique identifier for the group
    - name: Display name of the workspace group
    - region: Region information (name, provider)
    - firewallRanges: List of allowed IP ranges for the group
    - allowAllTraffic: Whether all traffic is allowed to the group
    - createdAt: Timestamp of group creation
    - terminatedAt: Timestamp when the group was terminated (if applicable)

    Use this tool to:
    1. Get workspace group IDs for other operations
    2. Plan maintenance windows

    Related operations:
    - Use workspaces_info to list workspaces within a group
    - Use execute_sql to run queries on workspaces in a group
#### Tool: **`workspaces_info`**
List all workspaces within a specified workspace group in SingleStore.

    Returns detailed information for each workspace:
    - createdAt: Timestamp of workspace creation
    - deploymentType: Type of deployment (e.g., 'PRODUCTION')
    - endpoint: Connection URL for database access
    - name: Display name of the workspace
    - size: Compute and storage configuration
    - state: Current status (e.g., 'ACTIVE', 'PAUSED')
    - terminatedAt: End timestamp if applicable
    - workspaceGroupID: Workspacegroup identifier
    - workspaceID: Unique workspace identifier
Parameters|Type|Description
-|-|-
`workspace_group_id`|`string`|Unique identifier of the workspace group

---
