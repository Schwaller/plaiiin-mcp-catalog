AWS service pricing and cost estimates.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-pricing-mcp-server](https://hub.docker.com/repository/docker/mcp/aws-pricing-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (9)
Tools provided by this Server|Short Description
-|-
`analyze_cdk_project`|Analyze a CDK project to identify AWS services used.|
`analyze_terraform_project`|Analyze a Terraform project to identify AWS services used.|
`generate_cost_report`|Generate a detailed cost analysis report based on pricing data for one or more AWS services.|
`get_bedrock_patterns`|Get architecture patterns for Amazon Bedrock applications, including component relationships and cost considerations|
`get_price_list_urls`|Get download URLs for bulk pricing data files.|
`get_pricing`|Get detailed pricing information from AWS Price List API with optional filters.|
`get_pricing_attribute_values`|Get valid values for pricing filter attributes.|
`get_pricing_service_attributes`|Get filterable attributes available for an AWS service in the Pricing API.|
`get_pricing_service_codes`|Get AWS service codes available in the Price List API.|

---
## Tools Details

#### Tool: **`analyze_cdk_project`**
Analyze a CDK project to identify AWS services used. This tool dynamically extracts service information from CDK constructs without relying on hardcoded service mappings.
Parameters|Type|Description
-|-|-
`project_path`|`string`|Path to the project directory

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`analyze_terraform_project`**
Analyze a Terraform project to identify AWS services used. This tool dynamically extracts service information from Terraform resource declarations.
Parameters|Type|Description
-|-|-
`project_path`|`string`|Path to the project directory

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`generate_cost_report`**
Generate a detailed cost analysis report based on pricing data for one or more AWS services.

This tool requires AWS pricing data and provides options for adding detailed cost information.

IMPORTANT REQUIREMENTS:
- ALWAYS include detailed unit pricing information (e.g., "$0.0008 per 1K input tokens")
- ALWAYS show calculation breakdowns (unit price × usage = total cost)
- ALWAYS specify the pricing model (e.g., "ON DEMAND")
- ALWAYS list all assumptions and exclusions explicitly

Output Format Options:
- 'markdown' (default): Generates a well-formatted markdown report
- 'csv': Generates a CSV format report with sections for service information, unit pricing, cost calculations, etc.

Example usage:

```json
{
  // Required parameters
  "pricing_data": {
    // This should contain pricing data retrieved from get_pricing
    "status": "success",
    "service_name": "bedrock",
    "data": "... pricing information ...",
    "message": "Retrieved pricing for bedrock from AWS Pricing url"
  },
  "service_name": "Amazon Bedrock",

  // Core parameters (commonly used)
  "related_services": ["Lambda", "S3"],
  "pricing_model": "ON DEMAND",
  "assumptions": [
    "Standard ON DEMAND pricing model",
    "No caching or optimization applied",
    "Average request size of 4KB"
  ],
  "exclusions": [
    "Data transfer costs between regions",
    "Custom model training costs",
    "Development and maintenance costs"
  ],
  "output_file": "cost_analysis_report.md",  // or "cost_analysis_report.csv" for CSV format
  "format": "markdown",  // or "csv" for CSV format

  // Advanced parameter for complex scenarios
  "detailed_cost_data": {
    "services": {
      "Amazon Bedrock Foundation Models": {
        "usage": "Processing 1M input tokens and 500K output tokens with Claude 3.5 Haiku",
        "estimated_cost": "$80.00",
        "free_tier_info": "No free tier for Bedrock foundation models",
        "unit_pricing": {
          "input_tokens": "$0.0008 per 1K tokens",
          "output_tokens": "$0.0016 per 1K tokens"
        },
        "usage_quantities": {
          "input_tokens": "1,000,000 tokens",
          "output_tokens": "500,000 tokens"
        },
        "calculation_details": "$0.0008/1K × 1,000K input tokens + $0.0016/1K × 500K output tokens = $80.00"
      },
      "AWS Lambda": {
        "usage": "6,000 requests per month with 512 MB memory",
        "estimated_cost": "$0.38",
        "free_tier_info": "First 12 months: 1M requests/month free",
        "unit_pricing": {
          "requests": "$0.20 per 1M requests",
          "compute": "$0.0000166667 per GB-second"
        },
        "usage_quantities": {
          "requests": "6,000 requests",
          "compute": "6,000 requests × 1s × 0.5GB = 3,000 GB-seconds"
        },
        "calculation_details": "$0.20/1M × 0.006M requests + $0.0000166667 × 3,000 GB-seconds = $0.38"
      }
    }
  },

  // Recommendations parameter - can be provided directly or generated
  "recommendations": {
    "immediate": [
      "Optimize prompt engineering to reduce token usage for Claude 3.5 Haiku",
      "Configure Knowledge Base OCUs based on actual query patterns",
      "Implement response caching for common queries to reduce token usage"
    ],
    "best_practices": [
      "Monitor OCU utilization metrics and adjust capacity as needed",
      "Use prompt caching for repeated context across API calls",
      "Consider provisioned throughput for predictable workloads"
    ]
  }
}
```
Parameters|Type|Description
-|-|-
`pricing_data`|`object`|Raw pricing data from AWS pricing tools
`service_name`|`string`|Name of the AWS service
`assumptions`|`string` *optional*|List of assumptions for cost analysis
`detailed_cost_data`|`string` *optional*|Detailed cost information for complex scenarios
`exclusions`|`string` *optional*|List of items excluded from cost analysis
`format`|`string` *optional*|Output format ("markdown" or "csv")
`output_file`|`string` *optional*|Path to save the report file
`pricing_model`|`string` *optional*|Pricing model (e.g., "ON DEMAND", "Reserved")
`recommendations`|`string` *optional*|Direct recommendations or guidance for generation
`related_services`|`string` *optional*|List of related AWS services

---
#### Tool: **`get_bedrock_patterns`**
Get architecture patterns for Amazon Bedrock applications, including component relationships and cost considerations
#### Tool: **`get_price_list_urls`**
Get download URLs for bulk pricing data files.

    **PURPOSE:** Access complete AWS pricing datasets as downloadable files for historical analysis and bulk processing.

    **WORKFLOW:** Use this for historical pricing analysis or bulk data processing when current pricing from get_pricing() isn't sufficient.

    **PARAMETERS:**
    - Service code from get_pricing_service_codes() (e.g., 'AmazonEC2', 'AmazonS3')
    - AWS region (e.g., 'us-east-1', 'eu-west-1')
    - Optional: effective_date for historical pricing (default: current date)

    **RETURNS:** Dictionary with download URLs for different formats:
    - 'csv': Direct download URL for CSV format
    - 'json': Direct download URL for JSON format

    **USE CASES:**
    - Historical pricing analysis (get_pricing() only provides current pricing)
    - Bulk data processing without repeated API calls
    - Offline analysis of complete pricing datasets
    - Savings Plans analysis across services

    **FILE PROCESSING:**
    - CSV files: Lines 1-5 are metadata, Line 6 contains headers, Line 7+ contains pricing data
    - Use `tail -n +7 pricing.csv | grep "t3.medium"` to filter data
Parameters|Type|Description
-|-|-
`region`|`string`|AWS region (e.g., "us-east-1", "eu-west-1")
`service_code`|`string`|AWS service code (e.g., "AmazonEC2", "AmazonS3", "AmazonES")
`effective_date`|`string` *optional*|Effective date for pricing in format "YYYY-MM-DD HH:MM" (default: current timestamp)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pricing`**
Get detailed pricing information from AWS Price List API with optional filters.

    **PARAMETERS:**
    - service_code (required): AWS service code (e.g., 'AmazonEC2', 'AmazonS3', 'AmazonES')
    - region (optional): AWS region string (e.g., 'us-east-1') OR list for multi-region comparison (e.g., ['us-east-1', 'eu-west-1']). Omit for global services like DataTransfer or CloudFront that don't have region-specific pricing.
    - filters (optional): List of filter dictionaries in format {'Field': str, 'Type': str, 'Value': str}
    - max_allowed_characters (optional): Response size limit in characters (default: 100,000, use -1 for unlimited)
    - output_options (optional): OutputOptions object for response transformation and size reduction
    - max_results (optional): Maximum number of results to return per page (default: 100, min: 1, max: 100)
    - next_token (optional): Pagination token from previous response to get next page of results

    **MANDATORY WORKFLOW - ALWAYS FOLLOW:**

    **Step 1: Discover Available Options**
    ```python
    service_codes = get_pricing_service_codes()                              # Find correct service (skip if known)
    attributes = get_pricing_service_attributes('AmazonEC2')                 # Discover filterable dimensions
    attribute_values = get_pricing_attribute_values('AmazonEC2', 'memory')   # Get valid values for filtering
    ```

    **Step 2: Build Precise Filters**
    ```python
    # Use ONLY values discovered in Step 1
    filters = [
       {"Field": "memory", "Value": ["8 GiB", "16 GiB", "32 GiB"], "Type": "ANY_OF"},     # Multiple options
       {"Field": "instanceType", "Value": "m5", "Type": "CONTAINS"},                      # Pattern matching
       {"Field": "instanceType", "Value": ["t2", "m4"], "Type": "NONE_OF"}                # Exclude older
   ]
    ```

    **Step 3: Execute Query**
    ```python
    pricing = get_pricing('AmazonEC2', 'us-east-1', filters)
    ```

    **FILTER TYPES:**
    - **EQUALS**: Exact match (default) - `{"Field": "instanceType", "Value": "m5.large"}`
    - **ANY_OF**: Multiple options - `{"Field": "memory", "Value": ["8 GiB", "16 GiB"], "Type": "ANY_OF"}`
    - **CONTAINS**: Pattern match - `{"Field": "instanceType", "Value": "m5", "Type": "CONTAINS"}`
    - **NONE_OF**: Exclusion - `{"Field": "instanceType", "Value": ["t2", "m4"], "Type": "NONE_OF"}`

    **CRITICAL: ANY_OF FILTER VALUE LIMITS:**
    - **1024 CHARACTER LIMIT**: Total length of all values in ANY_OF arrays cannot exceed 1024 characters
    - **PROGRESSIVE FILTERING**: Start with minimal qualifying options, expand if needed
    - **EXAMPLE VIOLATION**: `["8 GiB", "16 GiB", "32 GiB", "64 GiB", "96 GiB", "128 GiB", ...]` (TOO LONG)
    - **CORRECT APPROACH**: `["8 GiB", "16 GiB", "32 GiB", "36 GiB", "48 GiB"]` (TARGETED LIST)

    **COMMON USE CASES:**

    **COST OPTIMIZATION - EXHAUSTIVE MINIMUM-FIRST APPROACH:** When users ask for "lowest price", "cheapest", or cost optimization
    - **LOWER = CHEAPER ASSUMPTION**: For cost optimization, assume lower capabilities cost less than higher ones
      * 32 GB storage is cheaper than 300 GB storage
      * 8 GiB RAM is cheaper than 64 GiB RAM
    - **CRITICAL FOR COST QUERIES**: Start IMMEDIATELY above minimum requirement and test ALL options incrementally
    - **EXHAUSTIVE ENUMERATION REQUIRED**: Each storage/memory tier is MUTUALLY EXCLUSIVE - must list each one explicitly
    - **STOP AT REASONABLE UPPER BOUND**: For cost optimization, limit upper bound to 2-3x minimum requirement to avoid expensive options
    - **exclude_free_products**: ESSENTIAL for cost analysis - removes $0.00 reservation placeholders, SQL licensing variants, and special pricing entries that obscure actual billable instances when finding cheapest options
    - Use ANY_OF for efficient multi-option comparison in single API call
    - Multi-attribute capability filtering for minimum requirements
    - Combine CONTAINS + NONE_OF for refined discovery

    **OUTPUT OPTIONS (Response Size & Performance Control):**
    - **PURPOSE**: Transform and optimize API responses for ALL services, especially critical for large services (EC2, RDS)
    - **IMMEDIATE COMBINED APPROACH**: `{"pricing_terms": ["OnDemand", "FlatRate"], "product_attributes": ["instanceType", "location", "memory"]}`
    - **ATTRIBUTE DISCOVERY**: Use get_pricing_service_attributes() - same names for filters and output_options
    - **SIZE REDUCTION**: 80%+ reduction with combined pricing_terms + product_attributes
    - **exclude_free_products**: Remove products with $0.00 OnDemand pricing (useful when you know service has paid tiers)
    - **WHEN TO USE**: Always for large services, recommended for all services to improve performance

    **CRITICAL REQUIREMENTS:**
    - **NEVER GUESS VALUES**: Always use get_pricing_attribute_values() to discover valid options
    - **EXHAUSTIVE ENUMERATION**: For cost optimization, list ALL qualifying tiers individually - they are mutually exclusive
    - **USE SPECIFIC FILTERS**: Large services (EC2, RDS) require 2-3 filters minimum
    - **NEVER USE MULTIPLE CALLS**: When ANY_OF can handle it in one call
    - **VERIFY EXISTENCE**: Ensure all filter values exist in the service before querying
    - **FOR "CHEAPEST" QUERIES**: Focus on lower-end options that meet minimum requirements, test incrementally
    - **EXPLORE ALTERNATIVES**: When response includes "alternatives" field, MUST fetch their pricing if applicable to the use case before answering

    **CONSTRAINTS:**
    - **CURRENT PRICING ONLY**: Use get_price_list_urls for historical data
    - **NO SPOT/SAVINGS PLANS**: Only OnDemand, FlatRate, and Reserved Instance pricing available (ANY combination possible)
    - **CHARACTER LIMIT**: 100,000 characters default response limit (use output_options to reduce)
    - **REGION AUTO-FILTER**: Region parameter automatically creates regionCode filter

    **ANTI-PATTERNS:**
    - DO NOT make multiple API calls that could be combined with ANY_OF
    - DO NOT build cross-products manually when API can handle combinations
    - DO NOT call get_pricing_service_codes() when service code is already known (e.g., "AmazonEC2")
    - DO NOT use EQUALS without first checking get_pricing_attribute_values()
    - DO NOT skip discovery workflow for any use case
    - DO NOT use broad queries without specific filters on large services
    - DO NOT assume attribute values exist across different services/regions
    - DO NOT skip intermediate tiers: Missing 50GB, 59GB options when testing 32GB → 75GB jump
    - DO NOT set upper bounds too high: Including 500GB+ storage when user needs ≥30GB (wastes character limit)
    - DO NOT ignore alternatives field or use only ["OnDemand"] in output_options

    **EXAMPLE USE CASES:**

    **1. Cost-Optimized Multi-Attribute Filtering (CORRECT APPROACH):**
    ```python
    # Find cheapest EC2 instances meeting minimum requirements (>= 8 GiB memory, >= 30 GB storage)
    # EXHAUSTIVE ENUMERATION of qualifying tiers - each is mutually exclusive
    filters = [
       {"Field": "memory", "Value": ["8 GiB", "16 GiB", "32 GiB"], "Type": "ANY_OF"},  # All tiers ≥8GB up to reasonable limit
       {"Field": "storage", "Value": ["1 x 32 SSD", "1 x 60 SSD", "1 x 75 NVMe SSD"], "Type": "ANY_OF"},  # All tiers ≥30GB up to reasonable limit
       {"Field": "instanceType", "Value": ["t2", "m4"], "Type": "NONE_OF"},  # Exclude older generations
       {"Field": "tenancy", "Value": "Shared", "Type": "EQUALS"}  # Exclude more expensive dedicated
    ]
    pricing = get_pricing('AmazonEC2', 'us-east-1', filters)
    ```

    **2. Efficient Multi-Region Comparison:**
    ```python
    # Compare same configuration across regions - use region parameter for multi-region
    filters = [{"Field": "instanceType", "Value": "m5.large", "Type": "EQUALS"}]
    pricing = get_pricing('AmazonEC2', ['us-east-1', 'us-west-2', 'eu-west-1'], filters)
    ```

    **3. Large service with output optimization (recommended approach):**
    ```python
    output_options = {"pricing_terms": ["OnDemand", "FlatRate"], "product_attributes": ["instanceType", "location"], "exclude_free_products": true}
    pricing = get_pricing('AmazonEC2', 'us-east-1', filters, output_options=output_options)
    ```

    **4. Pattern-Based Discovery:**
    ```python
    # Find all Standard storage tiers except expensive ones
    filters = [
        {"Field": "storageClass", "Value": "Standard", "Type": "CONTAINS"},
        {"Field": "storageClass", "Value": ["Standard-IA"], "Type": "NONE_OF"}
    ]
    ```

    **FILTERING STRATEGY:**
    - **Large Services (EC2, RDS)**: ALWAYS use 2-3 specific filters to prevent 200+ record responses
    - **Small Services**: May work with single filter or no filters
    - **Multi-Option Analysis**: Use ANY_OF instead of multiple API calls
    - **Pattern Discovery**: Use CONTAINS for finding families or tiers
    - **Smart Exclusion**: Use NONE_OF for compliance or cost filtering

    **SUCCESS CRITERIA:**
    - Used discovery workflow (skip get_pricing_service_codes() if service known)
    - Applied appropriate filters for the service size
    - Used exact values from get_pricing_attribute_values()
    - Used ANY_OF for multi-option scenarios instead of multiple calls
    - For cost optimization: tested ALL qualifying tiers exhaustively (in a reasonable range)
    - Included ["OnDemand", "FlatRate"] in output_options and explored all alternatives
Parameters|Type|Description
-|-|-
`service_code`|`string`|AWS service code (e.g., "AmazonEC2", "AmazonS3", "AmazonES")
`filters`|`string` *optional*|Optional list of filters to apply to the pricing query
`max_allowed_characters`|`integer` *optional*|Maximum response length in characters (default: 100,000, use -1 for unlimited)
`max_results`|`integer` *optional*|Maximum number of results to return per page (default: 100, max: 100)
`next_token`|`string` *optional*|Pagination token from previous response to get next page of results
`output_options`|`string` *optional*|Optional output filtering options to reduce response size. Use {"pricing_terms": ["OnDemand", "FlatRate"]} to significantly reduce response size for large services like EC2.
`region`|`string` *optional*|AWS region(s) - single region string (e.g., "us-east-1") or list for multi-region comparison (e.g., ["us-east-1", "us-west-2", "eu-west-1"]). Optional: omit for global services like DataTransfer or CloudFront that don't have region-specific pricing.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pricing_attribute_values`**
Get valid values for pricing filter attributes.

    **PURPOSE:** Discover what values are available for specific pricing filter attributes of an AWS service.

    **WORKFLOW:** Use this after get_pricing_service_attributes() to see valid values for each filter attribute.

    **PARAMETERS:**
    - Service code from get_pricing_service_codes() (e.g., 'AmazonEC2', 'AmazonRDS')
    - List of attribute names from get_pricing_service_attributes() (e.g., ['instanceType', 'location'])
    - filters (optional): Dictionary mapping attribute names to regex patterns (e.g., {'instanceType': 't3'})

    **RETURNS:** Dictionary mapping attribute names to their valid values. Filtered attributes return only matching values, unfiltered attributes return all values.

    **EXAMPLE RETURN:**
    ```
    {
        'instanceType': ['t2.micro', 't3.medium', 'm5.large', ...],
        'location': ['US East (N. Virginia)', 'EU (London)', ...]
    }
    ```

    **NEXT STEPS:** Use these values in get_pricing() filters to get specific pricing data.

    **ERROR HANDLING:** Uses "all-or-nothing" approach - if any attribute fails, the entire operation fails.

    **EXAMPLES:**
    - Single attribute: ['instanceType'] returns {'instanceType': ['t2.micro', 't3.medium', ...]}
    - Multiple attributes: ['instanceType', 'location'] returns both mappings
    - Partial filtering: filters={'instanceType': 't3'} applies only to instanceType, location returns all values
Parameters|Type|Description
-|-|-
`attribute_names`|`array`|List of attribute names (e.g., ["instanceType", "location", "storageClass"])
`service_code`|`string`|AWS service code (e.g., "AmazonEC2", "AmazonS3", "AmazonES")
`filters`|`string` *optional*|Optional dictionary mapping attribute names to regex patterns for filtering their values (e.g., {"instanceType": "t3", "operatingSystem": "Linux"})

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pricing_service_attributes`**
Get filterable attributes available for an AWS service in the Pricing API.

    **PURPOSE:** Discover what pricing dimensions (filters) are available for a specific AWS service.

    **WORKFLOW:** Use this after get_pricing_service_codes() to see what filters you can apply to narrow down pricing queries.

    **PARAMETERS:**
    - service_code: AWS service code from get_pricing_service_codes() (e.g., 'AmazonEC2', 'AmazonRDS')
    - filter (optional): Case-insensitive regex pattern to filter attribute names (e.g., "instance" matches "instanceType", "instanceFamily")

    **RETURNS:** List of attribute names (e.g., 'instanceType', 'location', 'storageClass') that can be used as filters.

    **NEXT STEPS:**
    - Use get_pricing_attribute_values() to see valid values for each attribute
    - Use these attributes in get_pricing() filters to get specific pricing data

    **EXAMPLE:** For 'AmazonRDS' you might get ['engineCode', 'instanceType', 'deploymentOption', 'location'].
Parameters|Type|Description
-|-|-
`service_code`|`string`|AWS service code (e.g., "AmazonEC2", "AmazonS3", "AmazonES")
`filter`|`string` *optional*|Optional case-insensitive regex pattern to filter service attribute names

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pricing_service_codes`**
Get AWS service codes available in the Price List API.

    **PURPOSE:** Discover which AWS services have pricing information available in the AWS Price List API.

    **PARAMETERS:**
    - filter (optional): Case-insensitive regex pattern to filter service codes (e.g., "bedrock" matches "AmazonBedrock", "AmazonBedrockService")

    **WORKFLOW:** This is the starting point for any pricing query. Use this first to find the correct service code.

    **RETURNS:** List of service codes (e.g., 'AmazonEC2', 'AmazonS3', 'AWSLambda') that can be used with other pricing tools.

    **NEXT STEPS:**
    - Use get_pricing_service_attributes() to see what filters are available for a service
    - Use get_pricing() to get actual pricing data for a service

    **NOTE:** Service codes may differ from AWS console names (e.g., 'AmazonES' for OpenSearch, 'AWSLambda' for Lambda).
Parameters|Type|Description
-|-|-
`filter`|`string` *optional*|Optional case-insensitive regex pattern to filter service codes

*This tool is read-only. It does not modify its environment.*

---

## Screenshots

![AWS Pricing screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-pricing-1.png)

![AWS Pricing screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-pricing-2.png)

![AWS Pricing screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-pricing-3.png)
