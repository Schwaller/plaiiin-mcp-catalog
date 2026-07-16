HDX MCP Server provides access to humanitarian data through the Humanitarian Data Exchange (HDX) API - https://data.humdata.org/hapi. This server offers 33 specialized tools for retrieving humanitarian information including affected populations (refugees, IDPs, returnees), baseline demographics, food security indicators, conflict data, funding information, and operational presence across hundreds of countries and territories. See repository for instructions on getting a free HDX_APP_INDENTIFIER for access.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/hdx](https://hub.docker.com/repository/docker/mcp/hdx)
**Author**|[dividor](https://github.com/dividor)
**Repository**|https://github.com/dividor/hdx-mcp

## Available Tools (29)
Tools provided by this Server|Short Description
-|-
`affected_people_humanitarian_needs_get`|OCHA's Humanitarian Needs data, based on the Joint and Intersectoral Analysis Framework (JIAF), provides information about the number of people in need during a crisis.|
`affected_people_idps_get`|Get idps data 🎯 **CRITICAL - Data Coverage Warning**: Data coverage is only determined by the metadata_data_availability_get tool.|
`affected_people_refugees_get`|UNHCR's Refugee data provides information about displaced people in a crisis.|
`affected_people_returnees_get`|Get returnees data 🎯 **CRITICAL - Data Coverage Warning**: Data coverage is only determined by the metadata_data_availability_get tool.|
`baseline_population_get`|Baseline population data sourced and maintained by UNFPA (UN Population Fund).|
`climate_rainfall_get`|Rainfall data .|
`coordination_conflict_events_get`|Armed Conflict Location & Events Data from ACLED.|
`coordination_funding_get`|OCHA's funding data from the Financial Tracking Service provides information on humanitarian aid contributions.|
`coordination_national_risk_get`|European Commission national risk data from the INFORM-risk framework.|
`coordination_operational_presence_get`|OCHA's 3W (Who is doing What Where) Operational Presence data provides information about which organizations are working in different locations affected by a crisis.|
`food_prices_get`|The World Food Programme (WFP) food prices data provides information about food prices for a range of commodities at markets across the world.|
`food_security_get`|Integrated Food Security Phase Classification from the IPC.|
`hdx_get_dataset_info`|Get detailed information about a specific HDX dataset.|
`hdx_search_locations`|Search for locations (countries) in the HDX system.|
`hdx_server_info`|Get information about the HDX MCP server instance.|
`metadata_admin1_get`|Not all data are available for all locations.|
`metadata_admin2_get`|Not all data are available for all locations.|
`metadata_currency_get`|Provide currency information to use in conjunction with the food-prices endpoint **Query Parameters:** - **app_identifier** (Required): base64 encoded application name and email, as in `base64("app_name:email")`.|
`metadata_data_availability_get`|Provide currency information to use in conjunction with the food-prices endpoint **Query Parameters:** - **app_identifier** (Required): base64 encoded application name and email, as in `base64("app_name:email")`.|
`metadata_dataset_get`|Get information about the <a href="https://data.humdata.org/dataset">HDX Datasets</a> that are used as data sources for HDX HAPI.|
`metadata_location_get`|Not all data are available for all locations.|
`metadata_org_get`|Get the list of organizations represented in the data available in HDX HAPI 🔄 **Pagination**: You can page through results using `limit` and `offset` parameters (limit=records per page, offset=starting position).|
`metadata_org_type_get`|There is no agreed standard for the classification of organizations.|
`metadata_resource_get`|Get information about the resources that are used as data sources for HDX HAPI.|
`metadata_sector_get`|There are a variety of standards for the naming of humanitarian sectors.|
`metadata_wfp_commodity_get`|Provide commodity information to use in conjunction with the food-prices endpoint **Query Parameters:** - **app_identifier** (Required): base64 encoded application name and email, as in `base64("app_name:email")`.|
`metadata_wfp_market_get`|Provide physical market location information to use in conjunction with the food-prices endpoint **Query Parameters:** - **app_identifier** (Required): base64 encoded application name and email, as in `base64("app_name:email")`.|
`poverty_rate_get`|Poverty rate data from the Oxford Department of International Development.|
`util_version_get`|Display the API and SQL Alchemy versions 🔄 **Pagination**: You can page through results using `limit` and `offset` parameters (limit=records per page, offset=starting position).|

---
## Tools Details

#### Tool: **`affected_people_humanitarian_needs_get`**
OCHA's Humanitarian Needs data, based on the Joint and Intersectoral Analysis Framework (JIAF), provides information about the number of people in need during a crisis. See the more detailed technical <a href="https://hdx-hapi.readthedocs.io/en/latest/data_usage_guides/affected_people/#humanitarian-needs">HDX HAPI documentation</a>, and the <a href="https://www.jiaf.info/">original JIAF source</a> website.

**Query Parameters:**

- **app_identifier** (Required): base64 encoded application name and email, as in `base64("app_name:email")`. This value can also be passed in the `X-HDX-HAPI-APP-IDENTIFIER` header. See the *encoded_app_identifier* endpoint.

- **category**: A category combining gender, age range, disability marker and population group information

- **sector_code**: Filter the response by the sector code.

- **population_status**: Filter the response by the population status, available values are described <a href="https://hdx-hapi.readthedocs.io/en/latest/data_usage_guides/enums/#population-status">here.</a>

- **population_min**: Filter the response by a lower bound for the population.

- **population_max**: Filter the response by a upper bound for the population.

- **sector_name**: Filter the response by the sector name.

- **has_hrp**: Filter the response by the has_hrp flag. The has_hrp flag indicates whether a country has a Humanitarian Response Plan.

- **in_gho**: Filter the response by the in_gho flag. The in_gho flag indicates whether a country is in the <a href="https://humanitarianaction.info/">Global Humanitarian Overview</a>.

- **start_date**: Filter entries to include rows where the reference period overlaps with or extends beyond this date, e.g. 2020, 2020-01, 2020-01-01 or 2020-01-01T00:00:00

- **end_date**: Filter entries to include rows where the reference period overlaps with or begins prior to this date, e.g. 2020, 2020-01, 2020-01-01, 2020-01-01 or 2020-01-01T23:59:59

- **location_code**: Filter the response by a location (typically a country). The location codes use the ISO-3 (ISO 3166 alpha-3) codes. Use the metadata_location_get tool to get available location codes and names.

- **location_name**: Filter the response by a location (typically a country). The location names are based on the "short name" from the <a href="https://unstats.un.org/unsd/methodology/m49/#fn2">UN M49 Standard</a>. Use the metadata_location_get tool to get available location codes and names.

- **admin1_code**: Filter the response by the 1st subnational administrative divisions. The admin1 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>. Use the metadata_admin1_get tool to get available admin1 codes and names.

- **admin1_name**: Filter the response by the 1st subnational administrative divisions. The admin1 names refer to either the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a> or those provided in the original data source. Use the metadata_admin1_get tool to get available admin1 codes and names.

- **admin2_code**: Filter the response by the 2nd subnational administrative divisions. The admin2 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>. Use the metadata_admin2_get tool to get available admin2 codes and names.

- **admin2_name**: Filter the response by the 2nd subnational administrative divisions. The admin2 names refer to either the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a> or those provided in the original data source. Use the metadata_admin2_get tool to get available admin2 codes and names.

- **admin_level**: Filter the response by admin level.

- **output_format**: No description.

- **limit**: Maximum number of records to return. The system will not return more than 10,000 records.

- **offset**: Number of records to skip in the response. Use in conjunction with the limit parameter to paginate.

**Responses:**

- **200** (Success): Successful Response
  - Content-Type: `application/json`

  - **Response Properties:**

  - **Example:**
```json
{
  "data": [
    {
      "location_code": "string",
      "location_name": "string",
      "admin1_code": "unknown_type",
      "admin_level": 1,
      "reference_period_end": "unknown_type",
      "population_status": "AFF",
      "admin2_name": "unknown_type",
      "admin1_name": "unknown_type",
      "resource_hdx_id": "string",
      "sector_code": "string",
      "population": 1,
      "reference_period_start": "2024-01-01T12:00:00Z",
      "sector_name": "unknown_type",
      "category": "string",
      "admin2_code": "unknown_type"
    }
  ]
}
```

- **400**: Bad Request
  - Content-Type: `application/json`

  - **Response Properties:**

  - **Example:**
```json
{
  "detail": "string"
}
```

- **422**: Validation Error
  - Content-Type: `application/json`

  - **Response Properties:**

  - **Example:**
```json
{
  "detail": [
    {
      "loc": [
        "unknown_type"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

- **500**: Internal Server Error
  - Content-Type: `application/json`

  - **Response Properties:**

  - **Example:**
```json
{
  "error_sample_list": [
    "unknown"
  ],
  "error": "string"
}
```
Parameters|Type|Description
-|-|-
`admin1_code`|`string` *optional*|Filter the response by the 1st subnational administrative divisions. The admin1 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>. Use the metadata_admin1_get tool to get available admin1 codes and names.
`admin1_name`|`string` *optional*|Filter the response by the 1st subnational administrative divisions. The admin1 names refer to either the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a> or those provided in the original data source. Use the metadata_admin1_get tool to get available admin1 codes and names.
`admin2_code`|`string` *optional*|Filter the response by the 2nd subnational administrative divisions. The admin2 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>. Use the metadata_admin2_get tool to get available admin2 codes and names.
`admin2_name`|`string` *optional*|Filter the response by the 2nd subnational administrative divisions. The admin2 names refer to either the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a> or those provided in the original data source. Use the metadata_admin2_get tool to get available admin2 codes and names.
`admin_level`|`string` *optional*|Filter the response by admin level.
`category`|`string` *optional*|A category combining gender, age range, disability marker and population group information
`end_date`|`string` *optional*|Filter entries to include rows where the reference period overlaps with or begins prior to this date, e.g. 2020, 2020-01, 2020-01-01, 2020-01-01 or 2020-01-01T23:59:59
`has_hrp`|`string` *optional*|Filter the response by the has_hrp flag. The has_hrp flag indicates whether a country has a Humanitarian Response Plan.
`in_gho`|`string` *optional*|Filter the response by the in_gho flag. The in_gho flag indicates whether a country is in the <a href="https://humanitarianaction.info/">Global Humanitarian Overview</a>.
`limit`|`integer` *optional*|Maximum number of records to return. The system will not return more than 10,000 records.
`location_code`|`string` *optional*|Filter the response by a location (typically a country). The location codes use the ISO-3 (ISO 3166 alpha-3) codes. Use the metadata_location_get tool to get available location codes and names.
`location_name`|`string` *optional*|Filter the response by a location (typically a country). The location names are based on the "short name" from the <a href="https://unstats.un.org/unsd/methodology/m49/#fn2">UN M49 Standard</a>. Use the metadata_location_get tool to get available location codes and names.
`offset`|`integer` *optional*|Number of records to skip in the response. Use in conjunction with the limit parameter to paginate.
`output_format`|`string` *optional*|
`population_max`|`string` *optional*|Filter the response by a upper bound for the population.
`population_min`|`string` *optional*|Filter the response by a lower bound for the population.
`population_status`|`string` *optional*|Filter the response by the population status, available values are described <a href="https://hdx-hapi.readthedocs.io/en/latest/data_usage_guides/enums/#population-status">here.</a>
`sector_code`|`string` *optional*|Filter the response by the sector code.
`sector_name`|`string` *optional*|Filter the response by the sector name.
`start_date`|`string` *optional*|Filter entries to include rows where the reference period overlaps with or extends beyond this date, e.g. 2020, 2020-01, 2020-01-01 or 2020-01-01T00:00:00

---
#### Tool: **`affected_people_idps_get`**
Get idps data

🎯 **CRITICAL - Data Coverage Warning**: Data coverage is only determined by the metadata_data_availability_get tool. Just because a country is in the system doesn't mean it has data. ALWAYS verify data availability before making data queries. 

🎯 **CRITICAL - Administrative Level Efficiency**: Before making aggregate queries (totals, country-wide statistics), ALWAYS check data availability using metadata_data_availability_get for the target country. Use the LOWEST available admin level (0=country, 1=state, 2=district) to avoid downloading excessive granular data. For country totals, use admin level 0 if available, otherwise level 1. Never query admin level 2 for simple aggregations when level 0/1 is sufficient.

🔄 **Pagination**: You can page through results using `limit` and `offset` parameters (limit=records per page, offset=starting position).

⚠️ **CRITICAL - Never Manually Aggregate Data**: IMPORTANT: Never sum data yourself, only take the data verbatim from the tool. NEVER aggregate totals yourself to answer a question if you do not have the values already aggregated from the tool. Do NOT sum up individual records, calculate country-wide statistics from subnational data, or aggregate across time periods/demographics yourself. If data is not pre-aggregated, inform the user that aggregate data is not available. Always use the most appropriate administrative level that has pre-aggregated data.

**Query Parameters:**

- **app_identifier** (Required): base64 encoded application name and email, as in `base64("app_name:email")`. This value can also be passed in the `X-HDX-HAPI-APP-IDENTIFIER` header. See the *encoded_app_identifier* endpoint.

- **has_hrp**: Filter the response by the has_hrp flag. The has_hrp flag indicates whether a country has a Humanitarian Response Plan.

- **in_gho**: Filter the response by the in_gho flag. The in_gho flag indicates whether a country is in the <a href="https://humanitarianaction.info/">Global Humanitarian Overview</a>.

- **start_date**: Filter entries to include rows where the reference period overlaps with or extends beyond this date, e.g. 2020, 2020-01, 2020-01-01 or 2020-01-01T00:00:00

- **end_date**: Filter entries to include rows where the reference period overlaps with or begins prior to this date, e.g. 2020, 2020-01, 2020-01-01, 2020-01-01 or 2020-01-01T23:59:59

- **location_code**: Filter the response by a location (typically a country). The location codes use the ISO-3 (ISO 3166 alpha-3) codes. Use the metadata_location_get tool to get available location codes and names.

- **location_name**: Filter the response by a location (typically a country). The location names are based on the "short name" from the <a href="https://unstats.un.org/unsd/methodology/m49/#fn2">UN M49 Standard</a>. Use the metadata_location_get tool to get available location codes and names.

- **admin1_code**: Filter the response by the 1st subnational administrative divisions. The admin1 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>. Use the metadata_admin1_get tool to get available admin1 codes and names.

- **admin1_name**: Filter the response by the 1st subnational administrative divisions. The admin1 names refer to either the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a> or those provided in the original data source. Use the metadata_admin1_get tool to get available admin1 codes and names.

- **admin2_code**: Filter the response by the 2nd subnational administrative divisions. The admin2 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>. Use the metadata_admin2_get tool to get available admin2 codes and names.

- **admin2_name**: Filter the response by the 2nd subnational administrative divisions. The admin2 names refer to either the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a> or those provided in the original data source. Use the metadata_admin2_get tool to get available admin2 codes and names.

- **admin_level**: Filter the response by admin level.

- **output_format**: No description.

- **limit**: Maximum number of records to return. The system will not return more than 10,000 records.

- **offset**: Number of records to skip in the response. Use in conjunction with the limit parameter to paginate.

**Responses:**

- **200** (Success): Successful Response
  - Content-Type: `application/json`

  - **Response Properties:**

  - **Example:**
```json
{
  "data": [
    {
      "location_code": "string",
      "location_name": "string",
      "admin1_code": "unknown_type",
      "admin_level": 1,
      "reference_period_end": "unknown_type",
      "assessment_type": "BA",
      "admin2_name": "unknown_type",
      "admin1_name": "unknown_type",
      "resource_hdx_id": "string",
      "population": 1,
      "operation": "string",
      "reference_period_start": "2024-01-01T12:00:00Z",
      "reporting_round": 1,
      "admin2_code": "unknown_type"
    }
  ]
}
```

- **400**: Bad Request
  - Content-Type: `application/json`

  - **Response Properties:**

  - **Example:**
```json
{
  "detail": "string"
}
```

- **422**: Validation Error
  - Content-Type: `application/json`

  - **Response Properties:**

  - **Example:**
```json
{
  "detail": [
    {
      "loc": [
        "unknown_type"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

- **500**: Internal Server Error
  - Content-Type: `application/json`

  - **Response Properties:**

  - **Example:**
```json
{
  "error_sample_list": [
    "unknown"
  ],
  "error": "string"
}
```
Parameters|Type|Description
-|-|-
`admin1_code`|`string` *optional*|Filter the response by the 1st subnational administrative divisions. The admin1 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>. Use the metadata_admin1_get tool to get available admin1 codes and names.
`admin1_name`|`string` *optional*|Filter the response by the 1st subnational administrative divisions. The admin1 names refer to either the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a> or those provided in the original data source. Use the metadata_admin1_get tool to get available admin1 codes and names.
`admin2_code`|`string` *optional*|Filter the response by the 2nd subnational administrative divisions. The admin2 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>. Use the metadata_admin2_get tool to get available admin2 codes and names.
`admin2_name`|`string` *optional*|Filter the response by the 2nd subnational administrative divisions. The admin2 names refer to either the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a> or those provided in the original data source. Use the metadata_admin2_get tool to get available admin2 codes and names.
`admin_level`|`string` *optional*|Filter the response by admin level.
`end_date`|`string` *optional*|Filter entries to include rows where the reference period overlaps with or begins prior to this date, e.g. 2020, 2020-01, 2020-01-01, 2020-01-01 or 2020-01-01T23:59:59
`has_hrp`|`string` *optional*|Filter the response by the has_hrp flag. The has_hrp flag indicates whether a country has a Humanitarian Response Plan.
`in_gho`|`string` *optional*|Filter the response by the in_gho flag. The in_gho flag indicates whether a country is in the <a href="https://humanitarianaction.info/">Global Humanitarian Overview</a>.
`limit`|`integer` *optional*|Maximum number of records to return. The system will not return more than 10,000 records.
`location_code`|`string` *optional*|Filter the response by a location (typically a country). The location codes use the ISO-3 (ISO 3166 alpha-3) codes. Use the metadata_location_get tool to get available location codes and names.
`location_name`|`string` *optional*|Filter the response by a location (typically a country). The location names are based on the "short name" from the <a href="https://unstats.un.org/unsd/methodology/m49/#fn2">UN M49 Standard</a>. Use the metadata_location_get tool to get available location codes and names.
`offset`|`integer` *optional*|Number of records to skip in the response. Use in conjunction with the limit parameter to paginate.
`output_format`|`string` *optional*|
`start_date`|`string` *optional*|Filter entries to include rows where the reference period overlaps with or extends beyond this date, e.g. 2020, 2020-01, 2020-01-01 or 2020-01-01T00:00:00

---
#### Tool: **`affected_people_refugees_get`**
UNHCR's Refugee data provides information about displaced people in a crisis. See the more detailed technical <a href="https://hdx-hapi.readthedocs.io/en/latest/data_usage_guides/affected_people/#refugees-persons-of-concern">HDX HAPI documentation</a>, and the <a href="https://data.humdata.org/dataset/unhcr-population-data-for-world">original HDX source</a> website.

**Query Parameters:**

- **app_identifier** (Required): base64 encoded application name and email, as in `base64("app_name:email")`. This value can also be passed in the `X-HDX-HAPI-APP-IDENTIFIER` header. See the *encoded_app_identifier* endpoint.

- **population_group**: Filter the response by the population group, available values are described <a href="https://hdx-hapi.readthedocs.io/en/latest/data_usage_guides/enums/#population-group">here.</a>

- **population_min**: Filter the response by a lower bound for the population.

- **population_max**: Filter the response by a upper bound for the population.

- **gender**: Filter the response by the gender, available values are described <a href="https://hdx-hapi.readthedocs.io/en/latest/data_usage_guides/enums/#gender">here.</a>

- **age_range**: Filter the response by the age range. These are expressed as [start age]-[end age], or [start age]+ for an age range starting at [start age] or above. The end age is assumed to be inclusive, though that is not always explicit in the source data.

- **origin_location_code**: Filter the response by a location (typically a country). The location codes use the ISO-3 (ISO 3166 alpha-3) codes. Use the metadata_location_get tool to get available location codes and names.

- **origin_location_name**: F

[...]

## Screenshots

![Humanitarian Data Exchange screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/hdx-1.png)
