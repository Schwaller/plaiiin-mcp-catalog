An MCP server for Astra DB workloads.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/astra-db](https://hub.docker.com/repository/docker/mcp/astra-db)
**Author**|[datastax](https://github.com/datastax)
**Repository**|https://github.com/datastax/astra-db-mcp

## Available Tools (19)
Tools provided by this Server|Short Description
-|-
`BulkCreateRecords`|Create multiple records in a collection at once|
`BulkDeleteRecords`|Delete multiple records from a collection at once|
`BulkUpdateRecords`|Update multiple records in a collection at once|
`CreateCollection`|Create a new collection in the database|
`CreateRecord`|Create a new record in a collection|
`DeleteCollection`|Delete a collection from the database|
`DeleteRecord`|Delete a record from a collection|
`EstimateDocumentCount`|Estimate the number of documents in a collection using a fast, approximate count method|
`FindDistinctValues`|Find distinct values for a field in a collection|
`FindRecord`|Find records in a collection by field value|
`GetCollections`|Get all collections in the Astra DB database|
`GetRecord`|Get a specific record from a collection by ID|
`HelpAddToClient`|Help the user add the Astra DB client to their MCP client|
`HybridSearch`|Search for records using both vector similarity and text matching|
`ListRecords`|List records from a collection in the database|
`OpenBrowser`|Open a web browser to a specific URL|
`UpdateCollection`|Update an existing collection in the database|
`UpdateRecord`|Update an existing record in a collection|
`VectorSearch`|Search for records in a collection using vector similarity|

---
## Tools Details

#### Tool: **`BulkCreateRecords`**
Create multiple records in a collection at once
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to create the records in
`records`|`array`|Array of records to insert

---
#### Tool: **`BulkDeleteRecords`**
Delete multiple records from a collection at once
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection containing the records
`recordIds`|`array`|Array of record IDs to delete

---
#### Tool: **`BulkUpdateRecords`**
Update multiple records in a collection at once
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection containing the records
`records`|`array`|Array of records to update with their IDs

---
#### Tool: **`CreateCollection`**
Create a new collection in the database
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to create
`dimension`|`number` *optional*|The dimensions of the vector collection, if vector is true
`metric`|`string` *optional*|The similarity metric to use for vector search (cosine, euclidean, or dot_product)
`vector`|`boolean` *optional*|Whether to create a vector collection

---
#### Tool: **`CreateRecord`**
Create a new record in a collection
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to create the record in
`record`|`object`|The record data to insert

---
#### Tool: **`DeleteCollection`**
Delete a collection from the database
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to delete

---
#### Tool: **`DeleteRecord`**
Delete a record from a collection
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection containing the record
`recordId`|`string`|ID of the record to delete

---
#### Tool: **`EstimateDocumentCount`**
Estimate the number of documents in a collection using a fast, approximate count method
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to estimate document count for

---
#### Tool: **`FindDistinctValues`**
Find distinct values for a field in a collection
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to search in
`field`|`string`|Field name to find distinct values for
`filter`|`object` *optional*|Optional filter to apply before finding distinct values

---
#### Tool: **`FindRecord`**
Find records in a collection by field value
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to search in
`field`|`string`|Field name to search by (e.g., 'title', '_id', or any property)
`value`|`string`|Value to search for in the specified field
`limit`|`number` *optional*|Maximum number of records to return

---
#### Tool: **`GetCollections`**
Get all collections in the Astra DB database
#### Tool: **`GetRecord`**
Get a specific record from a collection by ID
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to get the record from
`recordId`|`string`|ID of the record to retrieve

---
#### Tool: **`HelpAddToClient`**
Help the user add the Astra DB client to their MCP client
#### Tool: **`HybridSearch`**
Search for records using both vector similarity and text matching
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to search in
`queryVector`|`array`|The vector to search for similar vectors
`textQuery`|`string`|The text query to search for
`fields`|`array` *optional*|Fields to search in for text matching
`limit`|`number` *optional*|Maximum number of records to return
`weights`|`object` *optional*|Weights for vector and text components

---
#### Tool: **`ListRecords`**
List records from a collection in the database
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to list records from
`limit`|`number` *optional*|Maximum number of records to return

---
#### Tool: **`OpenBrowser`**
Open a web browser to a specific URL
Parameters|Type|Description
-|-|-
`url`|`string`|The URL to open in the browser

---
#### Tool: **`UpdateCollection`**
Update an existing collection in the database
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to update
`newName`|`string`|New name for the collection

---
#### Tool: **`UpdateRecord`**
Update an existing record in a collection
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection containing the record
`record`|`object`|The updated record data
`recordId`|`string`|ID of the record to update

---
#### Tool: **`VectorSearch`**
Search for records in a collection using vector similarity
Parameters|Type|Description
-|-|-
`collectionName`|`string`|Name of the collection to search in
`queryVector`|`array`|The vector to search for similar vectors
`filter`|`object` *optional*|Additional filter criteria for the search
`limit`|`number` *optional*|Maximum number of records to return
`minScore`|`number` *optional*|Minimum similarity score (0.0 to 1.0)

---

## Screenshots

![Astra DB screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/astra-db-1.png)

![Astra DB screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/astra-db-2.png)
