Interact with Neo4j using Cypher graph queries.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/neo4j-cypher](https://hub.docker.com/repository/docker/mcp/neo4j-cypher)
**Author**|[neo4j-contrib](https://github.com/neo4j-contrib)
**Repository**|https://github.com/neo4j-contrib/mcp-neo4j

## Available Tools (3)
Tools provided by this Server|Short Description
-|-
`get_neo4j_schema`|Get Neo4j Schema|
`read_neo4j_cypher`|Read Neo4j Cypher|
`write_neo4j_cypher`|Write Neo4j Cypher|

---
## Tools Details

#### Tool: **`get_neo4j_schema`**
Returns nodes, their properties (with types and indexed flags), and relationships
using APOC's schema inspection.

You should only provide a `sample_size` value if requested by the user, or tuning the retrieval performance.

Performance Notes:
    - If `sample_size` is not provided, uses the server's default sample setting defined in the server configuration.
    - If retrieving the schema times out, try lowering the sample size, e.g. `sample_size=100`.
    - To sample the entire graph use `sample_size=-1`.
Parameters|Type|Description
-|-|-
`sample_size`|`integer` *optional*|The sample size used to infer the graph schema. Larger samples are slower, but more accurate. Smaller samples are faster, but might miss information.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`read_neo4j_cypher`**
Execute a read Cypher query on the neo4j database.
Parameters|Type|Description
-|-|-
`query`|`string`|The Cypher query to execute.
`params`|`object` *optional*|The parameters to pass to the Cypher query.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`write_neo4j_cypher`**
Execute a write Cypher query on the neo4j database.
Parameters|Type|Description
-|-|-
`query`|`string`|The Cypher query to execute.
`params`|`object` *optional*|The parameters to pass to the Cypher query.

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
