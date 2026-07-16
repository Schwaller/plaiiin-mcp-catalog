Data warehouse operations and queries.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/redshift-mcp-server](https://hub.docker.com/repository/docker/mcp/redshift-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (6)
Tools provided by this Server|Short Description
-|-
`execute_query`|Execute a SQL query against a Redshift cluster or serverless workgroup.|
`list_clusters`|List all available Amazon Redshift clusters and serverless workgroups.|
`list_columns`|List all columns in a specified table within a Redshift schema.|
`list_databases`|List all databases in a specified Amazon Redshift cluster.|
`list_schemas`|List all schemas in a specified database within a Redshift cluster.|
`list_tables`|List all tables in a specified schema within a Redshift database.|

---
## Tools Details

#### Tool: **`execute_query`**
Execute a SQL query against a Redshift cluster or serverless workgroup.

This tool uses the Redshift Data API to execute SQL queries and return results.
It supports both provisioned clusters and serverless workgroups, and handles
various data types in the result set.

## Usage Requirements

- Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
- The cluster must be available and accessible.
- Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
- The user must have appropriate permissions to execute queries in the specified database.

## Parameters

- cluster_identifier: The unique identifier of the Redshift cluster to query.
                     IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
- database_name: The database name to execute the query against.
                IMPORTANT: Use a valid database name from the list_databases tool.
- sql: The SQL statement to execute. Should be a single SQL statement.

## Response Structure

Returns a QueryResult object with the following structure:

- columns: List of column names in the result set.
- rows: List of rows, where each row is a list of values.
- row_count: Number of rows returned.
- execution_time_ms: Query execution time in milliseconds.
- query_id: Unique identifier for the query execution.

## Usage Tips

1. First use list_clusters to get valid cluster identifiers.
2. Then use list_databases to get valid database names for the cluster.
3. Ensure the cluster status is 'available' before executing queries.
4. Use LIMIT clauses for exploratory queries to avoid large result sets.
5. Consider using the metadata discovery tools to understand table structures before querying.

## Data Type Handling

The tool automatically handles various Redshift data types:
- String values (VARCHAR, CHAR, TEXT).
- Numeric values (INTEGER, BIGINT, DECIMAL, FLOAT).
- Boolean values.
- NULL values.
- Date and timestamp values (returned as strings).

## Security Considerations

- Avoid dynamic SQL construction with user input.
- Consider database object permissions.
- Queries run in read-only mode and must be a single statement; writes and
  multi-statement submissions are rejected.
Parameters|Type|Description
-|-|-
`cluster_identifier`|`string`|The cluster identifier to execute the query on. Must be a valid cluster identifier from the list_clusters tool.
`database_name`|`string`|The database name to execute the query against. Must be a valid database name from the list_databases tool.
`sql`|`string`|The SQL statement to execute. Should be a single SQL statement.

---
#### Tool: **`list_clusters`**
List all available Amazon Redshift clusters and serverless workgroups.

This tool discovers and returns information about all Redshift clusters and serverless workgroups
in your AWS account, including their current status, connection details, and configuration.

## Usage Requirements

- Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
- Required IAM permissions: redshift:DescribeClusters, redshift-serverless:ListWorkgroups, redshift-serverless:GetWorkgroup.

## Response Structure

Returns a list of RedshiftCluster objects with the following structure:

- identifier: Unique identifier for the cluster/workgroup.
- type: Type of cluster (provisioned or serverless).
- status: Current status of the cluster.
- database_name: Default database name.
- endpoint: Connection endpoint information.
- port: Connection port.
- vpc_id: VPC ID where the cluster resides.
- node_type: Node type (for provisioned clusters).
- number_of_nodes: Number of nodes (for provisioned clusters).
- creation_time: When the cluster was created.
- master_username: Master username for the cluster.
- publicly_accessible: Whether the cluster is publicly accessible.
- encrypted: Whether the cluster is encrypted.
- tags: Tags associated with the cluster.

## Usage Tips

1. Use this tool to discover available Redshift instances before attempting connections.
2. Note the cluster identifiers for use with other database tools.
3. Check the status field to ensure clusters are 'available' before querying.
4. Use the endpoint and port information for direct database connections if needed.
5. Consider the cluster type (provisioned vs serverless) when planning your queries.

## Interpretation Best Practices

1. Filter results by status to find only available clusters.
2. Use cluster identifiers as input for other Redshift tools.
3. Consider cluster configuration (node type, encryption) for performance planning.
4. Check tags for environment or team information to select appropriate clusters.
#### Tool: **`list_columns`**
List all columns in a specified table within a Redshift schema.

This tool queries the SVV_ALL_COLUMNS system view to discover all columns
that the user has access to in the specified table, including detailed information
about data types, constraints, and column properties.

## Usage Requirements

- Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
- The cluster must be available and accessible.
- Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
- The user must have access to the database to query system views.

## Parameters

- cluster_identifier: The unique identifier of the Redshift cluster to query.
                     IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
- column_database_name: The database name to list columns for.
                       IMPORTANT: Use a valid database name from the list_databases tool.
- column_schema_name: The schema name to list columns for.
                     IMPORTANT: Use a valid schema name from the list_schemas tool.
- column_table_name: The table name to list columns for.
                    IMPORTANT: Use a valid table name from the list_tables tool.

## Response Structure

Returns a list of RedshiftColumn objects with the following structure:

- database_name: The name of the database.
- schema_name: The name of the schema.
- table_name: The name of the table.
- column_name: The name of the column.
- ordinal_position: The position of the column in the table.
- column_default: The default value of the column.
- is_nullable: Whether the column is nullable (yes or no).
- data_type: The data type of the column.
- character_maximum_length: The maximum number of characters in the column.
- numeric_precision: The numeric precision.
- numeric_scale: The numeric scale.
- remarks: Remarks about the column.

## Usage Tips

1. First use list_clusters to get valid cluster identifiers.
2. Then use list_databases to get valid database names for the cluster.
3. Then use list_schemas to get valid schema names for the database.
4. Then use list_tables to get valid table names for the schema.
5. Ensure the cluster status is 'available' before querying columns.
6. Note data types and constraints for query planning and data validation.

## Interpretation Best Practices

1. Use ordinal_position to understand column order in the table.
2. Check is_nullable for required vs optional fields.
3. Use data_type information for proper data handling in queries.
4. Consider character_maximum_length for string field validation.
5. Use numeric_precision and numeric_scale for numeric field handling.
6. Use column names for SELECT statements and query construction.
Parameters|Type|Description
-|-|-
`cluster_identifier`|`string`|The cluster identifier to query for columns. Must be a valid cluster identifier from the list_clusters tool.
`column_database_name`|`string`|The database name to list columns for. Must be a valid database name from the list_databases tool.
`column_schema_name`|`string`|The schema name to list columns for. Must be a valid schema name from the list_schemas tool.
`column_table_name`|`string`|The table name to list columns for. Must be a valid table name from the list_tables tool.

---
#### Tool: **`list_databases`**
List all databases in a specified Amazon Redshift cluster.

This tool queries the SVV_REDSHIFT_DATABASES system view to discover all databases
that the user has access to in the specified cluster, including local databases
and databases created from datashares.

## Usage Requirements

- Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
- The cluster must be available and accessible.
- Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
- The user must have access to the specified database to query system views.

## Parameters

- cluster_identifier: The unique identifier of the Redshift cluster to query.
                     IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
- database_name: The database to connect to for querying system views (defaults to 'dev').

## Response Structure

Returns a list of RedshiftDatabase objects with the following structure:

- database_name: The name of the database.
- database_owner: The database owner user ID.
- database_type: The type of database (local or shared).
- database_acl: Access control information (for internal use).
- database_options: The properties of the database.
- database_isolation_level: The isolation level (Snapshot Isolation or Serializable).

## Usage Tips

1. First use list_clusters to get valid cluster identifiers.
2. Ensure the cluster status is 'available' before querying databases.
3. Use the default database name unless you know a specific database exists.
4. Note database types to understand if they are local or shared from datashares.

## Interpretation Best Practices

1. Focus on 'local' database types for cluster-native databases.
2. 'shared' database types indicate databases from datashares.
3. Use database names for subsequent schema and table discovery.
4. Consider database isolation levels for transaction planning.
Parameters|Type|Description
-|-|-
`cluster_identifier`|`string`|The cluster identifier to query for databases. Must be a valid cluster identifier from the list_clusters tool.
`database_name`|`string` *optional*|The database to connect to for querying system views. Defaults to "dev".

---
#### Tool: **`list_schemas`**
List all schemas in a specified database within a Redshift cluster.

This tool queries the SVV_ALL_SCHEMAS system view to discover all schemas
that the user has access to in the specified database, including local schemas,
external schemas, and shared schemas from datashares.

## Usage Requirements

- Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
- The cluster must be available and accessible.
- Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
- The user must have access to the database to query system views.

## Parameters

- cluster_identifier: The unique identifier of the Redshift cluster to query.
                     IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
- schema_database_name: The database name to list schemas for. Also used to connect to.
                       IMPORTANT: Use a valid database name from the list_databases tool.

## Response Structure

Returns a list of RedshiftSchema objects with the following structure:

- database_name: The name of the database where the schema exists.
- schema_name: The name of the schema.
- schema_owner: The user ID of the schema owner.
- schema_type: The type of the schema (external, local, or shared).
- schema_acl: The permissions for the specified user or user group for the schema.
- source_database: The name of the source database for external schema.
- schema_option: The options of the schema (external schema attribute).

## Usage Tips

1. First use list_clusters to get valid cluster identifiers.
2. Then use list_databases to get valid database names for the cluster.
3. Ensure the cluster status is 'available' before querying schemas.
4. Note schema types to understand if they are local, external, or shared.
5. External schemas connect to external data sources like S3 or other databases.

## Interpretation Best Practices

1. Focus on 'local' schema types for cluster-native schemas.
2. 'external' schema types indicate connections to external data sources.
3. 'shared' schema types indicate schemas from datashares.
4. Use schema names for subsequent table and column discovery.
5. Consider schema permissions (schema_acl) for access planning.
Parameters|Type|Description
-|-|-
`cluster_identifier`|`string`|The cluster identifier to query for schemas. Must be a valid cluster identifier from the list_clusters tool.
`schema_database_name`|`string`|The database name to list schemas for. Also used to connect to. Must be a valid database name from the list_databases tool.

---
#### Tool: **`list_tables`**
List all tables in a specified schema within a Redshift database.

This tool queries the SVV_ALL_TABLES system view to discover all tables
that the user has access to in the specified schema, including base tables,
views, external tables, and shared tables.

## Usage Requirements

- Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
- The cluster must be available and accessible.
- Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
- The user must have access to the database to query system views.

## Parameters

- cluster_identifier: The unique identifier of the Redshift cluster to query.
                     IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
- table_database_name: The database name to list tables for.
                      IMPORTANT: Use a valid database name from the list_databases tool.
- table_schema_name: The schema name to list tables for.
                    IMPORTANT: Use a valid schema name from the list_schemas tool.

## Response Structure

Returns a list of RedshiftTable objects with the following structure:

- database_name: The name of the database where the table exists.
- schema_name: The schema name for the table.
- table_name: The name of the table.
- table_acl: The permissions for the specified user or user group for the table.
- table_type: The type of the table (views, base tables, external tables, shared tables).
- remarks: Remarks about the table.

## Usage Tips

1. First use list_clusters to get valid cluster identifiers.
2. Then use list_databases to get valid database names for the cluster.
3. Then use list_schemas to get valid schema names for the database.
4. Ensure the cluster status is 'available' before querying tables.
5. Note table types to understand if they are base tables, views, external tables, or shared tables.

## Interpretation Best Practices

1. Focus on 'TABLE' table types for regular database tables.
2. 'VIEW' table types indicate database views.
3. 'EXTERNAL TABLE' types indicate connections to external data sources.
4. 'SHARED TABLE' types indicate tables from datashares.
5. Use table names for subsequent column discovery and query operations.
6. Consider table permissions (table_acl) for access planning.
Parameters|Type|Description
-|-|-
`cluster_identifier`|`string`|The cluster identifier to query for tables. Must be a valid cluster identifier from the list_clusters tool.
`table_database_name`|`string`|The database name to list tables for. Must be a valid database name from the list_databases tool.
`table_schema_name`|`string`|The schema name to list tables for. Also used to connect to. Must be a valid schema name from the list_schemas tool.

---

## Screenshots

![Amazon Redshift screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-redshift-1.png)

![Amazon Redshift screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-redshift-2.png)

![Amazon Redshift screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-redshift-3.png)
