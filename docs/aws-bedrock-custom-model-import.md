Manage custom models in Bedrock.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-bedrock-custom-model-import-mcp-server](https://hub.docker.com/repository/docker/mcp/aws-bedrock-custom-model-import-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (6)
Tools provided by this Server|Short Description
-|-
`create_model_import_job`|Create a model import job to import a model into Amazon Bedrock.|
`delete_imported_model`|Delete an imported model from Amazon Bedrock.|
`get_imported_model`|Get imported model details from Amazon Bedrock.|
`get_model_import_job`|Get model import job details from Amazon Bedrock.|
`list_imported_models`|List imported models in Amazon Bedrock.|
`list_model_import_jobs`|List model import jobs in Amazon Bedrock.|

---
## Tools Details

#### Tool: **`create_model_import_job`**
Create a model import job to import a model into Amazon Bedrock.

This tool creates a model import job in Amazon Bedrock to import a custom model.
The job name and model name are mandatory parameters. The S3 URI for the model data source
is optional and will be automatically inferred from the model name if not provided.

## Usage Instructions
1. Create descriptive job and model names based on the model you want to import
   - The tool itself will automatically add a timestamp suffix to distinguish names from multiple imports
   - Example: For a LLAMA-2 model, use "llama-2-import-job" and "llama-2" for job name and model name respectively
2. The S3 URI is NOT required - it will be automatically inferred from the model name
3. For advanced configurations, you can optionally specify:
   - Role ARN for permissions
   - VPC configuration for secure imports
   - KMS key for encryption
   - Tags for resource organization

## Best Practices
- Use clear, descriptive names for both jobName and importedModelName
- Name the model based on its architecture and purpose (e.g., "llama-2-7b-chat")
- When importing multiple versions of the same model, use consistent naming with version indicators
Parameters|Type|Description
-|-|-
`request`|`string`|The model import job request containing job name, model name, and optional parameters

---
#### Tool: **`delete_imported_model`**
Delete an imported model from Amazon Bedrock.

This tool permanently deletes a custom model that was previously imported into Amazon Bedrock.
This operation cannot be undone and will permanently remove the model from your AWS account.

## Usage Instructions
1. Provide either the model name or ARN as the model_identifier parameter
2. You can get a list of available models using the list_imported_models tool
3. Verify you're deleting the correct model before proceeding

## Important Considerations
- This operation is IRREVERSIBLE - the model will be permanently deleted
- Any applications using this model will fail after deletion
- Consider backing up important model data before deletion
- Deletion may take some time to complete for large models

## When to Use
- When you no longer need a specific model
- To manage costs by removing unused models
Parameters|Type|Description
-|-|-
`model_identifier`|`string`|The name or ARN of the model to delete

---
#### Tool: **`get_imported_model`**
Get imported model details from Amazon Bedrock.

This tool retrieves detailed information about a custom model that was previously
imported into Amazon Bedrock. If the exact model name is not found, it will attempt
to find a close match using approximate matching.

## Usage Instructions
1. Provide the model name or ARN as the model_identifier parameter
2. The tool will attempt to find close matches if the exact name isn't found

## Information Returned
- Model ARN and creation time
- Model architecture details
- Whether the model supports chat or instructions
- Custom model units used for billing the model (if applicable)
- KMS key information (if encrypted)
- Import job details and data source

## How to Use This Information
- Verify model details before using in applications
- Check if the model supports instruction for chat applications using Bedrock Converse API
- Review the model details to trace model provenance
- Use the model ARN when configuring inference endpoints
Parameters|Type|Description
-|-|-
`model_identifier`|`string`|Name or ARN of the model

---
#### Tool: **`get_model_import_job`**
Get model import job details from Amazon Bedrock.

This tool retrieves detailed information about a model import job in Amazon Bedrock.
If the exact job name is not found, it will attempt to find a close match.

## Usage Instructions
1. Provide the job name or ARN as the job_identifier parameter
2. The tool will attempt to find close matches if the exact name isn't found

## Information Returned
- Job status (In Progress, Completed, or Failed)
- Creation, modification, and completion timestamps
- Job ARN and failure message (if applicable)
- Model details including name and ARN
- Configuration details including role ARN, data source, VPC config, and KMS key

## When to Use
- To check the status of an ongoing model import
- To troubleshoot failed imports by examining error messages
- To verify the configuration of a completed import
- To get the ARN of an imported model after job completion

## Status Indicators
- 🔄 In Progress: The import job is currently running
- ✅ Completed: The import job has successfully completed
- ❌ Failed: The import job encountered an error
Parameters|Type|Description
-|-|-
`job_identifier`|`string`|Name or ARN of the job

---
#### Tool: **`list_imported_models`**
List imported models in Amazon Bedrock.

This tool retrieves a list of models that have already been imported into Amazon Bedrock.
The results can be filtered and sorted using the optional request parameters.

## Usage Instructions
1. Call this tool without parameters to list all imported models
2. Optionally provide filtering parameters in the request:
   - creationTimeAfter: Filter models created after this time
   - creationTimeBefore: Filter models created before this time
   - nameContains: Filter models by name substring
   - sortBy: Sort results by field (e.g., CreationTime)
   - sortOrder: Sort order (Ascending, Descending)

## Information Returned
- Model name and ARN
- Creation time
- Model architecture
- Whether the model supports instruction tuning (✅ or ❌)

## How to Use This Information
- Note model names for use with other tools like get_imported_model
- Check instruction support to determine if models can be used for chat applications
- Review model architectures to understand model capabilities

## When to Use
- Before using get_imported_model to find the exact model name
- When you need to see all available models in your account
- To check if a specific model exists by filtering with nameContains
- To find the most recently imported models by sorting by creation time
Parameters|Type|Description
-|-|-
`request`|`string` *optional*|Optional request parameters for filtering and sorting the results

---
#### Tool: **`list_model_import_jobs`**
List model import jobs in Amazon Bedrock.

This tool retrieves a list of model import jobs in Amazon Bedrock.
The results can be filtered and sorted using the optional request parameters.

## Usage Instructions
1. Call this tool without parameters to list all model import jobs
2. Optionally provide filtering parameters in the request:
   - creationTimeAfter: Filter jobs created after this time
   - creationTimeBefore: Filter jobs created before this time
   - statusEquals: Filter jobs by status (InProgress, Completed, Failed)
   - nameContains: Filter jobs by name substring
   - sortBy: Sort results by field (e.g., CreationTime)
   - sortOrder: Sort order (Ascending, Descending)

## Information Returned
- Job name and ARN
- Status with visual indicator (🔄 In Progress, ✅ Completed, ❌ Failed)
- Creation and last modified times
- Associated model name and ARN

## How to Use This Information
- Monitor ongoing imports with status indicators
- Find recently created or modified jobs
- Identify completed jobs to access their imported models
- Troubleshoot failed imports

## When to Use
- To check the status of recent model imports
- Before using get_model_import_job to find the exact job name
- To monitor multiple ongoing imports
- To verify if a specific import job exists
- To find the job associated with a specific model
Parameters|Type|Description
-|-|-
`request`|`string` *optional*|Optional request parameters for filtering and sorting the results

---

## Screenshots

![AWS Bedrock Custom Model Import screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-bedrock-custom-model-import-1.png)

![AWS Bedrock Custom Model Import screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-bedrock-custom-model-import-2.png)

![AWS Bedrock Custom Model Import screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-bedrock-custom-model-import-3.png)
