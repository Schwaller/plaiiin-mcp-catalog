Detailed cost analysis and reporting.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/cost-explorer-mcp-server](https://hub.docker.com/repository/docker/mcp/cost-explorer-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (7)
Tools provided by this Server|Short Description
-|-
`get_cost_and_usage`|[DEPRECATED] Retrieve AWS cost and usage data.|
`get_cost_and_usage_comparisons`|[DEPRECATED] Compare AWS costs and usage between two time periods.|
`get_cost_comparison_drivers`|[DEPRECATED] Analyze what drove cost changes between two time periods.|
`get_cost_forecast`|[DEPRECATED] Retrieve AWS cost forecasts based on historical usage patterns.|
`get_dimension_values`|[DEPRECATED] Retrieve available dimension values for AWS Cost Explorer.|
`get_tag_values`|[DEPRECATED] Retrieve available tag values for AWS Cost Explorer.|
`get_today_date`|[DEPRECATED] Retrieve current date information in UTC time zone.|

---
## Tools Details

#### Tool: **`get_cost_and_usage`**
[DEPRECATED] Retrieve AWS cost and usage data.

This tool retrieves AWS cost and usage data for AWS services during a specified billing period,
with optional filtering and grouping. It dynamically generates cost reports tailored to specific needs
by specifying parameters such as granularity, billing period dates, and filter criteria.

Note: The end_date is treated as inclusive in this tool, meaning if you specify an end_date of
"2025-01-31", the results will include data for January 31st. This differs from the AWS Cost Explorer
API which treats end_date as exclusive.

IMPORTANT: When using UsageQuantity metric, AWS aggregates usage numbers without considering units.
This makes results meaningless when different usage types have different units (e.g., EC2 compute hours
vs data transfer GB). For meaningful UsageQuantity results, you MUST be very specific with filtering, including USAGE_TYPE or USAGE_TYPE_GROUP.

Example: Get monthly costs for EC2 and S3 services in us-east-1 for May 2025
    await get_cost_and_usage(
        ctx=context,
        date_range={
            "start_date": "2025-05-01",
            "end_date": "2025-05-31"
        },
        granularity="MONTHLY",
        group_by={"Type": "DIMENSION", "Key": "SERVICE"},
        filter_expression={
            "And": [
                {
                    "Dimensions": {
                        "Key": "SERVICE",
                        "Values": ["Amazon Elastic Compute Cloud - Compute", "Amazon Simple Storage Service"],
                        "MatchOptions": ["EQUALS"]
                    }
                },
                {
                    "Dimensions": {
                        "Key": "REGION",
                        "Values": ["us-east-1"],
                        "MatchOptions": ["EQUALS"]
                    }
                }
            ]
        },
        metric="UnblendedCost"
    )

Example: Get meaningful UsageQuantity for specific EC2 instance usage
    await get_cost_and_usage(
        ctx=context,
        {
        "date_range": {
            "start_date": "2025-05-01",
            "end_date": "2025-05-31"
        },
        "filter_expression": {
            "And": [
            {
                "Dimensions": {
                "Values": [
                    "Amazon Elastic Compute Cloud - Compute"
                ],
                "Key": "SERVICE",
                "MatchOptions": [
                    "EQUALS"
                ]
                }
            },
            {
                "Dimensions": {
                "Values": [
                    "EC2: Running Hours"
                ],
                "Key": "USAGE_TYPE_GROUP",
                "MatchOptions": [
                    "EQUALS"
                ]
                }
            }
            ]
        },
        "metric": "UsageQuantity",
        "group_by": "USAGE_TYPE",
        "granularity": "MONTHLY"
        }
Parameters|Type|Description
-|-|-
`date_range`|`string`|The billing period start and end dates in YYYY-MM-DD format (end date is inclusive)
`filter_expression`|`string` *optional*|Filter criteria as a Python dictionary to narrow down AWS costs. Supports filtering by Dimensions (SERVICE, REGION, etc.), Tags, or CostCategories. You can use logical operators (And, Or, Not) for complex filters. MatchOptions validation: For Dimensions, valid values are ['EQUALS', 'CASE_SENSITIVE']. For Tags and CostCategories, valid values are ['EQUALS', 'ABSENT', 'CASE_SENSITIVE'] (defaults to EQUALS and CASE_SENSITIVE). Examples: 1) Simple service filter: {'Dimensions': {'Key': 'SERVICE', 'Values': ['Amazon Elastic Compute Cloud - Compute', 'Amazon Simple Storage Service'], 'MatchOptions': ['EQUALS']}}. 2) Region filter: {'Dimensions': {'Key': 'REGION', 'Values': ['us-east-1'], 'MatchOptions': ['EQUALS']}}. 3) Combined filter: {'And': [{'Dimensions': {'Key': 'SERVICE', 'Values': ['Amazon Elastic Compute Cloud - Compute'], 'MatchOptions': ['EQUALS']}}, {'Dimensions': {'Key': 'REGION', 'Values': ['us-east-1'], 'MatchOptions': ['EQUALS']}}]}.
`granularity`|`string` *optional*|The granularity at which cost data is aggregated. Valid values are DAILY, MONTHLY, HOURLY. If not provided, defaults to MONTHLY.
`group_by`|`string` *optional*|Either a dictionary with Type and Key for grouping costs, or simply a string key to group by (which will default to DIMENSION type). Example dictionary: {'Type': 'DIMENSION', 'Key': 'SERVICE'}. Example string: 'SERVICE'.
`metric`|`string` *optional*|The metric to return in the query. Valid values are AmortizedCost, BlendedCost, NetAmortizedCost, NetUnblendedCost, UnblendedCost, UsageQuantity. IMPORTANT: For UsageQuantity, the service aggregates usage numbers without considering units, making results meaningless when mixing different unit types (e.g., compute hours + data transfer GB). To get meaningful UsageQuantity metrics, you MUST filter by USAGE_TYPE or group by USAGE_TYPE/USAGE_TYPE_GROUP to ensure consistent units.

---
#### Tool: **`get_cost_and_usage_comparisons`**
[DEPRECATED] Compare AWS costs and usage between two time periods.

This tool compares cost and usage data between a baseline period and a comparison period,
providing percentage changes and absolute differences. Both periods must be exactly one month
and start/end on the first day of a month. The tool also provides detailed cost drivers
when available, showing what specific factors contributed to cost changes.

Important requirements:
- Both periods must be exactly one month duration
- Dates must start and end on the first day of a month (e.g., 2025-01-01 to 2025-02-01)
- Maximum lookback of 13 months (38 months if multi-year data enabled)
- Start dates must be equal to or no later than current date

Example: Compare January 2025 vs December 2024 EC2 costs
    await get_cost_and_usage_comparisons(
        ctx=context,
        baseline_date_range={
            "start_date": "2024-12-01",  # December 2024
            "end_date": "2025-01-01"
        },
        comparison_date_range={
            "start_date": "2025-01-01",  # January 2025
            "end_date": "2025-02-01"
        },
        metric_for_comparison="UnblendedCost",
        group_by={"Type": "DIMENSION", "Key": "SERVICE"},
        filter_expression={
            "Dimensions": {
                "Key": "SERVICE",
                "Values": ["Amazon Elastic Compute Cloud - Compute"],
                "MatchOptions": ["EQUALS"]
            }
        }
    )
Parameters|Type|Description
-|-|-
`baseline_date_range`|`string`|The reference period for comparison (exactly one month)
`comparison_date_range`|`string`|The comparison period (exactly one month)
`filter_expression`|`string` *optional*|Filter criteria as a Python dictionary to narrow down AWS cost comparisons. Supports filtering by Dimensions (SERVICE, REGION, etc.), Tags, or CostCategories. You can use logical operators (And, Or, Not) for complex filters. Same format as get_cost_and_usage filter_expression.
`group_by`|`string` *optional*|Either a dictionary with Type and Key for grouping comparisons, or simply a string key to group by (which will default to DIMENSION type). Example dictionary: {'Type': 'DIMENSION', 'Key': 'SERVICE'}. Example string: 'SERVICE'.
`metric_for_comparison`|`string` *optional*|The cost and usage metric to compare. Valid values are AmortizedCost, BlendedCost, NetAmortizedCost, NetUnblendedCost, UnblendedCost, UsageQuantity.

---
#### Tool: **`get_cost_comparison_drivers`**
[DEPRECATED] Analyze what drove cost changes between two time periods.

This tool provides detailed analysis of the TOP 10 most significant cost drivers
that caused changes between periods. AWS returns only the most impactful drivers
to focus on the changes that matter most for cost optimization.

The tool provides rich insights including:
- Top 10 most significant cost drivers across all services (or filtered subset)
- Specific usage types that drove changes (e.g., "BoxUsage:c5.large", "NatGateway-Hours")
- Multiple driver types: usage changes, savings plan impacts, enterprise discounts, support fees
- Both cost and usage quantity changes with units (hours, GB-months, etc.)
- Context about what infrastructure components changed
- Detailed breakdown of usage patterns vs pricing changes

Can be used with or without filters:
- Without filters: Shows top 10 cost drivers across ALL services
- With filters: Shows top 10 cost drivers within the filtered scope
- Multiple services: Can filter to multiple services and get top 10 within that scope

Both periods must be exactly one month and start/end on the first day of a month.

Important requirements:
- Both periods must be exactly one month duration
- Dates must start and end on the first day of a month (e.g., 2025-01-01 to 2025-02-01)
- Maximum lookback of 13 months (38 months if multi-year data enabled)
- Start dates must be equal to or no later than current date
- Results limited to top 10 most significant drivers (no pagination)

Example: Analyze top 10 cost drivers across all services
    await get_cost_comparison_drivers(
        ctx=context,
        baseline_date_range={
            "start_date": "2024-12-01",  # December 2024
            "end_date": "2025-01-01"
        },
        comparison_date_range={
            "start_date": "2025-01-01",  # January 2025
            "end_date": "2025-02-01"
        },
        metric_for_comparison="UnblendedCost",
        group_by={"Type": "DIMENSION", "Key": "SERVICE"}
        # No filter = top 10 drivers across all services
    )

Example: Analyze top 10 cost drivers for specific services
    await get_cost_comparison_drivers(
        ctx=context,
        baseline_date_range={
            "start_date": "2024-12-01",
            "end_date": "2025-01-01"
        },
        comparison_date_range={
            "start_date": "2025-01-01",
            "end_date": "2025-02-01"
        },
        metric_for_comparison="UnblendedCost",
        group_by={"Type": "DIMENSION", "Key": "SERVICE"},
        filter_expression={
            "Dimensions": {
                "Key": "SERVICE",
                "Values": ["Amazon Elastic Compute Cloud - Compute", "Amazon Simple Storage Service"],
                "MatchOptions": ["EQUALS"]
            }
        }
    )
Parameters|Type|Description
-|-|-
`baseline_date_range`|`string`|The reference period for comparison (exactly one month)
`comparison_date_range`|`string`|The comparison period (exactly one month)
`filter_expression`|`string` *optional*|Filter criteria as a Python dictionary to narrow down AWS cost driver analysis. Supports filtering by Dimensions (SERVICE, REGION, etc.), Tags, or CostCategories. You can use logical operators (And, Or, Not) for complex filters. Same format as get_cost_and_usage filter_expression.
`group_by`|`string` *optional*|Either a dictionary with Type and Key for grouping driver analysis, or simply a string key to group by (which will default to DIMENSION type). Example dictionary: {'Type': 'DIMENSION', 'Key': 'SERVICE'}. Example string: 'SERVICE'.
`metric_for_comparison`|`string` *optional*|The cost and usage metric to analyze drivers for. Valid values are AmortizedCost, BlendedCost, NetAmortizedCost, NetUnblendedCost, UnblendedCost, UsageQuantity.

---
#### Tool: **`get_cost_forecast`**
[DEPRECATED] Retrieve AWS cost forecasts based on historical usage patterns.

This tool generates cost forecasts for future periods using AWS Cost Explorer's machine learning models.
Forecasts are based on your historical usage patterns and can help with budget planning and cost optimization.

Important granularity limits:
- DAILY forecasts: Maximum 3 months into the future
- MONTHLY forecasts: Maximum 12 months into the future

Note: The forecast start date must be equal to or no later than the current date, while the end date
must be in the future. AWS automatically uses available historical data to generate forecasts.
Forecasts return total costs and cannot be grouped by dimensions like services or regions.

Example: Get monthly cost forecast for EC2 services for next quarter
    await get_cost_forecast(
        ctx=context,
        date_range={
            "start_date": "2025-06-19",  # Today or earlier
            "end_date": "2025-09-30"     # Future date
        },
        granularity="MONTHLY",
        filter_expression={
            "Dimensions": {
                "Key": "SERVICE",
                "Values": ["Amazon Elastic Compute Cloud - Compute"],
                "MatchOptions": ["EQUALS"]
            }
        },
        metric="UNBLENDED_COST",
        prediction_interval_level=80
    )
Parameters|Type|Description
-|-|-
`date_range`|`string`|The forecast period dates in YYYY-MM-DD format (start_date <= today, end_date > today)
`filter_expression`|`string` *optional*|Filter criteria as a Python dictionary to narrow down AWS cost forecasts. Supports filtering by Dimensions (SERVICE, REGION, etc.), Tags, or CostCategories. You can use logical operators (And, Or, Not) for complex filters. Same format as get_cost_and_usage filter_expression.
`granularity`|`string` *optional*|The granularity at which forecast data is aggregated. Valid values are DAILY and MONTHLY. DAILY forecasts support up to 3 months, MONTHLY forecasts support up to 12 months. If not provided, defaults to MONTHLY.
`metric`|`string` *optional*|The metric to forecast. Valid values are AMORTIZED_COST,BLENDED_COST,NET_AMORTIZED_COST,NET_UNBLENDED_COST,UNBLENDED_COST. Note: UsageQuantity forecasting is not supported by AWS Cost Explorer.
`prediction_interval_level`|`integer` *optional*|The confidence level for the forecast prediction interval. Valid values are 80 and 95. Higher values provide wider confidence ranges.

---
#### Tool: **`get_dimension_values`**
[DEPRECATED] Retrieve available dimension values for AWS Cost Explorer.

This tool retrieves all available and valid values for a specified dimension (e.g., SERVICE, REGION)
over a period of time. This is useful for validating filter values or exploring available options
for cost analysis.
Parameters|Type|Description
-|-|-
`date_range`|`string`|The billing period start and end dates in YYYY-MM-DD format
`dimension`|`string`|The dimension key to retrieve values for (e.g., SERVICE, REGION, LINKED_ACCOUNT)

---
#### Tool: **`get_tag_values`**
[DEPRECATED] Retrieve available tag values for AWS Cost Explorer.

This tool retrieves all available values for a specified tag key over a period of time.
This is useful for validating tag filter values or exploring available tag options for cost analysis.
Parameters|Type|Description
-|-|-
`date_range`|`string`|The billing period start and end dates in YYYY-MM-DD format
`tag_key`|`string`|The tag key to retrieve values for

---
#### Tool: **`get_today_date`**
[DEPRECATED] Retrieve current date information in UTC time zone.

This tool retrieves the current date in YYYY-MM-DD format and the current month in YYYY-MM format.
It's useful for calculating relevant dates when a user asks about the last N months/days.

## Screenshots

![AWS Cost Explorer screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cost-explorer-1.png)

![AWS Cost Explorer screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cost-explorer-2.png)

![AWS Cost Explorer screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cost-explorer-3.png)
