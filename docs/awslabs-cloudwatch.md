Metrics, alarms, and logs analysis.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/cloudwatch-mcp-server](https://hub.docker.com/repository/docker/mcp/cloudwatch-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (19)
Tools provided by this Server|Short Description
-|-
`analyze_log_group`|Analyzes a CloudWatch log group for anomalies, message patterns, and error patterns within a specified time window.|
`analyze_metric`|Analyzes CloudWatch metric data to determine seasonality, trend, data density and statistical properties.|
`cancel_logs_insight_query`|Cancels an ongoing CloudWatch Logs Insights query.|
`describe_log_groups`|Lists AWS CloudWatch log groups and saved queries associated with them, optionally filtering by a name prefix.|
`execute_cwl_insights_batch`|Run a CloudWatch Logs Insights query across multiple log groups, accounts, and regions.|
`execute_log_insights_query`|Executes a CloudWatch Logs Insights query and waits for the results to be available.|
`execute_promql_query`|Execute an instant PromQL query against CloudWatch.|
`execute_promql_range_query`|Execute a PromQL range query against CloudWatch.|
`get_active_alarms`|Gets all CloudWatch Alarms currently in ALARM state.|
`get_alarm_history`|Gets the history for a CloudWatch alarm with time range suggestions for investigation.|
`get_logs_insight_query_results`|Retrieves the results of a previously started CloudWatch Logs Insights query.|
`get_metric_data`|Retrieves CloudWatch metric data for a specific metric.|
`get_metric_metadata`|Gets metadata for a CloudWatch metric including description, unit and recommended statistics that can be used for metric data retrieval.|
`get_promql_label_values`|Get values for a specific PromQL label from CloudWatch.|
`get_promql_labels`|Get all label names available in CloudWatch PromQL.|
`get_promql_series`|Find time series matching label selectors in CloudWatch.|
`get_recommended_metric_alarms`|Gets recommended alarms for a CloudWatch metric.|
`recommend_indexes_account`|Triage tool: find which log groups would benefit from field indexing.|
`recommend_indexes_loggroup`|Recommend field indexes for a specific CloudWatch log group.|

---
## Tools Details

#### Tool: **`analyze_log_group`**
Analyzes a CloudWatch log group for anomalies, message patterns, and error patterns within a specified time window.

This tool performs an analysis of the specified log group by:
1. Discovering and checking log anomaly detectors associated with the log group
2. Retrieving anomalies from those detectors that fall within the specified time range
3. Identifying the top 5 most common message patterns
4. Finding the top 5 patterns containing error-related terms

Usage: Use this tool to detect anomalies and understand common patterns in your log data, particularly
focusing on error patterns that might indicate issues. This can help identify potential problems and
understand the typical behavior of your application.

Returns:
--------
A LogsAnalysisResult object containing:
    - log_anomaly_results: Information about anomaly detectors and their findings
        * anomaly_detectors: List of anomaly detectors for the log group
        * anomalies: List of anomalies that fall within the specified time range
    - top_patterns: Results of the query for most common message patterns
    - top_patterns_containing_errors: Results of the query for patterns containing error-related terms
        (error, exception, fail, timeout, fatal)
Parameters|Type|Description
-|-|-
`end_time`|`string`|ISO 8601 formatted end time for the CloudWatch Logs Insights query window (e.g., "2025-04-19T21:00:00+00:00").
`log_group_arn`|`string`|The log group arn to look for anomalies in, as returned by the describe_log_groups tools
`start_time`|`string`|ISO 8601 formatted start time for the CloudWatch Logs Insights query window (e.g., "2025-04-19T20:00:00+00:00").
`profile_name`|`string` *optional*|AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
`region`|`string` *optional*|AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.

---
#### Tool: **`analyze_metric`**
Analyzes CloudWatch metric data to determine seasonality, trend, data density and statistical properties.

This tool provides RAW DATA ONLY about historical metric data and performs analysis including:
- Seasonality detection
- Trend analysis
- Data density and publishing period
- Advanced statistical measures (min/max/median, std dev, noise)

Usage: Use this tool to get objective metric analysis data.
Parameters|Type|Description
-|-|-
`metric_name`|`string`|The name of the metric (e.g., 'CPUUtilization', 'Duration')
`namespace`|`string`|The namespace of the metric (e.g., 'AWS/EC2', 'AWS/Lambda')
`dimensions`|`array` *optional*|List of dimensions that identify the metric, each with name and value
`profile_name`|`string` *optional*|AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
`region`|`string` *optional*|AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
`statistic`|`string` *optional*|The statistic to use for the metric analysis

---
#### Tool: **`cancel_logs_insight_query`**
Cancels an ongoing CloudWatch Logs Insights query. If the query has already ended, returns an error that the given query is not running.

Usage: If a log query is started by execute_log_insights_query tool and has a polling time out, this tool can be used to cancel
it prematurely to avoid incurring additional costs.

Returns:
--------
    A LogsQueryCancelResult with a "success" key, which is True if the query was successfully cancelled.
Parameters|Type|Description
-|-|-
`query_id`|`string`|The unique ID of the ongoing query to cancel. CRITICAL: This ID is returned by the execute_log_insights_query tool.
`profile_name`|`string` *optional*|AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
`region`|`string` *optional*|AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.

---
#### Tool: **`describe_log_groups`**
Lists AWS CloudWatch log groups and saved queries associated with them, optionally filtering by a name prefix.

This tool retrieves information about log groups in the account, or log groups in accounts linked to this account as a monitoring account.
If a prefix is provided, only log groups with names starting with the specified prefix are returned.

Additionally returns any user saved queries that are associated with any of the returned log groups.

Usage: Use this tool to discover log groups that you'd retrieve or query logs from and queries that have been saved by the user.

Returns:
--------
List of log group metadata dictionaries and saved queries associated with them
   Each log group metadata contains details such as:
        - logGroupName: The name of the log group.
        - creationTime: Timestamp when the log group was created
        - retentionInDays: Retention period, if set
        - storedBytes: The number of bytes stored.
        - kmsKeyId: KMS Key Id used for data encryption, if set
        - dataProtectionStatus: Displays whether this log group has a protection policy, or whether it had one in the past, if set
        - logGroupClass: Type of log group class
        - logGroupArn: The Amazon Resource Name (ARN) of the log group. This version of the ARN doesn't include a trailing :* after the log group name.
    Any saved queries that are applicable to the returned log groups are also included.
Parameters|Type|Description
-|-|-
`account_identifiers`|`string` *optional*|When include_linked_accounts is set to True, use this parameter to specify the list of accounts to search. IMPORTANT: Only has affect if include_linked_accounts is True
`include_linked_accounts`|`string` *optional*|If the AWS account is a monitoring account, set this to True to have the tool return log groups in the accounts listed in account_identifiers.
                If this parameter is set to true and account_identifiers contains a null value, the tool returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account.
`log_group_class`|`string` *optional*|If specified, filters for only log groups of the specified class.
`log_group_name_prefix`|`string` *optional*|An exact prefix to filter log groups by name. IMPORTANT: Only log groups with names starting with this prefix will be returned.
`max_items`|`string` *optional*|The maximum number of log groups to return.
`profile_name`|`string` *optional*|AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
`region`|`string` *optional*|AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.

---
#### Tool: **`execute_cwl_insights_batch`**
Run a CloudWatch Logs Insights query across multiple log groups, accounts, and regions.

Automatically chunks log groups (max 50 per StartQuery), throttles concurrency
to 25% of account limits, retries transient failures, and splits time ranges
on 10k-record or timeout hits (up to 4 levels). Results are annotated with
_region, _logGroups, and optionally _account metadata.

For simple single-region queries on a few log groups, use execute_log_insights_query instead.

Raises:
    ValueError: If input parameters are invalid (e.g. start_time >= end_time).
Parameters|Type|Description
-|-|-
`end_time`|`string`|ISO 8601 end time (e.g. "2025-04-19T21:00:00+00:00").
`log_group_names`|`array`|List of CloudWatch log group names or ARNs to query. Use ARN format (arn:aws:logs:region:account-id:log-group:name) for cross-account/cross-region queries. These will be automatically chunked into batches of 50 per StartQuery call.
`query_string`|`string`|CloudWatch Logs Insights query string. See https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html
`regions`|`array`|List of AWS regions to query (e.g. ["us-east-1", "eu-west-1"]). The same query and log group names are executed in every region.
`start_time`|`string`|ISO 8601 start time (e.g. "2025-04-19T20:00:00+00:00").
`account_label`|`string` *optional*|Optional account identifier to annotate results with (e.g., "prod-123456789012"). Useful for cross-account queries from a monitoring account to label which source account the data came from.
`limit`|`string` *optional*|Max log events per chunk. Use this or a `| limit N` clause in the query to avoid overwhelming the agent context window.
`max_timeout`|`integer` *optional*|Max seconds to poll each chunk before giving up (default 120).
`profile_name`|`string` *optional*|AWS CLI profile name (e.g., "prod-readonly", "default"). Falls back to AWS_PROFILE env var or default credential chain.

---
#### Tool: **`execute_log_insights_query`**
Executes a CloudWatch Logs Insights query and waits for the results to be available.

IMPORTANT: The operation must include exactly one of the following parameters: log_group_names, or log_group_identifiers.

CRITICAL: The volume of returned logs can easily overwhelm the agent context window. Always include a limit in the query
(| limit 50) or using the limit parameter.

Usage: Use to query, filter, collect statistics, or find patterns in one or more log groups. For example, the following
query lists exceptions per hour.

```
filter @message like /Exception/
| stats count(*) as exceptionCount by bin(1h)
| sort exceptionCount desc
```

Returns:
--------
    A dictionary containing the final query results, including:
        - status: The current status of the query (e.g., Scheduled, Running, Complete, Failed, etc.)
        - results: A list of the actual query results if the status is Complete.
        - statistics: Query performance statistics
        - messages: Any informational messages about the query
Parameters|Type|Description
-|-|-
`end_time`|`string`|ISO 8601 formatted end time for the CloudWatch Logs Insights query window (e.g., "2025-04-19T21:00:00+00:00").
`query_string`|`string`|The query string in the Cloudwatch Log Insights Query Language. See https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html.
`start_time`|`string`|ISO 8601 formatted start time for the CloudWatch Logs Insights query window (e.g., "2025-04-19T20:00:00+00:00").
`limit`|`string` *optional*|The maximum number of log events to return. It is critical to use either this parameter or a `| limit <int>` operator in the query to avoid consuming too many tokens of the agent.
`log_group_identifiers`|`string` *optional*|The list of up to 50 logGroupIdentifiers to query. You can specify them by the log group name or ARN. If a log group that you're querying is in a source account and you're using a monitoring account, you must use the ARN. CRITICAL: Exactly one of [log_group_names, log_group_identifiers] should be non-null.
`log_group_names`|`string` *optional*|The list of up to 50 log group names to be queried. CRITICAL: Exactly one of [log_group_names, log_group_identifiers] should be non-null.
`max_timeout`|`integer` *optional*|Maximum time in second to poll for complete results before giving up
`profile_name`|`string` *optional*|AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
`region`|`string` *optional*|AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.

---
#### Tool: **`execute_promql_query`**
Execute an instant PromQL query against CloudWatch.

Returns the current value of metrics at a single point in time (instant vector).
For time series over a range, use execute_promql_range_query instead.

Use this tool when:
- The user provides a PromQL expression
- The user references OTLP-ingested metrics or labels (@resource.*, @aws.*, @instrumentation.*)
- The user asks about enriched vended AWS metrics with OTel labels
- The user wants to query by AWS resource tags (@aws.tag.*)

Use get_metric_data instead when:
- The user references classic CloudWatch namespaces/dimensions (AWS/EC2, etc.)
- The user wants Metrics Insights SQL syntax

PromQL label conventions (OTLP scope to label mapping):
- @resource.{attr} - OTel resource attributes (e.g., @resource.service.name="myservice")
- @instrumentation.{attr} - instrumentation scope (e.g., @instrumentation.@name="cloudwatch.aws/ec2")
- @datapoint.{attr} or bare - datapoint attributes / CW dimensions (e.g., InstanceId="i-xxx")
- @aws.account_id, @aws.region - AWS system labels
- @aws.tag.{Key} - AWS resource tags (e.g., @aws.tag.Environment="production", @aws.tag.Team="backend")

For enriched vended AWS metrics, use histogram functions
(OTel enrichment must be enabled first: `aws cloudwatch start-otel-enrichment`):
- histogram_avg({CPUUtilization, "@instrumentation.@name"="cloudwatch.aws/ec2"})
- histogram_sum({Invocations, FunctionName="my-func"})

Limits: max 500 series returned, 7-day range, 20s timeout.

Example queries:
- {"http.server.active_requests", "@resource.service.name"="myservice"}
- histogram_avg({CPUUtilization, "@instrumentation.@name"="cloudwatch.aws/ec2"})
- sum by ("@aws.tag.Team")(histogram_sum({Invocations, "@instrumentation.@name"="cloudwatch.aws/lambda"}))
Parameters|Type|Description
-|-|-
`query`|`string`|The PromQL query to execute
`profile_name`|`string` *optional*|AWS CLI Profile Name. Falls back to AWS_PROFILE env or default credential chain.
`region`|`string` *optional*|AWS region. Defaults to AWS_REGION env or us-east-1. PromQL is available in: us-east-1, us-west-2, eu-west-1, ap-southeast-1, ap-southeast-2.
`time`|`string` *optional*|Evaluation timestamp (RFC3339 or Unix timestamp). Defaults to current time.

---
#### Tool: **`execute_promql_range_query`**
Execute a PromQL range query against CloudWatch.

Returns time series data over a time range (matrix). Use for trend analysis and graphs.

Use this tool when:
- The user provides a PromQL expression and wants data over a time window
- The user references OTLP-ingested metrics or labels (@resource.*, @aws.*, @instrumentation.*)
- The user asks about enriched vended AWS metrics with OTel labels

Use get_metric_data instead when:
- The user references classic CloudWatch namespaces/dimensions (AWS/EC2, etc.)
- The user wants Metrics Insights SQL syntax

For enriched vended AWS metrics, use histogram functions
(OTel enrichment must be enabled first: `aws cloudwatch start-otel-enrichment`):
- histogram_avg({CPUUtilization, "@instrumentation.@name"="cloudwatch.aws/ec2"})
- histogram_sum({Errors, "@instrumentation.@name"="cloudwatch.aws/lambda", "@aws.tag.Team"="backend"})

Limits: max 500 series, max 7-day range (including lookback), 20s timeout.

Example:
    query: 'avg_over_time({"http.server.active_requests", "@resource.service.name"="myservice"}[5m])'
    start: "2024-01-01T00:00:00Z"
    end: "2024-01-01T01:00:00Z"
    step: "5m"
Parameters|Type|Description
-|-|-
`end`|`string`|End timestamp (RFC3339 or Unix timestamp)
`query`|`string`|The PromQL query to execute
`start`|`string`|Start timestamp (RFC3339 or Unix timestamp)
`step`|`string`|Query resolution step width (e.g., '60s', '5m', '1h')
`profile_name`|`string` *optional*|AWS CLI Profile Name. Falls back to AWS_PROFILE env or default credential chain.
`region`|`string` *optional*|AWS region. Defaults to AWS_REGION env or us-east-1. PromQL is available in: us-east-1, us-west-2, eu-west-1, ap-southeast-1, ap-southeast-2.

---
#### Tool: **`get_active_alarms`**
Gets all CloudWatch Alarms currently in ALARM state.

This tool retrieves all CloudWatch Alarms that are currently in the ALARM state,
including both metric alarms and composite alarms. Results are optimized for
LLM reasoning with summary-level information.

Usage: Use this tool to get an overview of all active alarms in your AWS account
for troubleshooting, monitoring, and operational awareness.
Parameters|Type|Description
-|-|-
`max_items`|`string` *optional*|Maximum number of alarms to return (default: 50). Large values may cause context window overflow and impact LLM performance.
`profile_name`|`string` *optional*|AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
`region`|`string` *optional*|AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.

---
#### Tool: **`get_alarm_history`**
Gets the history for a CloudWatch alarm with time range suggestions for investigation.

This tool retrieves the history for a specified CloudWatch alarm, focusing primarily
on state transitions to ALARM state. It also provides suggested time ranges for
investigation based on the alarm's configuration and history.

Usage: Use this tool to understand when an alarm fired and get useful time ranges
for investigating the underlying issue using other CloudWatch tools. The tool is
particularly useful for identifying patterns like alarm flapping (going in and out
of alarm state frequently).
Parameters|Type|Description
-|-|-
`alarm_name`|`string`|Name of the alarm to retrieve history for
`end_time`|`string` *optional*|The end time for the history query in ISO format (e.g., '2023-01-01T00:00:00Z') or as a datetime object. Defaults to current time.
`history_item_type`|`string` *optional*|Type of history items to retrieve. Possible values: 'ConfigurationUpdate', 'StateUpdate', 'Action'. Defaults to 'StateUpdate'.
`include_component_alarms`|`string` *optional*|For composite alarms, whether to include details about component alarms. Defaults to false.
`max_items`|`string` *optional*|Maximum number of history items to return (default: 50). Large values may cause context window overflow and impact LLM performance. Adjust time-range to limit responses.
`profile_name`|`string` *optional*|AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
`region`|`string` *optional*|AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
`start_time`|`string` *optional*|The start time for the history query in ISO format (e.g., '2023-01-01T00:00:00Z') or as a datetime object. Defaults to 24 hours ago.

---
#### Tool: **`get_logs_insight_query_results`**
Retrieves the results of a previously started CloudWatch Logs Insights query.

Usage: If a log query is started by execute_log_insights_query tool and has a polling time out, this tool can be used to try to retrieve
the query results again.

Returns:
--------
    A dictionary containing the final query results, including:
        - status: The current status of the query (e.g., Scheduled, Running, Complete, Failed, etc.)
        - results: A list of the actual query results if the status is Complete.
        - statistics: Query performance statistics
        - messages: Any informational messages about the query
Parameters|Type|Description
-|-|-
`query_id`|`string`|The unique ID of the query to retrieve the results for. CRITICAL: This ID is returned by the execute_log_insights_query tool.
`profile_name`|`string` *optional*|AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
`region`|`string` *optional*|AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.

---
#### Tool: **`get_metric_data`**
Retrieves CloudWatch metric data for a specific metric.

This tool retrieves metric data from CloudWatch for a specific metric identified by its
namespace, metric name, and dimensions, within a specified time range. It can use either
standard GetMetricData API or CloudWatch Metrics Insights for more advanced querying.

The function automatically determines whether to use standard GetMetricData or Metrics Insights
based on the parameters provided. If any Metrics Insights specific parameters are provided
(group_by_dimension, schema_dimension_keys, limit, sort_order, or order_by_statistic), it will use Metrics Insights.

When using group_by_dimension, you must include that dimension in schema_dimension_keys.

For advanced use cases, the optional `queries` parameter accepts a list of `MetricDataQueryInput`
objects and unlocks capabilities that the single-metric path cannot express: percentile statistics
(p50, p90, p99...), metric math expressions (e.g. `errors / invocations`), and multi-metric
batching (retrieving many metrics in a single API call). When `queries` is provided,
`namespace`, `metric_name`, `dimensions`, and `statistic` are not used.

`start_time` is optional; when omitted, it defaults to 3 hours before `end_time`
(which itself defaults to the current UTC time).

Usage: Use this tool to get actual metric data from CloudWatch for analysis or visualization.

Returns:
    GetMetricDataResponse: An object containing the metric data results

Example 1 (Standard GetMetricData):
    result = await get_metric_data(
        ctx,
        namespace="AWS/EC2",
        metric_name="CPUUtilization",
        start_time="2023-01-01T00:00:00Z",
        dimensions=[
            Dimension(name="InstanceId", value="i-1234567890abcdef0")
        ],
        statistic="Average"
        # Period will be auto-calculated based on time window and target_datapoints
    )

Example 2 (Metrics Insights with group by):
    result = await get_metric_data(
        ctx,
        namespace="AWS/EC2",
        metric_name="CPUUtilization",
        start_time="2023-01-01T00:00:00Z",
        end_time="2023-01-02T00:00:00Z",
        statistic="AVG",
        schema_dimension_keys=["InstanceType"],
        group_by_dimension="InstanceType"
        # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceType") GROUP BY "InstanceType"
    )

Example 3 (Metrics Insight

[...]

## Screenshots

![Amazon CloudWatch screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cloudwatch-1.png)

![Amazon CloudWatch screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cloudwatch-2.png)

![Amazon CloudWatch screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cloudwatch-3.png)
