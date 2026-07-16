Seamless interaction with Novita AI platform resources.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/novita](https://hub.docker.com/repository/docker/mcp/novita)
**Author**|[novitalabs](https://github.com/novitalabs)
**Repository**|https://github.com/novitalabs/novita-mcp-server

## Available Tools (20)
Tools provided by this Server|Short Description
-|-
`create-container-registry-auth`||
`create-gpu-instance`||
`create-network-storage`||
`create-template`||
`delete-container-registry-auth`||
`delete-gpu-instance`||
`delete-network-storage`||
`delete-template`||
`get-gpu-instance`||
`get-template`||
`list-clusters`||
`list-container-registry-auths`||
`list-gpu-instances`||
`list-network-storage`||
`list-products`||
`list-templates`||
`restart-gpu-instance`||
`start-gpu-instance`||
`stop-gpu-instance`||
`update-network-storage`||

---
## Tools Details

#### Tool: **`create-container-registry-auth`**

Parameters|Type|Description
-|-|-
`name`|`string`|Name for the container registry auth.
`password`|`string`|Registry password.
`username`|`string`|Registry username.

---
#### Tool: **`create-gpu-instance`**

Parameters|Type|Description
-|-|-
`gpuNum`|`number`|Number of GPUs allocated to the instance. The availableGpuNumber of the product must be greater than or equal to the gpuNum.
`imageUrl`|`string`|Docker image URL to initialize the instance
`name`|`string`|Name for the instance. Must contain only numbers, letters, and hyphens
`productId`|`string`|ID of the product used to deploy the instance. The availableGpuNumber of the product must be greater than 0. You can use the `list-products` tool to get or check the product ID if needed. Before calling the MCP tool, MUST show me the details of the product to help me identify it, including name, price, etc.
`rootfsSize`|`number`|Root filesystem size (container disk size) in GB. Free tier includes 60GB.
`command`|`string` *optional*|Container start command to run when the instance starts
`env`|`array` *optional*|Environment variables
`imageAuthId`|`string` *optional*|ID of the container registry auth. Required only when the imageUrl is private. You can use the `list-container-registry-auths` tool to check the ID if you're not sure.
`kind`|`string` *optional*|Type of the instance
`networkStorages`|`array` *optional*|Network storages to mount
`ports`|`string` *optional*|Ports to expose (e.g., '8888/http', '22/tcp'), separated by commas if multiple. Maximum of 10 ports.

---
#### Tool: **`create-network-storage`**

Parameters|Type|Description
-|-|-
`clusterId`|`string`|The ID of the cluster to create network storage. Must be from the `list-clusters` tool result, and the cluster must have supportNetworkStorage set to true
`storageName`|`string`|Name for the network storage. Use only letters, numbers, and hyphens
`storageSize`|`number`|Size of the network storage in GB

---
#### Tool: **`create-template`**

Parameters|Type|Description
-|-|-
`template`|`object`|

---
#### Tool: **`delete-container-registry-auth`**

Parameters|Type|Description
-|-|-
`id`|`string`|ID of the container registry auth to delete. Please ensure it exists before deleting. Before calling the MCP tool, please show me the name to help identify it. You can use the `list-container-registry-auths` tool to check the ID if needed.

---
#### Tool: **`delete-gpu-instance`**

Parameters|Type|Description
-|-|-
`instanceId`|`string`|ID of the instance to delete. Before calling the MCP tool to delete the instance, MUST show me the details of the instance to help me identify it, including id, name, etc.

---
#### Tool: **`delete-network-storage`**

Parameters|Type|Description
-|-|-
`storageId`|`string`|The unique ID of the network storage to delete. Please ensure it exists before updating.

---
#### Tool: **`delete-template`**

Parameters|Type|Description
-|-|-
`templateId`|`string`|ID of the template to delete. Please ensure it exists before deleting. Before calling the MCP tool, please show me the name to help identify it. You can use the `get-template` tool to check the ID if needed.

---
#### Tool: **`get-gpu-instance`**

Parameters|Type|Description
-|-|-
`instanceId`|`string`|ID of the instance to retrieve

---
#### Tool: **`get-template`**

Parameters|Type|Description
-|-|-
`templateId`|`string`|ID of the template to retrieve

---
#### Tool: **`list-clusters`**

#### Tool: **`list-container-registry-auths`**

#### Tool: **`list-gpu-instances`**

Parameters|Type|Description
-|-|-
`name`|`string` *optional*|Filter by the instance name
`pageNumber`|`number` *optional*|Page number to return, start from 
`pageSize`|`number` *optional*|Number of instances to return, 
`productName`|`string` *optional*|Filter by the product name
`status`|`string` *optional*|Filter by the instance status

---
#### Tool: **`list-network-storage`**

Parameters|Type|Description
-|-|-
`pageNo`|`number` *optional*|Page number
`pageSize`|`number` *optional*|Page size
`storageId`|`string` *optional*|ID for the network storage
`storageName`|`string` *optional*|Name for the network storage

---
#### Tool: **`list-products`**

Parameters|Type|Description
-|-|-
`clusterId`|`string` *optional*|ID of the cluster to list products from. You can use the `list-clusters` tool to get the cluster ID.
`productName`|`string` *optional*|Name of the product to filter by.

---
#### Tool: **`list-templates`**

Parameters|Type|Description
-|-|-
`channel`|`array` *optional*|Channels of template to return
`pageNum`|`number` *optional*|Page number to return, start from 1
`pageSize`|`number` *optional*|Number of templates to return in each page
`type`|`string` *optional*|Type of template to return

---
#### Tool: **`restart-gpu-instance`**

Parameters|Type|Description
-|-|-
`instanceId`|`string`|ID of the instance to restart. Before calling the MCP tool to restart the instance, MUST show me the details of the instance to help me identify it, including id, name, etc.

---
#### Tool: **`start-gpu-instance`**

Parameters|Type|Description
-|-|-
`instanceId`|`string`|ID of the instance to start

---
#### Tool: **`stop-gpu-instance`**

Parameters|Type|Description
-|-|-
`instanceId`|`string`|ID of the instance to stop. Before calling the MCP tool to stop the instance, MUST show me the details of the instance to help me identify it, including id, name, etc.

---
#### Tool: **`update-network-storage`**

Parameters|Type|Description
-|-|-
`storageId`|`string`|The unique ID of the network storage to update. Please ensure it exists before updating.
`storageSize`|`number`|New size in GB (must be larger than current size). You can use the `list-network-storage` tool to get the current size if you don't know it.
`storageName`|`string` *optional*|New name for the network storage. This is optional, if not provided, the name will not be changed. Use only letters, numbers, and hyphens

---
