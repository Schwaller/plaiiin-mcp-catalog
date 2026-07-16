A Model Context Protocol server that provides access to Shodan API functionality.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/cyreslab-ai-shodan](https://hub.docker.com/repository/docker/mcp/cyreslab-ai-shodan)
**Author**|[Cyreslab-AI](https://github.com/Cyreslab-AI)
**Repository**|https://github.com/Cyreslab-AI/shodan-mcp-server

## Available Tools (5)
Tools provided by this Server|Short Description
-|-
`get_host_info`|Get detailed information about a specific IP address|
`get_ssl_info`|Get SSL certificate information for a domain|
`scan_network_range`|Scan a network range (CIDR notation) for devices|
`search_iot_devices`|Search for specific types of IoT devices|
`search_shodan`|Search Shodan's database for devices and services|

---
## Tools Details

#### Tool: **`get_host_info`**
Get detailed information about a specific IP address
Parameters|Type|Description
-|-|-
`ip`|`string`|IP address to look up
`fields`|`array` *optional*|List of fields to include in the results (e.g., ['ip_str', 'ports', 'location.country_name'])
`max_items`|`number` *optional*|Maximum number of items to include in arrays (default: 5)

---
#### Tool: **`get_ssl_info`**
Get SSL certificate information for a domain
Parameters|Type|Description
-|-|-
`domain`|`string`|Domain name to look up SSL certificates for (e.g., example.com)

---
#### Tool: **`scan_network_range`**
Scan a network range (CIDR notation) for devices
Parameters|Type|Description
-|-|-
`cidr`|`string`|Network range in CIDR notation (e.g., 192.168.1.0/24)
`fields`|`array` *optional*|List of fields to include in the results (e.g., ['ip_str', 'ports', 'location.country_name'])
`max_items`|`number` *optional*|Maximum number of items to include in results (default: 5)

---
#### Tool: **`search_iot_devices`**
Search for specific types of IoT devices
Parameters|Type|Description
-|-|-
`device_type`|`string`|Type of IoT device to search for (e.g., 'webcam', 'router', 'smart tv')
`country`|`string` *optional*|Optional country code to limit search (e.g., 'US', 'DE')
`max_items`|`number` *optional*|Maximum number of items to include in results (default: 5)

---
#### Tool: **`search_shodan`**
Search Shodan's database for devices and services
Parameters|Type|Description
-|-|-
`query`|`string`|Shodan search query (e.g., 'apache country:US')
`facets`|`array` *optional*|List of facets to include in the search results (e.g., ['country', 'org'])
`fields`|`array` *optional*|List of fields to include in the results (e.g., ['ip_str', 'ports', 'location.country_name'])
`max_items`|`number` *optional*|Maximum number of items to include in arrays (default: 5)
`page`|`number` *optional*|Page number for results pagination (default: 1)
`summarize`|`boolean` *optional*|Whether to return a summary of the results instead of the full data (default: false)

---

## Screenshots

![Shodan screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/cyreslab-ai-shodan-1.png)
