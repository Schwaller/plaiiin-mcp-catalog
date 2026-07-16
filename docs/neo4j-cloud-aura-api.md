Manage Neo4j Aura database instances through the Neo4j Aura API.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/neo4j-cloud-aura-api](https://hub.docker.com/repository/docker/mcp/neo4j-cloud-aura-api)
**Author**|[neo4j-contrib](https://github.com/neo4j-contrib)
**Repository**|https://github.com/neo4j-contrib/mcp-neo4j

## Available Tools (12)
Tools provided by this Server|Short Description
-|-
`create_instance`|Create Instance|
`delete_instance`|Delete Instance|
`get_instance_by_name`|Get Instance by Name|
`get_instance_details`|Get Instance Details|
`get_tenant_details`|Get Tenant Details|
`list_instances`|List Instances|
`list_tenants`|List Tenants|
`pause_instance`|Pause Instance|
`resume_instance`|Resume Instance|
`update_instance_memory`|Update Instance Memory|
`update_instance_name`|Update Instance Name|
`update_instance_vector_optimization`|Update Instance Vector Optimization|

---
## Tools Details

#### Tool: **`create_instance`**
Create a new Neo4j Aura database instance.
Parameters|Type|Description
-|-|-
`name`|`string`|Name for the new instance
`tenant_id`|`string`|ID of the tenant/project where the instance will be created
`cloud_provider`|`string` *optional*|Cloud provider (gcp, aws, azure)
`graph_analytics_plugin`|`boolean` *optional*|Whether to enable the graph analytics plugin
`memory`|`integer` *optional*|Memory allocation in GB
`region`|`string` *optional*|Region for the instance (e.g., 'us-central1')
`source_instance_id`|`string` *optional*|ID of the source instance to clone from
`type`|`string` *optional*|Instance type (free-db, professional-db, enterprise-db, or business-critical)
`vector_optimized`|`boolean` *optional*|Whether the instance is optimized for vector operations

*This tool interacts with external entities.*

---
#### Tool: **`delete_instance`**
Delete a Neo4j Aura database instance.
Parameters|Type|Description
-|-|-
`instance_id`|`string`|

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`get_instance_by_name`**
Find a Neo4j Aura instance by name and returns the details including the id.
Parameters|Type|Description
-|-|-
`name`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`get_instance_details`**
Get details for one or more Neo4j Aura instances by ID.
Parameters|Type|Description
-|-|-
`instance_ids`|`array`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`get_tenant_details`**
Get details for a specific Neo4j Aura tenant/project.
Parameters|Type|Description
-|-|-
`tenant_id`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`list_instances`**
List all Neo4j Aura database instances.
#### Tool: **`list_tenants`**
List all Neo4j Aura tenants/projects.
#### Tool: **`pause_instance`**
Pause a Neo4j Aura database instance.
Parameters|Type|Description
-|-|-
`instance_id`|`string`|

*This tool interacts with external entities.*

---
#### Tool: **`resume_instance`**
Resume a paused Neo4j Aura database instance.
Parameters|Type|Description
-|-|-
`instance_id`|`string`|

*This tool interacts with external entities.*

---
#### Tool: **`update_instance_memory`**
Update the memory allocation of a Neo4j Aura instance.
Parameters|Type|Description
-|-|-
`instance_id`|`string`|
`memory`|`integer`|

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`update_instance_name`**
Update the name of a Neo4j Aura instance.
Parameters|Type|Description
-|-|-
`instance_id`|`string`|
`name`|`string`|

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`update_instance_vector_optimization`**
Update the vector optimization setting of a Neo4j Aura instance.
Parameters|Type|Description
-|-|-
`instance_id`|`string`|
`vector_optimized`|`boolean`|

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
