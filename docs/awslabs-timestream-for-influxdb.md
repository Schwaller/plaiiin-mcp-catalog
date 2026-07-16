Time-series database operations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/timestream-for-influxdb-mcp-server](https://hub.docker.com/repository/docker/mcp/timestream-for-influxdb-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (26)
Tools provided by this Server|Short Description
-|-
`CreateDbCluster`|Create a new Timestream for InfluxDB database cluster.|
`CreateDbInstance`|Create a new Timestream for InfluxDB database instance|
`CreateDbParamGroup`|Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.|
`DeleteDbCluster`|Deletes a Timestream for InfluxDB cluster by the db_cluster_id|
`DeleteDbInstance`|Deletes a Timestream for InfluxDB DB instance by the instance-identifier|
`GetDbCluster`|Returns a Timestream for InfluxDB DB cluster details by the db_cluster_id|
`GetDbInstance`|Returns a Timestream for InfluxDB DB instance details by the instance-identifier|
`GetDbParameterGroup`|Get a Timestream for InfluxDB DB parameter group details for a db_parameter_group_id|
`InfluxDBCreateBucket`|Create a new bucket in InfluxDB.|
`InfluxDBCreateOrg`|Create a new organization in InfluxDB.|
`InfluxDBListBuckets`|List all buckets in InfluxDB.|
`InfluxDBListOrgs`|List all organizations in InfluxDB.|
`InfluxDBQuery`|Query data from InfluxDB using Flux query language.|
`InfluxDBWriteLP`|Write data in Line Protocol format to InfluxDB.|
`InfluxDBWritePoints`|Write data points to InfluxDB endpoint.|
`ListClustersByStatus`|Returns a list of Timestream for InfluxDB DB clusters filtered by status (case-insensitive).|
`ListDbClusters`|List all Timestream for InfluxDB DB clusters.|
`ListDbInstances`|List all Timestream for InfluxDB DB instances|
`ListDbParamGroups`|List all Timestream for InfluxDB DB parameter groups.|
`ListTagsForResource`|A list of tags applied to the resource.|
`LsInstancesByStatus`|Returns a list of Timestream for InfluxDB DB instances filtered by status (case-insensitive).|
`LsInstancesOfCluster`|List all Timestream for InfluxDB instances belonging to a specific DB cluster.|
`TagResource`|Tags are composed of a Key/Value pairs.|
`UntagResource`|Removes the tags, identified by the keys, from the specified resource.|
`UpdateDbCluster`|Updates a Timestream for InfluxDB cluster.|
`UpdateDbInstance`|Updates a Timestream for InfluxDB DB instance.|

---
## Tools Details

#### Tool: **`CreateDbCluster`**
Create a new Timestream for InfluxDB database cluster.
Parameters|Type|Description
-|-|-
`allocated_storage_gb`|`integer`|The amount of storage to allocate for your DB storage type in GiB (gibibytes).
`db_instance_type`|`string`|The Timestream for InfluxDB DB instance type to run InfluxDB on.
`name`|`string`|The name that uniquely identifies the DB cluster when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint.
`password`|`string`|The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative task and also use the InfluxDB CLI to create an operator token.
`vpc_security_group_ids`|`array`|A list of VPC security group IDs to associate with the DB.
`vpc_subnet_ids`|`array`|A list of VPC subnet IDs to associate with the DB. Provide at least two VPC subnet IDs in different Availability Zones when deploying with a Multi-AZ standby.
`bucket`|`string` *optional*|The name of the initial InfluxDB bucket.
`db_parameter_group_identifier`|`string` *optional*|The id of the DB parameter group to assign to your DB.
`db_storage_type`|`string` *optional*|The Timestream for InfluxDB DB storage type to read and write InfluxDB data.
`deployment_type`|`string` *optional*|Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability.
`failover_mode`|`string` *optional*|Specifies the behavior of failure recovery when the primary node of the cluster fails.
`log_delivery_configuration`|`string` *optional*|Configuration for sending InfluxDB engine logs to a specified S3 bucket.
`networkType`|`string` *optional*|Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4 or DUAL.
`organization`|`string` *optional*|The name of the initial organization for the initial admin user in InfluxDB.An InfluxDB organization is a workspace for a group of users
`port`|`string` *optional*|The port number on which InfluxDB accepts connections. Default: 8086
`publicly_accessible`|`boolean` *optional*|Configures the DB with a public IP to facilitate access from outside the VPC.
`tags`|`string` *optional*|A list of tags to assign to the DB.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)
`username`|`string` *optional*|The username of the initial admin user created in InfluxDB.

---
#### Tool: **`CreateDbInstance`**
Create a new Timestream for InfluxDB database instance
Parameters|Type|Description
-|-|-
`allocated_storage_gb`|`integer`|The amount of storage to allocate for your DB storage type in GiB (gibibytes).
`db_instance_name`|`string`|The name that uniquely identifies the DB instance. This name will also be a prefix included in the endpoint. DB instance names must be unique per customer and per region.
`db_instance_type`|`string`|The Timestream for InfluxDB DB instance type to run InfluxDB on.
`password`|`string`|The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative task and also use the InfluxDB CLI to create an operator token.
`vpc_security_group_ids`|`array`|A list of VPC security group IDs to associate with the DB.
`vpc_subnet_ids`|`array`|A list of VPC subnet IDs to associate with the DB. Provide at least two VPC subnet IDs in different Availability Zones when deploying with a Multi-AZ standby.
`bucket`|`string` *optional*|The name of the initial InfluxDB bucket.
`db_parameter_group_id`|`string` *optional*|The id of the DB parameter group to assign to your DB.
`db_storage_type`|`string` *optional*|The Timestream for InfluxDB DB storage type to read and write InfluxDB data.
`deployment_type`|`string` *optional*|Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability.
`networkType`|`string` *optional*|Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4 or DUAL.
`organization`|`string` *optional*|The name of the initial organization for the initial admin user in InfluxDB.An InfluxDB organization is a workspace for a group of users
`port`|`string` *optional*|The port number on which InfluxDB accepts connections. Default: 8086
`publicly_accessible`|`boolean` *optional*|Configures the DB with a public IP to facilitate access from outside the VPC.
`tags`|`string` *optional*|A list of tags to assign to the DB.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)
`username`|`string` *optional*|The username of the initial admin user created in InfluxDB.

---
#### Tool: **`CreateDbParamGroup`**
Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.
Parameters|Type|Description
-|-|-
`name`|`string`|The name of the DB parameter group. The name must be unique per customer and per region.
`description`|`string` *optional*|A description of the DB parameter group.
`parameters`|`string` *optional*|A list of the parameters that comprise the DB parameter group.
`tags`|`string` *optional*|A list of tags to assign to the DB.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)

---
#### Tool: **`DeleteDbCluster`**
Deletes a Timestream for InfluxDB cluster by the db_cluster_id
Parameters|Type|Description
-|-|-
`db_cluster_id`|`string`|Service-generated unique identifier of the DB cluster.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)

---
#### Tool: **`DeleteDbInstance`**
Deletes a Timestream for InfluxDB DB instance by the instance-identifier
Parameters|Type|Description
-|-|-
`identifier`|`string`|The id of the DB instance.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)

---
#### Tool: **`GetDbCluster`**
Returns a Timestream for InfluxDB DB cluster details by the db_cluster_id
Parameters|Type|Description
-|-|-
`db_cluster_id`|`string`|Service-generated unique identifier of the DB cluster.

---
#### Tool: **`GetDbInstance`**
Returns a Timestream for InfluxDB DB instance details by the instance-identifier
Parameters|Type|Description
-|-|-
`identifier`|`string`|The id of the DB instance.

---
#### Tool: **`GetDbParameterGroup`**
Get a Timestream for InfluxDB DB parameter group details for a db_parameter_group_id
Parameters|Type|Description
-|-|-
`identifier`|`string`|The id of the DB parameter group.

---
#### Tool: **`InfluxDBCreateBucket`**
Create a new bucket in InfluxDB.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|The name of the bucket to create.
`description`|`string` *optional*|Description of the bucket.
`org`|`string` *optional*|The organization name. Falls back to INFLUXDB_ORG env var if not provided.
`retention_seconds`|`string` *optional*|Retention period in seconds. 0 or None means infinite retention.
`token`|`string` *optional*|The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)
`url`|`string` *optional*|The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided.
`verify_ssl`|`boolean` *optional*|Whether to verify SSL with https connections.

---
#### Tool: **`InfluxDBCreateOrg`**
Create a new organization in InfluxDB.
Parameters|Type|Description
-|-|-
`org_name`|`string`|The name of the organization to create.
`token`|`string` *optional*|The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)
`url`|`string` *optional*|The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided.
`verify_ssl`|`boolean` *optional*|Whether to verify SSL with https connections.

---
#### Tool: **`InfluxDBListBuckets`**
List all buckets in InfluxDB.
Parameters|Type|Description
-|-|-
`org`|`string` *optional*|The organization name. Falls back to INFLUXDB_ORG env var if not provided.
`token`|`string` *optional*|The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided.
`url`|`string` *optional*|The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided.
`verify_ssl`|`boolean` *optional*|Whether to verify SSL with https connections.

---
#### Tool: **`InfluxDBListOrgs`**
List all organizations in InfluxDB.
Parameters|Type|Description
-|-|-
`token`|`string` *optional*|The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided.
`url`|`string` *optional*|The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided.
`verify_ssl`|`boolean` *optional*|Whether to verify SSL with https connections.

---
#### Tool: **`InfluxDBQuery`**
Query data from InfluxDB using Flux query language.
Parameters|Type|Description
-|-|-
`query`|`string`|The Flux query string.
`org`|`string` *optional*|The organization name. Falls back to INFLUXDB_ORG env var if not provided.
`token`|`string` *optional*|The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided.
`url`|`string` *optional*|The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided.
`verify_ssl`|`boolean` *optional*|Whether to verify SSL with https connections.

---
#### Tool: **`InfluxDBWriteLP`**
Write data in Line Protocol format to InfluxDB.
Parameters|Type|Description
-|-|-
`bucket`|`string`|The destination bucket for writes.
`data_line_protocol`|`string`|Data in InfluxDB Line Protocol format.
`org`|`string` *optional*|The organization name. Falls back to INFLUXDB_ORG env var if not provided.
`sync_mode`|`string` *optional*|The synchronization mode, either 'synchronous' or 'asynchronous'.
`time_precision`|`string` *optional*|The precision for the unix timestamps within the body line-protocol. One of: ns, us, ms, s (default is ns).
`token`|`string` *optional*|The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)
`url`|`string` *optional*|The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided.
`verify_ssl`|`boolean` *optional*|Whether to verify SSL with https connections.

---
#### Tool: **`InfluxDBWritePoints`**
Write data points to InfluxDB endpoint.
Parameters|Type|Description
-|-|-
`bucket`|`string`|The destination bucket for writes.
`points`|`array`|List of data points to write. Each point should be a dictionary with measurement, tags, fields, and optional time.
`org`|`string` *optional*|The organization name. Falls back to INFLUXDB_ORG env var if not provided.
`sync_mode`|`string` *optional*|The synchronization mode, either 'synchronous' or 'asynchronous'.
`time_precision`|`string` *optional*|The precision for the unix timestamps within the body line-protocol. One of: ns, us, ms, s (default is ns).
`token`|`string` *optional*|The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)
`url`|`string` *optional*|The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided.
`verify_ssl`|`boolean` *optional*|Whether to verify SSL with https connections.

---
#### Tool: **`ListClustersByStatus`**
Returns a list of Timestream for InfluxDB DB clusters filtered by status (case-insensitive).
Parameters|Type|Description
-|-|-
`status`|`string`|The status to filter DB clusters by (case-insensitive).

---
#### Tool: **`ListDbClusters`**
List all Timestream for InfluxDB DB clusters.
Parameters|Type|Description
-|-|-
`max_results`|`string` *optional*|The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output.
`next_token`|`string` *optional*|The pagination token. To resume pagination, provide the next-token value as an argument of a subsequent API invocation.

---
#### Tool: **`ListDbInstances`**
List all Timestream for InfluxDB DB instances
Parameters|Type|Description
-|-|-
`max_results`|`string` *optional*|The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output.
`next_token`|`string` *optional*|The pagination token. To resume pagination, provide the next-token value as an argument of a subsequent API invocation.

---
#### Tool: **`ListDbParamGroups`**
List all Timestream for InfluxDB DB parameter groups.
Parameters|Type|Description
-|-|-
`max_results`|`string` *optional*|The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output.
`next_token`|`string` *optional*|The pagination token. To resume pagination, provide the next-token value as an argument of a subsequent API invocation.

---
#### Tool: **`ListTagsForResource`**
A list of tags applied to the resource.
Parameters|Type|Description
-|-|-
`resource_arn`|`string`|The Amazon Resource Name (ARN) of the tagged resource.

---
#### Tool: **`LsInstancesByStatus`**
Returns a list of Timestream for InfluxDB DB instances filtered by status (case-insensitive).
Parameters|Type|Description
-|-|-
`status`|`string`|The status to filter DB instances by (case-insensitive).

---
#### Tool: **`LsInstancesOfCluster`**
List all Timestream for InfluxDB instances belonging to a specific DB cluster.
Parameters|Type|Description
-|-|-
`db_cluster_id`|`string`|Service-generated unique identifier of the DB cluster.
`max_results`|`string` *optional*|The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output.
`next_token`|`string` *optional*|The pagination token. To resume pagination, provide the next-token value as an argument of a subsequent API invocation.

---
#### Tool: **`TagResource`**
Tags are composed of a Key/Value pairs. Apply them to Timestream for InfluxDB resource.
Parameters|Type|Description
-|-|-
`resource_arn`|`string`|The Amazon Resource Name (ARN) of the tagged resource.
`tags`|`object`|A list of key-value pairs as tags.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)

---
#### Tool: **`UntagResource`**
Removes the tags, identified by the keys, from the specified resource.
Parameters|Type|Description
-|-|-
`resource_arn`|`string`|The Amazon Resource Name (ARN) of the tagged resource.
`tag_keys`|`array`|The keys used to identify the tags to remove.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)

---
#### Tool: **`UpdateDbCluster`**
Updates a Timestream for InfluxDB cluster.
Parameters|Type|Description
-|-|-
`db_cluster_id`|`string`|Service-generated unique identifier of the DB cluster.
`db_instance_type`|`string` *optional*|Update the DB cluster to use the specified DB instance Type.
`db_parameter_group_identifier`|`string` *optional*|Update the DB cluster to use the specified DB parameter group.
`failover_mode`|`string` *optional*|Update the DB cluster's failover behavior.
`log_delivery_configuration`|`string` *optional*|The log delivery configuration to apply to the DB cluster.
`port`|`string` *optional*|Update the DB cluster to use the specified port.
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)

---
#### Tool: **`UpdateDbInstance`**
Updates a Timestream for InfluxDB DB instance.
Parameters|Type|Description
-|-|-
`identifier`|`string`|The id of the DB instance.
`allocated_storage_gb`|`string` *optional*|The amount of storage to allocate for your DB storage type (in gibibytes).
`db_instance_type`|`string` *optional*|Update the DB cluster to use the specified DB instance Type.
`db_parameter_group_identifier`|`string` *optional*|The id of the DB parameter group to assign to your DB.
`db_storage_type`|`string` *optional*|The Timestream for InfluxDB DB storage type to read and write InfluxDB data.
`deployment_type`|`string` *optional*|Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability.
`log_delivery_configuration`|`string` *optional*|Configuration for sending InfluxDB engine logs to a specified S3 bucket.
`port`|`string` *optional*|The port number on which InfluxDB accepts connections. Default: 8086
`tool_write_mode`|`boolean` *optional*|Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False)

---

## Screenshots

![Amazon Timestream for InfluxDB screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/awslabs-timestream-for-influxdb-1.png)

![Amazon Timestream for InfluxDB screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/awslabs-timestream-for-influxdb-2.png)

![Amazon Timestream for InfluxDB screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/awslabs-timestream-for-influxdb-3.png)
