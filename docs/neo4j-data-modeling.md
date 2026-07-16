MCP server that assists in creating, validating and visualizing graph data models.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/neo4j-data-modeling](https://hub.docker.com/repository/docker/mcp/neo4j-data-modeling)
**Author**|[neo4j-contrib](https://github.com/neo4j-contrib)
**Repository**|https://github.com/neo4j-contrib/mcp-neo4j

## Available Tools (16)
Tools provided by this Server|Short Description
-|-
`export_to_arrows_json`|Export to Arrows JSON|
`export_to_neo4j_graphrag_pkg_schema`|Export to Neo4j GraphRAG Schema|
`export_to_owl_turtle`|Export to OWL Turtle|
`export_to_pydantic_models`|Export to Pydantic Models|
`get_constraints_cypher_queries`|Get Constraints Cypher Queries|
`get_example_data_model`|Get Example Data Model|
`get_mermaid_config_str`|Get Mermaid Config|
`get_node_cypher_ingest_query`|Get Node Cypher Ingest Query|
`get_relationship_cypher_ingest_query`|Get Relationship Cypher Ingest Query|
`list_example_data_models`|List Example Data Models|
`load_from_arrows_json`|Load from Arrows JSON|
`load_from_neo4j_graphrag_pkg_schema`|Load from Neo4j GraphRAG Schema|
`load_from_owl_turtle`|Load from OWL Turtle|
`validate_data_model`|Validate Data Model|
`validate_node`|Validate Node|
`validate_relationship`|Validate Relationship|

---
## Tools Details

#### Tool: **`export_to_arrows_json`**
Export the data model to the Arrows web application format.
Returns a JSON string. This should be presented to the user as an artifact if possible.
Accepts either a DataModel object or a JSON string of the DataModel object.
Parameters|Type|Description
-|-|-
`data_model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`export_to_neo4j_graphrag_pkg_schema`**
Export a data model to a Neo4j Graphrag Python Package schema.
Returns a dictionary containing the Neo4j Graphrag Python Package schema.
Accepts either a DataModel object or a JSON string of the DataModel object.
Parameters|Type|Description
-|-|-
`data_model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`export_to_owl_turtle`**
Export a data model to an OWL Turtle string.
This process is lossy since OWL does not support properties on relationships.
Returns a string representation of the data model in OWL Turtle format.
Accepts either a DataModel object or a JSON string of the DataModel object.
Parameters|Type|Description
-|-|-
`data_model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`export_to_pydantic_models`**
Export a data model to Pydantic models.
Returns a string representation of the Pydantic models for the data model as a Python file.
Accepts either a DataModel object or a JSON string of the DataModel object.
Parameters|Type|Description
-|-|-
`data_model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_constraints_cypher_queries`**
Get the Cypher queries to create constraints on the data model.
This creates range indexes on the key properties of the nodes and relationships and enforces uniqueness and existence of the key properties.
Accepts either a DataModel object or a JSON string of the DataModel object.
Parameters|Type|Description
-|-|-
`data_model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_example_data_model`**
Get an example graph data model from the available templates. Returns a DataModel object and the Mermaid visualization configuration for the example graph data model.
Parameters|Type|Description
-|-|-
`example_name`|`string`|Name of the example to load: 'patient_journey', 'supply_chain', 'software_dependency', 'oil_gas_monitoring', 'customer_360', 'fraud_aml', or 'health_insurance_fraud'

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_mermaid_config_str`**
Get the Mermaid configuration string for the data model.
This may be visualized in Claude Desktop and other applications with Mermaid support.
Accepts either a DataModel object or a JSON string of the DataModel object.
Parameters|Type|Description
-|-|-
`data_model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_node_cypher_ingest_query`**
Get the Cypher query to ingest a list of Node records into a Neo4j database.
This should be used to ingest data into a Neo4j database.
This is a parameterized Cypher query that takes a list of records as input to the $records parameter.
Parameters|Type|Description
-|-|-
`node`|`string`|The node to get the Cypher query for. Accepts either a Node object or a JSON string of the Node object.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_relationship_cypher_ingest_query`**
Get the Cypher query to ingest a list of Relationship records into a Neo4j database.
This should be used to ingest data into a Neo4j database.
This is a parameterized Cypher query that takes a list of records as input to the $records parameter.
The records must contain the Relationship properties, if any, as well as the sourceId and targetId properties of the start and end nodes respectively.
Parameters|Type|Description
-|-|-
`data_model`|`string`|The data model snippet that contains the relationship, start node and end node. Accepts either a DataModel object or a JSON string of the DataModel object.
`relationship_end_node_label`|`string`|The label of the relationship end node.
`relationship_start_node_label`|`string`|The label of the relationship start node.
`relationship_type`|`string`|The type of the relationship to get the Cypher query for.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_example_data_models`**
List all available example data models with descriptions. Returns a dictionary with example names and their descriptions.
#### Tool: **`load_from_arrows_json`**
Load a data model from the Arrows web application format. Returns a data model as a JSON string.
Parameters|Type|Description
-|-|-
`arrows_data_model_dict`|`object`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`load_from_neo4j_graphrag_pkg_schema`**
Load a data model from a Neo4j Graphrag Python Package schema.
Returns a DataModel object.
Accepts a Neo4j Graphrag Python Package schema dictionary.
Parameters|Type|Description
-|-|-
`neo4j_graphrag_python_package_schema`|`object`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`load_from_owl_turtle`**
Load a data model from an OWL Turtle string.
This process is lossy and some components of the ontology may be lost in the data model schema.
Returns a DataModel object.
Parameters|Type|Description
-|-|-
`owl_turtle_str`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`validate_data_model`**
Validate the entire data model.
Returns True if the data model is valid, otherwise raises a ValueError.
If return_validated is True, returns the validated data model.
Accepts either a DataModel object or a JSON string of the DataModel object.
Parameters|Type|Description
-|-|-
`data_model`|`string`|
`return_validated`|`boolean` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`validate_node`**
Validate a single node.
Returns True if the node is valid, otherwise raises a ValueError.
If return_validated is True, returns the validated node.
Accepts either a Node object or a JSON string of the Node object.
Parameters|Type|Description
-|-|-
`node`|`string`|
`return_validated`|`boolean` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`validate_relationship`**
Validate a single relationship.
Returns True if the relationship is valid, otherwise raises a ValueError.
If return_validated is True, returns the validated relationship.
Accepts either a Relationship object or a JSON string of the Relationship object.
Parameters|Type|Description
-|-|-
`relationship`|`string`|
`return_validated`|`boolean` *optional*|

*This tool is read-only. It does not modify its environment.*

---
