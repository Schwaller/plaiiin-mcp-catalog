ElastiCache control plane operations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/elasticache-mcp-server](https://hub.docker.com/repository/docker/mcp/elasticache-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (39)
Tools provided by this Server|Short Description
-|-
`batch-apply-update-action`|Apply service update to multiple ElastiCache resources.|
`batch-stop-update-action`|Stop service update for multiple ElastiCache resources.|
`complete-migration`|Complete migration to an Amazon ElastiCache replication group.|
`connect-jump-host-cache-cluster`|Configures an existing EC2 instance as a jump host to access an ElastiCache cluster.|
`connect-jump-host-replication-group`|Configures an existing EC2 instance as a jump host to access an ElastiCache replication group.|
`connect-jump-host-serverless-cache`|Configures an existing EC2 instance as a jump host to access an ElastiCache serverless cache.|
`create-cache-cluster`|Create an Amazon ElastiCache cache cluster.|
`create-jump-host-cache-cluster`|Creates an EC2 jump host instance to access an ElastiCache cluster via SSH tunnel.|
`create-jump-host-replication-group`|Creates an EC2 jump host instance to access an ElastiCache replication group via SSH tunnel.|
`create-jump-host-serverless-cache`|Creates an EC2 jump host instance to access an ElastiCache serverless cache via SSH tunnel.|
`create-log-group`|Create a new CloudWatch Logs log group.|
`create-replication-group`|Create an Amazon ElastiCache replication group.|
`create-serverless-cache`|Create a new Amazon ElastiCache serverless cache.|
`delete-cache-cluster`|Delete an Amazon ElastiCache cache cluster.|
`delete-replication-group`|Delete an Amazon ElastiCache replication group.|
`delete-serverless-cache`|Delete an Amazon ElastiCache serverless cache.|
`describe-cache-clusters`|Describe one or more ElastiCache cache clusters.|
`describe-cache-engine-versions`|Returns a list of the available cache engines and their versions.|
`describe-engine-default-parameters`|Returns the default engine and system parameter information for the specified cache engine family.|
`describe-events`|Returns events related to clusters, cache security groups, and parameter groups.|
`describe-log-groups`|Describe CloudWatch Logs log groups.|
`describe-log-streams`|Describe CloudWatch Logs log streams.|
`describe-replication-groups`|Describe one or more ElastiCache replication groups.|
`describe-serverless-caches`|Describe Amazon ElastiCache serverless caches in your AWS account.|
`describe-service-updates`|Returns details of the service updates.|
`filter-log-events`|Filter log events from CloudWatch Logs.|
`get-cost-and-usage`|Get cost and usage data for ElastiCache resources.|
`get-log-events`|Get log events from CloudWatch Logs.|
`get-metric-statistics`|Get CloudWatch metric statistics.|
`get-ssh-tunnel-command-cache-cluster`|Generates an SSH tunnel command to connect to an ElastiCache cluster through an EC2 jump host.|
`get-ssh-tunnel-command-replication-group`|Generates an SSH tunnel command to connect to an ElastiCache replication group through an EC2 jump host.|
`get-ssh-tunnel-command-serverless-cache`|Generates an SSH tunnel command to connect to an ElastiCache serverless cache through an EC2 jump host.|
`list-delivery-streams`|List your delivery streams.|
`modify-cache-cluster`|Modify an existing Amazon ElastiCache cache cluster.|
`modify-replication-group`|Modify an existing Amazon ElastiCache replication group.|
`modify-replication-group-shard-configuration`|Modify the shard configuration of an existing Amazon ElastiCache replication group.|
`modify-serverless-cache`|Modify an Amazon ElastiCache serverless cache.|
`start-migration`|Start migration to an Amazon ElastiCache replication group.|
`test-migration`|Test migration to an Amazon ElastiCache replication group.|

---
## Tools Details

#### Tool: **`batch-apply-update-action`**
Apply service update to multiple ElastiCache resources.

Parameters:
    service_update_name (str): The unique ID of the service update to apply.
    replication_group_ids (Optional[List[str]]): List of replication group IDs to update.
        Either this or cache_cluster_ids must be provided.
    cache_cluster_ids (Optional[List[str]]): List of cache cluster IDs to update.
        Either this or replication_group_ids must be provided.

Returns:
    Dict containing information about the batch update operation.
Parameters|Type|Description
-|-|-
`service_update_name`|`string`|
`cache_cluster_ids`|`string` *optional*|
`replication_group_ids`|`string` *optional*|

---
#### Tool: **`batch-stop-update-action`**
Stop service update for multiple ElastiCache resources.

Parameters:
    service_update_name (str): The unique ID of the service update to stop.
    replication_group_ids (Optional[List[str]]): List of replication group IDs to stop update.
        Either this or cache_cluster_ids must be provided.
    cache_cluster_ids (Optional[List[str]]): List of cache cluster IDs to stop update.
        Either this or replication_group_ids must be provided.

Returns:
    Dict containing information about the batch stop operation.
Parameters|Type|Description
-|-|-
`service_update_name`|`string`|
`cache_cluster_ids`|`string` *optional*|
`replication_group_ids`|`string` *optional*|

---
#### Tool: **`complete-migration`**
Complete migration to an Amazon ElastiCache replication group.

This tool completes the migration of data from a Redis instance to an ElastiCache replication group.
It finalizes the data migration process and transitions the replication group to normal operation.
Parameters|Type|Description
-|-|-
`request`|`string`|The CompleteMigrationRequest object containing:

---
#### Tool: **`connect-jump-host-cache-cluster`**
Configures an existing EC2 instance as a jump host to access an ElastiCache cluster.
Parameters|Type|Description
-|-|-
`cache_cluster_id`|`string`|
`instance_id`|`string`|

---
#### Tool: **`connect-jump-host-replication-group`**
Configures an existing EC2 instance as a jump host to access an ElastiCache replication group.
Parameters|Type|Description
-|-|-
`instance_id`|`string`|
`replication_group_id`|`string`|

---
#### Tool: **`connect-jump-host-serverless-cache`**
Configures an existing EC2 instance as a jump host to access an ElastiCache serverless cache.
Parameters|Type|Description
-|-|-
`instance_id`|`string`|
`serverless_cache_name`|`string`|

---
#### Tool: **`create-cache-cluster`**
Create an Amazon ElastiCache cache cluster.
Parameters|Type|Description
-|-|-
`request`|`string`|

---
#### Tool: **`create-jump-host-cache-cluster`**
Creates an EC2 jump host instance to access an ElastiCache cluster via SSH tunnel.
Parameters|Type|Description
-|-|-
`cache_cluster_id`|`string`|
`key_name`|`string`|
`instance_type`|`string` *optional*|
`security_group_id`|`string` *optional*|
`subnet_id`|`string` *optional*|

---
#### Tool: **`create-jump-host-replication-group`**
Creates an EC2 jump host instance to access an ElastiCache replication group via SSH tunnel.
Parameters|Type|Description
-|-|-
`key_name`|`string`|
`replication_group_id`|`string`|
`instance_type`|`string` *optional*|
`security_group_id`|`string` *optional*|
`subnet_id`|`string` *optional*|

---
#### Tool: **`create-jump-host-serverless-cache`**
Creates an EC2 jump host instance to access an ElastiCache serverless cache via SSH tunnel.
Parameters|Type|Description
-|-|-
`key_name`|`string`|
`serverless_cache_name`|`string`|
`instance_type`|`string` *optional*|
`security_group_id`|`string` *optional*|
`subnet_id`|`string` *optional*|

---
#### Tool: **`create-log-group`**
Create a new CloudWatch Logs log group.
Parameters|Type|Description
-|-|-
`log_group_name`|`string`|The name of the log group to create
`kms_key_id`|`string` *optional*|The Amazon Resource Name (ARN) of the KMS key to use for encryption
`log_group_class`|`string` *optional*|Specify one of the following classes:
`tags`|`string` *optional*|The key-value pairs to use for the tags

---
#### Tool: **`create-replication-group`**
Create an Amazon ElastiCache replication group.

This tool creates a new replication group with specified configuration including:
- Basic replication group settings
- Cache node configuration
- Network and security settings
- Encryption settings
- Backup and maintenance settings
- Monitoring and logging settings
Parameters|Type|Description
-|-|-
`request`|`string`|The CreateReplicationGroupRequest object containing all parameters

---
#### Tool: **`create-serverless-cache`**
Create a new Amazon ElastiCache serverless cache.

This tool creates a new serverless cache with specified configuration including:
- Serverless cache name and capacity
- Optional VPC and security settings
- Optional encryption settings
- Optional snapshot restoration and backup settings
- Optional usage limits and user groups
- Optional tags

Parameters:
    serverless_cache_name (str): Name of the serverless cache.
    engine (str): Cache engine type.
    description (Optional[str]): Description for the cache.
    kms_key_id (Optional[str]): KMS key ID for encryption.
    major_engine_version (Optional[str]): Major engine version.
    snapshot_arns_to_restore (Optional[List[str]]): List of snapshot ARNs to restore from.
    subnet_ids (Optional[List[str]]): List of subnet IDs for VPC configuration.
    tags (Optional[Union[str, List[Dict[str, Optional[str]]], Dict[str, Optional[str]]]]): Tags to apply to the cache.
        Tag requirements:
        - Key: (string) Required. The key for the tag. Must not be empty.
        - Value: (string) Optional. The tag's value. May be null.

        Supports three formats:
        1. Shorthand syntax: "Key=value,Key2=value2" or "Key=,Key2=" for null values
        2. Dictionary: {"key": "value", "key2": null}
        3. JSON array: [{"Key": "string", "Value": "string"}, {"Key": "string2", "Value": null}]

        Can be None if no tags are needed.
    security_group_ids (Optional[List[str]]): List of security group IDs.
    cache_usage_limits (Optional[CacheUsageLimits]): Usage limits for the cache. Structure:
        {
            "DataStorage": {
                "Maximum": int,  # Maximum storage in GB
                "Minimum": int,  # Minimum storage in GB
                "Unit": "GB"     # Storage unit (currently only GB is supported)
            },
            "ECPUPerSecond": {
                "Maximum": int,  # Maximum ECPU per second
                "Minimum": int   # Minimum ECPU per second
            }
        }
    user_group_id (Optional[str]): ID of the user group to associate with the cache.
    snapshot_retention_limit (Optional[int]): Number of days for which ElastiCache retains automatic snapshots.
    daily_snapshot_time (Optional[str]): Time range (in UTC) when daily snapshots are taken (e.g., '04:00-05:00').

Returns:
    Dict containing information about the created serverless cache.
Parameters|Type|Description
-|-|-
`request`|`string`|

---
#### Tool: **`delete-cache-cluster`**
Delete an Amazon ElastiCache cache cluster.

This tool deletes an existing cache cluster. Optionally, it can create a final
snapshot of the cluster before deletion.

Parameters:
    cache_cluster_id (str): The ID of the cache cluster to delete.
    final_snapshot_identifier (Optional[str]): The user-supplied name of a final
        cache cluster snapshot. This is the unique name that identifies the
        snapshot. ElastiCache creates the snapshot, and then deletes the cache
        cluster immediately afterward.

Returns:
    Dict containing information about the deleted cache cluster.
Parameters|Type|Description
-|-|-
`cache_cluster_id`|`string`|
`final_snapshot_identifier`|`string` *optional*|

---
#### Tool: **`delete-replication-group`**
Delete an Amazon ElastiCache replication group.

This tool deletes an existing replication group. You can optionally retain the primary cluster
as a standalone cache cluster or create a final snapshot before deletion.

Parameters:
    replication_group_id (str): The identifier of the replication group to delete.
    retain_primary_cluster (Optional[bool]): If True, retains the primary cluster as a standalone
        cache cluster. If False, deletes all clusters in the replication group.
    final_snapshot_name (Optional[str]): The name of a final cache cluster snapshot to create
        before deleting the replication group.

Returns:
    Dict containing information about the deleted replication group.
Parameters|Type|Description
-|-|-
`replication_group_id`|`string`|
`final_snapshot_name`|`string` *optional*|
`retain_primary_cluster`|`string` *optional*|

---
#### Tool: **`delete-serverless-cache`**
Delete an Amazon ElastiCache serverless cache.

This tool deletes a specified serverless cache from your AWS account.
The cache must exist and be in a deletable state.

Parameters:
    serverless_cache_name (str): Name of the serverless cache to delete.
    final_snapshot_name (Optional[str]): Name of the final snapshot to create before deletion.

Returns:
    Dict containing the deletion response or error information.
Parameters|Type|Description
-|-|-
`serverless_cache_name`|`string`|
`final_snapshot_name`|`string` *optional*|

---
#### Tool: **`describe-cache-clusters`**
Describe one or more ElastiCache cache clusters.

This tool returns information about provisioned cache clusters. If a cache cluster ID
is specified, information about only that cache cluster is returned. Otherwise, information
about up to MaxRecords cache clusters is returned.

Parameters:
    cache_cluster_id (Optional[str]): The identifier for the cache cluster to describe.
        If not provided, information about all cache clusters is returned.
    max_records (Optional[int]): The maximum number of records to include in the response.
        If more records exist than the specified MaxRecords value, a marker is included
        in the response so that the remaining results can be retrieved.
    marker (Optional[str]): An optional marker returned from a previous request. Use this marker
        for pagination of results from this operation. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified
        by MaxRecords.
    show_cache_node_info (Optional[bool]): Whether to include detailed information about
        cache nodes in the response.
    show_cache_clusters_not_in_replication_groups (Optional[bool]): Whether to show only
        cache clusters that are not members of a replication group.

Returns:
    Dict containing information about the cache cluster(s), including:
    - CacheClusters: List of cache clusters
    - Marker: Pagination marker for next set of results
Parameters|Type|Description
-|-|-
`cache_cluster_id`|`string` *optional*|
`marker`|`string` *optional*|
`max_records`|`string` *optional*|
`show_cache_clusters_not_in_replication_groups`|`string` *optional*|
`show_cache_node_info`|`string` *optional*|

---
#### Tool: **`describe-cache-engine-versions`**
Returns a list of the available cache engines and their versions.

Parameters:
    engine (Optional[str]): The cache engine to return. Valid values: memcached | redis | valkey
    engine_version (Optional[str]): The cache engine version to return.
        Example: memcached 1.4.14, redis 6.x, valkey 8.0
    cache_parameter_group_family (Optional[str]): The name of a specific cache parameter group family.
        Valid values are: memcached1.4 | memcached1.5 | memcached1.6 | redis2.6 | redis2.8 |
        redis3.2 | redis4.0 | redis5.0 | redis6.x | redis7.x | valkey7.x | valkey8.x
    max_records (Optional[int]): The maximum number of records to include in the response.
        If more records exist than the specified MaxRecords value, a marker is included
        in the response so that the remaining results can be retrieved.
    marker (Optional[str]): An optional marker returned from a previous request. Use this marker
        for pagination of results from this operation. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified
        by MaxRecords.
    default_only (Optional[bool]): If true, specifies that only the default version of the specified engine
        or engine and major version combination is to be returned.

Returns:
    Dict containing information about the cache engine versions, including:
    - CacheEngineVersions: List of cache engine versions
    - Marker: Pagination marker for next set of results
Parameters|Type|Description
-|-|-
`cache_parameter_group_family`|`string` *optional*|
`default_only`|`string` *optional*|
`engine`|`string` *optional*|
`engine_version`|`string` *optional*|
`marker`|`string` *optional*|
`max_records`|`string` *optional*|

---
#### Tool: **`describe-engine-default-parameters`**
Returns the default engine and system parameter information for the specified cache engine family.

Parameters:
    cache_parameter_group_family (str): The name of the cache parameter group family.
        Valid values are: memcached1.4 | memcached1.5 | memcached1.6 | redis2.6 | redis2.8 |
        redis3.2 | redis4.0 | redis5.0 | redis6.x | redis7.x | valkey7.x | valkey8.x
    max_records (Optional[int]): The maximum number of records to include in the response.
        If more records exist than the specified MaxRecords value, a marker is included
        in the response so that the remaining results can be retrieved.
    marker (Optional[str]): An optional marker returned from a previous request. Use this marker
        for pagination of results from this operation. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified
        by MaxRecords.

Returns:
    Dict containing information about the engine default parameters, including:
    - Parameters: List of parameters with their details
    - CacheParameterGroupFamily: The name of the cache parameter group family
    - Marker: Pagination marker for next set of results
Parameters|Type|Description
-|-|-
`cache_parameter_group_family`|`string`|
`marker`|`string` *optional*|
`max_records`|`string` *optional*|

---
#### Tool: **`describe-events`**
Returns events related to clusters, cache security groups, and parameter groups.

Parameters:
    source_type (Optional[str]): The event source to retrieve events for. If not specified, all
        events are returned. Valid values: cache-cluster | cache-parameter-group |
        cache-security-group | cache-subnet-group | replication-group | user | user-group
    source_identifier (Optional[str]): The identifier of the event source for which events are
        returned. For example, if source_type is cache-cluster, you can specify a cluster
        identifier to see all events for only that cluster.
    start_time (Optional[datetime]): The beginning of the time interval to retrieve events for,
        specified in ISO 8601 format.
    end_time (Optional[datetime]): The end of the time interval to retrieve events for,
        specified in ISO 8601 format.
    duration (Optional[int]): The number of minutes worth of events to retrieve.
    max_records (Optional[int]): The maximum number of records to include in the response.
        If more records exist than the specified MaxRecords value, a marker is included
        in the response so that the remaining results can be retrieved.
    marker (Optional[str]): An optional marker returned from a previous request. Use this marker
        for pagination of results from this operation. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified
        by MaxRecords.

Returns:
    Dict containing information about the events, including:
    - Events: List of events
    - Marker: Pagination marker for next set of results
Parameters|Type|Description
-|-|-
`duration`|`string` *optional*|
`end_time`|`string` *optional*|
`marker`|`string` *optional*|
`max_records`|`string` *optional*|
`source_identifier`|`string` *optional*|
`source_type`|`string` *optional*|
`start_time`|`string` *optional*|

---
#### Tool: **`describe-log-groups`**
Describe CloudWatch Logs log groups.
Parameters|Type|Description
-|-|-
`account_identifiers`|`string` *optional*|List of account IDs to filter log groups
`include_linked_accounts`|`string` *optional*|Whether to include log groups from linked accounts
`log_group_class`|`string` *optional*|Filter by log group class (STANDARD or INFREQUENT_ACCESS)
`log_group_identifiers`|`string` *optional*|List of log group identifiers to describe
`log_group_name_pattern`|`string` *optional*|Pattern to match log group names
`log_group_name_prefix`|`string` *optional*|Prefix to filter log groups by name
`max_items`|`string` *optional*|Maximum number of records to return in total
`page_size`|`string` *optional*|Number of records to include in each page
`starting_token`|`string` *optional*|Token for starting the list from a specific page

---
#### Tool: **`describe-log-streams`**
Describe CloudWatch Logs log streams.
Parameters|Type|Description
-|-|-
`descending`|`string` *optional*|If true, results are returned in descending order.
`log_group_identifier`|`string` *optional*|The unique identifier of the log group.
`log_group_name`|`string` *optional*|The name of the log group containing the log streams to describe.
`log_stream_name_prefix`|`string` *optional*|The prefix to match when describing log streams.
`max_items`|`string` *optional*|Maximum number of records to return in total.
`order_by`|`string` *optional*|The parameter to sort by (LogStreamName or LastEventTime).
`page_size`|`string` *optional*|Number of records to include in each page.
`starting_token`|`string` *optional*|Token for starting the list from a specific page.

---
#### Tool: **`describe-replication-groups`**
Describe one or more ElastiCache replication groups.

This tool returns information about provisioned replication groups. If a replication group ID
is specified, information about only that replication group is returned. Otherwise, information
about up to MaxRecords replication groups is returned.

Parameters:
    replication_group_id (Optional[str]): The identifier for the replication group to describe.
        If not provided, information about all replication groups is returned.
    max_records (Optional[int]): The maximum number of records to include in the response.
        If more records exist than the specified MaxRecords value, a marker is included
        in the response so that the remaining results can be retrieved.
    marker (Optional[str]): An optional marker returned from a previous request. Use this marker
        for pagination of results from this operation. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified
        by MaxRecords.

Returns:
    Dict containing information about the replication group(s), including:
    - ReplicationGroups: List of replication groups
    - Marker: Pagination marker for next set of results
Parameters|Type|Description
-|-|-
`marker`|`string` *optional*|
`max_records`|`string` *optional*|
`replication_group_id`|`string` *optional*|

---
#### Tool: **`describe-serverless-caches`**
Describe Amazon ElastiCache serverless caches in your AWS account.

This tool retrieves detailed information about serverless caches including:
- Cache configuration
- Cache endpoints
- Cache status
- Cache size
- Cache connections

Parameters:
    serverless_cache_name (Optional[str]): Name of the serverless cache to describe. If not provided, describes all caches.
    max_items (Optional[int]): Maximum number of results to return.
    starting_token (Optional[str]): Token to start the list from a specific page.
    page_size (Optional[int]): Number of records to include in each page.

Returns:
    Dict containing information about the serverless cache(s).
Parameters|Type|Description
-|-|-
`max_items`|`string` *optional*|
`page_size`|`string` *optional*|
`serverless_cache_name`|`string` *optional*|
`starting_token`|`string` *optional*

[...]

## Screenshots

![Amazon ElastiCache screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-elasticache-1.png)

![Amazon ElastiCache screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-elasticache-2.png)

![Amazon ElastiCache screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-elasticache-3.png)
