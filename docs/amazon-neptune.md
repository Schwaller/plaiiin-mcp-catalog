Graph database queries with Cypher and Gremlin.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/amazon-neptune-mcp-server](https://hub.docker.com/repository/docker/mcp/amazon-neptune-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (4)
Tools provided by this Server|Short Description
-|-
`get_graph_schema`|Get the schema for the graph including the vertex and edge labels as well as the (vertex)-[edge]->(vertex) combinations.|
`get_graph_status`|Get the status of the currently configured Amazon Neptune graph.|
`run_gremlin_query`|Executes the provided Tinkerpop Gremlin against the graph.|
`run_opencypher_query`|Executes the provided openCypher against the graph.|

---
## Tools Details

#### Tool: **`get_graph_schema`**
Get the schema for the graph including the vertex and edge labels as well as the
(vertex)-[edge]->(vertex) combinations.
#### Tool: **`get_graph_status`**
Get the status of the currently configured Amazon Neptune graph.
#### Tool: **`run_gremlin_query`**
Executes the provided Tinkerpop Gremlin against the graph.
Parameters|Type|Description
-|-|-
`query`|`string`|

---
#### Tool: **`run_opencypher_query`**
Executes the provided openCypher against the graph.
Parameters|Type|Description
-|-|-
`query`|`string`|
`parameters`|`string` *optional*|

---

## Screenshots

![Amazon Neptune screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/amazon-neptune-1.png)

![Amazon Neptune screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/amazon-neptune-2.png)

![Amazon Neptune screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/amazon-neptune-3.png)
