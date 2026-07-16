Industrial IoT asset management.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-iot-sitewise-mcp-server](https://hub.docker.com/repository/docker/mcp/aws-iot-sitewise-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (41)
Tools provided by this Server|Short Description
-|-
`batch_get_asset_property_aggregates`|Get aggregated values for multiple asset properties.|
`batch_get_asset_property_value`|Get the current values for multiple asset properties.|
`batch_get_asset_property_value_hist`|Get the historical values for multiple asset properties.|
`convert_multiple_timestamps`|Convert multiple Unix epoch timestamps to human-readable format.|
`convert_unix_timestamp`|Convert Unix epoch timestamp to human-readable format.|
`create_bulk_import_schema`|Construct and validate a bulk import schema.|
`create_timestamp_range`|Create a formatted timestamp range from start and end timestamps.|
`describe_action`|Describe an action in AWS IoT SiteWise.|
`describe_asset`|Retrieve information about an asset.|
`describe_asset_model`|Retrieve information about an asset model.|
`describe_bulk_import_job`|Get detailed information about a specific bulk import job in AWS IoT SiteWise.|
`describe_computation_model`|Describe a computation model in AWS IoT SiteWise.|
`describe_computation_model_execution_summary`|Describe a computation model execution summary in AWS IoT SiteWise.|
`describe_default_encryption_config`|Retrieve information about the default encryption configuration for your AWS account.|
`describe_execution`|Describe an execution in AWS IoT SiteWise.|
`describe_gateway`|Retrieve information about a gateway.|
`describe_gateway_capability_config`|Retrieve information about a gateway capability configuration.|
`describe_logging_options`|Retrieve the current AWS IoT SiteWise logging options.|
`describe_storage_configuration`|Retrieve information about the storage configuration for your AWS account.|
`describe_time_series`|Retrieve information about a time series (data stream).|
`execute_query`|Execute comprehensive SQL queries against AWS IoT SiteWise data using the executeQuery API.|
`get_asset_property_aggregates`|Get aggregated values for an asset property.|
`get_asset_property_value`|Get the current value for the given asset property.|
`get_asset_property_value_history`|Get the history of an asset property's values.|
`get_current_timestamp`|Get the current Unix timestamp and formatted time.|
`get_interpl_asset_property_values`|Get interpolated values for an asset property for a specified time interval.|
`get_metadata_transfer_job`|Get details of a metadata transfer job.|
`get_sitewise_server_mode`|Get the current SiteWise server mode and available capabilities.|
`list_actions`|List actions for a specific target resource in AWS IoT SiteWise.|
`list_asset_model_properties`|Retrieve a paginated list of properties associated with an asset model.|
`list_asset_models`|Retrieve a paginated list of summaries for all asset models.|
`list_assets`|Retrieve a paginated list of asset summaries.|
`list_associated_assets`|Retrieve a paginated list of associated assets.|
`list_bulk_import_jobs`|List bulk import jobs in AWS IoT SiteWise.|
`list_computation_model_data_binding_usages`|Find computation models that use a given resource in data binding.|
`list_computation_model_resolve_to_resources`|List computation model resolve to resources in AWS IoT SiteWise.|
`list_computation_models`|List computation models in AWS IoT SiteWise.|
`list_executions`|List executions for a specific target resource in AWS IoT SiteWise.|
`list_gateways`|Retrieve a paginated list of gateways.|
`list_metadata_transfer_jobs`|List metadata transfer jobs.|
`list_time_series`|Retrieve a paginated list of time series (data streams).|

---
## Tools Details

#### Tool: **`batch_get_asset_property_aggregates`**
Get aggregated values for multiple asset properties.
Parameters|Type|Description
-|-|-
`entries`|`array`|The list of asset property aggregate entries for the batch get request
`max_results`|`integer` *optional*|The maximum number of results to return (1-4000)
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`region`|`string` *optional*|AWS region

---
#### Tool: **`batch_get_asset_property_value`**
Get the current values for multiple asset properties.
Parameters|Type|Description
-|-|-
`entries`|`array`|The list of asset property identifiers for the batch get request
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`region`|`string` *optional*|AWS region

---
#### Tool: **`batch_get_asset_property_value_hist`**
Get the historical values for multiple asset properties.
Parameters|Type|Description
-|-|-
`entries`|`array`|The list of asset property historical value entries for the batch get request
`max_results`|`integer` *optional*|The maximum number of results to return (1-4000)
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`region`|`string` *optional*|AWS region

---
#### Tool: **`convert_multiple_timestamps`**
Convert multiple Unix epoch timestamps to human-readable format.

This tool converts multiple timestamps at once, useful for processing
API responses that contain several timestamp fields.
Parameters|Type|Description
-|-|-
`timestamps`|`object`|Dictionary of timestamp names and values
`format_string`|`string` *optional*|Python strftime format string for output formatting

---
#### Tool: **`convert_unix_timestamp`**
Convert Unix epoch timestamp to human-readable format.

This tool provides accurate timestamp conversion to prevent AI agents from
making conversion errors when interpreting Unix timestamps from API responses.
Parameters|Type|Description
-|-|-
`timestamp`|`string`|Unix epoch timestamp (seconds since 1970-01-01)
`format_string`|`string` *optional*|Python strftime format string for output formatting
`timezone`|`string` *optional*|Timezone for conversion (currently only supports UTC)

---
#### Tool: **`create_bulk_import_schema`**
Construct and validate a bulk import schema.
Parameters|Type|Description
-|-|-
`asset_models`|`string` *optional*|List of asset model definitions. Each must include:
`assets`|`string` *optional*|List of asset definitions. Each must include:

---
#### Tool: **`create_timestamp_range`**
Create a formatted timestamp range from start and end timestamps.

This tool formats a range of timestamps for display, useful for showing
training periods, evaluation periods, or other time ranges.
Parameters|Type|Description
-|-|-
`end_timestamp`|`string`|End Unix epoch timestamp
`start_timestamp`|`string`|Start Unix epoch timestamp
`format_string`|`string` *optional*|Python strftime format string for output formatting

---
#### Tool: **`describe_action`**
Describe an action in AWS IoT SiteWise.

Retrieves detailed information about a specific action, including
its definition, payload, target resource, execution time, and resolution details.
Parameters|Type|Description
-|-|-
`action_id`|`string`|The ID of the action to describe (required)
`region`|`string` *optional*|AWS region (default: us-east-1)

---
#### Tool: **`describe_asset`**
Retrieve information about an asset.
Parameters|Type|Description
-|-|-
`asset_id`|`string`|The ID of the asset (UUID format: 12345678-1234-1234-1234-123456789012 or external ID format: externalId:my-external-id)
`exclude_properties`|`boolean` *optional*|Whether to exclude asset properties from the response
`region`|`string` *optional*|AWS region

---
#### Tool: **`describe_asset_model`**
Retrieve information about an asset model.
Parameters|Type|Description
-|-|-
`asset_model_id`|`string`|The ID of the asset model (UUID format: 12345678-1234-1234-1234-123456789012 or external ID format: externalId:my-external-id)
`asset_model_version`|`string` *optional*|The version of the asset model (LATEST, ACTIVE)
`exclude_properties`|`boolean` *optional*|Whether to exclude asset model properties
`region`|`string` *optional*|AWS region

---
#### Tool: **`describe_bulk_import_job`**
Get detailed information about a specific bulk import job in AWS IoT SiteWise.

This function retrieves comprehensive details about a bulk import job including its configuration,
status, progress, error information, and execution statistics.
Parameters|Type|Description
-|-|-
`job_id`|`string`|The ID of the bulk import job to describe (UUID format)
`region`|`string` *optional*|AWS region

---
#### Tool: **`describe_computation_model`**
Describe a computation model in AWS IoT SiteWise.

Retrieves detailed information about a specific computation model, including
its configuration, data bindings, status, and metadata.
Parameters|Type|Description
-|-|-
`computation_model_id`|`string`|The ID of the computation model to describe (required, must be in UUID format)
`computation_model_version`|`string` *optional*|Optional version of the computation model
`region`|`string` *optional*|AWS region (default: us-east-1)

---
#### Tool: **`describe_computation_model_execution_summary`**
Describe a computation model execution summary in AWS IoT SiteWise.

This tool intelligently determines whether to use resolve parameters based on the
computation model configuration:
- For Asset Model Level Configuration: Uses resolve parameters if provided to get execution summary for specific assets
- For Asset Level Configuration: Ignores resolve parameters as they're not needed (already tied to specific assets)

**Smart Optimization**: If you know the configuration type, provide it via the `configuration_type`
parameter to avoid an additional API call to describe_computation_model for type detection.
Parameters|Type|Description
-|-|-
`computation_model_id`|`string`|The ID of the computation model (required, must be in UUID format)
`configuration_type`|`string` *optional*|Optional configuration type hint to avoid auto-detection API call.
`region`|`string` *optional*|AWS region (default: us-east-1)
`resolve_to_resource_id`|`string` *optional*|Optional ID of the resolved resource (only used for asset model level configurations)
`resolve_to_resource_type`|`string` *optional*|Optional type of the resolved resource (ASSET, only used for asset model level configurations)

---
#### Tool: **`describe_default_encryption_config`**
Retrieve information about the default encryption configuration for your AWS account.
Parameters|Type|Description
-|-|-
`region`|`string` *optional*|AWS region

---
#### Tool: **`describe_execution`**
Describe an execution in AWS IoT SiteWise.

Retrieves detailed information about a specific execution, including execution details,
status, timestamps, target resource information, and execution results. This provides
comprehensive information about the execution process.
Parameters|Type|Description
-|-|-
`execution_id`|`string`|The ID of the execution to describe (required)
`region`|`string` *optional*|AWS region (default: us-east-1)

---
#### Tool: **`describe_gateway`**
Retrieve information about a gateway.
Parameters|Type|Description
-|-|-
`gateway_id`|`string`|The ID of the gateway device
`region`|`string` *optional*|AWS region

---
#### Tool: **`describe_gateway_capability_config`**
Retrieve information about a gateway capability configuration.
Parameters|Type|Description
-|-|-
`capability_namespace`|`string`|The namespace of the capability configuration
`gateway_id`|`string`|The ID of the gateway that defines the capability configuration
`region`|`string` *optional*|AWS region

---
#### Tool: **`describe_logging_options`**
Retrieve the current AWS IoT SiteWise logging options.
Parameters|Type|Description
-|-|-
`region`|`string` *optional*|AWS region

---
#### Tool: **`describe_storage_configuration`**
Retrieve information about the storage configuration for your AWS account.
Parameters|Type|Description
-|-|-
`region`|`string` *optional*|AWS region

---
#### Tool: **`describe_time_series`**
Retrieve information about a time series (data stream).
Parameters|Type|Description
-|-|-
`alias`|`string` *optional*|The alias that identifies the time series
`asset_id`|`string` *optional*|The ID of the asset in which the asset property was created
`property_id`|`string` *optional*|The ID of the asset property
`region`|`string` *optional*|AWS region

---
#### Tool: **`execute_query`**
Execute comprehensive SQL queries against AWS IoT SiteWise data using the executeQuery API.

The AWS IoT SiteWise query language supports SQL capabilities including:
- Views: asset, asset_property, raw_time_series,         latest_value_time_series, precomputed_aggregates
- SQL clauses: SELECT, FROM, WHERE, GROUP BY, ORDER BY, HAVING, LIMIT
- Functions: Aggregation, date/time, string, mathematical, conditional
- Operators: Comparison, logical, arithmetic, pattern matching (LIKE)
- JOIN operations: JOIN, LEFT JOIN,
    UNION (prefer implicit joins for performance)

Available Views and Schema (From Official AWS Documentation):

ASSET VIEW: Contains information about the asset and model derivation
- asset_id (string), asset_name (string), asset_description (string)
- asset_model_id (string), parent_asset_id (string),
    asset_external_id (string)
- asset_external_model_id (string), hierarchy_id (string)

ASSET_PROPERTY VIEW: Contains information about the asset property's structure
- asset_id (string), property_id (string), property_name (string),
    property_alias (string)
- property_external_id (string), asset_composite_model_id (string),
    property_type (string)
- property_data_type (string), int_attribute_value (integer),
    double_attribute_value (double)
- boolean_attribute_value (boolean), string_attribute_value (string)

RAW_TIME_SERIES VIEW: Contains the historical data of the time series
- asset_id (string), property_id (string), property_alias (string),
    event_timestamp (timestamp)
- quality (string), boolean_value (boolean), int_value (integer),
    double_value (double), string_value (string)

LATEST_VALUE_TIME_SERIES VIEW: Contains the latest value of the time series
- asset_id (string), property_id (string), property_alias (string),
    event_timestamp (timestamp)
- quality (string), boolean_value (boolean), int_value (integer),
    double_value (double), string_value (string)

PRECOMPUTED_AGGREGATES VIEW: Contains automatically computed         aggregated asset property values
- asset_id (string), property_id (string), property_alias (string),
    event_timestamp (timestamp)
- quality (string), resolution (string), sum_value (double),
    count_value (integer)
- average_value (double), maximum_value (double),
    minimum_value (double), stdev_value (double)

Complete SQL Function Reference (From AWS IoT SiteWise User Guide):

DATE/TIME FUNCTIONS:
- DATE_ADD(
    unit,
    value,
    date): Add time to date (e.g.,
    DATE_ADD(DAY, 7, event_timestamp))    - DATE_SUB(
    unit,
    value,
    date): Subtract time from date (e.g.,
    DATE_SUB(
        YEAR,
        2,
        event_timestamp))    - TIMESTAMP_ADD(
            unit,
            value,
            timestamp): Add time to timestamp
- TIMESTAMP_SUB(unit, value, timestamp): Subtract time from timestamp
- NOW(
    ): Current timestamp (supported,
    but use TIMESTAMP_ADD/SUB for math operations)    -             TIMESTAMP literals: Use TIMESTAMP '2023-01-01 00:00:00' for specific dates
- CAST(expression AS TIMESTAMP): Convert string to timestamp

Note: NOW() IS supported. When doing math on NOW() or         any timestamp, use TIMESTAMP_ADD/TIMESTAMP_SUB functions rather than             +/- operators.

TYPE CONVERSION FUNCTIONS:
- TO_DATE(integer): Convert epoch milliseconds to date
- TO_DATE(expression, format): Convert string to date with format
- TO_TIMESTAMP(double): Convert epoch seconds to timestamp
- TO_TIMESTAMP(string, format): Convert string to timestamp with format
- TO_TIME(int): Convert epoch milliseconds to time
- TO_TIME(string, format): Convert string to time with format
- CAST(expression AS data_type): Convert between BOOLEAN, INTEGER,
    TIMESTAMP, DATE, STRING, etc.

AGGREGATE FUNCTIONS:
- AVG(expression): Average value
- COUNT(expression): Count rows (COUNT(*) is supported)
- MAX(expression): Maximum value
- MIN(expression): Minimum value
- SUM(expression): Sum values
- STDDEV(expression): Standard deviation
- GROUP BY expression: Group results
- HAVING boolean-expression: Filter grouped results

IMPORTANT LIMITATIONS:
- Window functions, CTEs (WITH clauses), DISTINCT, SELECT *, and         ILIKE are NOT supported

SUPPORTED FEATURES:
- CASE statements (CASE WHEN...THEN...ELSE...END pattern) ARE supported
- COUNT(*) IS supported (only SELECT * is blocked)
- Use implicit JOINs for better performance when possible
Parameters|Type|Description
-|-|-
`query_statement`|`string`|SQL query statement to execute against AWS IoT SiteWise data
`max_results`|`integer` *optional*|The maximum number of results to return (1-10000)
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`region`|`string` *optional*|AWS region

---
#### Tool: **`get_asset_property_aggregates`**
Get aggregated values for an asset property.
Parameters|Type|Description
-|-|-
`aggregate_types`|`string` *optional*|The data aggregating function (AVERAGE, COUNT, MAXIMUM, MINIMUM, SUM, STANDARD_DEVIATION)
`asset_id`|`string` *optional*|The ID of the asset
`end_date`|`string` *optional*|The inclusive end of the range (ISO 8601 format)
`max_results`|`integer` *optional*|The maximum number of results to return (1-4000)
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`property_alias`|`string` *optional*|The alias that identifies the property
`property_id`|`string` *optional*|The ID of the asset property
`qualities`|`string` *optional*|The quality by which to filter asset data (GOOD, BAD, UNCERTAIN)
`region`|`string` *optional*|AWS region
`resolution`|`string` *optional*|The time interval over which to aggregate data
`start_date`|`string` *optional*|The exclusive start of the range (ISO 8601 format)
`time_ordering`|`string` *optional*|The chronological sorting order (ASCENDING, DESCENDING)

---
#### Tool: **`get_asset_property_value`**
Get the current value for the given asset property.
Parameters|Type|Description
-|-|-
`asset_id`|`string` *optional*|The ID of the asset
`property_alias`|`string` *optional*|The alias that identifies the property
`property_id`|`string` *optional*|The ID of the asset property
`region`|`string` *optional*|AWS region

---
#### Tool: **`get_asset_property_value_history`**
Get the history of an asset property's values.
Parameters|Type|Description
-|-|-
`asset_id`|`string` *optional*|The ID of the asset
`end_date`|`string` *optional*|The inclusive end of the range (ISO 8601 format)
`max_results`|`integer` *optional*|The maximum number of results to return (1-4000)
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`property_alias`|`string` *optional*|The alias that identifies the property
`property_id`|`string` *optional*|The ID of the asset property
`qualities`|`string` *optional*|The quality by which to filter asset data (GOOD, BAD, UNCERTAIN)
`region`|`string` *optional*|AWS region
`start_date`|`string` *optional*|The exclusive start of the range (ISO 8601 format)
`time_ordering`|`string` *optional*|The chronological sorting order (ASCENDING, DESCENDING)

---
#### Tool: **`get_current_timestamp`**
Get the current Unix timestamp and formatted time.

This tool provides the current timestamp in both Unix epoch format
and human-readable format, useful for reference when working with timestamps.

Returns:
    Dictionary containing current timestamp information
#### Tool: **`get_interpl_asset_property_values`**
Get interpolated values for an asset property for a specified time interval.
Parameters|Type|Description
-|-|-
`asset_id`|`string` *optional*|The ID of the asset
`end_time_in_seconds`|`string` *optional*|The inclusive end of the range (Unix epoch time in seconds)
`interpolation_type`|`string` *optional*|The interpolation type (LINEAR_INTERPOLATION, LOCF_INTERPOLATION)
`interval_in_seconds`|`integer` *optional*|The time interval in seconds over which to interpolate data
`interval_window_in_seconds`|`string` *optional*|The query interval for interpolated values
`max_results`|`integer` *optional*|The maximum number of results to return (1-250)
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`property_alias`|`string` *optional*|The alias that identifies the property
`property_id`|`string` *optional*|The ID of the asset property
`quality`|`string` *optional*|The quality of the asset property value (GOOD, BAD, UNCERTAIN)
`region`|`string` *optional*|AWS region
`start_time_in_seconds`|`string` *optional*|The exclusive start of the range (Unix epoch time in seconds)

---
#### Tool: **`get_metadata_transfer_job`**
Get details of a metadata transfer job.
Parameters|Type|Description
-|-|-
`metadata_transfer_job_id`|`string`|The metadata transfer job ID to retrieve
`region`|`string` *optional*|AWS region

---
#### Tool: **`get_sitewise_server_mode`**
Get the current SiteWise server mode and available capabilities.

This tool helps users understand what operations are available
and provides guidance for enabling write operations if needed.

Returns:
    Dictionary containing server mode information and capabilities
#### Tool: **`list_actions`**
List actions for a specific target resource in AWS IoT SiteWise.

Retrieves a paginated list of actions associated with a specific target resource.
You can filter by resolved resource and control pagination.
Parameters|Type|Description
-|-|-
`target_resource_id`|`string`|The ID of the target resource (required)
`target_resource_type`|`string`|The type of resource - ASSET or COMPUTATION_MODEL (required)
`max_results`|`string` *optional*|Optional maximum number of results to return (1-250)
`next_token`|`string` *optional*|Optional token for pagination to get the next set of results
`region`|`string` *optional*|AWS region (default: us-east-1)
`resolve_to_resource_id`|`string` *optional*|Optional ID of the resolved resource
`resolve_to_resource_type`|`string` *optional*|Optional type of the resolved resource (ASSET)

---
#### Tool: **`list_asset_model_properties`**
Retrieve a paginated list of properties associated with an asset model.
Parameters|Type|Description
-|-|-
`asset_model_id`|`string`|The ID of the asset model (UUID format: 12345678-1234-1234-1234-123456789012 or external ID format: externalId:my-external-id)
`asset_model_version`|`string` *optional*|The version of the asset model (LATEST, ACTIVE)
`filter_type`|`string` *optional*|Filter properties by type (ALL, BASE)
`max_results`|`integer` *optional*|The maximum number of results to return (1-250)
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`region`|`string` *optional*|AWS region

---
#### Tool: **`list_asset_models`**
Retrieve a paginated list of summaries for all asset models.
Parameters|Type|Description
-|-|-
`asset_model_types`|`string` *optional*|The type of asset model (ASSET_MODEL, COMPONENT_MODEL)
`max_results`|`integer` *optional*|The maximum number of results to return (1-250)
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`region`|`string` *optional*|AWS region

---
#### Tool: **`list_assets`**
Retrieve a paginated list of asset summaries.
Parameters|Type|Description
-|-|-
`asset_model_id`|`string` *optional*|The ID of the asset model by which to filter the list of assets
`filter_type`|`string` *optional*|Filter assets by ALL or TOP_LEVEL
`max_results`|`integer` *optional*|The maximum number of results to return (1-250)
`next_token`|`string` *optional*|The token to be used for the next set of paginated results
`region`|`string` *optional*|AWS region

---
#### Tool: **`list_associated_assets`**
Retrieve a paginated list of associated assets.
Parameters|Type|Description
-|-|-
`asset_id`|`string`|The ID of the asset to query (UUID format: 12345678-1234-1234-1234-123456789012 

[...]

## Screenshots

![AWS IoT SiteWise screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-iot-sitewise-1.png)

![AWS IoT SiteWise screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-iot-sitewise-2.png)

![AWS IoT SiteWise screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-iot-sitewise-3.png)
