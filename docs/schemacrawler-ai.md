The SchemaCrawler AI MCP Server enables natural language interaction with your database schema using an MCP client in "Agent" mode. It allows users to explore tables, columns, foreign keys, triggers, stored procedures and more simply by asking questions like "Explain the code for the interest calculation stored procedure". You can also ask it to help with SQL, since it knows your schema. This is ideal for developers, DBAs, and data analysts who want to streamline schema comprehension and query development without diving into dense documentation.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/schemacrawler-ai](https://hub.docker.com/repository/docker/mcp/schemacrawler-ai)
**Author**|[schemacrawler](https://github.com/schemacrawler)
**Repository**|https://github.com/schemacrawler/SchemaCrawler-AI

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`database_server_information`|Show database server information|
`describe_entities`|Describe entities in the ER model|
`describe_relationships`|Describe relationships in the ER model|
`describe_routines`|Describe stored procedures and functions|
`describe_tables`|Describe tables and views|
`list`|List database objects|
`list_across_tables`|List dependent database objects across tables|
`mcp-server-health`|SchemaCrawler AI MCP Server Health|

---
## Tools Details

#### Tool: **`database_server_information`**
Provides database environment and server configuration metadata, including engine type and version, collation, encoding, parameters, capabilities, and platform details. Adapts output to the specific database (such as Oracle, SQL Server, PostgreSQL and so on) to support platform-aware SQL generation and schema analysis.
#### Tool: **`describe_entities`**
Generates detailed documentation for entities in the ER model, including entity type such as strong, weak and subtype entities, and attributes. Supports regex-based entity name filtering to optimize tool performance. Returns data as a JSON object.
Parameters|Type|Description
-|-|-
`entity_kind`|`string` *optional*|Indicates the types of entities to return - for example, strong, weak
or subtype entities. It can also return associations (or bridge or join tables).

`entity_name`|`string` *optional*|Name of entity to describe, from the ER model.
May be specified as a regular expression, matching the fully qualified
entity name (including the schema).
Try not to match all entities, but instead use a regular expression
to match a subset or match a single entity, since otherwise results may
be large.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`describe_relationships`**
Generates detailed documentation for relationships in the ER model, including 1..1, 1..M, M..N and optional relationships. Supports regex-based relationship name filtering  to optimize tool performance. Returns data as a JSON object.
Parameters|Type|Description
-|-|-
`cardinality`|`string` *optional*|Indicates the types of relationships to return - for example, 1..1, 1..M, M..N
and optional relationships.

`relationship_name`|`string` *optional*|Name of relationships to describe, from the ER model.
May be specified as a regular expression, matching the fully qualified
relationship name (including the schema).
Try not to match all relationships, but instead use a regular expression
to match a subset or match a single relationships, since otherwise results may
be large.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`describe_routines`**
Generates detailed documentation for database routines (stored procedures and functions), including parameter metadata (input/ output parameters, data types, default values), return types, dependencies (on tables, views, or other routines), and full DDL definitions. Supports regex-based routine name filtering and configurable detail levels to optimize tool performance. Returns data as a JSON object.
Parameters|Type|Description
-|-|-
`description_scope`|`array` *optional*|Indicates what details of the database stored procedure or function
to return - parameters (including return types), attributes,
and routine definition.
Parameters, return types, and remarks or comments are always returned.

`routine_name`|`string` *optional*|Name of database routine (stored procedure or function) to describe.
May be specified as a regular expression matching the fully qualified
stored procedure or function names (including the schema).
Try not to match all routines, but instead use a regular expression
to match a subset, since otherwise results may be large.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`describe_tables`**
Generates detailed documentation for database tables and views, including column definitions (names, data types, constraints, nullability), primary and foreign key relationships, index and trigger information, table attributes, and complete DDL definitions. Supports regex-based table name filtering and configurable detail levels to optimize tool performance. Returns data as a JSON object.
Parameters|Type|Description
-|-|-
`description_scope`|`array` *optional*|Indicates what details of the database table or view to return -
columns, primary key, foreign keys, indexes, triggers, attributes,
and table definition. Also returns which objects reference a given table
as "used by objects".
Columns, primary keys, foreign key references to other tables,
and remarks or comments are always returned by default.
The other details can be requested.
The results could be large.

`table_name`|`string` *optional*|Name of database table or view to describe.
May be specified as a regular expression, matching the fully qualified
table name (including the schema).
Try not to match all tables, but instead use a regular expression
to match a subset or match a single table, since otherwise results may
be large.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list`**
Makes an inventory of database schema objects such as tables, views, stored procedures, functions, sequences, synonyms, and more. This is an essential starting point for database exploration, database asset management, and schema analysis. The tool supports object type filtering and pattern-based searching. Returns JSON data.
Parameters|Type|Description
-|-|-
`database_object_name`|`string` *optional*|Name of database object to list.
Is a regular expression, matching the fully qualified
database object name (including the schema). May match
more than one database object.
Use an empty string if all database objects are requested.

`database_object_type`|`string` *optional*|Type of database object to list, like tables (including views),
routines (that is, stored procedures and functions),
schemas (that is, databases or catalogs), sequences, or synonyms.
If the parameter is not provided, all database objects are listed.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_across_tables`**
Makes an inventory of table-dependent objects across the database schema, including columns, indexes, foreign keys, triggers, and constraints. Enables impact analysis, dependency tracking, performance tuning, and refactoring without inspecting individual tables. The corresponding tables are identified, and their details can be obtained later by describing those tables. Supports regex-based table name filtering and configurable detail levels to optimize tool performance. Returns JSON data.
Parameters|Type|Description
-|-|-
`dependant_object_type`|`string`|Type of database table dependant objects, like columns, indexes,
foreign keys or triggers.

`dependant_object_name`|`string` *optional*|Name of table dependant object.
May be a regular expression, matching the fully qualified
dependant object name (including the schema and table). May match
more than one dependant object.
Use an empty string if all dependant objects are requested.
If not specified, all table dependant objects will be returned,
but the results could be large.

`table_name`|`string` *optional*|Name of database table for which dependant objects are described.
May be a regular expression, matching the fully qualified
table name (including the schema), in which case, multiple tables
may be returned.
Use an empty string if all tables are requested.
If not specified, all tables will be returned, but the results
could be large.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`mcp-server-health`**
Gets the SchemaCrawler AI MCP Server version and uptime status.
Parameters|Type|Description
-|-|-
`clientId`|`string`|
`eventId`|`string`|

*This tool is read-only. It does not modify its environment.*

---
