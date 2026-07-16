Enable AI agents to manage, monitor, and query CockroachDB using natural language. Perform complex database operations, cluster management, and query execution seamlessly through AI-driven workflows. Integrate effortlessly with MCP clients for scalable and high-performance data operations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/cockroachdb](https://hub.docker.com/repository/docker/mcp/cockroachdb)
**Author**|[amineelkouhen](https://github.com/amineelkouhen)
**Repository**|https://github.com/amineelkouhen/mcp-cockroachdb

## Available Tools (29)
Tools provided by this Server|Short Description
-|-
`analyze_performance`|Analyze query performance statistics for a given query or time range.|
`analyze_schema`|Analyze the schema and provide a summary of tables, views, and relationships.|
`bulk_import`|Bulk import data into a table from a file (CSV or Avro) stored in cloud or web storage.|
`connect`|Connect to the default CockroachDB database and create a connection pool.|
`connect_database`|Connect to a CockroachDB database and create a connection pool.|
`create_database`|Enable the creation of new databases.|
`create_index`|Create a new index on a specified table to improve query performance.|
`create_table`|Enable the creation of new tables in the current database.|
`create_view`|Create a view from a specific query.|
`describe_table`|Provide detailed schema information, column definitions, data types, and other metadata for a specified table.|
`drop_database`|Drop an existing database.|
`drop_index`|Drop an existing index.|
`drop_table`|Facilitate the deletion of existing tables from the database.|
`drop_view`|Drop an existing view.|
`execute_query`|Execute a SQL query with optional parameters and formatting.|
`execute_transaction`|Execute a list of SQL queries as a single transaction.|
`explain_query`|Return CockroachDB's statement plan for a preparable statement.|
`get_active_connections`|List active connections/sessions to the current database.|
`get_cluster_status`|Get cluster health and node distribution.|
`get_connection_status`|Get the current connection status and details.|
`get_database_settings`|Retrieve current database or cluster settings.|
`get_query_history`|Get the history of executed queries.|
`get_replication_status`|Get replication and distribution status for a table or the whole database.|
`get_table_relationships`|Get foreign key relationships for a table or all tables.|
`list_databases`|List all databases in the CockroachDB cluster.|
`list_tables`|List all tables present in the connected Cockroach database instance.|
`list_views`|List all views in a schema.|
`show_running_queries`|Show currently running queries on the cluster.|
`switch_database`|Switch the connection to a different database.|

---
## Tools Details

#### Tool: **`analyze_performance`**
Analyze query performance statistics for a given query or time range.
Parameters|Type|Description
-|-|-
`query`|`string`|
`time_range`|`string` *optional*|

---
#### Tool: **`analyze_schema`**
Analyze the schema and provide a summary of tables, views, and relationships.
Parameters|Type|Description
-|-|-
`db_schema`|`string` *optional*|

---
#### Tool: **`bulk_import`**
Bulk import data into a table from a file (CSV or Avro) stored in cloud or web storage. Supports S3, Azure Blob, Google Storage, HTTP/HTTPS URLs.
Parameters|Type|Description
-|-|-
`file_url`|`string`|
`format`|`string`|
`table_name`|`string`|
`delimiter`|`string` *optional*|
`skip_header`|`boolean` *optional*|

---
#### Tool: **`connect`**
Connect to the default CockroachDB database and create a connection pool.

Returns:
    A success message or an error message.
#### Tool: **`connect_database`**
Connect to a CockroachDB database and create a connection pool.
Parameters|Type|Description
-|-|-
`database`|`string`|
`host`|`string`|
`password`|`string`|
`port`|`integer`|
`sslcert`|`string`|
`sslkey`|`string`|
`sslmode`|`string`|
`sslrootcert`|`string`|
`username`|`string`|

---
#### Tool: **`create_database`**
Enable the creation of new databases.
Parameters|Type|Description
-|-|-
`database_name`|`string`|

---
#### Tool: **`create_index`**
Create a new index on a specified table to improve query performance. This tool allows users to define indexes on one or more columns, enabling faster data retrieval and optimized execution plans for read-heavy workloads.
Parameters|Type|Description
-|-|-
`columns`|`array`|
`index_name`|`string`|
`table_name`|`string`|

---
#### Tool: **`create_table`**
Enable the creation of new tables in the current database. You can instruct the AI to define table names, columns, and their types, streamlining database setup and schema evolution directly through natural language.
Parameters|Type|Description
-|-|-
`columns`|`array`|
`table_name`|`string`|

---
#### Tool: **`create_view`**
Create a view from a specific query.
Parameters|Type|Description
-|-|-
`query`|`string`|
`view_name`|`string`|

---
#### Tool: **`describe_table`**
Provide detailed schema information, column definitions, data types, and other metadata for a specified table. This allows the AI to accurately interpret table structures and formulate precise queries or data manipulation commands.
Parameters|Type|Description
-|-|-
`table_name`|`string`|
`db_schema`|`string` *optional*|

---
#### Tool: **`drop_database`**
Drop an existing database.
Parameters|Type|Description
-|-|-
`database_name`|`string`|

---
#### Tool: **`drop_index`**
Drop an existing index.
Parameters|Type|Description
-|-|-
`index_name`|`string`|

---
#### Tool: **`drop_table`**
Facilitate the deletion of existing tables from the database. This tool is useful for cleaning up test environments or managing schema changes, always with the necessary confirmations for security.
Parameters|Type|Description
-|-|-
`table_name`|`string`|

---
#### Tool: **`drop_view`**
Drop an existing view.
Parameters|Type|Description
-|-|-
`view_name`|`string`|

---
#### Tool: **`execute_query`**
Execute a SQL query with optional parameters and formatting.
Parameters|Type|Description
-|-|-
`query`|`string`|
`format`|`string` *optional*|
`limit`|`string` *optional*|
`params`|`string` *optional*|

---
#### Tool: **`execute_transaction`**
Execute a list of SQL queries as a single transaction.
Parameters|Type|Description
-|-|-
`queries`|`array`|

---
#### Tool: **`explain_query`**
Return CockroachDB's statement plan for a preparable statement. You can use this information to optimize the query. If you run it with Analyze, it executes the SQL query and generates a statement plan with execution statistics.
Parameters|Type|Description
-|-|-
`query`|`string`|
`analyze`|`boolean` *optional*|

---
#### Tool: **`get_active_connections`**
List active connections/sessions to the current database.

Returns:
    Active sessions on the cluster.
#### Tool: **`get_cluster_status`**
Get cluster health and node distribution.
Parameters|Type|Description
-|-|-
`detailed`|`boolean` *optional*|

---
#### Tool: **`get_connection_status`**
Get the current connection status and details.

Returns:
    The connection status or an error message.
#### Tool: **`get_database_settings`**
Retrieve current database or cluster settings.

Returns:
    All cluster settings.
#### Tool: **`get_query_history`**
Get the history of executed queries.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|

---
#### Tool: **`get_replication_status`**
Get replication and distribution status for a table or the whole database.
Parameters|Type|Description
-|-|-
`table_name`|`string`|

---
#### Tool: **`get_table_relationships`**
Get foreign key relationships for a table or all tables.
Parameters|Type|Description
-|-|-
`table_name`|`string` *optional*|

---
#### Tool: **`list_databases`**
List all databases in the CockroachDB cluster.

Returns:
    A list of databases with row count or an error message.
#### Tool: **`list_tables`**
List all tables present in the connected Cockroach database instance. This is invaluable for AI to understand the database’s landscape and identify relevant data sources for a given query.
Parameters|Type|Description
-|-|-
`db_schema`|`string` *optional*|

---
#### Tool: **`list_views`**
List all views in a schema.
Parameters|Type|Description
-|-|-
`db_schema`|`string` *optional*|

---
#### Tool: **`show_running_queries`**
Show currently running queries on the cluster.
Parameters|Type|Description
-|-|-
`min_duration`|`string` *optional*|
`node_id`|`integer` *optional*|
`user`|`string` *optional*|

---
#### Tool: **`switch_database`**
Switch the connection to a different database.
Parameters|Type|Description
-|-|-
`database`|`string`|

---
