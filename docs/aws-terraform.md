Terraform on AWS best practices, infrastructure as code patterns, and security compliance with Checkov.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-terraform](https://hub.docker.com/repository/docker/mcp/aws-terraform)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (7)
Tools provided by this Server|Short Description
-|-
`ExecuteTerraformCommand`|[DEPRECATED] Execute Terraform workflow commands against an AWS account.|
`ExecuteTerragruntCommand`|[DEPRECATED] Execute Terragrunt workflow commands against an AWS account.|
`RunCheckovScan`|[DEPRECATED] Run Checkov security scan on Terraform code.|
`SearchAwsProviderDocs`|[DEPRECATED] Search AWS provider documentation for resources and attributes.|
`SearchAwsccProviderDocs`|[DEPRECATED] Search AWSCC provider documentation for resources and attributes.|
`SearchSpecificAwsIaModules`|[DEPRECATED] Search for specific AWS-IA Terraform modules.|
`SearchUserProvidedModule`|[DEPRECATED] Search for a user-provided Terraform registry module.|

---
## Tools Details

#### Tool: **`ExecuteTerraformCommand`**
[DEPRECATED] Execute Terraform workflow commands against an AWS account.

DEPRECATED: This server is deprecated. Use HashiCorp's official Terraform
MCP Server instead: https://github.com/hashicorp/terraform-mcp-server

This tool runs Terraform commands (init, plan, validate, apply, destroy) in the
specified working directory, with optional variables and region settings.

Parameters:
    command: Terraform command to execute
    working_directory: Directory containing Terraform files
    variables: Terraform variables to pass
    aws_region: AWS region to use
    strip_ansi: Whether to strip ANSI color codes from output

Returns:
    A TerraformExecutionResult object containing command output and status
Parameters|Type|Description
-|-|-
`command`|`string`|Terraform command to execute
`working_directory`|`string`|Directory containing Terraform files
`aws_region`|`string` *optional*|AWS region to use
`strip_ansi`|`boolean` *optional*|Whether to strip ANSI color codes from output
`variables`|`string` *optional*|Terraform variables to pass

---
#### Tool: **`ExecuteTerragruntCommand`**
[DEPRECATED] Execute Terragrunt workflow commands against an AWS account.

DEPRECATED: This server is deprecated. Use HashiCorp's official Terraform
MCP Server instead: https://github.com/hashicorp/terraform-mcp-server

This tool runs Terragrunt commands (init, plan, validate, apply, destroy, run-all) in the
specified working directory, with optional variables and region settings. Terragrunt extends
Terraform's functionality by providing features like remote state management, dependencies
between modules, and the ability to execute Terraform commands on multiple modules at once.

Parameters:
    command: Terragrunt command to execute
    working_directory: Directory containing Terragrunt files
    variables: Terraform variables to pass
    aws_region: AWS region to use
    strip_ansi: Whether to strip ANSI color codes from output
    include_dirs: Directories to include in a multi-module run
    exclude_dirs: Directories to exclude from a multi-module run
    run_all: Run command on all modules in subdirectories
    terragrunt_config: Path to a custom terragrunt config file (not valid with run-all)

Returns:
    A TerragruntExecutionResult object containing command output and status
Parameters|Type|Description
-|-|-
`command`|`string`|Terragrunt command to execute
`working_directory`|`string`|Directory containing Terragrunt files
`aws_region`|`string` *optional*|AWS region to use
`exclude_dirs`|`string` *optional*|Directories to exclude from a multi-module run
`include_dirs`|`string` *optional*|Directories to include in a multi-module run
`run_all`|`boolean` *optional*|Run command on all modules in subdirectories
`strip_ansi`|`boolean` *optional*|Whether to strip ANSI color codes from output
`terragrunt_config`|`string` *optional*|Path to a custom terragrunt config file (not valid with run-all)
`variables`|`string` *optional*|Terraform variables to pass

---
#### Tool: **`RunCheckovScan`**
[DEPRECATED] Run Checkov security scan on Terraform code.

DEPRECATED: This server is deprecated. Use HashiCorp's official Terraform
MCP Server instead: https://github.com/hashicorp/terraform-mcp-server

This tool runs Checkov to scan Terraform code for security and compliance issues,
identifying potential vulnerabilities and misconfigurations according to best practices.

Checkov (https://www.checkov.io/) is an open-source static code analysis tool that
can detect hundreds of security and compliance issues in infrastructure-as-code.

Parameters:
    working_directory: Directory containing Terraform files to scan
    framework: Framework to scan (default: terraform)
    check_ids: Optional list of specific check IDs to run
    skip_check_ids: Optional list of check IDs to skip
    output_format: Format for scan results (default: json)

Returns:
    A CheckovScanResult object containing scan results and identified vulnerabilities
Parameters|Type|Description
-|-|-
`working_directory`|`string`|Directory containing Terraform files
`check_ids`|`string` *optional*|Specific check IDs to run
`framework`|`string` *optional*|Framework to scan (terraform, cloudformation, etc.)
`output_format`|`string` *optional*|Output format (json, cli, etc.)
`skip_check_ids`|`string` *optional*|Check IDs to skip

---
#### Tool: **`SearchAwsProviderDocs`**
[DEPRECATED] Search AWS provider documentation for resources and attributes.

DEPRECATED: This server is deprecated. Use HashiCorp's official Terraform
MCP Server instead: https://github.com/hashicorp/terraform-mcp-server

This tool searches the Terraform AWS provider documentation for information about
a specific asset in the AWS Provider Documentation, assets can be either resources or data sources. It retrieves comprehensive details including descriptions, example code snippets, argument references, and attribute references.

Use the 'asset_type' parameter to specify if you are looking for information about provider resources, data sources, or both. Valid values are 'resource', 'data_source' or 'both'.

The tool will automatically handle prefixes - you can search for either 'aws_s3_bucket' or 's3_bucket'.

Examples:
    - To get documentation for an S3 bucket resource:
      search_aws_provider_docs(asset_name='aws_s3_bucket')

    - To search only for data sources:
      search_aws_provider_docs(asset_name='aws_ami', asset_type='data_source')

    - To search for both resource and data source documentation of a given name:
      search_aws_provider_docs(asset_name='aws_instance', asset_type='both')

Parameters:
    asset_name: Name of the service (asset) to look for (e.g., 'aws_s3_bucket', 'aws_lambda_function')
    asset_type: Type of documentation to search - 'resource' (default), 'data_source', or 'both'

Returns:
    A list of matching documentation entries with details including:
    - Resource name and description
    - URL to the official documentation
    - Example code snippets
    - Arguments with descriptions
    - Attributes with descriptions
Parameters|Type|Description
-|-|-
`asset_name`|`string`|Name of the AWS service (asset) to look for (e.g., "aws_s3_bucket", "aws_lambda_function")
`asset_type`|`string` *optional*|Type of documentation to search - 'resource' (default), 'data_source', or 'both'

---
#### Tool: **`SearchAwsccProviderDocs`**
[DEPRECATED] Search AWSCC provider documentation for resources and attributes.

DEPRECATED: This server is deprecated. Use HashiCorp's official Terraform
MCP Server instead: https://github.com/hashicorp/terraform-mcp-server

The AWSCC provider is based on the AWS Cloud Control API
and provides a more consistent interface to AWS resources compared to the standard AWS provider.

This tool searches the Terraform AWSCC provider documentation for information about
a specific asset in the AWSCC Provider Documentation, assets can be either resources or data sources. It retrieves comprehensive details including descriptions, example code snippets, and schema references.

Use the 'asset_type' parameter to specify if you are looking for information about provider resources, data sources, or both. Valid values are 'resource', 'data_source' or 'both'.

The tool will automatically handle prefixes - you can search for either 'awscc_s3_bucket' or 's3_bucket'.

Examples:
    - To get documentation for an S3 bucket resource:
      search_awscc_provider_docs(asset_name='awscc_s3_bucket')
      search_awscc_provider_docs(asset_name='awscc_s3_bucket', asset_type='resource')

    - To search only for data sources:
      search_aws_provider_docs(asset_name='awscc_appsync_api', kind='data_source')

    - To search for both resource and data source documentation of a given name:
      search_aws_provider_docs(asset_name='awscc_appsync_api', kind='both')

    - Search of a resource without the prefix:
      search_awscc_provider_docs(resource_type='ec2_instance')

Parameters:
    asset_name: Name of the AWSCC Provider resource or data source to look for (e.g., 'awscc_s3_bucket', 'awscc_lambda_function')
    asset_type: Type of documentation to search - 'resource' (default), 'data_source', or 'both'. Some resources and data sources share the same name

Returns:
    A list of matching documentation entries with details including:
    - Resource name and description
    - URL to the official documentation
    - Example code snippets
    - Schema information (required, optional, read-only, and nested structures attributes)
Parameters|Type|Description
-|-|-
`asset_name`|`string`|Name of the AWSCC service (asset) to look for (e.g., awscc_s3_bucket, awscc_lambda_function)
`asset_type`|`string` *optional*|Type of documentation to search - 'resource' (default), 'data_source', or 'both'

---
#### Tool: **`SearchSpecificAwsIaModules`**
[DEPRECATED] Search for specific AWS-IA Terraform modules.

DEPRECATED: This server is deprecated. Use HashiCorp's official Terraform
MCP Server instead: https://github.com/hashicorp/terraform-mcp-server

This tool checks for information about four specific AWS-IA modules:
- aws-ia/bedrock/aws - Amazon Bedrock module for generative AI applications
- aws-ia/opensearch-serverless/aws - OpenSearch Serverless collection for vector search
- aws-ia/sagemaker-endpoint/aws - SageMaker endpoint deployment module
- aws-ia/serverless-streamlit-app/aws - Serverless Streamlit application deployment

It returns detailed information about these modules, including their README content,
variables.tf content, and submodules when available.

The search is performed across module names, descriptions, README content, and variable
definitions. This allows you to find modules based on their functionality or specific
configuration options.

Examples:
    - To get information about all four modules:
      search_specific_aws_ia_modules()

    - To find modules related to Bedrock:
      search_specific_aws_ia_modules(query='bedrock')

    - To find modules related to vector search:
      search_specific_aws_ia_modules(query='vector search')

    - To find modules with specific configuration options:
      search_specific_aws_ia_modules(query='endpoint_name')

Parameters:
    query: Optional search term to filter modules (empty returns all four modules)

Returns:
    A list of matching modules with their details, including:
    - Basic module information (name, namespace, version)
    - Module documentation (README content)
    - Input and output parameter counts
    - Variables from variables.tf with descriptions and default values
    - Submodules information
    - Version details and release information
Parameters|Type|Description
-|-|-
`query`|`string`|Optional search term to filter modules (empty returns all four modules)

---
#### Tool: **`SearchUserProvidedModule`**
[DEPRECATED] Search for a user-provided Terraform registry module.

DEPRECATED: This server is deprecated. Use HashiCorp's official Terraform
MCP Server instead: https://github.com/hashicorp/terraform-mcp-server

This tool takes a Terraform registry module URL and analyzes its input variables,
output variables, README, and other details to provide comprehensive information
about the module.

The module URL should be in the format "namespace/name/provider" (e.g., "hashicorp/consul/aws")
or "registry.terraform.io/namespace/name/provider".

Examples:
    - To search for the HashiCorp Consul module:
      search_user_provided_module(module_url='hashicorp/consul/aws')

    - To search for a specific version of a module:
      search_user_provided_module(module_url='terraform-aws-modules/vpc/aws', version='3.14.0')

    - To search for a module with specific variables:
      search_user_provided_module(
          module_url='terraform-aws-modules/eks/aws',
          variables={'cluster_name': 'my-cluster', 'vpc_id': 'vpc-12345'}
      )

Parameters:
    module_url: URL or identifier of the Terraform module (e.g., "hashicorp/consul/aws")
    version: Optional specific version of the module to analyze
    variables: Optional dictionary of variables to use when analyzing the module

Returns:
    A SearchUserProvidedModuleResult object containing module information
Parameters|Type|Description
-|-|-
`module_url`|`string`|URL or identifier of the Terraform module (e.g., "hashicorp/consul/aws")
`variables`|`string` *optional*|Variables to use when analyzing the module
`version`|`string` *optional*|Specific version of the module to analyze

---

## Screenshots

![AWS Terraform screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/aws-terraform-1.png)

![AWS Terraform screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/aws-terraform-2.png)

![AWS Terraform screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/aws-terraform-3.png)
