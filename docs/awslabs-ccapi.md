Direct resource management with security scanning.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/ccapi-mcp-server](https://hub.docker.com/repository/docker/mcp/ccapi-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (14)
Tools provided by this Server|Short Description
-|-
`check_environment_variables`|Check if required environment variables are set correctly.|
`create_resource`|Create an AWS resource.|
`create_template`|Create a CloudFormation template from existing resources using the IaC Generator API.|
`delete_resource`|Delete an AWS resource.|
`explain`|MANDATORY: Explain any data in clear, human-readable format.|
`generate_infrastructure_code`|Generate infrastructure code before resource creation or update.|
`get_aws_account_info`|Get information about the current AWS account being used.|
`get_aws_session_info`|Get information about the current AWS session.|
`get_resource`|Get details of a specific AWS resource.|
`get_resource_request_status`|Get the status of a long running operation with the request token.|
`get_resource_schema_information`|Get schema information for an AWS resource.|
`list_resources`|List AWS resources of a specified type.|
`run_checkov`|Run Checkov security and compliance scanner on server-stored CloudFormation template.|
`update_resource`|Update an AWS resource.|

---
## Tools Details

#### Tool: **`check_environment_variables`**
Check if required environment variables are set correctly.
#### Tool: **`create_resource`**
Create an AWS resource.

This tool automatically adds default identification tags to all resources for support and troubleshooting purposes.

IMPORTANT: Always check the response for 'security_warning' field and display any warnings to the user.
Parameters|Type|Description
-|-|-
`credentials_token`|`string`|Credentials token from get_aws_session_info() to ensure AWS credentials are valid
`explained_token`|`string`|Explained token from explain() - properties will be retrieved from this token
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`region`|`string` *optional*|The AWS region that the operation should be performed in
`security_scan_token`|`string` *optional*|Security scan token from approve_security_findings() to ensure security checks were performed (only required when SECURITY_SCANNING=enabled)
`skip_security_check`|`boolean` *optional*|Skip security checks (only when SECURITY_SCANNING=disabled)

---
#### Tool: **`create_template`**
Create a CloudFormation template from existing resources using the IaC Generator API.

This tool allows you to generate CloudFormation templates from existing AWS resources
that are not already managed by CloudFormation. The template generation process is
asynchronous, so you can check the status of the process and retrieve the template
once it's complete. You can pass up to 500 resources at a time.

IMPORTANT FOR LLMs: This tool only generates CloudFormation templates. If users request
other IaC formats (Terraform, CDK, etc.), follow this workflow:
1. Use create_template() to generate CloudFormation template from existing resources
2. Convert the CloudFormation to the requested format using your native capabilities
3. For Terraform specifically: Create both resource definitions AND import blocks
   so users can import existing resources into Terraform state
   ⚠️ ALWAYS USE TERRAFORM IMPORT BLOCKS (NOT TERRAFORM IMPORT COMMANDS) ⚠️
4. Provide both the original CloudFormation and converted IaC to the user

Example workflow for "create Terraform import for these resources":
1. create_template() → get CloudFormation template
2. Convert to Terraform resource blocks
3. Generate corresponding Terraform import blocks (NOT terraform import commands)
   Example: import { to = aws_s3_bucket.example, id = "my-bucket" }
4. Provide complete Terraform configuration with import blocks

Examples:
1. Start template generation for an S3 bucket:
   create_template(
       template_name="my-template",
       resources=[{"ResourceType": "AWS::S3::Bucket", "ResourceIdentifier": {"BucketName": "my-bucket"}}],
       deletion_policy="RETAIN",
       update_replace_policy="RETAIN"
   )

2. Check status of template generation:
   create_template(template_id="arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/abcdef12-3456-7890-abcd-ef1234567890")

3. Retrieve generated template:
   create_template(
       template_id="arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/abcdef12-3456-7890-abcd-ef1234567890",
       output_format="YAML"
   )
Parameters|Type|Description
-|-|-
`deletion_policy`|`string` *optional*|Default DeletionPolicy for resources in the template (RETAIN, DELETE, or SNAPSHOT)
`output_format`|`string` *optional*|Output format for the template (JSON or YAML)
`region`|`string` *optional*|The AWS region that the operation should be performed in
`resources`|`string` *optional*|List of resources to include in the template, each with 'ResourceType' and 'ResourceIdentifier'
`template_id`|`string` *optional*|ID of an existing template generation process to check status or retrieve template
`template_name`|`string` *optional*|Name for the generated template
`update_replace_policy`|`string` *optional*|Default UpdateReplacePolicy for resources in the template (RETAIN, DELETE, or SNAPSHOT)

---
#### Tool: **`delete_resource`**
Delete an AWS resource.
Parameters|Type|Description
-|-|-
`credentials_token`|`string`|Credentials token from get_aws_session_info() to ensure AWS credentials are valid
`explained_token`|`string`|Explained token from explain() to ensure deletion was explained
`identifier`|`string`|The primary identifier of the resource to get (e.g., bucket name for S3 buckets)
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`confirmed`|`boolean` *optional*|Confirm that you want to delete this resource
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`explain`**
MANDATORY: Explain any data in clear, human-readable format.

For infrastructure operations (create/update/delete):
- CONSUMES generated_code_token and returns explained_token
- You MUST immediately display the returned explanation to user
- You MUST use the returned explained_token for create/update/delete operations

For general data explanation:
- Pass any data in 'content' parameter
- Provides comprehensive explanation of the data structure

CRITICAL: You MUST immediately display the full explanation content to the user after calling this tool.
The response contains an 'explanation' field that you MUST show to the user - this is MANDATORY.
Never proceed with create/update/delete operations without first showing the user what will happen.

Returns:
    explanation: Comprehensive explanation you MUST display to user
    explained_token: New token for infrastructure operations (if applicable)
Parameters|Type|Description
-|-|-
`content`|`string` *optional*|Any data to explain - infrastructure properties, JSON, dict, list, etc.
`context`|`string` *optional*|Context about what this data represents (e.g., 'KMS key creation', 'S3 bucket update')
`format`|`string` *optional*|Explanation format: detailed, summary, technical
`generated_code_token`|`string` *optional*|Generated code token from generate_infrastructure_code (for infrastructure operations)
`operation`|`string` *optional*|Operation type: create, update, delete, analyze
`user_intent`|`string` *optional*|Optional: User's stated purpose

---
#### Tool: **`generate_infrastructure_code`**
Generate infrastructure code before resource creation or update.
Parameters|Type|Description
-|-|-
`credentials_token`|`string`|Credentials token from get_aws_session_info() to ensure AWS credentials are valid
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`identifier`|`string` *optional*|The primary identifier of the resource for update operations
`patch_document`|`array` *optional*|A list of RFC 6902 JSON Patch operations for update operations
`properties`|`object` *optional*|A dictionary of properties for the resource
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`get_aws_account_info`**
Get information about the current AWS account being used.

Common questions this tool answers:
- "What AWS account am I using?"
- "Which AWS region am I in?"
- "What AWS profile is being used?"
- "Show me my current AWS session information"

Returns:
    A dictionary containing AWS account information:
    {
        "profile": The AWS profile name being used,
        "account_id": The AWS account ID,
        "region": The AWS region being used,
        "readonly_mode": True if the server is in read-only mode,
        "readonly_message": A message about read-only mode limitations if enabled,
        "using_env_vars": Boolean indicating if using environment variables for credentials
    }
#### Tool: **`get_aws_session_info`**
Get information about the current AWS session.

This tool provides details about the current AWS session, including the profile name,
account ID, region, and credential information. Use this when you need to confirm which
AWS session and account you're working with.

IMPORTANT: Always display the AWS context information to the user when this tool is called.
Show them: AWS Profile (or "Environment Variables"), Authentication Type, Account ID, and Region so they know
exactly which AWS account and region will be affected by any operations.

Authentication types to display:
- 'env': "Environment Variables (AWS_ACCESS_KEY_ID)"
- 'sso_profile': "AWS SSO Profile"
- 'assume_role_profile': "Assume Role Profile"
- 'standard_profile': "Standard AWS Profile"
- 'profile': "AWS Profile"

SECURITY: If displaying environment variables that contain sensitive values (AWS_ACCESS_KEY_ID,
AWS_SECRET_ACCESS_KEY), mask all but the last 4 characters with asterisks (e.g., "AKIA****1234").

Returns:
    A dictionary containing AWS session information including profile, account_id, region, etc.
Parameters|Type|Description
-|-|-
`environment_token`|`string`|Environment token from check_environment_variables() to ensure environment is properly configured

---
#### Tool: **`get_resource`**
Get details of a specific AWS resource.
Parameters|Type|Description
-|-|-
`identifier`|`string`|The primary identifier of the resource to get (e.g., bucket name for S3 buckets)
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`analyze_security`|`boolean` *optional*|Whether to perform security analysis on the resource using Checkov
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`get_resource_request_status`**
Get the status of a long running operation with the request token.
Parameters|Type|Description
-|-|-
`request_token`|`string`|The request_token returned from the long running operation
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`get_resource_schema_information`**
Get schema information for an AWS resource.

Parameters:
    resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")

Returns:
    The resource schema information
Parameters|Type|Description
-|-|-
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`list_resources`**
List AWS resources of a specified type.

Parameters:
    resource_type: The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
    region: AWS region to use (e.g., "us-east-1", "us-west-2")

Returns:
    A dictionary containing:
    {
        "resources": List of resource identifiers
    }
Parameters|Type|Description
-|-|-
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`analyze_security`|`boolean` *optional*|Whether to perform security analysis on the resources (limited to first 5 resources)
`max_resources_to_analyze`|`integer` *optional*|Maximum number of resources to analyze when analyze_security=True
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`run_checkov`**
Run Checkov security and compliance scanner on server-stored CloudFormation template.

SECURITY: This tool only scans CloudFormation templates stored server-side from generate_infrastructure_code().
AI agents cannot provide different content to bypass security scanning.

CRITICAL WORKFLOW REQUIREMENTS:
ALWAYS after running this tool:
1. Call explain() to show the security scan results to the user (both passed and failed checks)

If scan_status='FAILED' (security issues found):
2. Ask the user how they want to proceed: "fix", "proceed anyway", or "cancel"
3. WAIT for the user's actual response - do not assume their decision
4. Only after receiving user input, call approve_security_findings() with their decision

If scan_status='PASSED' (all checks passed):
2. You can proceed directly to create_resource() after showing the results

WORKFLOW REQUIREMENTS:
1. ALWAYS provide a concise summary of security findings (passed/failed checks)
2. Only show detailed output if user specifically requests it
3. If CRITICAL security issues found: BLOCK resource creation, explain risks, provide resolution steps, ask multiple times for confirmation with warnings
4. If non-critical security issues found: Ask user how to proceed (fix issues, proceed anyway, or cancel)
Parameters|Type|Description
-|-|-
`explained_token`|`string`|Explained token from explain() containing CloudFormation template to scan
`framework`|`string` *optional*|The framework to scan (cloudformation, terraform, kubernetes, etc.)

---
#### Tool: **`update_resource`**
Update an AWS resource.

IMPORTANT: Always check the response for 'security_warning' field and display any warnings to the user.
Parameters|Type|Description
-|-|-
`credentials_token`|`string`|Credentials token from get_aws_session_info() to ensure AWS credentials are valid
`explained_token`|`string`|Explained token from explain() to ensure exact properties with default tags are used
`identifier`|`string`|The primary identifier of the resource to get (e.g., bucket name for S3 buckets)
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`patch_document`|`array` *optional*|A list of RFC 6902 JSON Patch operations to apply
`region`|`string` *optional*|The AWS region that the operation should be performed in
`security_scan_token`|`string` *optional*|Security scan token from run_checkov() to ensure security checks were performed (only required when SECURITY_SCANNING=enabled)
`skip_security_check`|`boolean` *optional*|Skip security checks (not recommended)

---

## Screenshots

![AWS Cloud Control API screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-ccapi-1.png)

![AWS Cloud Control API screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-ccapi-2.png)

![AWS Cloud Control API screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-ccapi-3.png)
