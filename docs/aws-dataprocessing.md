Data processing and transformation services.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-dataprocessing-mcp-server](https://hub.docker.com/repository/docker/mcp/aws-dataprocessing-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (32)
Tools provided by this Server|Short Description
-|-
`add_inline_policy`|Add a new inline policy to an IAM role.|
`analyze_s3_usage_for_data_processing`|Analyze S3 bucket usage patterns for data processing services (Glue, EMR, Athena).|
`create_data_processing_role`|Create a new IAM role for data processing services.|
`get_policies_for_role`|Get all policies attached to an IAM role.|
`get_roles_for_service`|Get all IAM roles that can be assumed by a specific AWS service.|
`list_s3_buckets`|List S3 buckets that have 'glue' in their name and are in the specified region.|
`manage_aws_athena_data_catalogs`|Manage AWS Athena data catalogs with both read and write operations.|
`manage_aws_athena_databases_and_tables`|Manage AWS Athena databases and tables with read operations.|
`manage_aws_athena_named_queries`|Manage saved SQL queries in AWS Athena.|
`manage_aws_athena_query_executions`|Execute and manage AWS Athena SQL queries.|
`manage_aws_athena_workgroups`|Manage AWS Athena workgroups with both read and write operations.|
`manage_aws_emr_clusters`|Manage AWS EMR EC2 clusters with comprehensive control over cluster lifecycle.|
`manage_aws_emr_ec2_instances`|Manage AWS EMR EC2 instances with both read and write operations.|
`manage_aws_emr_ec2_steps`|Manage AWS EMR EC2 steps for processing data on EMR clusters.|
`manage_aws_glue_catalog`|Manage AWS Glue Data Catalog with both read and write operations.|
`manage_aws_glue_classifiers`|Manage AWS Glue classifiers to determine data formats and schemas.|
`manage_aws_glue_connections`|Manage AWS Glue Data Catalog connections with both read and write operations.|
`manage_aws_glue_crawler_management`|Manage AWS Glue crawler schedules and monitor performance metrics.|
`manage_aws_glue_crawlers`|Manage AWS Glue crawlers to discover and catalog data sources.|
`manage_aws_glue_databases`|Manage AWS Glue Data Catalog databases with both read and write operations.|
`manage_aws_glue_encryption`|Manage AWS Glue Data Catalog Encryption Settings for data protection.|
`manage_aws_glue_jobs`|Manage AWS Glue ETL jobs and job runs with both read and write operations.|
`manage_aws_glue_partitions`|Manage AWS Glue Data Catalog partitions with both read and write operations.|
`manage_aws_glue_resource_policies`|Manage AWS Glue Resource Policies for access control.|
`manage_aws_glue_security_configurations`|Manage AWS Glue Security Configurations for data encryption.|
`manage_aws_glue_sessions`|Manage AWS Glue Interactive Sessions for running Spark and Ray workloads.|
`manage_aws_glue_statements`|Manage AWS Glue Interactive Session Statements for executing code and retrieving results.|
`manage_aws_glue_tables`|Manage AWS Glue Data Catalog tables with both read and write operations.|
`manage_aws_glue_triggers`|Manage AWS Glue triggers to automate workflow and job execution.|
`manage_aws_glue_usage_profiles`|Manage AWS Glue Usage Profiles for resource allocation and cost management.|
`manage_aws_glue_workflows`|Manage AWS Glue workflows to orchestrate complex ETL activities.|
`upload_to_s3`|Upload Python code content directly to an S3 bucket using putObject.|

---
## Tools Details

#### Tool: **`add_inline_policy`**
Add a new inline policy to an IAM role.

This tool creates a new inline policy with the specified permissions and adds it to an IAM role.
Inline policies are embedded within the role and cannot be attached to multiple roles. Commonly used
for granting data processing services access to AWS resources, enabling Glue jobs to access data sources,
and configuring permissions for CloudWatch logging and S3 access.

## Requirements
- The server must be run with the `--allow-write` flag
- The role must exist in your AWS account
- The policy name must be unique within the role
- You cannot modify existing policies with this tool

## Permission Format
The permissions parameter can be either a single policy statement or a list of statements.

### Single Statement Example
```json
{
    "Effect": "Allow",
    "Action": ["s3:GetObject", "s3:PutObject"],
    "Resource": "arn:aws:s3:::example-bucket/*"
}
```

## Common Data Processing Permission Examples

### Glue Job Permissions
```json
{
    "Effect": "Allow",
    "Action": [
        "glue:*",
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket",
        "iam:PassRole"
    ],
    "Resource": "*"
}
```

### EMR Cluster Permissions
```json
{
    "Effect": "Allow",
    "Action": [
        "elasticmapreduce:*",
        "ec2:DescribeInstances",
        "ec2:DescribeSecurityGroups",
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject"
    ],
    "Resource": "*"
}
```

### Athena Query Permissions
```json
{
    "Effect": "Allow",
    "Action": [
        "athena:*",
        "glue:GetDatabase",
        "glue:GetTable",
        "glue:GetPartition",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:PutObject"
    ],
    "Resource": "*"
}
```

## Usage Tips
- Follow the principle of least privilege by granting only necessary permissions
- Use specific resources rather than "*" whenever possible
- Consider using conditions to further restrict permissions
- Group related permissions into logical policies with descriptive names
Parameters|Type|Description
-|-|-
`permissions`|`string`|Permissions to include in the policy as IAM policy statements in JSON format.
            Can be either a single statement object or an array of statement objects.
`policy_name`|`string`|Name of the inline policy to create. Must be unique within the role.
`role_name`|`string`|Name of the IAM role to add the policy to. The role must exist.

---
#### Tool: **`analyze_s3_usage_for_data_processing`**
Analyze S3 bucket usage patterns for data processing services (Glue, EMR, Athena).

This tool helps identify which buckets are actively used by data processing services
and which ones might be idle or underutilized.
Parameters|Type|Description
-|-|-
`bucket_name`|`string` *optional*|Optional specific bucket to analyze (None for all buckets)

---
#### Tool: **`create_data_processing_role`**
Create a new IAM role for data processing services.

This tool creates a new IAM role with the appropriate trust relationship for the specified
data processing service (Glue, EMR, or Athena). It can also attach managed policies and
add an inline policy to the role.

## Requirements
- The server must be run with the `--allow-write` flag
- The role name must be unique within your AWS account
- Valid AWS credentials with permissions to create IAM roles

## Service Types
- **glue**: Creates a role that can be assumed by the Glue service
- **emr**: Creates a role that can be assumed by the EMR service
- **athena**: Creates a role that can be assumed by the Athena service

## Common Managed Policies. add these policies
- Glue: 'arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole'
- EMR: 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole'
- Athena: 'arn:aws:iam::aws:policy/service-role/AmazonAthenaFullAccess'

## Usage Tips
- Always provide a descriptive name and description for the role
- Attach only the necessary managed policies to follow least privilege
- Use inline policies for custom permissions specific to your use case
- Consider adding S3 access permissions for data sources and targets
Parameters|Type|Description
-|-|-
`role_name`|`string`|Name of the IAM role to create. Must be unique within your AWS account.
`service_type`|`string`|Type of data processing service: 'glue', 'emr', or 'athena'.
`description`|`string` *optional*|Optional description for the IAM role.
`inline_policy`|`string` *optional*|Optional inline policy to add to the role.
`managed_policy_arns`|`string` *optional*|Optional list of managed policy ARNs to attach to the role.

---
#### Tool: **`get_policies_for_role`**
Get all policies attached to an IAM role.

This tool retrieves all policies associated with an IAM role, providing a comprehensive view
of the role's permissions and trust relationships. It helps you understand the current
permissions, identify missing or excessive permissions, troubleshoot data processing issues,
and verify trust relationships for service roles.

## Requirements
- The role must exist in your AWS account
- Valid AWS credentials with permissions to read IAM role information

## Response Information
The response includes role ARN, assume role policy document (trust relationships),
role description, managed policies with their documents, and inline policies with
their documents.

## Usage Tips
- Use this tool before adding new permissions to understand existing access
- Check the assume role policy to verify which services or roles can assume this role
- Look for overly permissive policies that might pose security risks
- Use with add_inline_policy to implement least-privilege permissions
- For Glue jobs, ensure the role has access to required data sources and targets
- For EMR clusters, verify EC2 instance profile permissions
- For Athena queries, check S3 bucket access permissions
Parameters|Type|Description
-|-|-
`role_name`|`string`|Name of the IAM role to get policies for. The role must exist in your AWS account.

---
#### Tool: **`get_roles_for_service`**
Get all IAM roles that can be assumed by a specific AWS service.

This tool retrieves all IAM roles in your AWS account that have a trust relationship
with the specified service. It helps you identify which roles can be used for services
like Glue jobs, EMR clusters, or Athena queries, making it easier to select the appropriate
role when creating these resources.

## Service Types
Common service types include:
- **glue**: AWS Glue service (glue.amazonaws.com)
- **emr**: Amazon EMR service (elasticmapreduce.amazonaws.com)
- **athena**: Amazon Athena service (athena.amazonaws.com)
- You can also specify other AWS service principals

## Response Information
The response includes a list of roles that can be assumed by the specified service,
with details such as role name, ARN, description, creation date, and the full
assume role policy document.

## Usage Tips
- Use this tool to find existing roles before creating new ones
- Verify that roles have the necessary permissions for your use case
- For Glue jobs, look for roles with AWSGlueServiceRole or similar policies
- For EMR clusters, look for roles with AmazonElasticMapReduceRole or similar policies
- For Athena queries, look for roles with AmazonAthenaFullAccess or similar policies
Parameters|Type|Description
-|-|-
`service_type`|`string`|Type of data processing service: 'glue', 'emr', 'athena', or other AWS service name.

---
#### Tool: **`list_s3_buckets`**
List S3 buckets that have 'glue' in their name and are in the specified region.

This tool helps identify S3 buckets commonly used for data processing workflows,
particularly those related to AWS Glue operations. It provides usage statistics
and idle time information to help with resource management.

## Requirements
- Valid AWS credentials with permissions to list S3 buckets
- S3:ListAllMyBuckets permission

## Response Information
The response includes bucket name, creation date, region, object count,
last modified date, and idle time analysis.

## Usage Tips
- Use this tool to find existing data processing buckets before creating new ones
- Monitor idle buckets that haven't been accessed for 90+ days
- Verify bucket regions match your data processing service regions
- Check object counts to understand bucket usage patterns
Parameters|Type|Description
-|-|-
`region`|`string` *optional*|AWS region to filter buckets by (defaults to AWS_REGION environment variable)

---
#### Tool: **`manage_aws_athena_data_catalogs`**
Manage AWS Athena data catalogs with both read and write operations.

This tool provides operations for managing Athena data catalogs, including creating,
retrieving, listing, updating, and deleting data catalogs. Data catalogs are used to
organize and access data sources in Athena, enabling you to query data across various
sources like AWS Glue Data Catalog, Apache Hive metastores, or federated sources.

## Requirements
- The server must be run with the `--allow-write` flag for create-data-catalog, delete-data-catalog, and update-data-catalog operations
- Appropriate AWS permissions for Athena data catalog operations

## Operations
- **create-data-catalog**: Create a new data catalog
- **delete-data-catalog**: Delete an existing data catalog
- **get-data-catalog**: Get information about a single data catalog
- **list-data-catalogs**: List all data catalogs
- **update-data-catalog**: Update an existing data catalog

## Usage Tips
- Use list-data-catalogs to find available data catalogs
- Data catalogs can be of type LAMBDA, GLUE, HIVE, or FEDERATED
- Parameters are specific to the type of data catalog

## Example
```
# List all data catalogs
{'operation': 'list-data-catalogs', 'max_results': 10}

# Create a Glue data catalog
{
    'operation': 'create-data-catalog',
    'name': 'my-glue-catalog',
    'type': 'GLUE',
    'description': 'My Glue Data Catalog',
    'parameters': {'catalog-id': '123456789012'},
}
```
Parameters|Type|Description
-|-|-
`operation`|`string`|Operation to perform: create-data-catalog, delete-data-catalog, get-data-catalog, list-data-catalogs, update-data-catalog. Choose read-only operations when write access is disabled.
`delete_catalog_only`|`string` *optional*|For delete-data-catalog operation, whether to delete only the Athena Data Catalog (true) or also its resources (false). Only applicable for FEDERATED catalogs.
`description`|`string` *optional*|Description of the data catalog (optional for create-data-catalog and update-data-catalog).
`max_results`|`string` *optional*|Maximum number of results to return for list-data-catalogs operation (range: 2-50).
`name`|`string` *optional*|Name of the data catalog (required for create-data-catalog, delete-data-catalog, get-data-catalog, update-data-catalog). The catalog name must be unique for the AWS account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters.
`next_token`|`string` *optional*|Pagination token for list-data-catalogs operation.
`parameters`|`string` *optional*|Parameters for the data catalog (optional for create-data-catalog and update-data-catalog). Format depends on catalog type (e.g., for LAMBDA: 'metadata-function=lambda_arn,record-function=lambda_arn' or 'function=lambda_arn').
`tags`|`string` *optional*|Tags for the data catalog (optional for create-data-catalog).
`type`|`string` *optional*|Type of the data catalog (required for create-data-catalog and update-data-catalog). Valid values: LAMBDA, GLUE, HIVE, FEDERATED.
`work_group`|`string` *optional*|The name of the workgroup (required if making an IAM Identity Center request).

---
#### Tool: **`manage_aws_athena_databases_and_tables`**
Manage AWS Athena databases and tables with read operations.

This tool provides operations for retrieving information about databases and tables
in Athena data catalogs. These are read-only operations that do not modify any resources.

## Requirements
- Appropriate AWS permissions for Athena database and table operations

## Operations
- **get-database**: Get information about a single database
- **get-table-metadata**: Get metadata for a specific table
- **list-databases**: List all databases in a data catalog
- **list-table-metadata**: List metadata for all tables in a database

## Usage Tips
- Use list-databases to find available databases in a data catalog
- Use list-table-metadata to find available tables in a database
- The expression parameter for list-table-metadata supports filtering tables by name pattern

## Example
```
# List all databases in a catalog
{'operation': 'list-databases', 'catalog_name': 'AwsDataCatalog', 'max_results': 10}

# Get metadata for a specific table
{
    'operation': 'get-table-metadata',
    'catalog_name': 'AwsDataCatalog',
    'database_name': 'my_database',
    'table_name': 'my_table',
}
```
Parameters|Type|Description
-|-|-
`catalog_name`|`string`|Name of the data catalog.
`operation`|`string`|Operation to perform: get-database, get-table-metadata, list-databases, list-table-metadata. These are read-only operations.
`database_name`|`string` *optional*|Name of the database (required for get-database, get-table-metadata, list-table-metadata).
`expression`|`string` *optional*|Expression to filter tables (optional for list-table-metadata). A regex pattern that pattern-matches table names.
`max_results`|`string` *optional*|Maximum number of results to return for list-databases (range: 1-50) and list-table-metadata (range: 1-50) operations.
`next_token`|`string` *optional*|Pagination token for list-databases and list-table-metadata operations.
`table_name`|`string` *optional*|Name of the table (required for get-table-metadata).
`work_group`|`string` *optional*|The name of the workgroup (required if making an IAM Identity Center request).

---
#### Tool: **`manage_aws_athena_named_queries`**
Manage saved SQL queries in AWS Athena.

This tool provides operations for creating, retrieving, updating, and deleting named queries
in AWS Athena. Named queries are saved SQL statements that can be easily reused, shared with
team members, and executed without having to rewrite complex queries.

## Requirements
- The server must be run with the `--allow-write` flag for create-named-query, delete-named-query, and update-named-query operations
- Appropriate AWS permissions for Athena named query operations

## Operations
- **batch-get-named-query**: Get details for up to 50 named queries by their IDs
- **create-named-query**: Save a new SQL query with a name and description
- **delete-named-query**: Remove a saved query
- **get-named-query**: Retrieve a single named query by ID
- **list-named-queries**: List available named query IDs
- **update-named-query**: Modify an existing named query

## Example
```python
# Create a named query
create_response = await manage_aws_athena_named_queries(
    operation='create-named-query',
    name='Daily Active Users',
    description='Query to calculate daily active users',
    database='analytics',
    query_string='SELECT date, COUNT(DISTINCT user_id) AS active_users FROM user_events GROUP BY date ORDER BY date DESC',
    work_group='primary',
)

# Later, retrieve the named query
query = await manage_aws_athena_named_queries(
    operation='get-named-query', named_query_id=create_response.named_query_id
)
```
Parameters|Type|Description
-|-|-
`operation`|`string`|Operation to perform: batch-get-named-query, create-named-query, delete-named-query, get-named-query, list-named-queries, update-named-query. Choose read-only operations when write access is disabled.
`client_request_token`|`string` *optional*|A unique case-sensitive string used to ensure the request to create the query is idempotent (optional for create-named-query).
`database`|`string` *optional*|Database context for the named query (required for create-named-query, optional for update-named-query).
`description`|`string` *optional*|Description of the named query (optional for create-named-query and update-named-query, max 1024 chars).
`max_results`|`string` *optional*|Maximum number of results to return for list-named-queries operation.
`name`|`string` *optional*|Name of the named query (required for create-named-query and update-named-query).
`named_query_id`|`string` *optional*|ID of the named query (required for get-named-query, delete-named-query, update-named-query).
`named_query_ids`|`string` *optional*|List of named query IDs (required for batch-get-named-query, max 50 IDs).
`next_token`|`string` *optional*|Pagination token for list-named-queries operation.
`query_string`|`string` *optional*|The SQL query string (required for create-named-query and update-named-query).
`work_group`|`string` *optional*|The name of the workgroup (optional for create-named-query and list-named-queries).

---
#### Tool: **`manage_aws_athena_query_executions`**
Execute and manage AWS Athena SQL queries.

This tool provides comprehensive operations for AWS Athena query management, including
starting new queries, monitoring execution status, retrieving results, and analyzing
performance statistics.

## Requirements
- The server must be run with the `--allow-write` flag if start-query-execution contains any write operation for example DDL commands, Insert, Update, Delete Commands or any flag updates
- Appropriate AWS permissions for Athena query operations

## Operations
- **batch-get-query-execution**: Get details for up to 50 query executions by their IDs
- **get-query-execution**: Get complete information about a single query execution
- **get-query-results**: Retrieve the results of a completed query
- **get-query-runtime-statistics**: Get performance statistics for a query execution
- **list-query-executions**: List available query execution IDs (up to 50)
- **start-query-execution**: Execute a new SQL query
- **stop-query-execution**: Cancel a running query

## Example
```python
# Start a new query
response = await manage_aws_athena_queries(
    operation='start-query-execution',
    query_string='SELECT * FROM my_database.my_table LIMIT 10',
    query_execution_context={'Database': 'my_database', 'Catalog': 'my_catalog'},
    work_group='primary',
)

# Get the query results
results = await manage_aws_athena_queries(
    operation='get-query-results', query_execution_id=response.query_execution_id
)
```
Parameters|Type|Description
-|-|-
`operation`|`string`|Operation to perform: batch-get-query-execution, get-query-execution, get-query-results, get-query-runtime-statistics, list-query-executions, start-query-execution, stop-query-execution. Choose read-only operations when write access is disabled.
`client_request_token`|`string` *optional*|A unique case-sensitive string used to ensure the request to create the query is idempotent (optional for start-query-execution).
`execution_parameters`|`string` *optional*|Execution parameters for parameterized queries (optional for start-query-execution).
`max_results`|`string` *optional*|Maximum number of results to return (1-1000 for get-query-results, 0-50 for list-query-executions).
`next_token`|`string` *optional*|Pagination token for get-query-results and list-query-executions operations.
`query_execution_context`|`string` *optional*|Context for the query execution, such as database name and catalog (optional for start-query-execution).
`query_execution_id`|`string` *optional*|ID of the query execution (required for get-query-execution, get-query-results, get-query-runtime-statistics, stop-query-execution).
`query_execution_ids`|`string` *optional*|List of query execution IDs (required for batch-get-query-execution, max 50 IDs).
`query_result_type`|`string` *optional*|Type of query results to return: DATA_ROWS (default) or DATA_MANIFEST (optional for get-query-results).
`query_string`|`string` *optional*|The SQL query string to execute (required for start-query-execution).
`result_configuration`|`string` *optional*|Configuration for query results, such as output location and encryption (optional for start-query-execution).
`result_reuse_configuration`|`string` *optional*|Specifies the query result reuse behavior for the query (optional for start-query-execution).
`work_group`|`string` *optional*|The name of the workgroup in which the query is being started (optional for start-query-execution, list-query-executions).

---
#### Tool: **`manage_aws_athena_workgroups`**
Manage AWS Athena workgroups with both read and write operations.

This tool provides operations for managing Athena workgroups, including creating,
retrieving, listing, updating, and deleting workgroups. Workgroups allow you to
isolate queries for different user groups and control query execution settings.

## Requirements
- The server must be run with the `--allow-write

[...]

## Screenshots

![AWS Data Processing screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-dataprocessing-1.png)

![AWS Data Processing screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-dataprocessing-2.png)

![AWS Data Processing screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-dataprocessing-3.png)
