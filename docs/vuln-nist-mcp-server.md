This MCP server exposes tools to query the NVD/CVE REST API and return formatted text results suitable for LLM consumption via the MCP protocol. It includes automatic query chunking for large date ranges and parallel processing for improved performance.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/vuln-nist-mcp-server](https://hub.docker.com/repository/docker/mcp/vuln-nist-mcp-server)
**Author**|[HaroldFinchIFT](https://github.com/HaroldFinchIFT)
**Repository**|https://github.com/HaroldFinchIFT/vuln-nist-mcp-server

## Available Tools (6)
Tools provided by this Server|Short Description
-|-
`cve_change_history`|Retrieve change history for a CVE or a time window.|
`cves_by_cpe`|List CVEs associated with a specific CPE|
`get_cve_by_id`|Retrieve a CVE by its CVE-ID|
`get_temporal_context`|Get current date and temporal context when it needed.|
`kevs_between`|List CVEs added to CISA KEV catalog in a date window.|
`search_cves`|Search CVEs by keyword in description, with flexible time filtering.|

---
## Tools Details

#### Tool: **`cve_change_history`**
Retrieve change history for a CVE or a time window.
    If no cve_id is provided and the date range exceeds 120 days,
    the query is split into multiple chunks (max 120 days each) and results aggregated.
Parameters|Type|Description
-|-|-
`changeEndDate`|`string` *optional*|
`changeStartDate`|`string` *optional*|
`cve_id`|`string` *optional*|
`resultsPerPage`|`string` *optional*|
`startIndex`|`string` *optional*|

---
#### Tool: **`cves_by_cpe`**
List CVEs associated with a specific CPE
Parameters|Type|Description
-|-|-
`cpe_name`|`string` *optional*|
`is_vulnerable`|`string` *optional*|

---
#### Tool: **`get_cve_by_id`**
Retrieve a CVE by its CVE-ID
Parameters|Type|Description
-|-|-
`cve_id`|`string` *optional*|

---
#### Tool: **`get_temporal_context`**
Get current date and temporal context when it needed.

    **USAGE**: Call this tool FIRST when user asks for time-relative question like "this year", "last year", "6 months ago", etc.

    Returns current date context and examples for constructing specific date parameters.
#### Tool: **`kevs_between`**
List CVEs added to CISA KEV catalog in a date window.
    If the requested window exceeds 90 days, the query is automatically
    split into multiple chunks (max 90 days each) and results are aggregated.
Parameters|Type|Description
-|-|-
`kevEndDate`|`string` *optional*|
`kevStartDate`|`string` *optional*|
`resultsPerPage`|`string` *optional*|
`startIndex`|`string` *optional*|

---
#### Tool: **`search_cves`**
Search CVEs by keyword in description, with flexible time filtering.

    **IMPORTANT**: For time-relative queries (this year, last year, etc.), call get_temporal_context() FIRST to get current date information.

    **Date filtering logic (in priority order):**
    - If start_date and end_date are provided → use them directly
    - Else if last_days is provided → calculate start_date = now - last_days
    - Else fallback to last 30 days

    **Technical notes:**
    - If the time period > 120 days, queries are split into 120-day chunks
    - start_date, end_date: Use ISO 8601 format: "YYYY-MM-DDTHH:MM:SS"
    - recent_days parameter is deprecated, use last_days instead.
Parameters|Type|Description
-|-|-
`end_date`|`string` *optional*|
`keyword`|`string` *optional*|
`last_days`|`string` *optional*|
`recent_days`|`string` *optional*|
`resultsPerPage`|`integer` *optional*|
`startIndex`|`integer` *optional*|
`start_date`|`string` *optional*|

---
