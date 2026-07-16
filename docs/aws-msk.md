Managed Kafka cluster operations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-msk-mcp-server](https://hub.docker.com/repository/docker/mcp/aws-msk-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (12)
Tools provided by this Server|Short Description
-|-
`describe_cluster_operation`|Gets information about a cluster operation.|
`describe_topic`|Returns details for a specific topic on an MSK cluster.|
`describe_topic_partitions`|Returns partition information for a specific topic on an MSK cluster.|
`describe_vpc_connection`|Gets detailed information about a VPC connection.|
`get_cluster_best_practices`|Gets best practices and quotas for AWS MSK clusters.|
`get_cluster_info`|Gets comprehensive information about MSK clusters.|
`get_cluster_telemetry`|Gets telemetry data for MSK clusters.|
`get_configuration_info`|Gets information about MSK configurations.|
`get_global_info`|Gets global information about MSK resources.|
`list_customer_iam_access`|Lists IAM access information for an MSK cluster.|
`list_tags_for_resource`|Lists all tags for an MSK resource.|
`list_topics`|Returns all topics in an MSK cluster.|

---
## Tools Details

#### Tool: **`describe_cluster_operation`**
Gets information about a cluster operation.
Parameters|Type|Description
-|-|-
`cluster_operation_arn`|`string`|The Amazon Resource Name (ARN) of the cluster operation
`region`|`string`|AWS region

---
#### Tool: **`describe_topic`**
Returns details for a specific topic on an MSK cluster.
Parameters|Type|Description
-|-|-
`cluster_arn`|`string`|The Amazon Resource Name (ARN) that uniquely identifies the cluster
`region`|`string`|AWS region
`topic_name`|`string`|The name of the topic to describe

---
#### Tool: **`describe_topic_partitions`**
Returns partition information for a specific topic on an MSK cluster.
Parameters|Type|Description
-|-|-
`cluster_arn`|`string`|The Amazon Resource Name (ARN) that uniquely identifies the cluster
`region`|`string`|AWS region
`topic_name`|`string`|The name of the topic to describe partitions for
`max_results`|`string` *optional*|Maximum number of partitions to return
`next_token`|`string` *optional*|Token for pagination

---
#### Tool: **`describe_vpc_connection`**
Gets detailed information about a VPC connection.
Parameters|Type|Description
-|-|-
`region`|`string`|AWS region
`vpc_connection_arn`|`string`|The Amazon Resource Name (ARN) of the VPC connection

---
#### Tool: **`get_cluster_best_practices`**
Gets best practices and quotas for AWS MSK clusters.
Parameters|Type|Description
-|-|-
`instance_type`|`string`|The AWS MSK broker instance type (e.g., kafka.m5.large, kafka.m5.xlarge, express.m7g.large)
`number_of_brokers`|`integer`|The total number of brokers in the MSK cluster

---
#### Tool: **`get_cluster_info`**
Gets comprehensive information about MSK clusters.
Parameters|Type|Description
-|-|-
`cluster_arn`|`string`|The ARN of the cluster to get information for
`region`|`string`|AWS region
`info_type`|`string` *optional*|Type of information to retrieve (metadata, brokers, nodes, compatible_versions, policy, operations, client_vpc_connections, scram_secrets, all)
`kwargs`|`object` *optional*|Additional arguments specific to each info type

---
#### Tool: **`get_cluster_telemetry`**
Gets telemetry data for MSK clusters.
Parameters|Type|Description
-|-|-
`action`|`string`|The operation to perform (metrics, available_metrics)
`cluster_arn`|`string`|The ARN of the cluster (required for cluster operations)
`region`|`string`|AWS region
`kwargs`|`object` *optional*|Additional arguments based on the action type

---
#### Tool: **`get_configuration_info`**
Gets information about MSK configurations.
Parameters|Type|Description
-|-|-
`action`|`string`|The operation to perform: 'describe', 'revisions', or 'revision_details'
`arn`|`string`|The Amazon Resource Name (ARN) of the configuration
`region`|`string`|AWS region
`kwargs`|`object` *optional*|Additional arguments based on the action

---
#### Tool: **`get_global_info`**
Gets global information about MSK resources.
Parameters|Type|Description
-|-|-
`region`|`string`|AWS region
`info_type`|`string` *optional*|Type of information to retrieve (clusters, configurations, vpc_connections, kafka_versions, all)
`kwargs`|`object` *optional*|Additional arguments specific to each info type

---
#### Tool: **`list_customer_iam_access`**
Lists IAM access information for an MSK cluster.
Parameters|Type|Description
-|-|-
`cluster_arn`|`string`|The ARN of the MSK cluster
`region`|`string`|AWS region

---
#### Tool: **`list_tags_for_resource`**
Lists all tags for an MSK resource.
Parameters|Type|Description
-|-|-
`arn`|`string`|The Amazon Resource Name (ARN) of the resource
`region`|`string`|AWS region

---
#### Tool: **`list_topics`**
Returns all topics in an MSK cluster.
Parameters|Type|Description
-|-|-
`cluster_arn`|`string`|The Amazon Resource Name (ARN) that uniquely identifies the cluster
`region`|`string`|AWS region
`max_results`|`string` *optional*|The maximum number of results to return in the response (default maximum 100 results per API call)
`next_token`|`string` *optional*|The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response
`topic_name_filter`|`string` *optional*|Returns topics starting with given name

---

## Screenshots

![Amazon MSK screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-msk-1.png)

![Amazon MSK screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-msk-2.png)

![Amazon MSK screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-msk-3.png)
