The SQLite MCP Server transforms SQLite into a powerful, AI-ready database engine. It combines standard relational operations with advanced analytics, text and vector search, geospatial capabilities, and intelligent workflow automation. By layering business intelligence tools, semantic resources, and guided prompts on top of SQLite, it enables both developers and AI assistants to interact with data more naturally and effectively.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/sqlite-mcp-server](https://hub.docker.com/repository/docker/mcp/sqlite-mcp-server)
**Author**|[neverinfamous](https://github.com/neverinfamous)
**Repository**|https://github.com/neverinfamous/sqlite-mcp-server

## Available Tools (25)
Tools provided by this Server|Short Description
-|-
`read_query`|Execute a SELECT query on the SQLite database|
`write_query`|Execute an INSERT, UPDATE, or DELETE query on the SQLite database|
`create_table`|Create a new table in the SQLite database|
`list_tables`|List all tables in the SQLite database|
`describe_table`|Get the schema information for a specific table|
`append_insight`|Add a business insight to the memo|
`create_fts_table`|Create a FTS5 virtual table for full-text search|
`fts_search`|Perform enhanced full-text search with ranking and snippets|
`create_embeddings_table`|Create a table optimized for storing embeddings with metadata|
`semantic_search`|Perform semantic similarity search using cosine similarity|
`hybrid_search`|Combine FTS5 keyword search with semantic similarity|
`descriptive_statistics`|Calculate comprehensive descriptive statistics for a numeric column|
`correlation_analysis`|Calculate correlation coefficient between two numeric columns|
`regression_analysis`|Perform linear regression analysis between two variables|
`outlier_detection`|Detect outliers using IQR method and Z-score analysis|
`create_csv_table`|Create a virtual table to access CSV files|
`create_json_collection_table`|Create virtual table for JSON file collections (JSONL, JSON arrays)|
`analyze_csv_schema`|Analyze CSV file and infer data types without creating table|
`fuzzy_match`|Find fuzzy matches using Levenshtein distance and sequence matching|
`text_similarity`|Calculate text similarity between columns or against reference text|
`backup_database`|Create a backup of the database to a file|
`restore_database`|Restore database from a backup file|
`vacuum_database`|Optimize database by reclaiming unused space and defragmenting|
`integrity_check`|Check database integrity and report any corruption|
`database_stats`|Get database performance and usage statistics|

---
## Tools Details

#### Tool: **`read_query`**
Execute a SELECT query on the SQLite database
Parameters|Type|Description
-|-|-
`query`|`string`|SELECT SQL query to execute

---
#### Tool: **`write_query`**
Execute an INSERT, UPDATE, or DELETE query on the SQLite database
Parameters|Type|Description
-|-|-
`query`|`string`|SQL query to execute

---
#### Tool: **`create_table`**
Create a new table in the SQLite database
Parameters|Type|Description
-|-|-
`query`|`string`|CREATE TABLE SQL statement

---
#### Tool: **`list_tables`**
List all tables in the SQLite database
#### Tool: **`describe_table`**
Get the schema information for a specific table
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name of the table to describe

---
#### Tool: **`append_insight`**
Add a business insight to the memo
Parameters|Type|Description
-|-|-
`insight`|`string`|Business insight discovered from data analysis

---
#### Tool: **`create_fts_table`**
Create a FTS5 virtual table for full-text search
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name for the FTS5 table
`columns`|`array`|List of columns to include in FTS5 index

---
#### Tool: **`fts_search`**
Perform enhanced full-text search with ranking and snippets
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name of the FTS5 table to search
`query`|`string`|FTS5 search query

---
#### Tool: **`create_embeddings_table`**
Create a table optimized for storing embeddings with metadata
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name for the embeddings table
`embedding_dim`|`number`|Dimension of the embedding vectors

---
#### Tool: **`semantic_search`**
Perform semantic similarity search using cosine similarity
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name of the embeddings table to search
`query_embedding`|`array`|Query embedding vector for similarity search

---
#### Tool: **`hybrid_search`**
Combine FTS5 keyword search with semantic similarity
Parameters|Type|Description
-|-|-
`embeddings_table`|`string`|Name of the embeddings table
`fts_table`|`string`|Name of the FTS5 table
`query_text`|`string`|Text query for FTS5 keyword search
`query_embedding`|`array`|Query embedding for semantic search

---
#### Tool: **`descriptive_statistics`**
Calculate comprehensive descriptive statistics for a numeric column
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name of the table
`column_name`|`string`|Name of the numeric column to analyze

---
#### Tool: **`correlation_analysis`**
Calculate correlation coefficient between two numeric columns
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name of the table
`column_x`|`string`|First numeric column
`column_y`|`string`|Second numeric column

---
#### Tool: **`regression_analysis`**
Perform linear regression analysis between two variables
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name of the table
`x_column`|`string`|Independent variable column
`y_column`|`string`|Dependent variable column

---
#### Tool: **`outlier_detection`**
Detect outliers using IQR method and Z-score analysis
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name of the table
`column_name`|`string`|Name of the numeric column to analyze

---
#### Tool: **`create_csv_table`**
Create a virtual table to access CSV files
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name for the CSV virtual table
`csv_file_path`|`string`|Path to the CSV file

---
#### Tool: **`create_json_collection_table`**
Create virtual table for JSON file collections (JSONL, JSON arrays)
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name for the JSON collection virtual table
`json_file_path`|`string`|Path to JSON file (JSONL or JSON array)

---
#### Tool: **`analyze_csv_schema`**
Analyze CSV file and infer data types without creating table
Parameters|Type|Description
-|-|-
`csv_file_path`|`string`|Path to the CSV file to analyze

---
#### Tool: **`fuzzy_match`**
Find fuzzy matches using Levenshtein distance and sequence matching
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name of the table
`column_name`|`string`|Name of the column to search
`search_term`|`string`|Term to find fuzzy matches for

---
#### Tool: **`text_similarity`**
Calculate text similarity between columns or against reference text
Parameters|Type|Description
-|-|-
`table_name`|`string`|Name of the table
`column_name`|`string`|Name of the column to analyze

---
#### Tool: **`backup_database`**
Create a backup of the database to a file
Parameters|Type|Description
-|-|-
`backup_path`|`string`|Path where backup file will be created

---
#### Tool: **`restore_database`**
Restore database from a backup file
Parameters|Type|Description
-|-|-
`backup_path`|`string`|Path to backup file to restore from
`confirm`|`boolean`|Confirmation flag (required to prevent accidental restores)

---
#### Tool: **`vacuum_database`**
Optimize database by reclaiming unused space and defragmenting
#### Tool: **`integrity_check`**
Check database integrity and report any corruption
#### Tool: **`database_stats`**
Get database performance and usage statistics
