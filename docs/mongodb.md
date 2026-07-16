A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/mongodb](https://hub.docker.com/repository/docker/mcp/mongodb)
**Author**|[mongodb-js](https://github.com/mongodb-js)
**Repository**|https://github.com/mongodb-js/mongodb-mcp-server

## Available Tools (25)
Tools provided by this Server|Short Description
-|-
`aggregate`|aggregate|
`aggregate-db`|aggregate-db|
`collection-indexes`|collection-indexes|
`collection-schema`|collection-schema|
`collection-storage-size`|collection-storage-size|
`connect`|connect|
`count`|count|
`create-collection`|create-collection|
`create-index`|create-index|
`db-stats`|db-stats|
`delete-many`|delete-many|
`drop-collection`|drop-collection|
`drop-database`|drop-database|
`drop-index`|drop-index|
`explain`|explain|
`export`|export|
`find`|find|
`insert-many`|insert-many|
`list-collections`|list-collections|
`list-databases`|list-databases|
`list-knowledge-sources`|list-knowledge-sources|
`mongodb-logs`|mongodb-logs|
`rename-collection`|rename-collection|
`search-knowledge`|search-knowledge|
`update-many`|update-many|

---
## Tools Details

#### Tool: **`aggregate`**
Run an aggregation against a MongoDB collection
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`pipeline`|`array`|An array of aggregation stages to execute.
If the user has asked for a vector search, `$vectorSearch` **MUST** be the first stage of the pipeline, or the first stage of a `$unionWith` subpipeline.
If the user has asked for lexical/Atlas search, use `$search` instead of `$text`.
### Usage Rules for `$vectorSearch`
- **Index Type Detection:**
  Use the collection-indexes tool to determine if the target field has a classic vector index (type: 'vector') or an auto-embed index (type: 'autoEmbed').
- **Classic Vector Search (type: 'vector'):**
  Use 'queryVector' with embeddings as an array of numbers.
- **Auto-Embed Vector Search (type: 'autoEmbed'):**
  Use 'query' - MongoDB automatically generates embeddings at query time. Do NOT use 'queryVector' or 'embeddingParameters' for auto-embed indexes.
- **Unset embeddings:**
  Unless the user explicitly requests the embeddings, add an `$unset` stage **at the end of the pipeline** to remove the embedding field and avoid context limits. **The $unset stage in this situation is mandatory**.
- **Pre-filtering:**
  If the user requests additional filtering, include filters in `$vectorSearch.filter` only for pre-filter fields in the vector index.
  NEVER include fields in $vectorSearch.filter that are not part of the vector index.
- **Post-filtering:**
  For all remaining filters, add a $match stage after $vectorSearch.
- If unsure which fields are filterable, use the collection-indexes tool to determine valid prefilter fields.
- If no requested filters are valid prefilters, omit the filter key from $vectorSearch.

### Usage Rules for `$search`
- Include the index name, unless you know for a fact there's a default index. If unsure, use the collection-indexes tool to determine the index name.
- The `$search` stage supports multiple operators, such as 'autocomplete', 'text', 'geoWithin', and others. Choose the approprate operator based on the user's query. If unsure of the exact syntax, consult the MongoDB Atlas Search documentation, which can be found here: https://www.mongodb.com/docs/atlas/atlas-search/operators-and-collectors/

`responseBytesLimit`|`number` *optional*|The maximum number of bytes to return in the response. This value is capped by the server's configured maxBytesPerQuery and cannot be exceeded. Note to LLM: If the entire aggregation result is required, use the "export" tool instead of increasing this limit.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`aggregate-db`**
Run an aggregation against a MongoDB database
Parameters|Type|Description
-|-|-
`database`|`string`|Database name
`pipeline`|`array`|An array of aggregation stages to execute. The first stage must be a database-level aggregation stage (one of `$changeStream`, `$currentOp`, `$documents`, `$listLocalSessions`, `$queryStats`). https://www.mongodb.com/docs/manual/reference/mql/aggregation-stages/#db.aggregate---stages
`responseBytesLimit`|`number` *optional*|The maximum number of bytes to return in the response. This value is capped by the server's configured maxBytesPerQuery and cannot be exceeded.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`collection-indexes`**
Describe the indexes for a collection
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`collection-schema`**
Describe the schema for a collection
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`responseBytesLimit`|`number` *optional*|The maximum number of bytes to return in the response. This value is capped by the server's configured maxBytesPerQuery and cannot be exceeded.
`sampleSize`|`number` *optional*|Number of documents to sample for schema inference

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`collection-storage-size`**
Gets the size of the collection
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`connect`**
Connect to a MongoDB instance. The config resource captures if the server is already connected to a MongoDB cluster. If the user has configured a connection string or has previously called the connect tool, a connection is already established and there's no need to call this tool unless the user has explicitly requested to switch to a new MongoDB cluster.
Parameters|Type|Description
-|-|-
`connectionString`|`string`|MongoDB connection string (in the mongodb:// or mongodb+srv:// format)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`count`**
Gets the number of documents in a MongoDB collection using db.collection.count() and query as an optional filter parameter
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`query`|`object` *optional*|A filter/query parameter. Allows users to filter the documents to count. Matches the syntax of the filter argument of db.collection.count().

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`create-collection`**
Creates a new collection in a database. If the database doesn't exist, it will be created automatically.
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name

---
#### Tool: **`create-index`**
Create an index for a collection
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`definition`|`array`|The index definition. Use 'classic' for standard indexes, 'vectorSearch' for vector search indexes, and 'search' for Atlas Search (lexical) indexes.
`name`|`string` *optional*|The name of the index

---
#### Tool: **`db-stats`**
Returns statistics that reflect the use state of a single database
Parameters|Type|Description
-|-|-
`database`|`string`|Database name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`delete-many`**
Removes all documents that match the filter from a MongoDB collection
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`filter`|`object` *optional*|The query filter, specifying the deletion criteria. Matches the syntax of the filter argument of db.collection.deleteMany()

*This tool may perform destructive updates.*

---
#### Tool: **`drop-collection`**
Removes a collection or view from the database. The method also removes any indexes associated with the dropped collection.
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name

*This tool may perform destructive updates.*

---
#### Tool: **`drop-database`**
Removes the specified database, deleting the associated data files
Parameters|Type|Description
-|-|-
`database`|`string`|Database name

*This tool may perform destructive updates.*

---
#### Tool: **`drop-index`**
Drop an index for the provided database and collection.
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`indexName`|`string`|The name of the index to be dropped.
`type`|`string`|The type of index to be deleted. Use 'classic' for standard indexes and 'search' for atlas search and vector search indexes.

*This tool may perform destructive updates.*

---
#### Tool: **`explain`**
Returns statistics describing the execution of the winning plan chosen by the query optimizer for the evaluated method
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`method`|`array`|The method and its arguments to run
`verbosity`|`string` *optional*|The verbosity of the explain plan, defaults to queryPlanner. If the user wants to know how fast is a query in execution time, use executionStats. It supports all verbosities as defined in the MongoDB Driver.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`export`**
Export a query or aggregation results in the specified EJSON format.
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`exportTarget`|`array`|The export target along with its arguments.
`exportTitle`|`string`|A short description to uniquely identify the export.
`jsonExportFormat`|`string` *optional*|The format to be used when exporting collection data as EJSON with default being relaxed.
relaxed: A string format that emphasizes readability and interoperability at the expense of type preservation. That is, conversion from relaxed format to BSON can lose type information.
canonical: A string format that emphasizes type preservation at the expense of readability and interoperability. That is, conversion from canonical to BSON will generally preserve type information except in certain specific cases.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`find`**
Run a find query against a MongoDB collection
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`filter`|`object` *optional*|The query filter, matching the syntax of the query argument of db.collection.find()
`limit`|`number` *optional*|The maximum number of documents to return
`projection`|`object` *optional*|The projection, matching the syntax of the projection argument of db.collection.find()
`responseBytesLimit`|`number` *optional*|The maximum number of bytes to return in the response. This value is capped by the server's configured maxBytesPerQuery and cannot be exceeded. Note to LLM: If the entire query result is required, use the "export" tool instead of increasing this limit.
`sort`|`object` *optional*|A document, describing the sort order, matching the syntax of the sort argument of cursor.sort(). The keys of the object are the fields to sort on, while the values are the sort directions (1 for ascending, -1 for descending).

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`insert-many`**
Insert an array of documents into a MongoDB collection. If the list of documents is above com.mongodb/maxRequestPayloadBytes, consider inserting them in batches.
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`documents`|`array`|The array of documents to insert, matching the syntax of the document argument of db.collection.insertMany().

---
#### Tool: **`list-collections`**
List all collections for a given database
Parameters|Type|Description
-|-|-
`database`|`string`|Database name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list-databases`**
List all databases for a MongoDB connection
#### Tool: **`list-knowledge-sources`**
List available data sources in the MongoDB Assistant knowledge base. Use this to explore available data sources or to find search filter parameters to use in search-knowledge.
#### Tool: **`mongodb-logs`**
Returns the most recent logged mongod events
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|The maximum number of log entries to return.
`type`|`string` *optional*|The type of logs to return. Global returns all recent log entries, while startupWarnings returns only warnings and errors from when the process started.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`rename-collection`**
Renames a collection in a MongoDB database
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`newName`|`string`|The new name for the collection
`dropTarget`|`boolean` *optional*|If true, drops the target collection if it exists

---
#### Tool: **`search-knowledge`**
Search for information in the MongoDB Assistant knowledge base. This includes official documentation, curated expert guidance, and other resources provided by MongoDB. Supports filtering by data source and version.
Parameters|Type|Description
-|-|-
`query`|`string`|A natural language query to search for in the MongoDB Assistant knowledge base. This should be a single question or a topic that is relevant to the user's MongoDB use case.
`dataSources`|`array` *optional*|A list of one or more data sources to limit the search to. You can specify a specific version of a data source by providing the version label. If not provided, the latest version of all data sources will be searched. Available data sources and their versions can be listed by calling the list-knowledge-sources tool.
`limit`|`number` *optional*|The maximum number of results to return

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`update-many`**
Updates all documents that match the specified filter for a collection. If the list of documents is above com.mongodb/maxRequestPayloadBytes, consider updating them in batches.
Parameters|Type|Description
-|-|-
`collection`|`string`|Collection name
`database`|`string`|Database name
`update`|`object`|An update document describing the modifications to apply using update operator expressions
`filter`|`object` *optional*|The selection criteria for the update, matching the syntax of the filter argument of db.collection.updateOne()
`upsert`|`boolean` *optional*|Controls whether to insert a new document if no documents match the filter

---
