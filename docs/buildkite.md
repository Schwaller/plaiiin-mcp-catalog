Buildkite MCP lets agents interact with Buildkite Builds, Jobs, Logs, Packages and Test Suites.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/buildkite](https://hub.docker.com/repository/docker/mcp/buildkite)
**Author**|[buildkite](https://github.com/buildkite)
**Repository**|https://github.com/buildkite/buildkite-mcp-server

## Available Tools (24)
Tools provided by this Server|Short Description
-|-
`access_token`|Get Access Token|
`create_build`|Create Build|
`create_pipeline`|Create Pipeline|
`current_user`|Get Current User|
`get_artifact`|Get Artifact|
`get_build`|Get Build|
`get_build_test_engine_runs`|Get Build Test Engine Runs|
`get_cluster`|Get Cluster|
`get_cluster_queue`|Get Cluster Queue|
`get_failed_executions`|Get Failed Test Executions|
`get_job_logs`|Get Job Logs|
`get_jobs`|Get Jobs|
`get_pipeline`|Get Pipeline|
`get_test`|Get Test|
`get_test_run`|Get Test Run|
`list_annotations`|List Annotations|
`list_artifacts`|Artifact List|
`list_builds`|List Builds|
`list_cluster_queues`|List Cluster Queues|
`list_clusters`|List Clusters|
`list_pipelines`|List Pipelines|
`list_test_runs`|List Test Runs|
`update_pipeline`|Update Pipeline|
`user_token_organization`|Get Organization for User Token|

---
## Tools Details

#### Tool: **`access_token`**
Get information about the current API access token including its scopes and UUID
#### Tool: **`create_build`**
Trigger a new build on a Buildkite pipeline for a specific commit and branch, with optional environment variables, metadata, and author information
Parameters|Type|Description
-|-|-
`branch`|`string`|The branch to build
`commit`|`string`|The commit SHA to build
`message`|`string`|The commit message for the build
`org_slug`|`string`|The organization slug for the owner of the pipeline
`pipeline_slug`|`string`|The slug of the pipeline
`environment`|`array` *optional*|Environment variables to set for the build
`metadata`|`array` *optional*|Meta-data values to set for the build

---
#### Tool: **`create_pipeline`**
Set up a new CI/CD pipeline in Buildkite with YAML configuration, repository connection, and cluster assignment
Parameters|Type|Description
-|-|-
`cluster_id`|`string`|The ID value of the cluster the pipeline will be associated with
`configuration`|`string`|The pipeline configuration in YAML format. Contains the build steps and pipeline settings. If not provided, a basic configuration will be used
`name`|`string`|The name of the pipeline
`org_slug`|`string`|The organization slug for the owner of the pipeline. This is used to determine where to create the pipeline
`repository_url`|`string`|The Git repository URL to use for the pipeline
`cancel_running_branch_builds`|`boolean` *optional*|Cancel running builds when new builds are created on the same branch
`default_branch`|`string` *optional*|The default branch for builds and metrics filtering
`description`|`string` *optional*|The description of the pipeline
`skip_queued_branch_builds`|`boolean` *optional*|Skip intermediate builds when new builds are created on the same branch
`tags`|`array` *optional*|Tags to apply to the pipeline. These can be used for filtering and organization

---
#### Tool: **`current_user`**
Get details about the user account that owns the API token, including name, email, avatar, and account creation date
#### Tool: **`get_artifact`**
Get detailed information about a specific artifact including its metadata, file size, SHA-1 hash, and download URL
Parameters|Type|Description
-|-|-
`url`|`string`|The URL of the artifact to get

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_build`**
Get detailed information about a specific build including its jobs, timing, and execution details
Parameters|Type|Description
-|-|-
`build_number`|`string`|The number of the build
`org`|`string`|The organization slug for the owner of the pipeline
`pipeline_slug`|`string`|The slug of the pipeline

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_build_test_engine_runs`**
Get test engine runs data for a specific build in Buildkite. This can be used to look up Test Runs.
Parameters|Type|Description
-|-|-
`build_number`|`string`|The number of the build
`org`|`string`|The organization slug for the owner of the pipeline
`pipeline_slug`|`string`|The slug of the pipeline

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_cluster`**
Get detailed information about a specific cluster including its name, description, default queue, and configuration
Parameters|Type|Description
-|-|-
`cluster_id`|`string`|The id of the cluster
`org`|`string`|The organization slug for the owner of the pipeline

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_cluster_queue`**
Get detailed information about a specific queue including its key, description, dispatch status, and hosted agent configuration
Parameters|Type|Description
-|-|-
`cluster_id`|`string`|The id of the cluster
`org`|`string`|The organization slug for the owner of the pipeline
`queue_id`|`string`|The id of the queue

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_failed_executions`**
Get failed test executions for a specific test run in Buildkite Test Engine. Optionally get the expanded failure details such as full error messages and stack traces.
Parameters|Type|Description
-|-|-
`org`|`string`|The organization slug for the owner of the test suite
`run_id`|`string`|The ID of the test run
`test_suite_slug`|`string`|The slug of the test suite the run belongs to
`include_failure_expanded`|`boolean` *optional*|Include the expanded failure details such as full error messages and stack traces. This can be used to explain and diganose the cause of test failures.
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_job_logs`**
Get the log output and metadata for a specific job, including content, size, and header timestamps. Automatically saves to file for large logs to avoid token limits.
Parameters|Type|Description
-|-|-
`build_number`|`string`|The build number
`job_uuid`|`string`|The UUID of the job
`org`|`string`|The organization slug for the owner of the pipeline
`pipeline_slug`|`string`|The slug of the pipeline

---
#### Tool: **`get_jobs`**
Get all jobs for a specific build including their state, timing, commands, and execution details
Parameters|Type|Description
-|-|-
`build_number`|`string`|The number of the build
`org`|`string`|The organization slug for the owner of the pipeline
`pipeline_slug`|`string`|The slug of the pipeline
`include_agent`|`boolean` *optional*|Include detailed agent information in the response. When false (default), only agent ID is included to reduce response size.
`job_state`|`string` *optional*|Filter jobs by state. Supports actual states (scheduled, running, passed, failed, canceled, skipped, etc.)
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 50)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pipeline`**
Get detailed information about a specific pipeline including its configuration, steps, environment variables, and build statistics
Parameters|Type|Description
-|-|-
`org`|`string`|The organization slug for the owner of the pipeline
`pipeline_slug`|`string`|The slug of the pipeline

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_test`**
Get a specific test in Buildkite Test Engine. This provides additional metadata for failed test executions
Parameters|Type|Description
-|-|-
`org`|`string`|The organization slug for the owner of the test suite
`test_id`|`string`|The ID of the test
`test_suite_slug`|`string`|The slug of the test suite

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_test_run`**
Get a specific test run in Buildkite Test Engine
Parameters|Type|Description
-|-|-
`org`|`string`|The organization slug for the owner of the test suite
`run_id`|`string`|The ID of the test run
`test_suite_slug`|`string`|The slug of the test suite

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_annotations`**
List all annotations for a build, including their context, style (success/info/warning/error), rendered HTML content, and creation timestamps
Parameters|Type|Description
-|-|-
`build_number`|`string`|The build number
`org`|`string`|The organization slug for the owner of the pipeline
`pipeline_slug`|`string`|The slug of the pipeline
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_artifacts`**
List all artifacts for a build across all jobs, including file details, paths, sizes, MIME types, and download URLs
Parameters|Type|Description
-|-|-
`build_number`|`string`|The build number
`org`|`string`|The organization slug for the owner of the pipeline
`pipeline_slug`|`string`|The slug of the pipeline

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_builds`**
List all builds for a pipeline with their status, commit information, and metadata
Parameters|Type|Description
-|-|-
`org`|`string`|The organization slug for the owner of the pipeline
`pipeline_slug`|`string`|The slug of the pipeline
`branch`|`string` *optional*|Filter builds by git branch name
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_cluster_queues`**
List all queues in a cluster with their keys, descriptions, dispatch status, and agent configuration
Parameters|Type|Description
-|-|-
`cluster_id`|`string`|The id of the cluster
`org`|`string`|The organization slug for the owner of the pipeline
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_clusters`**
List all clusters in an organization with their names, descriptions, default queues, and creation details
Parameters|Type|Description
-|-|-
`org`|`string`|The organization slug for the owner of the pipeline
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_pipelines`**
List all pipelines in an organization with their basic details, build counts, and current status
Parameters|Type|Description
-|-|-
`org`|`string`|The organization slug for the owner of the pipeline
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_test_runs`**
List all test runs for a test suite in Buildkite Test Engine
Parameters|Type|Description
-|-|-
`org`|`string`|The organization slug for the owner of the test suite
`test_suite_slug`|`string`|The slug of the test suite
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`update_pipeline`**
Modify an existing Buildkite pipeline's configuration, repository, settings, or metadata
Parameters|Type|Description
-|-|-
`org_slug`|`string`|The organization slug for the owner of the pipeline. This is used to determine where to update the pipeline
`pipeline_slug`|`string`|The slug of the pipeline to update
`cancel_running_branch_builds`|`boolean` *optional*|Cancel running builds when new builds are created on the same branch
`cluster_id`|`string` *optional*|The ID value of the cluster the pipeline will be associated with
`configuration`|`string` *optional*|The pipeline configuration in YAML format. Contains the build steps and pipeline settings. If not provided, the existing configuration will be used
`default_branch`|`string` *optional*|The default branch for builds and metrics filtering
`description`|`string` *optional*|The description of the pipeline
`name`|`string` *optional*|The name of the pipeline
`repository_url`|`string` *optional*|The Git repository URL to use for the pipeline
`skip_queued_branch_builds`|`boolean` *optional*|Skip intermediate builds when new builds are created on the same branch
`tags`|`array` *optional*|Tags to apply to the pipeline. These can be used for filtering and organization

---
#### Tool: **`user_token_organization`**
Get the organization associated with the user token used for this request
