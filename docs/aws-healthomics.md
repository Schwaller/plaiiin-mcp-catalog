Generate, run, debug lifescience workflows.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-healthomics-mcp-server](https://hub.docker.com/repository/docker/mcp/aws-healthomics-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (73)
Tools provided by this Server|Short Description
-|-
`ActivateAHOReadSets`|Activate archived read sets in a HealthOmics sequence store.|
`AnalyzeAHORunPerformance`|Analyze AWS HealthOmics workflow run performance and provide optimization recommendations.|
`CancelAHORunBatch`|Cancel all runs in a HealthOmics batch.|
`CheckContainerAvailability`|Check if a container image is available in ECR and accessible by HealthOmics.|
`CloneContainerToECR`|Clone a container image to a private ECR repository for HealthOmics use.|
`CreateAHOConfiguration`|Create a new HealthOmics configuration.|
`CreateAHORunCache`|Create a new HealthOmics run cache.|
`CreateAHORunGroup`|Create a new HealthOmics run group.|
`CreateAHOSequenceStore`|Create a new HealthOmics sequence store.|
`CreateAHOWorkflow`|Create a new HealthOmics workflow.|
`CreateAHOWorkflowVersion`|Create a new version of an existing workflow.|
`CreateCodeConnection`|Create a new CodeConnection.|
`CreateContainerRegistryMap`|Create a container registry map for HealthOmics workflows.|
`CreatePullThroughCacheForHealthOmics`|Create a pull-through cache rule configured for HealthOmics.|
`DeleteAHOBatch`|Delete a HealthOmics batch metadata (does not delete runs).|
`DeleteAHOConfiguration`|Delete a HealthOmics configuration.|
`DeleteAHORunBatch`|Delete all runs in a HealthOmics batch.|
`DiagnoseAHORunFailure`|Provides comprehensive diagnostic information for a failed workflow run.|
`GenerateAHORunTimeline`|Generate a Gantt-style timeline visualization for an AWS HealthOmics workflow run.|
`GetAHOBatch`|Get details of a specific HealthOmics batch.|
`GetAHOConfiguration`|Get details of a specific HealthOmics configuration.|
`GetAHOReadSetExportJob`|Get details about a read set export job.|
`GetAHOReadSetImportJob`|Get details about a read set import job.|
`GetAHOReadSetMetadata`|Get metadata for a specific read set in a HealthOmics sequence store.|
`GetAHOReferenceImportJob`|Get details about a reference import job.|
`GetAHOReferenceMetadata`|Get metadata for a specific reference in a HealthOmics reference store.|
`GetAHOReferenceStore`|Get details about a specific HealthOmics reference store.|
`GetAHORun`|Get details about a specific run.|
`GetAHORunCache`|Get details of a specific HealthOmics run cache.|
`GetAHORunEngineLogs`|Retrieve engine logs containing STDOUT and STDERR from the workflow engine process.|
`GetAHORunGroup`|Get details of a specific HealthOmics run group.|
`GetAHORunLogs`|Retrieve high-level run logs that show workflow execution events.|
`GetAHORunManifestLogs`|Retrieve run manifest logs produced when a workflow completes or fails.|
`GetAHORunTask`|Get details about a specific task.|
`GetAHOSequenceStore`|Get details about a specific HealthOmics sequence store.|
`GetAHOSupportedRegions`|Get the list of AWS regions where HealthOmics is available.|
`GetAHOTaskLogs`|Retrieve logs for a specific workflow task containing STDOUT and STDERR.|
`GetAHOWorkflow`|Get details about a specific workflow.|
`GetCodeConnection`|Get details about a specific CodeConnection.|
`GetSupportedFileTypes`|Get information about supported genomics file types.|
`GrantHealthOmicsRepositoryAccess`|Grant HealthOmics access to an ECR repository.|
`LintAHOWorkflowBundle`|Lint multi-file WDL or CWL workflow bundles and return validation findings.|
`LintAHOWorkflowDefinition`|Lint WDL or CWL workflow definitions and return validation findings.|
`ListAHOBatches`|List HealthOmics batches.|
`ListAHOConfigurations`|List HealthOmics configurations.|
`ListAHOReadSetExportJobs`|List read set export jobs for a sequence store.|
`ListAHOReadSetImportJobs`|List read set import jobs for a sequence store.|
`ListAHOReadSets`|List read sets in a HealthOmics sequence store with optional filtering.|
`ListAHOReferenceImportJobs`|List reference import jobs for a reference store.|
`ListAHOReferenceStores`|List HealthOmics reference stores.|
`ListAHOReferences`|List references in a HealthOmics reference store with optional filtering.|
`ListAHORunCaches`|List HealthOmics run caches.|
`ListAHORunGroups`|List HealthOmics run groups.|
`ListAHORunTasks`|List tasks for a specific run.|
`ListAHORuns`|List workflow runs.|
`ListAHORunsInBatch`|List runs within a HealthOmics batch.|
`ListAHOSequenceStores`|List HealthOmics sequence stores.|
`ListAHOWorkflowVersions`|List versions of a workflow.|
`ListAHOWorkflows`|List available HealthOmics workflows.|
`ListCodeConnections`|List available CodeConnections.|
`ListECRRepositories`|List ECR repositories with HealthOmics accessibility status.|
`ListPullThroughCacheRules`|List pull-through cache rules with HealthOmics usability status.|
`PackageAHOWorkflow`|Package workflow definition files into a base64-encoded ZIP.|
`SearchGenomicsFiles`|Search for genomics files across S3 buckets, HealthOmics sequence stores, and reference stores.|
`StartAHOReadSetExportJob`|Start a read set export job to export read sets from a sequence store to S3.|
`StartAHOReadSetImportJob`|Start a read set import job to import genomic files from S3 into a sequence store.|
`StartAHOReferenceImportJob`|Start a reference import job to import reference files from S3 into a reference store.|
`StartAHORun`|Start a workflow run.|
`StartAHORunBatch`|Start a new HealthOmics run batch.|
`UpdateAHORunCache`|Update an existing HealthOmics run cache.|
`UpdateAHORunGroup`|Update an existing HealthOmics run group.|
`UpdateAHOSequenceStore`|Update a HealthOmics sequence store.|
`ValidateHealthOmicsECRConfig`|Validate ECR configuration for HealthOmics workflows.|

---
## Tools Details

#### Tool: **`ActivateAHOReadSets`**
Activate archived read sets in a HealthOmics sequence store.

Starts an activation job to move read sets from archive storage back to active storage.
Parameters|Type|Description
-|-|-
`read_set_ids`|`string`|List of read set IDs to activate as a JSON list or array, e.g. ["id1", "id2"]
`sequence_store_id`|`string`|The ID of the sequence store
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.

---
#### Tool: **`AnalyzeAHORunPerformance`**
Analyze AWS HealthOmics workflow run performance and provide optimization recommendations.

This tool analyzes HealthOmics workflow runs to help users optimize:
- Resource utilization patterns (CPU, memory)
- Cost optimization opportunities
- Performance bottlenecks
- Resource allocation efficiency
- Runtime optimization suggestions

Use this tool when users ask about:
- "How can I optimize my HealthOmics runs?"
- "Why is my workflow using too many resources?"
- "How can I reduce costs for my genomic workflows?"
- "What resources are being wasted in my runs?"
- "How can I improve workflow performance?"

The tool summarizes run manifest logs containing task-level metrics
and provides a structured report with recommendations for optimization.
Parameters|Type|Description
-|-|-
`run_ids`|`string`|List of run IDs to analyze for resource optimization. Can be provided as a JSON array string like ["run1", "run2"] or as a comma-separated string like "run1,run2"
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`detailed`|`boolean` *optional*|Include very detailed task metrics in the report. Typically this is only required for granular analysis and can consume a large number of tokens in the agents context window. Default is False.
`headroom`|`number` *optional*|Headroom percentage for instance recommendations (0.0 to 1.0). Default is 0.20 (20%). This adds a buffer to recommended instance sizes to prevent over-optimization. Set this value to 0 for aggressive optimization

---
#### Tool: **`CancelAHORunBatch`**
Cancel all runs in a HealthOmics batch.
Parameters|Type|Description
-|-|-
`batch_id`|`string`|ID of the batch to cancel
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.

---
#### Tool: **`CheckContainerAvailability`**
Check if a container image is available in ECR and accessible by HealthOmics.

Queries ECR to determine if a specific container image exists in a repository
and whether HealthOmics has the required permissions to pull the image.
For pull-through cache repositories, indicates that the image may be pulled
on first access even if not currently cached.

When initiate_pull_through is True and the image is not found in a pull-through
cache repository that is accessible to HealthOmics, this function will attempt
to initiate the pull-through using ECR's batch_get_image API call. This triggers
ECR to pull the image from the upstream registry and cache it locally.
Parameters|Type|Description
-|-|-
`repository_name`|`string`|ECR repository name (e.g., "my-repo" or "docker-hub/library/ubuntu")
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`image_digest`|`string` *optional*|Image digest (sha256:...) - if provided, takes precedence over tag
`image_tag`|`string` *optional*|Image tag to check (default: "latest")
`initiate_pull_through`|`boolean` *optional*|If True and the image is not found in a pull-through cache repository that is accessible to HealthOmics, attempt to initiate the pull-through using batch_get_image API call

---
#### Tool: **`CloneContainerToECR`**
Clone a container image to a private ECR repository for HealthOmics use.

This tool copies a container image from an upstream registry (Docker Hub, Quay.io,
ECR Public) to your private ECR repository with appropriate HealthOmics access
permissions. It uses ECR pull-through cache to perform the copy.

The tool will:
1. Parse the source image reference (handling Docker Hub shorthand like "ubuntu:latest")
2. Find an existing pull-through cache rule for the source registry
3. Use the pull-through cache to pull the image into ECR
4. Grant HealthOmics access permissions to the repository
5. Return the ECR URI and digest for use in workflows

Image reference formats supported:
- "ubuntu:latest" -> registry-1.docker.io/library/ubuntu:latest
- "myorg/myimage:v1" -> registry-1.docker.io/myorg/myimage:v1
- "quay.io/biocontainers/samtools:1.17" -> quay.io/biocontainers/samtools:1.17
- "public.ecr.aws/lts/ubuntu:22.04" -> public.ecr.aws/lts/ubuntu:22.04
Parameters|Type|Description
-|-|-
`source_image`|`string`|Source container image reference (e.g., "ubuntu:latest", "myorg/myimage:v1", "quay.io/org/image:tag")
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`target_image_tag`|`string` *optional*|Target image tag. If not provided, uses source tag or "latest".
`target_repository_name`|`string` *optional*|Target ECR repository name. Only used if no pull-through cache exists. If not provided, derives from source image.

---
#### Tool: **`CreateAHOConfiguration`**
Create a new HealthOmics configuration.
Parameters|Type|Description
-|-|-
`name`|`string`|Configuration name (max 50 chars)
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`description`|`string` *optional*|Configuration description
`run_configurations`|`string` *optional*|Run configuration settings (e.g. securityGroupIds and subnetIds)
`tags`|`string` *optional*|Resource tags

---
#### Tool: **`CreateAHORunCache`**
Create a new HealthOmics run cache.
Parameters|Type|Description
-|-|-
`cache_behavior`|`string`|Cache behavior (CACHE_ALWAYS or CACHE_ON_FAILURE)
`cache_s3_location`|`string`|S3 URI for cache storage (e.g., s3://bucket/prefix)
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`cache_bucket_owner_id`|`string` *optional*|AWS account ID of the S3 bucket owner for cross-account access
`description`|`string` *optional*|Description for the run cache
`name`|`string` *optional*|Name for the run cache
`tags`|`string` *optional*|Tags to apply to the run cache

---
#### Tool: **`CreateAHORunGroup`**
Create a new HealthOmics run group.
Parameters|Type|Description
-|-|-
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`max_cpus`|`string` *optional*|Maximum CPUs for the run group (1-100000)
`max_duration`|`string` *optional*|Maximum duration in minutes (1-100000)
`max_gpus`|`string` *optional*|Maximum GPUs for the run group (1-100000)
`max_runs`|`string` *optional*|Maximum concurrent runs (1-100000)
`name`|`string` *optional*|Name for the run group (1-128 characters)
`tags`|`string` *optional*|Tags to apply to the run group

---
#### Tool: **`CreateAHOSequenceStore`**
Create a new HealthOmics sequence store.
Parameters|Type|Description
-|-|-
`name`|`string`|Name for the new sequence store
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`description`|`string` *optional*|Optional description for the sequence store
`fallback_location`|`string` *optional*|S3 URI for the fallback location of the sequence store
`sse_kms_key_arn`|`string` *optional*|KMS key ARN for server-side encryption of the sequence store
`tags`|`string` *optional*|Tags to apply to the sequence store as a JSON string or object, e.g. {"key": "value"}

---
#### Tool: **`CreateAHOWorkflow`**
Create a new HealthOmics workflow.
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the workflow
`accelerators`|`string` *optional*|Computational accelerator type (GPU). Currently unused by the HealthOmics service. Reserved for future support.
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`container_registry_map`|`string` *optional*|Optional container registry map with registryMappings (upstreamRegistryUrl, ecrRepositoryPrefix, upstreamRepositoryPrefix, ecrAccountId) and imageMappings (sourceImage, destinationImage) arrays
`container_registry_map_uri`|`string` *optional*|Optional S3 URI pointing to a JSON file containing container registry mappings. Cannot be used together with container_registry_map
`definition_repository`|`string` *optional*|Git repository configuration with connection_arn, full_repository_id, source_reference (type and value), and optional exclude_file_patterns. Cannot be used together with definition_source or definition_uri
`definition_source`|`string` *optional*|Workflow definition content: a local ZIP file path, S3 URI (s3://bucket/key.zip), or base64-encoded ZIP content. Cannot be used together with definition_uri or definition_repository.
`definition_uri`|`string` *optional*|S3 URI of the workflow definition ZIP file. Cannot be used together with definition_source or definition_repository
`definition_zip_base64`|`string` *optional*|[Deprecated: use definition_source] Base64-encoded workflow definition ZIP file.
`description`|`string` *optional*|Optional description of the workflow
`engine`|`string` *optional*|Workflow engine type (WDL, NEXTFLOW, CWL, WDL_LENIENT). WDL_LENIENT allows for some WDL directives that don't strictly meet the WDL spec and can be useful when migrating legacy workflows designed to run on Cromwell
`parameter_template`|`string` *optional*|Optional parameter template for the workflow
`parameter_template_path`|`string` *optional*|Path to parameter template JSON file within the repository (only valid with definition_repository)
`path_to_main`|`string` *optional*|Path to the main file in the workflow definition ZIP file. Not required if there is a top level main.wdl, main.cwl or main.nf files in the workflow package. Not required if there is only a single top level workflow file.
`readme`|`string` *optional*|README documentation: markdown content, local .md file path, or S3 URI (s3://bucket/key)
`readme_path`|`string` *optional*|Path to README markdown file within the repository (only valid with definition_repository)
`storage_capacity`|`string` *optional*|Default static storage capacity in GiB for workflow runs (required when storage_type is STATIC)
`storage_type`|`string` *optional*|Storage type for workflow runs (STATIC or DYNAMIC)
`tags`|`string` *optional*|Tags to apply to the workflow as a dict or JSON string, e.g. {"key": "value"}
`workflow_bucket_owner_id`|`string` *optional*|Expected AWS account ID of the S3 bucket owner for definition URI validation

---
#### Tool: **`CreateAHOWorkflowVersion`**
Create a new version of an existing workflow.
Parameters|Type|Description
-|-|-
`version_name`|`string`|Name for the new version
`workflow_id`|`string`|ID of the workflow
`accelerators`|`string` *optional*|Computational accelerator type (GPU). Currently unused by the HealthOmics service. Reserved for future support.
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`container_registry_map`|`string` *optional*|Optional container registry map with registryMappings (upstreamRegistryUrl, ecrRepositoryPrefix, upstreamRepositoryPrefix, ecrAccountId) and imageMappings (sourceImage, destinationImage) arrays
`container_registry_map_uri`|`string` *optional*|Optional S3 URI pointing to a JSON file containing container registry mappings. Cannot be used together with container_registry_map
`definition_repository`|`string` *optional*|Git repository configuration with connection_arn, full_repository_id, source_reference (type and value), and optional exclude_file_patterns. Cannot be used together with definition_source or definition_uri
`definition_source`|`string` *optional*|Workflow definition content: a local ZIP file path, S3 URI (s3://bucket/key.zip), or base64-encoded ZIP content. Cannot be used together with definition_uri or definition_repository.
`definition_uri`|`string` *optional*|S3 URI of the workflow definition ZIP file. Cannot be used together with definition_source or definition_repository
`definition_zip_base64`|`string` *optional*|[Deprecated: use definition_source] Base64-encoded workflow definition ZIP file.
`description`|`string` *optional*|Optional description of the workflow version
`engine`|`string` *optional*|Workflow engine type (WDL, NEXTFLOW, CWL, WDL_LENIENT). WDL_LENIENT allows for some WDL directives that don't strictly meet the WDL spec and can be useful when migrating legacy workflows designed to run on Cromwell
`parameter_template`|`string` *optional*|Optional parameter template for the workflow
`parameter_template_path`|`string` *optional*|Path to parameter template JSON file within the repository (only valid with definition_repository)
`path_to_main`|`string` *optional*|Path to the main file in the workflow definition ZIP file. Not required if there is a top level main.wdl, main.cwl or main.nf files in the workflow package. Not required if there is only a single top level workflow file.
`readme`|`string` *optional*|README documentation: markdown content, local .md file path, or S3 URI (s3://bucket/key)
`readme_path`|`string` *optional*|Path to README markdown file within the repository (only valid with definition_repository)
`storage_capacity`|`string` *optional*|Storage capacity in GB (required for STATIC)
`storage_type`|`string` *optional*|Storage type (STATIC or DYNAMIC)
`tags`|`string` *optional*|Tags to apply to the workflow version as a dict or JSON string, e.g. {"key": "value"}
`workflow_bucket_owner_id`|`string` *optional*|Expected AWS account ID of the S3 bucket owner for definition URI validation

---
#### Tool: **`CreateCodeConnection`**
Create a new CodeConnection.

This function creates a new AWS CodeConnection for connecting to a
third-party Git provider. The connection will be created in PENDING
status and requires OAuth authorization in the AWS Console to become
AVAILABLE.
Parameters|Type|Description
-|-|-
`connection_name`|`string`|Name for the new connection
`provider_type`|`string`|Git provider type: Bitbucket, GitHub, GitHubEnterpriseServer, GitLab, GitLabSelfManaged
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`tags`|`string` *optional*|Optional tags to apply to the connection

---
#### Tool: **`CreateContainerRegistryMap`**
Create a container registry map for HealthOmics workflows.

Creates a container registry map file that can be used when creating HealthOmics
workflows. Registry mappings allow workflows to use container images from upstream
registries (Docker Hub, Quay.io, ECR Public) without modifying the workflow
definition. The mappings redirect container pulls to your private ECR pull-through
caches.

By default, this tool discovers all HealthOmics-usable pull-through cache rules
in your ECR registry and creates mappings for them. You can also provide additional
registry mappings or specific image mappings for container overrides.
Parameters|Type|Description
-|-|-
`additional_registry_mappings`|`string` *optional*|Additional registry mappings to include beyond discovered pull-through caches. Each mapping has 'upstreamRegistryUrl' and 'ecrRepositoryPrefix'.
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.
`ecr_account_id`|`string` *optional*|AWS account ID for ECR repositories. If not provided, uses the current AWS account.
`ecr_region`|`string` *optional*|AWS region for ECR repositories. If not provided, uses the current configured region.
`image_mappings`|`string` *optional*|List of specific image mappings for container overrides. Each mapping has 'sourceImage' and 'destinationImage'. These take precedence over registry mappings.
`include_pull_through_caches`|`boolean` *optional*|If true, automatically discovers HealthOmics-usable ECR pull-through cache rules and creates registry mappings for them.
`output_format`|`string` *optional*|Output format: 'json' for raw JSON string, 'dict' for Python dictionary

---
#### Tool: **`CreatePullThroughCacheForHealthOmics`**
Create a pull-through cache rule configured for HealthOmics.

Creates an ECR pull-through cache rule for the specified upstream registry
and configures the necessary permissions for HealthOmics to use it. This includes:
1. Creating the pull-through cache rule
2. Updating the registry permissions policy to allow HealthOmics to create
   repositories and import images
3. Creating a repository creation template that grants HealthOmics the
   required permissions to pull images
Parameters|Type|Description
-|-|-
`upstream_registry`|`string`|Upstream registry type: docker-hub, quay, or ecr-public
`aws_profile`|`string` *optional*|AWS profile name for this operation. Overrides the default credential chain.
`aws_region`|`string` *optional*|AWS region for this operation. Overrides the server default.

[...]

## Screenshots

![AWS HealthOmics screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-healthomics-1.png)

![AWS HealthOmics screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-healthomics-2.png)

![AWS HealthOmics screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-healthomics-3.png)
