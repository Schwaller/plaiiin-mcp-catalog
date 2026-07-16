Official MCP server for Neo4j. Interact with Neo4j using Cypher graph queries.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/neo4j](https://hub.docker.com/repository/docker/mcp/neo4j)
**Author**|[neo4j](https://github.com/neo4j)
**Repository**|https://github.com/neo4j/mcp

## Available Tools (4)
Tools provided by this Server|Short Description
-|-
`get-schema`|Introspect labels, relationship types, and property keys to provide schema context for Neo4j.|
`read-cypher`|Execute arbitrary read-only Cypher queries against the configured Neo4j database.|
`write-cypher`|Execute arbitrary write Cypher queries (including schema/admin operations) against the configured Neo4j database.|
`list-gds-procedures`|List available Neo4j Graph Data Science (GDS) procedures in the connected Neo4j instance.|

---
## Tools Details

#### Tool: **`get-schema`**
Introspect labels, relationship types, and property keys to provide schema context for Neo4j.
#### Tool: **`read-cypher`**
Execute arbitrary read-only Cypher queries against the configured Neo4j database. Rejects writes, schema/admin operations, and PROFILE queries.
Parameters|Type|Description
-|-|-
`query`|`string`|Cypher query to execute in read mode. Must not perform writes, admin, schema, or PROFILE operations.

---
#### Tool: **`write-cypher`**
Execute arbitrary write Cypher queries (including schema/admin operations) against the configured Neo4j database. Use only in non-production environments.
Parameters|Type|Description
-|-|-
`query`|`string`|Cypher query to execute in write mode. Can perform writes, schema changes, and admin operations.

---
#### Tool: **`list-gds-procedures`**
List available Neo4j Graph Data Science (GDS) procedures in the connected Neo4j instance.
