Interact with your Elasticsearch indices through natural language conversations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/elasticsearch](https://hub.docker.com/repository/docker/mcp/elasticsearch)
**Author**|[elastic](https://github.com/elastic)
**Repository**|https://github.com/elastic/mcp-server-elasticsearch

## Available Tools (5)
Tools provided by this Server|Short Description
-|-
`esql`|Elasticsearch ES|QL query|
`get_mappings`|Get ES index mappings|
`get_shards`|Get ES shard information|
`list_indices`|List ES indices|
`search`|Elasticsearch search DSL query|

---
## Tools Details

#### Tool: **`esql`**
Perform an Elasticsearch ES|QL query.
Parameters|Type|Description
-|-|-
`query`|`string`|Complete Elasticsearch ES|QL query

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_mappings`**
Get field mappings for a specific Elasticsearch index
Parameters|Type|Description
-|-|-
`index`|`string`|Name of the Elasticsearch index to get mappings for

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_shards`**
Get shard information for all or specific indices.
Parameters|Type|Description
-|-|-
`index`|`string` *optional*|Optional index name to get shard information for

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_indices`**
List all available Elasticsearch indices
Parameters|Type|Description
-|-|-
`index_pattern`|`string`|Index pattern of Elasticsearch indices to list

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`search`**
Perform an Elasticsearch search with the provided query DSL.
Parameters|Type|Description
-|-|-
`index`|`string`|Name of the Elasticsearch index to search
`query_body`|`object`|Complete Elasticsearch query DSL object that can include query, size, from, sort, etc.
`fields`|`array` *optional*|Name of the fields that need to be returned (optional)

*This tool is read-only. It does not modify its environment.*

---
