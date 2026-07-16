MCP server for interacting with Atlan services including asset search, updates, and lineage traversal for comprehensive data governance and discovery.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/atlan](https://hub.docker.com/repository/docker/mcp/atlan)
**Author**|[atlanhq](https://github.com/atlanhq)
**Repository**|https://github.com/atlanhq/agent-toolkit

## Available Tools (14)
Tools provided by this Server|Short Description
-|-
`create_data_products`|Create Data Products in Atlan.|
`create_domains`|Create Data Domains or Sub Domains in Atlan.|
`create_dq_rules_tool`|Create one or multiple data quality rules in Atlan.|
`create_glossaries`|Create one or multiple AtlasGlossary assets in Atlan.|
`create_glossary_categories`|Create one or multiple AtlasGlossaryCategory assets in Atlan.|
`create_glossary_terms`|Create one or multiple AtlasGlossaryTerm assets in Atlan.|
`delete_dq_rules_tool`|Delete one or multiple data quality rules in Atlan.|
`get_assets_by_dsl_tool`|Execute the search with the given query dsl_query : Union[str, Dict[str, Any]] (required): The DSL query used to search the index.|
`query_asset_tool`|Execute a SQL query on a table/view asset.|
`schedule_dq_rules_tool`|Schedule data quality rule execution for one or multiple assets.|
`search_assets_tool`|Advanced asset search using FluentSearch with flexible conditions.|
`traverse_lineage_tool`|Traverse asset lineage in specified direction.|
`update_assets_tool`|Update one or multiple assets with different values for attributes or term operations.|
`update_dq_rules_tool`|Update existing data quality rules in Atlan.|

---
## Tools Details

#### Tool: **`create_data_products`**
Create Data Products in Atlan.

IMPORTANT BUSINESS RULES & CONSTRAINTS:
- Before creating a product, you may want to search for existing domains
  to get the qualified_name for the domain relationship
- Product names must be unique within the same domain
- At least one asset GUID must be provided for each product
Parameters|Type|Description
-|-|-
`products`|`string`|Either a single product
specification (dict) or a list of product specifications.

---
#### Tool: **`create_domains`**
Create Data Domains or Sub Domains in Atlan.

IMPORTANT BUSINESS RULES & CONSTRAINTS:
- Before creating a domain/subdomain, you may want to search for existing
  domains to avoid duplicates or to get the qualified_name for parent relationships
- Domain names must be unique at the top level
- Subdomain names must be unique within the same parent domain
Parameters|Type|Description
-|-|-
`domains`|`string`|Either a single domain
specification (dict) or a list of domain specifications.

---
#### Tool: **`create_dq_rules_tool`**
Create one or multiple data quality rules in Atlan.

Supports all rule types: column-level, table-level, and custom SQL rules.
Rules can be created individually or in bulk for efficient setup.
Parameters|Type|Description
-|-|-
`rules`|`string`|Either a single rule
specification or a list of rule specifications. Each specification
must include:
- rule_type (str): Type of rule (see Supported Rule Types) [REQUIRED]
- asset_qualified_name (str): Qualified name of the asset (Table, View, MaterialisedView, or SnowflakeDynamicTable) [REQUIRED]
- asset_type (str): Type of asset - "Table" | "View" | "MaterialisedView" | "SnowflakeDynamicTable" [OPTIONAL, default: "Table"]
- threshold_value (int/float): Threshold value for comparison [REQUIRED]
- column_qualified_name (str): Column qualified name [REQUIRED for column-level rules, NOT for Row Count/Custom SQL]
- threshold_compare_operator (str): Comparison operator (EQUAL, GREATER_THAN, etc.) [OPTIONAL, default varies by rule]
- threshold_unit (str): Time unit for Freshness rules (DAYS, HOURS, MINUTES) [REQUIRED for Freshness, N/A for others]
- alert_priority (str): Alert priority level (LOW, NORMAL, URGENT) [OPTIONAL, default: NORMAL]
- row_scope_filtering_enabled (bool): Enable row-level filtering [OPTIONAL]
- rule_conditions (List[Dict]): Conditions for String Length/Regex/Valid Values [REQUIRED for conditional rules]
- custom_sql (str): SQL query [REQUIRED for Custom SQL rules]
- rule_name (str): Name for the rule [REQUIRED for Custom SQL rules]
- dimension (str): DQ dimension [REQUIRED for Custom SQL rules]
- description (str): Rule description [OPTIONAL]

---
#### Tool: **`create_glossaries`**
Create one or multiple AtlasGlossary assets in Atlan.

IMPORTANT BUSINESS RULES & CONSTRAINTS:
- Check for duplicate names within the same request and ask user to choose different names
- Do NOT use search tool before creating glossaries - Atlan will handle existence validation
- If user gives ambiguous instructions, ask clarifying questions
Parameters|Type|Description
-|-|-
`glossaries`|`string`|Either a single glossary
specification (dict) or a list of glossary specifications. Each specification
can be a dictionary containing:
- name (str): Name of the glossary (required)
- user_description (str, optional): Detailed description of the glossary
  proposed by the user
- certificate_status (str, optional): Certification status
  ("VERIFIED", "DRAFT", or "DEPRECATED")

---
#### Tool: **`create_glossary_categories`**
Create one or multiple AtlasGlossaryCategory assets in Atlan.

IMPORTANT BUSINESS RULES & CONSTRAINTS:
- There cannot be two categories with the same name under the same glossary (at the same level)
- Under a parent category, there cannot be subcategories with the same name (at the same level)
- Categories with the same name can exist under different glossaries (this is allowed)
- Cross-level naming is allowed: category "a" can have subcategory "b", and category "b" can have subcategory "a"
- Example allowed structure: Glossary "bui" → category "a" → subcategory "b" AND category "b" → subcategory "a"
- Always check for duplicate names at the same level and ask user to choose different names
- Before creating a category, perform a single search to check if the glossary or categories with the same name already exist. Skip this step if you already have the required GUIDs.
- Example call for searching glossary and categories before category creation(Query - create categories Locations and Characters under Marvel Cinematic Universe (MCU) glossary):
    {
        "limit": 10,
        "conditions": {
            "type_name": ["AtlasGlossary", "AtlasGlossaryCategory"],
            "name": ["Marvel Cinematic Universe (MCU)", "Characters", "Locations"]
        }
    }
- If user gives ambiguous instructions, ask clarifying questions
Parameters|Type|Description
-|-|-
`categories`|`string`|Either a single category
specification (dict) or a list of category specifications. Each specification
can be a dictionary containing:
- name (str): Name of the category (required)
- glossary_guid (str): GUID of the glossary this category belongs to (required)
- user_description (str, optional): Detailed description of the category
  proposed by the user
- certificate_status (str, optional): Certification status
  ("VERIFIED", "DRAFT", or "DEPRECATED")
- parent_category_guid (str, optional): GUID of the parent category if this
  is a subcategory

---
#### Tool: **`create_glossary_terms`**
Create one or multiple AtlasGlossaryTerm assets in Atlan.

IMPORTANT BUSINESS RULES & CONSTRAINTS:
- Within a glossary, a term (single GUID) can be associated with many categories
- Two terms with the same name CANNOT exist within the same glossary (regardless of categories)
- A term is always anchored to a glossary and may also be associated with one or more categories inside the same glossary
- Before creating a term, perform a single search to check if the glossary, categories, or term with the same name already exist. Search for all relevant glossaries, categories, and terms in one call. Skip this step if you already have the required GUIDs.
- Example call for searching glossary categories and terms before term creation(Query - create a term fighterz under category Characters and Locations under Marvel Cinematic Universe (MCU) glossary):
    {
        "limit": 10,
        "conditions": {
            "type_name": ["AtlasGlossary", "AtlasGlossaryCategory","AtlasGlossaryTerm"],
            "name": ["Marvel Cinematic Universe (MCU)", "Characters", "Locations","fighterz"]
        }
    }
Parameters|Type|Description
-|-|-
`terms`|`string`|Either a single term
specification (dict) or a list of term specifications. Each specification
can be a dictionary containing:
- name (str): Name of the term (required)
- glossary_guid (str): GUID of the glossary this term belongs to (required)
- user_description (str, optional): Detailed description of the term
  proposed by the user
- certificate_status (str, optional): Certification status
  ("VERIFIED", "DRAFT", or "DEPRECATED")
- category_guids (List[str], optional): List of category GUIDs this term
  belongs to.

---
#### Tool: **`delete_dq_rules_tool`**
Delete one or multiple data quality rules in Atlan.
Parameters|Type|Description
-|-|-
`rule_guids`|`string`|Single rule GUID (string) or list of rule GUIDs to delete.

---
#### Tool: **`get_assets_by_dsl_tool`**
Execute the search with the given query
dsl_query : Union[str, Dict[str, Any]] (required):
    The DSL query used to search the index.

Example:
dsl_query = '''{
"query": {
    "function_score": {
        "boost_mode": "sum",
        "functions": [
            {"filter": {"match": {"starredBy": "john.doe"}}, "weight": 10},
            {"filter": {"match": {"certificateStatus": "VERIFIED"}}, "weight": 15},
            {"filter": {"match": {"certificateStatus": "DRAFT"}}, "weight": 10},
            {"filter": {"bool": {"must_not": [{"exists": {"field": "certificateStatus"}}]}}, "weight": 8},
            {"filter": {"bool": {"must_not": [{"terms": {"__typeName.keyword": ["Process", "DbtProcess"]}}]}}, "weight": 20}
        ],
        "query": {
            "bool": {
                "filter": [
                    {
                        "bool": {
                            "minimum_should_match": 1,
                            "must": [
                                {"bool": {"should": [{"terms": {"certificateStatus": ["VERIFIED"]}}]}},
                                {"term": {"__state": "ACTIVE"}}
                            ],
                            "must_not": [
                                {"term": {"isPartial": "true"}},
                                {"terms": {"__typeName.keyword": ["Procedure", "DbtColumnProcess", "BIProcess", "MatillionComponent", "SnowflakeTag", "DbtTag", "BigqueryTag", "AIApplication", "AIModel"]}},
                                {"terms": {"__typeName.keyword": ["MCIncident", "AnomaloCheck"]}}
                            ],
                            "should": [
                                {"terms": {"__typeName.keyword": ["Query", "Collection", "AtlasGlossary", "AtlasGlossaryCategory", "AtlasGlossaryTerm", "Connection", "File"]}},
                            ]
                        }
                    }
                ]
            },
            "score_mode": "sum"
        },
        "score_mode": "sum"
    }
},
"post_filter": {
    "bool": {
        "filter": [
            {
                "bool": {
                    "must": [{"terms": {"__typeName.keyword": ["Table", "Column"]}}],
                    "must_not": [{"exists": {"field": "termType"}}]
                }
            }
        ]
    },
    "sort": [
        {"_score": {"order": "desc"}},
        {"popularityScore": {"order": "desc"}},
        {"starredCount": {"order": "desc"}},
        {"name.keyword": {"order": "asc"}}
    ],
    "track_total_hits": true,
    "size": 10,
    "include_meta": false
}'''
response = get_assets_by_dsl(dsl_query)
Parameters|Type|Description
-|-|-
`dsl_query`|`string`|

---
#### Tool: **`query_asset_tool`**
Execute a SQL query on a table/view asset.

This tool enables querying table/view assets on the source similar to
what's available in the insights table. It uses the Atlan query capabilities
to execute SQL against connected data sources.

CRITICAL: Use READ-ONLY queries to retrieve data. Write and modify queries are not supported by this tool.
Parameters|Type|Description
-|-|-
`connection_qualified_name`|`string`|Connection qualified name to use for the query.
This is the same parameter used in search_assets_tool.
You can find this value by searching for Table/View assets using search_assets_tool
and extracting the first part of the 'qualifiedName' attribute.
Example: from "default/snowflake/1657275059/LANDING/FRONTEND_PROD/PAGES"
use "default/snowflake/1657275059"
`sql`|`string`|The SQL query to execute (read-only queries allowed)
`default_schema`|`string` *optional*|Default schema name to use for unqualified
objects in the SQL, in the form "DB.SCHEMA"
(e.g., "RAW.WIDEWORLDIMPORTERS_WAREHOUSE")

---
#### Tool: **`schedule_dq_rules_tool`**
Schedule data quality rule execution for one or multiple assets.
Parameters|Type|Description
-|-|-
`schedules`|`string`|Single schedule or list of schedules. Each schedule requires:
- asset_type (str): "Table", "View", "MaterialisedView", or "SnowflakeDynamicTable"
- asset_name (str): Name of the asset
- asset_qualified_name (str): Qualified name of the asset
- schedule_crontab (str): Cron expression (5 fields: min hour day month weekday)
- schedule_time_zone (str): Timezone (e.g., "UTC", "America/New_York")

---
#### Tool: **`search_assets_tool`**
Advanced asset search using FluentSearch with flexible conditions.
Parameters|Type|Description
-|-|-
`asset_type`|`string` *optional*|Type of asset to search for.
Either a class (e.g., Table, Column) or a string type name (e.g., "Table", "Column")
`conditions`|`string` *optional*|Dictionary of attribute conditions to match.
Format: {"attribute_name": value} or {"attribute_name": {"operator": operator, "value": value}}
`connection_qualified_name`|`string` *optional*|Connection qualified name to filter by. ex: default/snowflake/123456/abc
`date_range`|`string` *optional*|Date range filters.
Format: {"attribute_name": {"gte": start_timestamp, "lte": end_timestamp}}
`directly_tagged`|`string` *optional*|Whether to filter for directly tagged assets only. Defaults to True.
`domain_guids`|`string` *optional*|List of domain GUIDs to filter by.
`guids`|`string` *optional*|List of asset GUIDs to filter by.
`include_archived`|`string` *optional*|Whether to include archived assets. Defaults to False.
`include_attributes`|`string` *optional*|List of specific attributes to include in results.
Can be string attribute names or AtlanField objects.
`limit`|`string` *optional*|Maximum number of results to return. Defaults to 10.
`min_somes`|`string` *optional*|Minimum number of some_conditions that must match. Defaults to 1.
`negative_conditions`|`string` *optional*|Dictionary of attribute conditions to exclude.
Format: {"attribute_name": value} or {"attribute_name": {"operator": operator, "value": value}}
`offset`|`string` *optional*|Offset for pagination. Defaults to 0.
`some_conditions`|`string` *optional*|Conditions for where_some() queries that require min_somes of them to match.
Format: {"attribute_name": value} or {"attribute_name": {"operator": operator, "value": value}}
`sort_by`|`string` *optional*|Attribute to sort by. Defaults to None.
`sort_order`|`string` *optional*|Sort order, "ASC" or "DESC". Defaults to "ASC".
`tags`|`string` *optional*|List of tags to filter by.

---
#### Tool: **`traverse_lineage_tool`**
Traverse asset lineage in specified direction.

By default, essential attributes are included in results. Additional attributes can be
specified via include_attributes parameter for richer lineage information.
Parameters|Type|Description
-|-|-
`direction`|`string`|Direction to traverse ("UPSTREAM" or "DOWNSTREAM")
`guid`|`string`|GUID of the starting asset
`depth`|`string` *optional*|Maximum depth to traverse. Defaults to 1000000.
`immediate_neighbors`|`string` *optional*|Only return immediate neighbors. Defaults to True.
`include_attributes`|`string` *optional*|List of additional attribute names to include in results.
These will be added to the default set.
`size`|`string` *optional*|Maximum number of results to return. Defaults to 10.

---
#### Tool: **`update_assets_tool`**
Update one or multiple assets with different values for attributes or term operations.
Parameters|Type|Description
-|-|-
`assets`|`string`|Asset(s) to update.
Can be a single UpdatableAsset or a list of UpdatableAsset objects.
For asset of type_name=AtlasGlossaryTerm or type_name=AtlasGlossaryCategory, each asset dictionary MUST include a "glossary_guid" key which is the GUID of the glossary that the term belongs to.
`attribute_name`|`string`|Name of the attribute to update.
Supports "user_description", "certificate_status", "readme", and "term".
`attribute_values`|`string`|List of values to set for the attribute.
For certificateStatus, only "VERIFIED", "DRAFT", or "DEPRECATED" are allowed.
For readme, the value must be a valid Markdown string.
For term, the value must be a dict with "operation" and "term_guids" keys.

---
#### Tool: **`update_dq_rules_tool`**
Update existing data quality rules in Atlan.
Parameters|Type|Description
-|-|-
`rules`|`string`|Single rule dict or list of rule dicts. Required fields:
- qualified_name: Rule's qualified name
- rule_type: Rule type (e.g., "Null Count", "Row Count", "Custom SQL")
- asset_qualified_name: Table/view qualified name

---
