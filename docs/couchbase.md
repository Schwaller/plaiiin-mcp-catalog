Couchbase is a distributed document database with a powerful search engine and in-built operational and analytical capabilities.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/couchbase](https://hub.docker.com/repository/docker/mcp/couchbase)
**Author**|[couchbase](https://github.com/couchbase)
**Repository**|https://github.com/Couchbase-Ecosystem/mcp-server-couchbase

## Available Tools (20)
Tools provided by this Server|Short Description
-|-
`explain_sql_plus_plus_query`|Generate and evaluate an EXPLAIN plan for a SQL++ query.|
`get_buckets_in_cluster`|Get the names of all the accessible buckets in the cluster.|
`get_cluster_health_and_services`|Get cluster health status and list of all running services.|
`get_collections_in_scope`|Get the names of all collections in the given scope and bucket.|
`get_document_by_id`|Get a document by its ID from the specified scope and collection.|
`get_index_advisor_recommendations`|Get index recommendations from Couchbase Index Advisor for a given SQL++ query.|
`get_longest_running_queries`|Get the N longest running queries from the system:completed_requests catalog.|
`get_most_frequent_queries`|Get the N most frequent queries from the system:completed_requests catalog.|
`get_queries_not_selective`|Get queries that are not very selective from the system:completed_requests catalog.|
`get_queries_not_using_covering_index`|Get queries that don't use a covering index from the system:completed_requests catalog.|
`get_queries_using_primary_index`|Get queries that use a primary index from the system:completed_requests catalog.|
`get_queries_with_large_result_count`|Get queries with the largest result counts from the system:completed_requests catalog.|
`get_queries_with_largest_response_sizes`|Get queries with the largest response sizes from the system:completed_requests catalog.|
`get_schema_for_collection`|Get the schema for a collection in the specified scope.|
`get_scopes_and_collections_in_bucket`|Get the names of all scopes and collections in the bucket.|
`get_scopes_in_bucket`|Get the names of all scopes in the given bucket.|
`get_server_configuration_status`|Get the server status and configuration without establishing connection.|
`list_indexes`|List indexes in the cluster with optional filtering by bucket, scope, collection, and index name.|
`run_sql_plus_plus_query`|Run a SQL++ query on a scope and return the results as a list of JSON objects.|
`test_cluster_connection`|Test the connection to Couchbase cluster and optionally to a bucket.|

---
## Tools Details

#### Tool: **`explain_sql_plus_plus_query`**
Generate and evaluate an EXPLAIN plan for a SQL++ query. It provides information about the execution plan for the query.

The EXPLAIN statement is run in the specified scope in the specified bucket.
It returns query metadata along with an extracted plan and plan evaluation.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`query`|`string`|
`scope_name`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_buckets_in_cluster`**
Get the names of all the accessible buckets in the cluster.
#### Tool: **`get_cluster_health_and_services`**
Get cluster health status and list of all running services.

This tool provides health monitoring by:
- Getting health status of all running services with latency information (via ping)
- Listing all services running on the cluster with their endpoints
- Showing connection status and node information for each service

If bucket_name is provided, it actively pings services from the perspective of the bucket.
Otherwise, it uses cluster-level ping to get the health status of the cluster.

Returns:
- Cluster health status with service-level connection details and latency measurements
Parameters|Type|Description
-|-|-
`bucket_name`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_collections_in_scope`**
Get the names of all collections in the given scope and bucket.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`scope_name`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_document_by_id`**
Get a document by its ID from the specified scope and collection.
If the document is not found, it will raise an exception.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`collection_name`|`string`|
`document_id`|`string`|
`scope_name`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_index_advisor_recommendations`**
Get index recommendations from Couchbase Index Advisor for a given SQL++ query.

The Index Advisor analyzes the query and provides recommendations for optimal indexes.
This tool works with SELECT, UPDATE, DELETE, or MERGE queries.
The queries will be run on the specified scope in the specified bucket.

Returns a dictionary with:
- current_used_indexes: Array of currently used indexes (if any)
- recommended_indexes: Array of recommended secondary indexes (if any)
- recommended_covering_indexes: Array of recommended covering indexes (if any)

Each index object contains:
- index: The CREATE INDEX SQL++ command
- statements: Array of statement objects with the query and run count
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`query`|`string`|
`scope_name`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_longest_running_queries`**
Get the N longest running queries from the system:completed_requests catalog.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|Number of queries to return (default: 10)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_most_frequent_queries`**
Get the N most frequent queries from the system:completed_requests catalog.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|Number of queries to return (default: 10)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_queries_not_selective`**
Get queries that are not very selective from the system:completed_requests catalog.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|Number of queries to return (default: 10)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_queries_not_using_covering_index`**
Get queries that don't use a covering index from the system:completed_requests catalog.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|Number of queries to return (default: 10)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_queries_using_primary_index`**
Get queries that use a primary index from the system:completed_requests catalog.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|Number of queries to return (default: 10)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_queries_with_large_result_count`**
Get queries with the largest result counts from the system:completed_requests catalog.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|Number of queries to return (default: 10)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_queries_with_largest_response_sizes`**
Get queries with the largest response sizes from the system:completed_requests catalog.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|Number of queries to return (default: 10)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_schema_for_collection`**
Get the schema for a collection in the specified scope.
Returns a dictionary with the collection name and the schema returned by running INFER query on the Couchbase collection.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`collection_name`|`string`|
`scope_name`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_scopes_and_collections_in_bucket`**
Get the names of all scopes and collections in the bucket.
Returns a dictionary with scope names as keys and lists of collection names as values.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_scopes_in_bucket`**
Get the names of all scopes in the given bucket.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_server_configuration_status`**
Get the server status and configuration without establishing connection.
This tool can be used to verify if the server is running and check the configuration.
#### Tool: **`list_indexes`**
List indexes in the cluster with optional filtering by bucket, scope, collection, and index name.

Filters must be provided hierarchically: scope requires bucket, collection requires both, index requires all three.
Set ``return_raw_index_stats=True`` to get the unprocessed source row for each index.

Each result contains: name, definition (CREATE INDEX statement), status, isPrimary, bucket, scope, collection, lastScanTime.
If a required field is missing, the entry contains warning and raw_index_stats instead.

Source depends on cluster version: v8+ queries ``system:indexes`` via the
query service (RBAC-scoped — the connected user sees only indexes on
keyspaces they can access); older clusters fall back to the admin-level
Index Service REST API ``/getIndexStatus``.
Parameters|Type|Description
-|-|-
`bucket_name`|`string` *optional*|
`collection_name`|`string` *optional*|
`index_name`|`string` *optional*|
`return_raw_index_stats`|`boolean` *optional*|
`scope_name`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`run_sql_plus_plus_query`**
Run a SQL++ query on a scope and return the results as a list of JSON objects.

The query will be run on the specified scope in the specified bucket.
The query should use collection names directly without bucket/scope prefixes, as the scope context is automatically set.

Use ``named_parameters`` to bind values to ``$name`` placeholders in the
query instead of concatenating user input into the statement. This prevents
SQL++ injection

Example:
    query = "SELECT * FROM users WHERE age > 18"
    # Incorrect: "SELECT * FROM bucket.scope.users WHERE age > 18"
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`query`|`string`|
`scope_name`|`string`|
`named_parameters`|`string` *optional*|

---
#### Tool: **`test_cluster_connection`**
Test the connection to Couchbase cluster and optionally to a bucket.
This tool verifies the connection to the Couchbase cluster and bucket by establishing the connection if it is not already established.
If bucket name is not provided, it will not try to connect to the bucket specified in the MCP server settings.
Returns connection status and basic cluster information.
Parameters|Type|Description
-|-|-
`bucket_name`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

---
