Complete DynamoDB operations and table management.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/dynamodb-mcp-server](https://hub.docker.com/repository/docker/mcp/dynamodb-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`compute_performances_and_costs`|Calculate DynamoDB capacity units and monthly costs from access patterns.|
`dynamodb_data_model_schema_converter`|Retrieves the DynamoDB Data Model Schema Converter Expert prompt.|
`dynamodb_data_model_schema_validator`|Validates a schema.json file - the structured JSON representation of your DynamoDB data model.|
`dynamodb_data_model_validation`|Validates and tests DynamoDB data models against DynamoDB Local.|
`dynamodb_data_modeling`|Retrieves the complete DynamoDB Data Modeling Expert prompt.|
`generate_data_access_layer`|Generate Python code for a data access layer to interact with your DynamoDB tables.|
`generate_resources`|Generates resources from a DynamoDB data model JSON file (dynamodb_data_model.json).|
`source_db_analyzer`|Analyzes source database to extract schema and access patterns for DynamoDB modeling.|

---
## Tools Details

#### Tool: **`compute_performances_and_costs`**
Calculate DynamoDB capacity units and monthly costs from access patterns.

Call after completing data model design. Extracts patterns from Access Pattern Mapping
table and tables from Table Designs section in dynamodb_data_model.md.
Parameters|Type|Description
-|-|-
`access_pattern_list`|`array`|List of access patterns with operation details (required)
`table_list`|`array`|List of table definitions for storage cost calculation (required)
`workspace_dir`|`string`|Absolute path of the workspace directory (required). Cost analysis will be appended to dynamodb_data_model.md

---
#### Tool: **`dynamodb_data_model_schema_converter`**
Retrieves the DynamoDB Data Model Schema Converter Expert prompt.

This tool returns a specialized prompt for converting DynamoDB data models (dynamodb_data_model.md)
into schema.json - a structured JSON representation used for generating type-safe entities and repositories.
By default, also includes instructions for generating usage_data.json with realistic sample data.

The prompt guides through:
- Reading and parsing dynamodb_data_model.md files
- Converting table designs, GSIs, and access patterns into structured JSON format
- Validating generated schemas using the dynamodb_data_model_schema_validator tool
- Iteratively fixing validation errors (up to 8 iterations)
- Generating usage_data.json with realistic sample data from markdown tables (unless generate_usage_data=False)
- Creating isolated output folders with schema.json (and optionally usage_data.json)

When to set generate_usage_data=False:
- User explicitly asks for "schema only", "just schema", "without usage data", "without examples"
- User wants to skip sample data generation
- User only needs the schema structure for validation or review
Parameters|Type|Description
-|-|-
`generate_usage_data`|`boolean` *optional*|Set to False if user only wants schema.json without usage examples/sample data. Set to True (default) to generate both schema.json and usage_data.json with realistic sample data for code generation

---
#### Tool: **`dynamodb_data_model_schema_validator`**
Validates a schema.json file - the structured JSON representation of your DynamoDB data model.

This tool validates that your schema.json file is properly formatted and contains all required fields
for use with the repository generation tool and other automation tools. It provides detailed error
messages with suggestions for fixing any issues found.

Optionally, if usage_data_path is provided, it will also validate the usage_data.json file against
the schema to ensure consistency.

The validation checks:
- Required sections (table_config, entities) exist
- All required fields are present
- Field types are valid (string, integer, decimal, boolean, array, object, uuid)
- Enum values are correct (operation types, return types, etc.)
- Pattern IDs are unique across all entities
- GSI names match between gsi_list and gsi_mappings
- Fields referenced in templates exist in entity fields
- Range conditions are valid and have correct parameter counts
- Access patterns have valid operations and return types
- Usage data validation (if usage_data_path provided)

Security:
- Schema files must be within the current working directory or subdirectories
- Path traversal attempts (e.g., ../../../../etc/passwd) are blocked
Parameters|Type|Description
-|-|-
`schema_path`|`string`|Absolute path to the schema.json file to validate
`usage_data_path`|`string` *optional*|Optional absolute path to the usage_data.json file to validate alongside the schema

---
#### Tool: **`dynamodb_data_model_validation`**
Validates and tests DynamoDB data models against DynamoDB Local.

Use this tool to validate, test, and verify your DynamoDB data model after completing the design phase.
This tool automatically checks that all access patterns work correctly by executing them against a local
DynamoDB instance.

WHEN TO USE:
- After completing data model design with dynamodb_data_modeling tool
- When user asks to "validate", "test", "check", or "verify" their DynamoDB data model
- To ensure all access patterns execute correctly before deploying to production

WHAT IT DOES:
1. If dynamodb_data_model.json doesn't exist:
   - Returns complete JSON generation guide from json_generation_guide.md
   - Follow the guide to create the JSON file with tables, items, and access_patterns
   - Call this tool again after creating the JSON to validate

2. If dynamodb_data_model.json exists:
   - Validates the JSON structure (checks for required keys: tables, items, access_patterns)
   - Sets up DynamoDB Local environment (Docker/Podman/Finch/nerdctl or Java fallback)
   - Cleans up existing tables from previous validation runs
   - Creates tables and inserts test data from your model specification
   - Tests all defined access patterns by executing their AWS CLI implementations
   - Saves detailed validation results to dynamodb_model_validation.json
   - Transforms results to markdown format for comprehensive review

WHAT TO DO ON SUCCESSFUL COMPLETION:
After validation completes, you MUST present the user with TWO options:
1. Deploy to AWS: Call `generate_resources` tool with resource_type='cdk' to create a CDK app for provisioning tables
2. Generate Python code: Call `dynamodb_data_model_schema_converter` to convert the model to schema.json, then generate code

The user can choose one or both options. If they choose CDK first, you can still generate Python code afterward.
Parameters|Type|Description
-|-|-
`workspace_dir`|`string`|Absolute path of the workspace directory

---
#### Tool: **`dynamodb_data_modeling`**
Retrieves the complete DynamoDB Data Modeling Expert prompt.

This tool returns a prompt to help user with data modeling on DynamoDB.
The prompt guides through requirements gathering, access pattern analysis, and
schema design. The prompt contains:

- Structured 2-phase workflow (requirements → final design)
- Enterprise design patterns: hot partition analysis, write sharding, sparse GSIs, and more
- Cost optimization strategies and RPS-based capacity planning
- Multi-table design philosophy with advanced denormalization patterns
- Integration guidance for OpenSearch, Lambda, and analytics

Usage: Simply call this tool to get the expert prompt.

Returns: Complete expert system prompt as text (no parameters required)
#### Tool: **`generate_data_access_layer`**
Generate Python code for a data access layer to interact with your DynamoDB tables.

🔴 PREREQUISITE: Before calling this tool, you MUST first call `dynamodb_data_model_schema_converter`
to generate schema.json from dynamodb_data_model.md. This tool ONLY accepts schema.json.

TYPICAL WORKFLOW:
1. Complete data modeling with `dynamodb_data_modeling` tool (creates dynamodb_data_model.md)
2. Validate with `dynamodb_data_model_validation` tool (optional but recommended)
3. Optionally deploy infrastructure with `generate_resources` tool (resource_type='cdk')
4. Convert to schema: Call `dynamodb_data_model_schema_converter` tool (creates schema.json)
5. Generate code: Call this `generate_data_access_layer` tool with the path to schema.json

This tool generates a complete data access layer from your schema including:
- Type-safe entity classes with field validation using Pydantic
- Repository classes with optimistic locking and error handling for all operations
- Fully implemented access patterns
- Working usage examples with realistic sample data (if usage_data_path provided)
Parameters|Type|Description
-|-|-
`schema_path`|`string`|Path to the schema JSON file
`generate_sample_usage`|`boolean` *optional*|Generate usage examples and test cases
`language`|`string` *optional*|Target programming language (python)
`usage_data_path`|`string` *optional*|Path to usage_data.json file for realistic sample data (optional)

---
#### Tool: **`generate_resources`**
Generates resources from a DynamoDB data model JSON file (dynamodb_data_model.json).

This tool generates various resources based on the provided `dynamodb_data_model.json` file.
Currently supports generating a CDK app for deploying DynamoDB tables.

Supported resource types:
- cdk: CDK app for deploying DynamoDB tables.
       Generates a CDK app that provisions DynamoDB tables and GSIs as defined in `dynamodb_data_model.json`.

WHEN TO USE:
- After completing data model validation with `dynamodb_data_model_validation` tool
- When user asks to "deploy", "create CDK app", "generate CDK", or "provision infrastructure"
- When user wants to deploy their DynamoDB tables and GSIs to AWS using a CDK app

WHEN NOT TO USE:
- Before completing data model validation with `dynamodb_data_model_validation` tool
- Before having created the `dynamodb_data_model.json` file
- When user only wants to generate Python code without deploying infrastructure

WHAT TO DO ON SUCCESSFUL COMPLETION:
After CDK generation completes, you MUST ask the user if they want to:
1. Deploy the CDK app now (provide deployment instructions)
2. Generate Python data access layer code to interact with the tables (call `dynamodb_data_model_schema_converter` then `generate_data_access_layer`)
Parameters|Type|Description
-|-|-
`dynamodb_data_model_json_file`|`string`|Absolute path to the dynamodb_data_model.json file. Resources will be generated in the same directory.
`resource_type`|`string`|Type of resource to generate: 'cdk' for CDK app

---
#### Tool: **`source_db_analyzer`**
Analyzes source database to extract schema and access patterns for DynamoDB modeling.

WHEN TO USE: Call this tool when the user selects "Existing Database Analysis" option
after invoking the `dynamodb_data_modeling` tool. This extracts schema and query patterns
from an existing relational database to accelerate DynamoDB data model design.

IMPORTANT: Always ask the user which execution mode they prefer before calling this tool.

Execution Modes:
- self_service: Generates SQL queries for user to run manually, then parses their results.
- managed (MySQL only): Database connection via RDS Data API or hostname.

Supported Databases: MySQL, PostgreSQL, SQL Server, Oracle

Output: Generates analysis files (schema structure, access patterns, relationships) in
Markdown format. These files feed into the DynamoDB data modeling workflow to inform
table design, GSI selection, and access pattern mapping.

Returns: Analysis summary with file locations and next steps.
Parameters|Type|Description
-|-|-
`output_dir`|`string`|Absolute path for output folder. Must exist and be writable. REQUIRED.
`source_db_type`|`string`|Database type: 'mysql', 'postgresql', 'sqlserver', or 'oracle'
`aws_cluster_arn`|`string` *optional*|[managed/RDS Data API-based] Aurora cluster ARN. Use this OR hostname, not both. Env: MYSQL_CLUSTER_ARN.
`aws_region`|`string` *optional*|[managed] AWS region. REQUIRED. Env: AWS_REGION.
`aws_secret_arn`|`string` *optional*|[managed] Secrets Manager ARN for DB credentials. REQUIRED. Env: MYSQL_SECRET_ARN.
`execution_mode`|`string` *optional*|'self_service': generates SQL for user to run, then parses results. 'managed' (MySQL only): RDS Data API-based access (aws_cluster_arn) or Connection-based access (hostname+port).
`hostname`|`string` *optional*|[managed/connection-based] MySQL hostname. Use this OR aws_cluster_arn, not both. Env: MYSQL_HOSTNAME.
`max_query_results`|`string` *optional*|Max rows per query. Default: 500. Env: MYSQL_MAX_QUERY_RESULTS.
`pattern_analysis_days`|`string` *optional*|Days of query logs to analyze. Default: 30.
`port`|`string` *optional*|[managed/connection-based] MySQL port. Default: 3306. Env: MYSQL_PORT.
`queries_file_path`|`string` *optional*|[self_service] Output path for generated SQL queries (Step 1).
`query_result_file_path`|`string` *optional*|[self_service] Path to query results file for parsing (Step 2).
`source_identifier`|`string` *optional*|Identifier for the source to analyze. Accepts a database name (MySQL, PostgreSQL, SQL Server) or a schema/owner name (Oracle, where objects are scoped by schema rather than database). REQUIRED for self_service mode.

---

## Screenshots

![Amazon DynamoDB screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-dynamodb-1.png)

![Amazon DynamoDB screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-dynamodb-2.png)

![Amazon DynamoDB screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-dynamodb-3.png)
