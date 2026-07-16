Real-time network monitoring, security analysis, and firewall management through 28 specialized tools. Access security alerts, network flows, device status, and firewall rules directly from your Firewalla device.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/firewalla-mcp-server](https://hub.docker.com/repository/docker/mcp/firewalla-mcp-server)
**Author**|[amittell](https://github.com/amittell)
**Repository**|https://github.com/amittell/firewalla-mcp-server

## Available Tools (28)
Tools provided by this Server|Short Description
-|-
`create_target_list`|Create a new target list|
`delete_target_list`|Delete a target list|
`get_active_alarms`|Retrieve current security alerts and alarms from Firewalla firewall|
`get_alarm_trends`|Get historical alarm trend data (alarms generated per day)|
`get_bandwidth_usage`|Get top bandwidth consuming devices (convenience wrapper around get_device_status)|
`get_boxes`|Retrieve list of Firewalla boxes|
`get_device_status`|Check online/offline status of devices on Firewalla network|
`get_flow_data`|Query network traffic flows from Firewalla firewall|
`get_flow_insights`|Get category-based flow analysis including top content categories, bandwidth consumers, and blocked traffic.|
`get_network_rules`|Retrieve firewall rules and conditions|
`get_network_rules_summary`|Get overview statistics and counts of network rules by category (convenience wrapper)|
`get_offline_devices`|Get all offline devices (convenience wrapper around get_device_status)|
`get_recent_flow_activity`|Get recent network flow activity snapshot (last 10-20 minutes).|
`get_rule_trends`|Get historical rule trend data (rules created per day)|
`get_simple_statistics`|Retrieve basic statistics overview|
`get_specific_alarm`|Get detailed information for a specific Firewalla alarm|
`get_specific_target_list`|Retrieve a specific target list by ID|
`get_statistics_by_box`|Get statistics for each Firewalla box (top boxes by blocked flows or security alarms)|
`get_statistics_by_region`|Retrieve statistics by region (top regions by blocked flows)|
`get_target_lists`|Retrieve all target lists from Firewalla|
`pause_rule`|Temporarily disable an active firewall rule for a specified duration|
`resume_rule`|Resume a previously paused firewall rule, restoring it to active state|
`search_alarms`|Search alarms using full-text or field filters.|
`search_devices`|Search devices by name, IP, MAC or status (convenience wrapper with client-side filtering)|
`search_flows`|Search network flows with advanced query filters.|
`search_rules`|Search firewall rules by target, action or status.|
`search_target_lists`|Search target lists with client-side filtering (convenience wrapper around get_target_lists)|
`update_target_list`|Update an existing target list|

---
## Tools Details

#### Tool: **`create_target_list`**
Create a new target list
Parameters|Type|Description
-|-|-
`name`|`string`|Target list name (required, max 24 chars)
`owner`|`string`|Owner: "global" or box GID (required)
`targets`|`array`|Array of domains, IPs, or CIDR ranges (required)
`category`|`string` *optional*|Content category (optional)
`notes`|`string` *optional*|Additional description (optional)

---
#### Tool: **`delete_target_list`**
Delete a target list
Parameters|Type|Description
-|-|-
`id`|`string`|Target list ID to delete (required)

---
#### Tool: **`get_active_alarms`**
Retrieve current security alerts and alarms from Firewalla firewall
Parameters|Type|Description
-|-|-
`cursor`|`string` *optional*|Pagination cursor from previous response
`groupBy`|`string` *optional*|Group alarms by field (e.g., type, box)
`limit`|`number` *optional*|Results per page (optional, default: 200, API maximum: 500)
`query`|`string` *optional*|Search query for filtering alarms (default: status:1 for active). Use type:N where N is: 1=Security Activity, 2=Abnormal Upload, 3=Large Bandwidth Usage, 4=Monthly Data Plan, 5=New Device, 6=Device Back Online, 7=Device Offline, 8=Video Activity, 9=Gaming Activity, 10=Porn Activity, 11=VPN Activity, 12=VPN Connection Restored, 13=VPN Connection Error, 14=Open Port, 15=Internet Connectivity Update, 16=Large Upload. Examples: type:8 (video), type:10 (porn), region:US, source_ip:*
`sortBy`|`string` *optional*|Sort alarms (default: ts:desc)

---
#### Tool: **`get_alarm_trends`**
Get historical alarm trend data (alarms generated per day)
Parameters|Type|Description
-|-|-
`group`|`string` *optional*|Get trends for a specific box group

---
#### Tool: **`get_bandwidth_usage`**
Get top bandwidth consuming devices (convenience wrapper around get_device_status)
Parameters|Type|Description
-|-|-
`period`|`string`|Time period for bandwidth calculation
`box`|`string` *optional*|Filter devices under a specific Firewalla box
`limit`|`number` *optional*|Number of top devices to return

---
#### Tool: **`get_boxes`**
Retrieve list of Firewalla boxes
Parameters|Type|Description
-|-|-
`group`|`string` *optional*|Get boxes within a specific group (requires group ID)

---
#### Tool: **`get_device_status`**
Check online/offline status of devices on Firewalla network
Parameters|Type|Description
-|-|-
`limit`|`number`|Maximum number of devices to return (required)
`box`|`string` *optional*|Get devices under a specific Firewalla box (requires box ID)
`group`|`string` *optional*|Get devices under a specific box group (requires group ID)

---
#### Tool: **`get_flow_data`**
Query network traffic flows from Firewalla firewall
Parameters|Type|Description
-|-|-
`cursor`|`string` *optional*|Pagination cursor from previous response
`groupBy`|`string` *optional*|Group flows by specified values (e.g., "domain,box")
`limit`|`number` *optional*|Maximum results (optional, default: 200, API maximum: 500)
`query`|`string` *optional*|Search query for flows. Supports region:US for geographic filtering, protocol:tcp, blocked:true, domain:*, category:social, etc.
`sortBy`|`string` *optional*|Sort flows (default: "ts:desc")

---
#### Tool: **`get_flow_insights`**
Get category-based flow analysis including top content categories, bandwidth consumers, and blocked traffic. Ideal for answering questions like "what porn sites were accessed" or "what social media was used". Replaces time-based trends with actionable insights.
Parameters|Type|Description
-|-|-
`categories`|`array` *optional*|Filter to specific content categories (optional)
`include_blocked`|`boolean` *optional*|Include blocked traffic analysis (default: false)
`period`|`string` *optional*|Time period for analysis (default: 24h)

---
#### Tool: **`get_network_rules`**
Retrieve firewall rules and conditions
Parameters|Type|Description
-|-|-
`limit`|`number`|Maximum number of rules to return (required)
`query`|`string` *optional*|Search conditions for filtering rules

---
#### Tool: **`get_network_rules_summary`**
Get overview statistics and counts of network rules by category (convenience wrapper)
Parameters|Type|Description
-|-|-
`active_only`|`boolean` *optional*|Only include active rules in summary (default: true)
`rule_type`|`string` *optional*|Filter by rule type

---
#### Tool: **`get_offline_devices`**
Get all offline devices (convenience wrapper around get_device_status)
Parameters|Type|Description
-|-|-
`box`|`string` *optional*|Filter devices under a specific Firewalla box
`limit`|`number` *optional*|Maximum number of offline devices to return
`sort_by_last_seen`|`boolean` *optional*|Sort devices by last seen time (default: true)

---
#### Tool: **`get_recent_flow_activity`**
Get recent network flow activity snapshot (last 10-20 minutes). Returns up to 50 most recent flows for immediate analysis. CRITICAL: This is a quick snapshot tool only. Use this for: "what's happening right now?", current security threats, immediate network issues. DO NOT use for: historical analysis (use search_flows), getting more than 50 flows (use search_flows with limit), daily/weekly patterns (use search_flows with time queries like "ts:>24h"). For comprehensive analysis, always prefer search_flows.
#### Tool: **`get_rule_trends`**
Get historical rule trend data (rules created per day)
Parameters|Type|Description
-|-|-
`group`|`string` *optional*|Get trends for a specific box group

---
#### Tool: **`get_simple_statistics`**
Retrieve basic statistics overview
Parameters|Type|Description
-|-|-
`group`|`string` *optional*|Get statistics for specific box group

---
#### Tool: **`get_specific_alarm`**
Get detailed information for a specific Firewalla alarm
Parameters|Type|Description
-|-|-
`alarm_id`|`string`|Alarm ID (required for API call)

---
#### Tool: **`get_specific_target_list`**
Retrieve a specific target list by ID
Parameters|Type|Description
-|-|-
`id`|`string`|Target list ID (required)

---
#### Tool: **`get_statistics_by_box`**
Get statistics for each Firewalla box (top boxes by blocked flows or security alarms)
Parameters|Type|Description
-|-|-
`group`|`string` *optional*|Get statistics for specific box group
`limit`|`number` *optional*|Maximum number of results (optional, default: 5)
`type`|`string` *optional*|Statistics type to retrieve

---
#### Tool: **`get_statistics_by_region`**
Retrieve statistics by region (top regions by blocked flows)
Parameters|Type|Description
-|-|-
`group`|`string` *optional*|Get statistics for specific box group
`limit`|`number` *optional*|Maximum number of results (optional, default: 5)

---
#### Tool: **`get_target_lists`**
Retrieve all target lists from Firewalla
Parameters|Type|Description
-|-|-
`limit`|`number`|Maximum number of target lists to return (required)

---
#### Tool: **`pause_rule`**
Temporarily disable an active firewall rule for a specified duration
Parameters|Type|Description
-|-|-
`box`|`string`|Box GID for context (required by API)
`rule_id`|`string`|Rule ID to pause
`duration`|`number` *optional*|Duration in minutes to pause the rule (optional, default: 60, range: 1-1440)

---
#### Tool: **`resume_rule`**
Resume a previously paused firewall rule, restoring it to active state
Parameters|Type|Description
-|-|-
`box`|`string`|Box GID for context (required by API)
`rule_id`|`string`|Rule ID to resume

---
#### Tool: **`search_alarms`**
Search alarms using full-text or field filters. Alarm types: 1=Security Activity, 2=Abnormal Upload, 3=Large Bandwidth Usage, 4=Monthly Data Plan, 5=New Device, 6=Device Back Online, 7=Device Offline, 8=Video Activity, 9=Gaming Activity, 10=Porn Activity, 11=VPN Activity, 12=VPN Connection Restored, 13=VPN Connection Error, 14=Open Port, 15=Internet Connectivity Update, 16=Large Upload.
Parameters|Type|Description
-|-|-
`cursor`|`string` *optional*|Pagination cursor from previous response
`groupBy`|`string` *optional*|Group alarms by specified fields (comma-separated)
`limit`|`number` *optional*|Maximum results (optional, default: 200, API maximum: 500)
`query`|`string` *optional*|Search query using Firewalla syntax. Supported fields: type:1-16 (see alarm types above), resolved:true/false, status:1/2 (active/archived), source_ip:192.168.*, region:US (country code), gid:box_id, device.name:*, message:"text search". Examples: "type:8 AND region:US" (video from US), "type:10 AND status:1" (active porn alerts), "source_ip:192.168.* AND NOT resolved:true"
`sortBy`|`string` *optional*|Sort alarms (default: ts:desc)

---
#### Tool: **`search_devices`**
Search devices by name, IP, MAC or status (convenience wrapper with client-side filtering)
Parameters|Type|Description
-|-|-
`box`|`string` *optional*|Filter devices under a specific Firewalla box
`limit`|`number` *optional*|Maximum number of devices to return
`query`|`string` *optional*|Search query using Firewalla syntax. Supported fields: mac:AA:BB:CC:DD:EE:FF, ip:192.168.1.*, name:*iPhone*, online:true/false, vendor:Apple, gid:box_id, network.name:*, group.name:*. Examples: "online:false AND vendor:Apple", "ip:192.168.1.* AND name:*laptop*", "mac:AA:* OR name:*phone*"
`status`|`string` *optional*|Filter by online status

---
#### Tool: **`search_flows`**
Search network flows with advanced query filters. Use this for: historical analysis, specific time ranges, complex filtering, or when you need more than 50 flows. Supports pagination, time-based queries (e.g., "ts:>1h" for last hour), and all flow fields including geographic filtering. For quick "what's happening now" snapshots, use get_recent_flow_activity instead.
Parameters|Type|Description
-|-|-
`cursor`|`string` *optional*|Pagination cursor from previous response
`groupBy`|`string` *optional*|Group flows by specified values (e.g., "domain,box")
`limit`|`number` *optional*|Maximum results (optional, default: 200, API maximum: 500)
`query`|`string` *optional*|Search query using Firewalla syntax. Supported fields: protocol:tcp/udp, direction:inbound/outbound/local, blocked:true/false, bytes:>1MB, domain:*.example.com, region:US (country code), category:social/games/porn/etc, gid:box_id, device.ip:192.168.*, source_ip:*, destination_ip:*. Examples: "region:US AND protocol:tcp", "blocked:true AND bytes:>1MB", "category:social OR category:games"
`sortBy`|`string` *optional*|Sort flows (default: "ts:desc")

---
#### Tool: **`search_rules`**
Search firewall rules by target, action or status. Supports all rule fields.
Parameters|Type|Description
-|-|-
`query`|`string` *optional*|Search query using Firewalla syntax. Supported fields: action:allow/block/timelimit, target.type:domain/ip/device, target.value:*.facebook.com, status:active/paused, direction:bidirection/inbound/outbound, protocol:tcp/udp, gid:box_id, scope.type:device/network, notes:"description text". Examples: "action:block AND target.value:*.social.com", "status:paused", "target.type:domain AND action:block"

---
#### Tool: **`search_target_lists`**
Search target lists with client-side filtering (convenience wrapper around get_target_lists)
Parameters|Type|Description
-|-|-
`category`|`string` *optional*|Filter by category
`limit`|`number` *optional*|Maximum number of target lists to return
`owner`|`string` *optional*|Filter by owner (global or box gid)
`query`|`string` *optional*|Search query for target lists. Supported fields: name:*Social*, owner:global/box_gid, category:social/games/ad/porn/etc, targets:*.facebook.com, notes:"description text". Examples: "category:social", "owner:global AND name:*Block*", "targets:*.gaming.com"

---
#### Tool: **`update_target_list`**
Update an existing target list
Parameters|Type|Description
-|-|-
`id`|`string`|Target list ID (required)
`category`|`string` *optional*|Updated content category
`name`|`string` *optional*|Updated target list name (max 24 chars)
`notes`|`string` *optional*|Updated description
`targets`|`array` *optional*|Updated array of domains, IPs, or CIDR ranges

---
