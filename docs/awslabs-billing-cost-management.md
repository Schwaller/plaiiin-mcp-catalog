Billing and cost management.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/billing-cost-management-mcp-server](https://hub.docker.com/repository/docker/mcp/billing-cost-management-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (33)
Tools provided by this Server|Short Description
-|-
`aws-pricing`|Comprehensive AWS pricing analysis tool that provides access to AWS service pricing information and cost analysis capabilities.|
`bcm-pricing-calc`|Allows working with workload estimates using the AWS Billing and Cost Management Pricing Calculator API.|
`budgets`|Retrieves AWS budget information using the AWS Budgets API.|
`compute-optimizer`|Retrieves recommendations from AWS Compute Optimizer.|
`cost-anomaly`|Retrieves AWS cost anomalies using the Cost Explorer GetAnomalies API.|
`cost-comparison`|Retrieves AWS cost comparisons between two one-month periods.|
`cost-explorer`|Retrieves AWS cost and usage data using the Cost Explorer API.|
`cost-optimization`|Retrieves cost optimization recommendations from AWS Cost Optimization Hub.|
`describe-cost-category-definition`|Returns the full definition of a cost category using the DescribeCostCategoryDefinition API.|
`free-tier-usage`|Retrieves AWS Free Tier usage information using the Free Tier Usage API.|
`get-billing-group-cost-report`|Retrieves the margin summary report for a specific billing group, which includes the AWS cost and charged amount (pro forma cost) broken down by attributes such as AWS service name or billing period.|
`get-billing-view`|Returns the metadata associated to the specified billing view ARN.|
`get-resource-policy`|Returns the resource-based policy document attached to the resource in JSON format.|
`list-account-associations`|Lists linked accounts associated with the payer account from AWS Billing Conductor.|
`list-billing-group-cost-reports`|Retrieves a summary report of actual AWS charges and calculated AWS charges based on the associated pricing plan of a billing group.|
`list-billing-groups`|Retrieves a list of billing groups from AWS Billing Conductor.|
`list-billing-views`|Lists the billing views available for a given time period.|
`list-cost-allocation-tag-backfill-history`|Retrieves the history of cost allocation tag backfill requests using the ListCostAllocationTagBackfillHistory API.|
`list-cost-allocation-tags`|Lists cost allocation tags in the account using the ListCostAllocationTags API.|
`list-cost-category-definitions`|Lists all cost category definitions in the account using the ListCostCategoryDefinitions API.|
`list-custom-line-item-versions`|Retrieves a list of versions for a specific custom line item from AWS Billing Conductor.|
`list-custom-line-items`|Retrieves a list of custom line items (FFLIs) from AWS Billing Conductor.|
`list-pricing-plans`|Retrieves a list of pricing plans from AWS Billing Conductor.|
`list-pricing-plans-for-rule`|Lists the pricing plans associated with a specific pricing rule.|
`list-pricing-rules`|Retrieves a list of pricing rules from AWS Billing Conductor.|
`list-pricing-rules-for-plan`|Lists the pricing rules associated with a specific pricing plan.|
`list-resources-associated-to-custom-line-item`|Lists the resources associated to a custom line item from AWS Billing Conductor.|
`list-source-views-for-billing-view`|Lists the source views (managed AWS billing views) that a custom billing view is built from.|
`rec-details`|Get detailed cost optimization recommendation with integrated data from multiple AWS services.|
`ri-performance`|Retrieves AWS Reserved Instance (RI) coverage and utilization data using the Cost Explorer API.|
`session-sql`|Execute SQL queries on the persistent session database.|
`sp-performance`|Tool that retrieves AWS Savings Plans coverage and utilization data using the Cost Explorer API.|
`storage-lens`|Query S3 Storage Lens metrics data using Athena SQL.|

---
## Tools Details

#### Tool: **`aws-pricing`**
Comprehensive AWS pricing analysis tool that provides access to AWS service pricing information and cost analysis capabilities.

This tool supports four main operations:
1. get_service_codes: Get a comprehensive list of AWS service codes from the AWS Price List API
2. get_service_attributes: Get filterable attributes for a specific AWS service's pricing
3. get_attribute_values: Get all valid values for a specific attribute of an AWS service
4. get_pricing_from_api: Get detailed pricing information from AWS Price List API with optional filters

USE THE OPERATIONS IN THIS ORDER:
1. get_service_codes: Entry point - discover available AWS services and their unique service codes. Note that service codes may not match your expectations, so it's best to get service codes first.
2. get_service_attributes: Second step - understand which dimensions affect pricing for a chosen service
3. get_attribute_values: Third step - get possible values you can use in pricing filters
4. get_pricing_from_api: Final step - retrieve actual pricing data based on service and filters
**If you deviate from this order of operations, you will struggle to form the correct filters, and you will not get results from the API**

IMPORTANT GUIDELINES:
- When retrieving foundation model pricing, always use the latest models for comparison
- For database compatibility with services, only include confirmed supported databases
- Providing less information is better than giving incorrect information
- Price list APIs can return large data volumes. Use narrower filters to retrieve less data when possible
- Service codes often differ from AWS console names (e.g., 'AmazonES' for OpenSearch)
Parameters|Type|Description
-|-|-
`operation`|`string`|The pricing operation to perform ('get_service_codes', 'get_service_attributes', 'get_attribute_values', 'get_pricing_from_api')
`attribute_name`|`string` *optional*|Attribute name (e.g., 'instanceType', 'location', 'storageClass'). Required for get_attribute_values operation.
`filters`|`string` *optional*|Optional filters for pricing queries as a JSON string. Format: '{"instanceType": "t3.medium", "location": "US East (N. Virginia)"}'
`max_results`|`string` *optional*|Maximum number of results to return (optional)
`service_code`|`string` *optional*|AWS service code (e.g., 'AmazonEC2', 'AmazonS3', 'AmazonES'). Required for get_service_attributes, get_attribute_values, and get_pricing_from_api operations.

---
#### Tool: **`bcm-pricing-calc`**
Allows working with workload estimates using the AWS Billing and Cost Management Pricing Calculator API.

IMPORTANT USAGE GUIDELINES:
- Always first check the rate preference setting for the authorized principal by calling the get_preferences operation.
- DO NOT state assumptions about Free Tier API

USE THIS TOOL FOR:
- Listing available **workload estimates** for the logged in account.
- **Filter list of available workload estimates** using name, status, created date, or expiration date.
- Get **details of a workload estimate**.
- Get the list of **services, usage type, operation, and usage amount** modeled within a workload estimate.
- Get **rate preferences** set for Pricing Calculator. These rate preferences denote what rate preferences can be used by each account type in your organization.

## OPERATIONS

1) list_workload_estimates - list of available workload estimates
   Required: operation="list_workload_estimates"
   Optional: created_after, created_before, expires_after, expires_before, status_filter, name_filter, name_match_option, next_token, max_results
   Returns: List of all workload estimates for the account.

2) get_workload_estimate - get details of a workload estimate
   Required: operation="get_workload_estimate", identifier
   Returns: Details of a specific workload estimate.

3) list_workload_estimate_usage - list of modeled usage lines within a workload estimate
   Required: operation="get_workload_estimate", identifier
   Optional: usage_account_id_filter, service_code_filter, usage_type_filter, operation_filter, location_filter, usage_group_filter, next_token, max_results
   Returns: List of usage associated with a workload estimate.

4) get_preferences - get the rate preferences available to an account
   Required: operation="get_preferences"
   Returns: Retrieves the current preferences for AWS Billing and Cost Management Pricing Calculator.
Parameters|Type|Description
-|-|-
`operation`|`string`|
`created_after`|`string` *optional*|
`created_before`|`string` *optional*|
`expires_after`|`string` *optional*|
`expires_before`|`string` *optional*|
`identifier`|`string` *optional*|
`location_filter`|`string` *optional*|
`max_pages`|`string` *optional*|
`max_results`|`string` *optional*|
`name_filter`|`string` *optional*|
`name_match_option`|`string` *optional*|
`next_token`|`string` *optional*|
`operation_filter`|`string` *optional*|
`service_code_filter`|`string` *optional*|
`status_filter`|`string` *optional*|
`usage_account_id_filter`|`string` *optional*|
`usage_group_filter`|`string` *optional*|
`usage_type_filter`|`string` *optional*|

---
#### Tool: **`budgets`**
Retrieves AWS budget information using the AWS Budgets API.

This tool uses the DescribeBudgets API to retrieve all budgets for an account.

The API returns information about:
- Budget names, types, and time periods
- Budget limits (amount and unit)
- Current actual spend
- Forecasted spend
- Cost filters applied to budgets

With this information, you can determine which budgets have been exceeded or are projected to exceed their limits.

The tool automatically retrieves the AWS account ID of the calling identity or uses the provided account_id.
Parameters|Type|Description
-|-|-
`account_id`|`string` *optional*|Optional AWS account ID. If not provided, it will be retrieved automatically.
`budget_name`|`string` *optional*|Optional budget name filter. If provided, only returns information for the specified budget.
`max_results`|`integer` *optional*|Maximum number of results to return. Defaults to 100.

---
#### Tool: **`compute-optimizer`**
Retrieves recommendations from AWS Compute Optimizer.

IMPORTANT USAGE GUIDELINES:
- Focus on recommendations with the highest estimated savings first
- Include all relevant details when presenting specific recommendations

USE THIS TOOL FOR:
- **Performance optimization** (CPU, memory, network utilization analysis)
- **Performance-based rightsizing** (not cost-based)

DO NOT USE FOR: Cost optimization or idle detection (use cost-optimization-hub)

**Note:** Compute Optimizer is a regional service. Specify a `region` to get recommendations for resources in that region. If omitted, defaults to AWS_REGION env var or us-east-1.

This tool supports the following operations:
1. get_ec2_instance_recommendations: Get recommendations for EC2 instances
2. get_auto_scaling_group_recommendations: Get recommendations for Auto Scaling groups
3. get_ebs_volume_recommendations: Get recommendations for EBS volumes
4. get_lambda_function_recommendations: Get recommendations for Lambda functions
5. get_rds_recommendations: Get recommendations for RDS instances
6. get_ecs_service_recommendations: Get recommendations for ECS services

Each operation can be filtered by AWS account IDs, regions, finding types, and more.

Common finding types include:
- UNDERPROVISIONED: The resource doesn't have enough capacity
- OVERPROVISIONED: The resource has excess capacity and could be downsized
- OPTIMIZED: The resource is already optimized
- NOT_OPTIMIZED: The resource can be optimized but specific finding type isn't available
Parameters|Type|Description
-|-|-
`operation`|`string`|The operation to perform (e.g., 'get_ec2_instance_recommendations')
`account_ids`|`string` *optional*|Optional list of AWS account IDs as JSON array string
`filters`|`string` *optional*|Optional filter expression as JSON string
`max_results`|`string` *optional*|Maximum number of results to return (1-100)
`next_token`|`string` *optional*|Optional pagination token from a previous response
`region`|`string` *optional*|AWS region to query (e.g., 'us-west-2'). Defaults to AWS_REGION env var or us-east-1.

---
#### Tool: **`cost-anomaly`**
Retrieves AWS cost anomalies using the Cost Explorer GetAnomalies API.

This tool allows you to retrieve cost anomalies detected on your AWS account during a specified time period.
Anomalies are available for up to 90 days.

You can filter anomalies by:
- Date range (required)
- Monitor ARN (optional)
- Feedback status (optional)
- Total impact (optional)

Note: Both start_date and end_date are INCLUSIVE. To get anomalies including today, use today's date as end_date.

Feedback status options:
- YES: Anomalies marked as accurate
- NO: Anomalies marked as inaccurate
- PLANNED_ACTIVITY: Anomalies marked as planned activities
Parameters|Type|Description
-|-|-
`end_date`|`string`|End date in YYYY-MM-DD format (inclusive — use today's date to include today's anomalies). Required.
`start_date`|`string`|Start date in YYYY-MM-DD format (inclusive). Required.
`feedback`|`string` *optional*|Optional filter for anomalies by feedback status (YES, NO, PLANNED_ACTIVITY).
`max_results`|`string` *optional*|Optional maximum number of results to return.
`monitor_arn`|`string` *optional*|Optional ARN of a specific cost anomaly monitor to filter results.
`total_impact_end`|`string` *optional*|Optional end value for total impact filter (required when using BETWEEN operator).
`total_impact_operator`|`string` *optional*|Optional numeric operator for filtering by total impact (EQUAL, GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, BETWEEN).
`total_impact_start`|`string` *optional*|Optional start value for total impact filter.

---
#### Tool: **`cost-comparison`**
Retrieves AWS cost comparisons between two one-month periods.

Do not use this tool except for comparing the costs of one month to the costs of another month. This tool should not be used for week-over-week or quarter-over-quarter (e.g., comparing Q2 vs. Q1) analysis.

USE THIS TOOL ONLY FOR:
- **Month-to-month cost variance analysis** (e.g., January vs February)
- **Root cause analysis** of cost changes between specific months
- **Detailed cost driver identification** (what exactly caused the cost change)
- **Service-level impact analysis** for month-over-month changes
- **Executive reporting** on monthly cost variances

STRICT LIMITATIONS:
- ONLY compares exactly one month to another month
- Both periods must start on 1st day of month, end on 1st day of next month
- Cannot compare weeks, quarters, or custom periods
- DO NOT USE for general cost analysis or flexible time periods

This tool supports two main operations:
1. getCostAndUsageComparisons: Compare costs between two time periods with flexible grouping and filtering
2. getCostComparisonDrivers: Identify key factors driving cost changes between two time periods

Both operations require:
- BaselineTimePeriod: Earlier time period for comparison (must be exactly one month)
- ComparisonTimePeriod: Later time period for comparison (must be exactly one month)
- MetricForComparison: The cost metric to compare (e.g., BlendedCost, UnblendedCost)

Supported metrics for comparison include:
- AmortizedCost: Costs with upfront and recurring reservation fees spread across the period
- BlendedCost: Average cost of all usage throughout the billing period
- NetAmortizedCost: Amortized cost after discounts
- NetUnblendedCost: Unblended cost after discounts
- NormalizedUsageAmount: Normalized usage amount
- UnblendedCost: Actual costs incurred during the specified period
- UsageQuantity: Usage amounts in their respective units

You can group results by dimensions such as:
- SERVICE: AWS service (e.g., Amazon EC2, Amazon S3)
- LINKED_ACCOUNT: Member accounts in an organization
- REGION: AWS Region
- USAGE_TYPE: Type of usage (e.g., BoxUsage:t2.micro)
- INSTANCE_TYPE: EC2 instance type (e.g., t2.micro, m5.large)
- PLATFORM: Operating system (e.g., Windows, Linux)
- TENANCY: Instance tenancy (e.g., shared, dedicated)
- RECORD_TYPE: Record type (e.g., Usage, Credit, Tax)
- LEGAL_ENTITY_NAME: AWS seller of record

Note:
- Time periods must start and end on the first day of a month, with a duration of exactly one month
- The getCostComparisonDrivers operation automatically includes SERVICE and USAGE_TYPE dimensions
- Data is available for the last 13 months, or up to 38 months if multi-year data is enabled
Parameters|Type|Description
-|-|-
`baseline_end_date`|`string`|Baseline period end date in YYYY-MM-DD format (must be first day of next month)
`baseline_start_date`|`string`|Baseline period start date in YYYY-MM-DD format (must be first day of month)
`comparison_end_date`|`string`|Comparison period end date in YYYY-MM-DD format (must be first day of next month)
`comparison_start_date`|`string`|Comparison period start date in YYYY-MM-DD format (must be first day of month)
`metric_for_comparison`|`string`|The cost metric to compare (e.g., BlendedCost, UnblendedCost, AmortizedCost)
`operation`|`string`|The operation to perform: 'getCostAndUsageComparisons' or 'getCostComparisonDrivers'
`billing_view_arn`|`string` *optional*|Optional ARN of a specific billing view
`filter`|`string` *optional*|Optional filter to apply to the results as a JSON string
`group_by`|`string` *optional*|Optional grouping of results as a JSON string (e.g., '[{"Type": "DIMENSION", "Key": "SERVICE"}]')
`max_results`|`string` *optional*|Maximum number of results to return (default: 10, max: 2000 for comparisons, max: 10 for drivers)

---
#### Tool: **`cost-explorer`**
Retrieves AWS cost and usage data using the Cost Explorer API.

IMPORTANT USAGE GUIDELINES:
- Use UnblendedCost metric by default (not BlendedCost) unless user specifies otherwise
- Exclude record_types 'Credit' and 'Refund' by default unless user requests inclusion
- Choose DAILY granularity for periods <3 months, MONTHLY for longer periods
- Start with high-level dimensions (SERVICE, LINKED_ACCOUNT) before detailed ones
- Always remember that the end_date is exclusive

USE THIS TOOL FOR:
- **Historical cost trends** and spending analysis (any time period)
- **Usage pattern analysis** over time
- **Cost breakdown** by service, account, region, or any dimension
- **Forecasting** future costs and usage
- **Resource-level cost analysis** (last 14 days)
- **Multi-dimensional cost analysis** with complex grouping

## OPERATIONS

1) getCostAndUsage — account-level historical cost/usage
   Required: operation="getCostAndUsage", start_date, end_date, granularity, metrics
   Optional: group_by, filter, next_token, max_pages, billing_view_arn
   Example: {"operation": "getCostAndUsage", "start_date": "2024-01-01", "end_date": "2024-02-01", "granularity": "DAILY", "metrics": ["UnblendedCost"], "group_by": "[{"Type": "DIMENSION", "Key": "SERVICE"}]"}

2. getCostAndUsageWithResources - Resource-level cost data (limited to last 14 days)
   Required: operation="getCostAndUsageWithResources", filter, granularity, start_date, end_date
   Optional: metrics, group_by, next_token, max_pages, billing_view_arn
   Notes: RESOURCE_ID must be included in either filter OR group_by parameters. This operation is limited to past 14 days of data from current date. Hourly granularity is only available for EC2-Instances resource-level data. All other resource-level data is available at daily granularity.
   Example: {"operation": "getCostAndUsageWithResources", "start_date": "2025-08-07", "end_date": "2025-08-21", "granularity": "DAILY", "filter": "{"Dimensions": {"Key": "SERVICE", "Values": ["Amazon Elastic Compute Cloud - Compute"]}}", "group_by": "[{"Type": "DIMENSION", "Key": "RESOURCE_ID"}]"}
   Returns: Cost data with resource-level granularity

3. getDimensionValues - List of available values for specified dimension
   Required: operation="getDimensionValues", dimension, start_date, end_date
   Optional: context, search_string, filter, max_results, billing_view_arn
   Example: {"operation": "getDimensionValues", "dimension": "SERVICE", "start_date": "2024-01-01", "end_date": "2024-02-01"}
   Returns: List of values for specified dimension with automatic pagination

4. getCostForecast - Future cost projections
   Required: operation="getCostForecast", metric, granularity, start_date, end_date
   Optional: filter, prediction_interval_level, billing_view_arn
   Example: {"operation": "getCostForecast", "metric": "UNBLENDED_COST", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22"}
   Notes: metric value for this operation should be in all caps
   Returns: Cost forecast for specified time period and granularity

5. getUsageForecast - Future usage projections
   Required: operation="getUsageForecast", metric, granularity, start_date, end_date, filter
   Optional: prediction_interval_level, billing_view_arn
   Example 1: {"operation": "getUsageForecast", "metric": "USAGE_QUANTITY", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22", "filter": "{"Dimensions": {"Key": "USAGE_TYPE_GROUP", "Values": ["EC2-Instance"]}}"}
   Example 2: {"operation": "getUsageForecast", "metric": "USAGE_QUANTITY", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22", "filter": "{"And": [{"Dimensions": {"Key": "SERVICE", "Values": ["Amazon Elastic Compute Cloud - Compute"]}}, {"Dimensions": {"Key": "USAGE_TYPE", "Values": ["BoxUsage:p4de.24xlarge"]}}]}"}
   Example 3: {"operation": "getUsageForecast", "metric": "USAGE_QUANTITY", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22", "filter": "{"Dimensions": {"Key": "USAGE_TYPE", "Values": ["BoxUsage:p4de.24xlarge", "Reservation:p4de.24xlarge", "UnusedBox:p4de.24xlarge"]}}", "group_by": "[{"Type": "DIMENSION", "Key": "REGION"}]"}
   Notes: Valid values for metric is: USAGE_QUANTITY, NORMALIZED_USAGE_AMOUNT. Valid values for granularity is: DAILY, MONTHLY. Filter is REQUIRED and must specify USAGE_TYPE or USAGE_TYPE_GROUP to define what usage units to forecast.
   Returns: Usage forecast for specified time period and granularity

6. getTagsOrValues - Available cost allocation tags or values
   Required: operation="getTagsOrValues"
   Optional: start_date, end_date, search_string, next_token, max_pages, billing_view_arn
   Example 1: {"operation": "getTagsOrValues"}
   Example 2: {"operation": "getTagsOrValues", "tag_key": "Environment"}
   Returns: List of available cost allocation tags with automatic pagination. If tag values for a particular key are needed, pass the tag key as a parameter.

7. getCostCategories - Available cost categories or values inside a category
   Required: operation="getCostCategories", start_date, end_date
   Optional: cost_category_name, search_string, next_token, max_pages, billing_view_arn
   Example 1 (list category names): {"operation": "getCostCategories", "start_date": "2024-01-01", "end_date": "2024-08-01"}
   Example 2 (list values inside a category): {"operation": "getCostCategories", "cost_category_name": "CostCenters", "start_date": "2024-01-01", "end_date": "2024-08-01"}
   Notes: Without cost_category_name the response contains CostCategoryNames. With cost_category_name set the response contains CostCategoryValues for that category. Pagination is automatic.

8. getSavingsPlansUtilization - Savings Plans utilization data
   Required: operation="getSavingsPlansUtilization", start_date, end_date
   Optional: granularity, filter
   Example: {"operation": "getSavingsPlansUtilization", "granularity": "MONTHLY"}
   Notes: This operation supports only DAILY and MONTHLY granularity
   Returns: Savings Plans utilization for the specified time period

DIMENSION REFERENCE:
- AZ: The Availability Zone (e.g., us-east-1a)
- DATABASE_ENGINE: The Amazon RDS database (e.g., Aurora, MySQL)
- DEPLOYMENT_OPTION: RDS deployment scope (SingleAZ, MultiAZ)
- INSTANCE_TYPE: The EC2 instance type (e.g., m4.xlarge)
- INSTANCE_TYPE_FAMILY: Family of instances (e.g., Compute Optimized, Memory Optimized)
- LINKED_ACCOUNT: AWS member accounts
- OPERATING_SYSTEM: OS type (e.g., Windows, Linux)
- PLATFORM: EC2 operating s

[...]

## Screenshots

![AWS Billing and Cost Management screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-billing-cost-management-1.png)

![AWS Billing and Cost Management screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-billing-cost-management-2.png)

![AWS Billing and Cost Management screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-billing-cost-management-3.png)
