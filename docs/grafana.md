MCP server for Grafana.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/grafana](https://hub.docker.com/repository/docker/mcp/grafana)
**Author**|[grafana](https://github.com/grafana)
**Repository**|https://github.com/grafana/mcp-grafana

## Available Tools (65)
Tools provided by this Server|Short Description
-|-
`add_activity_to_incident`|Add activity to incident|
`alerting_manage_routing`|Manage alerting routing|
`alerting_manage_rules`|Manage alert rules|
`analyze_loki_labels`|Analyze Loki label strategy|
`check_datasources_health`|Check datasources health|
`create_annotation`|Create Annotation|
`create_datasource`|Create datasource|
`create_folder`|Create folder|
`create_incident`|Create incident|
`create_snapshot`|Create snapshot|
`delete_snapshot`|Delete snapshot|
`find_error_pattern_logs`|Find error patterns in logs|
`find_slow_requests`|Find slow requests|
`generate_deeplink`|Generate navigation deeplink|
`get_alert_group`|Get IRM alert group|
`get_annotation_tags`|Get Annotation Tags|
`get_annotations`|Get Annotations|
`get_assertions`|Get assertions summary|
`get_current_oncall_users`|Get current on-call users|
`get_dashboard_by_uid`|Get dashboard details|
`get_dashboard_panel_queries`|Get dashboard panel queries|
`get_dashboard_property`|Get dashboard property|
`get_dashboard_summary`|Get dashboard summary|
`get_datasource`|Get datasource|
`get_incident`|Get incident details|
`get_oncall_shift`|Get OnCall shift|
`get_panel_image`|Get panel or dashboard image|
`get_plugin`|Get plugin|
`get_sift_analysis`|Get Sift analysis|
`get_sift_investigation`|Get Sift investigation|
`get_snapshot`|Get snapshot|
`grafana_api_request`|Grafana API request|
`install_plugin`|Install plugin|
`list_alert_groups`|List IRM alert groups|
`list_datasources`|List datasources|
`list_incidents`|List incidents|
`list_loki_label_names`|List Loki label names|
`list_loki_label_values`|List Loki label values|
`list_oncall_schedules`|List OnCall schedules|
`list_oncall_teams`|List OnCall teams|
`list_oncall_users`|List OnCall users|
`list_prometheus_label_names`|List Prometheus label names|
`list_prometheus_label_values`|List Prometheus label values|
`list_prometheus_metric_metadata`|List Prometheus metric metadata|
`list_prometheus_metric_names`|List Prometheus metric names|
`list_provisioning_repositories`|List provisioning repositories|
`list_pyroscope_label_names`|List Pyroscope label names|
`list_pyroscope_label_values`|List Pyroscope label values|
`list_pyroscope_profile_types`|List Pyroscope profile types|
`list_sift_investigations`|List Sift investigations|
`list_snapshots`|List snapshots|
`query_loki_logs`|Query Loki logs|
`query_loki_patterns`|Query Loki patterns|
`query_loki_stats`|Get Loki log statistics|
`query_prometheus`|Query Prometheus metrics|
`query_prometheus_histogram`|Query Prometheus histogram percentile|
`query_pyroscope`|Query Pyroscope|
`search_dashboards`|Search dashboards|
`search_folders`|Search folders|
`search_plugin_information`|Search plugins|
`suggest_loki_alloy_label_config`|Suggest Alloy label enforcement config|
`update_annotation`|Update Annotation|
`update_dashboard`|Create or update dashboard|
`update_datasource`|Update datasource|
`validate_provisioning_file`|Validate provisioning file|

---
## Tools Details

#### Tool: **`add_activity_to_incident`**
Add a note (userNote activity) to an existing incident's timeline using its ID. The note body can include URLs which will be attached as context. Use this to add context to an incident.
Parameters|Type|Description
-|-|-
`body`|`string`|The body of the activity. URLs will be parsed and attached as context
`incidentId`|`string`|The ID of the incident to add the activity to
`eventTime`|`string` *optional*|The time that the activity occurred. If not provided, the current time will be used

---
#### Tool: **`alerting_manage_routing`**
Manage Grafana alerting routing configuration, including notification policies, contact points and time intervals.

Notification policies define how alerts are grouped, routed, and which contact points receive them.
Time intervals define active/mute periods for alert notifications.

When to use:
- Understanding how alerts are routed to contact points/receivers
- Debugging why an alert went to a specific receiver
- Checking grouping, timing, or mute interval settings

When NOT to use:
- Checking alert rule configuration or state (use alerting_manage_rules)
Parameters|Type|Description
-|-|-
`operation`|`string`|The operation to perform: 'get_notification_policies' to retrieve the notification policy tree, 'get_contact_points' to list all contact points, 'get_contact_point' to get a specific contact point by name, 'get_time_intervals' to list all time intervals, 'get_time_interval' to get a specific time interval by name
`contact_point_title`|`string` *optional*|Title of the contact point to retrieve (required for get_contact_point operation)
`datasource_uid`|`string` *optional*|Optional: UID of an Alertmanager-compatible datasource to query for receivers. If omitted, returns Grafana-managed contact points. Only used with get_contact_points.
`limit`|`integer` *optional*|The maximum number of results to return. Default is 100. Only used with get_contact_points.
`name`|`string` *optional*|Filter contact points by name (exact match). Only used with get_contact_points.
`time_interval_name`|`string` *optional*|Name of the time interval to retrieve (required for get_time_interval operation)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`alerting_manage_rules`**
Manage Grafana alert rules with full CRUD capabilities and filtering.

When to use:
- Understanding why an alert is or isn't firing
- Auditing alert rule configuration (queries, conditions, labels, notification settings)
- Finding alert rules by state, folder, group, or name
- Creating, updating, or deleting alert rules
- Comparing rule versions to see what changed

When NOT to use:
- Checking how alerts are routed to receivers (use alerting_manage_routing)
Parameters|Type|Description
-|-|-
`operation`|`string`|The operation to perform: 'list', 'get', 'versions', 'create', 'update', or 'delete'. To create a rule, use operation 'create' and provide all required fields in a single call. To update a rule, first use 'get' to retrieve its full configuration, then 'update' with all required fields plus your changes.
`annotations`|`object` *optional*|Optional annotations for the alert rule
`condition`|`string` *optional*|The query condition identifier, e.g. 'A', 'B' (required for 'create', 'update')
`data`|`array` *optional*|Array of alert query objects (required for 'create'/'update'). Each object has: datasourceUid (string, required), model (object with expr for data queries or type/expression/conditions for expressions), refId (string, auto-assigned if omitted), relativeTimeRange ({from, to} in seconds, defaults to {from:600,to:0}). For server-side expressions use datasourceUid '__expr__'. Example: [{datasourceUid: 'prometheus', model: {expr: 'up == 0'}}, {datasourceUid: '__expr__', model: {type: 'threshold', expression: 'A', conditions: [{evaluator: {type: 'gt', params: [0]}}]}}]
`datasource_uid`|`string` *optional*|Optional: UID of a Prometheus or Loki datasource to query for datasource-managed alert rules (for 'list' operation)
`disable_provenance`|`boolean` *optional*|If true, the alert remains editable in the Grafana UI (sets X-Disable-Provenance header). Defaults to true.
`exec_err_state`|`string` *optional*|State on execution error: NoData, Alerting, OK (required for 'create', 'update')
`folder_uid`|`string` *optional*|The folder UID. For 'list': filter by exact folder UID (mutually exclusive with search_folder). For 'create'/'update': the folder to store the rule in (required).
`for`|`string` *optional*|Duration before alert fires, e.g. '5m' (required for 'create', 'update')
`is_paused`|`boolean` *optional*|If true, the alert rule remains inactive, Default is false
`keep_firing_for`|`string` *optional*|Enables continous firing of alert for specified time even when condition is no longer met. Default is 0 (resolves immediately)
`label_selectors`|`array` *optional*|Prometheus-style selectors to filter alert rules by labels. Each string is a selector e.g. '{severity="critical", team=~"backend.*"}'. All selectors must match (AND).
`labels`|`object` *optional*|Optional labels for the alert rule
`limit_alerts`|`integer` *optional*|Limit alert instances per rule. For list: 0 omits alerts. For get: <=0 defaults to 200. Max 200.
`matchers`|`array` *optional*|Label matchers to filter alert instances. Each string is a Prometheus-style matcher e.g. 'severity="critical"', 'env!="dev"', 'team=~"backend.*"'. Requires Grafana 12.4+.
`missing_series_evals_to_resolve`|`integer` *optional*|Consecutive evaluation intervals with no data required to mark the alert as resolved. Default is 2.
`no_data_state`|`string` *optional*|State when no data: NoData, Alerting, OK (required for 'create', 'update')
`notification_settings`|`object` *optional*|Notification settings object. Fields: receiver (string, required), groupBy ([]string), groupWait/groupInterval/repeatInterval (duration strings), muteTimeIntervals/activeTimeIntervals ([]string).
`org_id`|`integer` *optional*|The organization ID (required for 'create', 'update')
`record`|`object` *optional*|Recording rule config. Fields: from (string, required - ref ID e.g. 'A'), metric (string, required - metric name), targetDatasourceUid (string, optional).
`rule_group`|`string` *optional*|The rule group name (required for 'create', 'update')
`rule_limit`|`integer` *optional*|Maximum number of rules to return (default 200, max 200). Requires Grafana 12.4+ (for 'list' operation)
`rule_type`|`string` *optional*|Filter by rule type (for 'list' operation)
`rule_uid`|`string` *optional*|The UID of the alert rule (required for 'get', 'versions', 'update', 'delete'; optional for 'create')
`search_folder`|`string` *optional*|Search folders by path using partial matching (for 'list' operation). Requires Grafana 12.4+. Mutually exclusive with folder_uid.
`search_rule_name`|`string` *optional*|Search alert rule names/titles using partial matching. Requires Grafana 12.4+ (for 'list' operation)
`states`|`array` *optional*|Filter by alert state: firing, pending, normal, recovering, nodata, error (for 'list' operation)
`title`|`string` *optional*|The title of the alert rule (required for 'create', 'update')

*This tool may perform destructive updates.*

---
#### Tool: **`analyze_loki_labels`**
Audits a Loki label strategy and optionally diagnoses query performance. Returns per-label verdicts, missing base labels, normalisation issues, and a recommended set. Pass datasourceUid for live cardinality or labels for static scoring; both may be combined.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string` *optional*|Datasource UID (live mode).
`endRfc3339`|`string` *optional*|
`expectedBaseLabels`|`array` *optional*|
`labels`|`array` *optional*|Caller-supplied labels (static mode).
`maxLabels`|`integer` *optional*|
`perfMetrics`|`object` *optional*|Runtime metrics; presence triggers perf diagnosis.
`selector`|`string` *optional*|Optional LogQL selector for stats / perf diagnosis.
`startRfc3339`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`check_datasources_health`**
Check datasource health. Filter by type or UIDs; omit both to check all.
Parameters|Type|Description
-|-|-
`offset`|`integer` *optional*|Number to skip for pagination
`type`|`string` *optional*|Plugin type filter; omit to check all
`uids`|`array` *optional*|UIDs to check

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`create_annotation`**
Create a new annotation on a dashboard or panel. Set format to 'graphite' and provide 'what' for Graphite-format annotations.
Parameters|Type|Description
-|-|-
`dashboardUid`|`string` *optional*|Dashboard UID
`data`|`object` *optional*|Optional JSON payload
`format`|`string` *optional*|Set to 'graphite' to create a Graphite-format annotation
`graphiteData`|`string` *optional*|Optional string payload for Graphite format
`panelId`|`integer` *optional*|Panel ID
`tags`|`array` *optional*|Optional list of tags
`text`|`string` *optional*|Annotation text (required unless format is graphite)
`time`|`integer` *optional*|Start time epoch ms
`timeEnd`|`integer` *optional*|End time epoch ms
`what`|`string` *optional*|Annotation text for Graphite format (required when format is graphite)
`when`|`integer` *optional*|Epoch ms timestamp for Graphite format

---
#### Tool: **`create_datasource`**
Create a datasource. If type is ambiguous, call search_plugin_information first; install the plugin if needed. IMPORTANT: always call this tool twice. First call: provide only the type — the tool returns a field schema. After receiving the schema, you MUST ask the user for every required field value explicitly; do not infer or use defaults without user confirmation. Second call: provide the type, the display name in the top-level name argument, schemaReviewed=true, and the fields map populated with values confirmed by the user. Never handle credentials — remind the user to rotate any detected. Returns UID, health check, and a config page link.
Parameters|Type|Description
-|-|-
`name`|`string`|Datasource display name
`type`|`string`|Grafana datasource plugin type, for example prometheus
`access`|`string` *optional*|How Grafana should access the datasource (proxy or direct)
`basicAuth`|`boolean` *optional*|Whether Grafana should use basic auth
`database`|`string` *optional*|Optional database name
`fields`|`object` *optional*|Datasource field values to provision, keyed by field key from the schema returned on the first call. The server uses each field's target (root or jsonData) to place values correctly in the YAML. Example: {"url": "http://prometheus:9090", "httpMethod": "POST"}.
`isDefault`|`boolean` *optional*|Whether this should become the default datasource
`schemaReviewed`|`boolean` *optional*|Set to true on the second call to confirm you reviewed the schema and collected values from the user.
`url`|`string` *optional*|Datasource base URL when required by the plugin
`withCredentials`|`boolean` *optional*|Whether Grafana should forward credentials such as cookies

---
#### Tool: **`create_folder`**
Create a Grafana folder. Provide a title and optional UID. Returns the created folder.
Parameters|Type|Description
-|-|-
`title`|`string`|The title of the folder.
`parentUid`|`string` *optional*|Optional parent folder UID. If set, the folder will be created under this parent.
`uid`|`string` *optional*|Optional folder UID. If omitted, Grafana will generate one.

---
#### Tool: **`create_incident`**
Create a new Grafana incident. Requires title, severity, and room prefix. Allows setting status and labels. This tool should be used judiciously and sparingly, and only after confirmation from the user, as it may notify or alarm lots of people.
Parameters|Type|Description
-|-|-
`roomPrefix`|`string`|The prefix of the room to create the incident in
`severity`|`string`|The severity of the incident
`title`|`string`|The title of the incident
`attachCaption`|`string` *optional*|The caption of the attachment
`attachUrl`|`string` *optional*|The URL of the attachment
`isDrill`|`boolean` *optional*|Whether the incident is a drill incident
`labels`|`array` *optional*|The labels to add to the incident
`status`|`string` *optional*|The status of the incident

---
#### Tool: **`create_snapshot`**
Create a Grafana snapshot from a full dashboard payload. Supports optional expiration and external snapshot fields.
Parameters|Type|Description
-|-|-
`dashboard`|`object`|Complete dashboard model to snapshot (as returned by Grafana dashboard APIs)
`deleteKey`|`string` *optional*|Secret key for deleting external snapshots. Required when external is true
`expires`|`integer` *optional*|Snapshot expiration in seconds (e.g. 3600 for 1 hour)
`external`|`boolean` *optional*|Store snapshot on external server. Requires key and deleteKey when true
`key`|`string` *optional*|Custom snapshot key. Required when external is true
`name`|`string` *optional*|Optional snapshot name

---
#### Tool: **`delete_snapshot`**
Delete a Grafana snapshot by snapshot key.
Parameters|Type|Description
-|-|-
`key`|`string`|Snapshot key to delete

*This tool may perform destructive updates.*

---
#### Tool: **`find_error_pattern_logs`**
Searches Loki logs for elevated error patterns compared to the last day's average, waits for the analysis to complete, and returns the results including any patterns found.
Parameters|Type|Description
-|-|-
`labels`|`object`|Labels to scope the analysis
`name`|`string`|The name of the investigation
`end`|`string` *optional*|End time for the investigation. Defaults to now if not specified.
`start`|`string` *optional*|Start time for the investigation. Defaults to 30 minutes ago if not specified.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`find_slow_requests`**
Searches relevant Tempo datasources for slow requests, waits for the analysis to complete, and returns the results.
Parameters|Type|Description
-|-|-
`labels`|`object`|Labels to scope the analysis
`name`|`string`|The name of the investigation
`end`|`string` *optional*|End time for the investigation. Defaults to now if not specified.
`start`|`string` *optional*|Start time for the investigation. Defaults to 30 minutes ago if not specified.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`generate_deeplink`**
Generate deeplink URLs for Grafana resources. Supports dashboards (requires dashboardUid or provisioningPreview), panels (requires dashboardUid or provisioningPreview, plus panelId), and Explore queries (requires datasourceUid and optionally queries). For dashboard and panel links, provisioningPreview points at a dashboard staged on a provisioning repository branch (e.g. a git-sync PR preview). For explore links, the time range and queries are embedded inside the Grafana explore state. Set shorten=true to also attempt a /goto/<uid> short URL; if shortening fails, the full deeplink is returned.
Parameters|Type|Description
-|-|-
`resourceType`|`string`|Type of resource: dashboard, panel, or explore
`dashboardUid`|`string` *optional*|Dashboard UID (for stored dashboards). Mutually exclusive with provisioningPreview for dashboard and panel types.
`datasourceUid`|`string` *optional*|Datasource UID (required for explore type)
`panelId`|`integer` *optional*|Panel ID (required for panel type)
`provisioningPreview`|`object` *optional*|Identifies a dashboard staged on a provisioning repository branch (e.g. a git-sync PR preview). Mutually exclusive with dashboardUid for dashboard and panel types.
`queries`|`array` *optional*|List of query objects for explore links (e.g. [{"refId":"A","expr":"up"}])
`queryParams`|`object` *optional*|Additional URL query parameters (for dashboard/panel types)
`shorten`|`boolean` *optional*|If true, try to shorten the generated URL to /goto/<uid>. If shortening fails, return the original deeplink.
`timeRange`|`object` *optional*|Time range for the link

---
#### Tool: **`get_alert_group`**
Get a specific alert group from Grafana OnCall by its ID. Returns the full alert group details.
Parameters|Type|Description
-|-|-
`alertGroupId`|`string`|The ID of the alert group to retrieve

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_annotation_tags`**
Returns annotation tags with optional filtering by tag name. Only the provided filters are applied.
Parameters|Type|Description
-|-|-
`limit`|`string` *optional*|Max results, default 100
`tag`|`string` *optional*|Optional filter by tag name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_annotations`**
Fetch Grafana annotations using filters such as dashboard UID, time range and tags.
Parameters|Type|Description
-|-|-
`alertUid`|`string` *optional*|Filter by alert UID
`dashboardUid`|`string` *optional*|Filter by dashboard UID
`from`|`integer` *optional*|Epoch ms start time
`limit`|`integer` *optional*|Max results default 100
`matchAny`|`boolean` *optional*|If true, match any tag (OR). If false, match all tags (AND). Default: false
`panelId`|`integer` *optional*|Filter by panel ID
`tags`|`array` *optional*|Filter by tags. Multiple tags allowed; use matchAny to control AND/OR logic
`to`|`integer` *optional*|Epoch ms end time
`type`|`string` *optional*|annotation or alert
`userId`|`integer` *optional*|Filter by creator user ID

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_assertions`**
Get assertion summary for a given entity with its type, name, env, site, namespace, and a time range
Parameters|Type|Description
-|-|-
`endTime`|`string`|The end time in RFC3339 format (e.g. 2024-01-01T00:00:00Z) or relative format (e.g. now)
`startTime`|`string`|The start time in RFC3339 format (e.g. 2024-01-01T00:00:00Z) or relative format (e.g. now-1h)
`entityName`|`string` *optional*|The name of the entity to list
`entityType`|`string` *optional*|The type of the entity to list (e.g. Service, Node, Pod, etc.)
`env`|`string` *optional*|The env of the entity to list
`namespace`|`string` *optional*|The namespace of the entity to list
`site`|`string` *optional*|The site of the entity to list

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_current_oncall_users`**
Get the list of users currently on-call for a specific Grafana OnCall schedule ID. Returns the schedule ID, name, and a list of detailed user objects for those currently on call.
Parameters|Type|Description
-|-|-
`scheduleId`|`string`|The ID of the schedule to get current on-call users for

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_dashboard_by_uid`**
Retrieves the complete dashboard, including panels, variables, and settings, for a specific dashboard identified by its UID. The response includes 'apiVersion' and 'isV2': when 'isV2' is true the dashboard uses the v2 schema (panels live under 'elements' keyed by name, arranged by 'layout'; variables under 'variables'), otherwise it is classic v1 ('panels[]' with 'templating.list'). WARNING: Large dashboards can consume significant context window space. Consider using get_dashboard_summary for overview or get_dashboard_property for specific data instead.
Parameters|Type|Description
-|-|-
`uid`|`string`|The UID of the dashboard

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_dashboard_panel_queries`**
Retrieve panel queries from a Grafana dashboard. Supports all datasource types (Prometheus, Loki, CloudWatch, SQL, etc.) and row-nested panels. Optionally filter to a specific panel by ID with `panelId`. Optionally provide `variables` for template variable substitution, which populates `processedQuery` and `requiredVariables` fields. Returns an array of objects with fields: title, query (raw expression), datasource (object with uid and type), and optionally processedQuery, refId, and requiredVariables.
Parameters|Type|Description
-|-|-
`uid`|`string`|The UID of the dashboard
`panelId`|`integer` *optional*|Optional panel ID to filter to a specific panel
`variables`|`object` *optional*|Optional variable substitutions (e.g., {"job": "api-server"})

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_dashboard_property`**
Get specific parts of a dashboard using JSONPath expressions to minimize context window usage. JSONPath targets the dashboard's native schema. Classic v1 paths: '$.title' (title)\, '$.panels[*].title' (all panel titles)\, '$.panels[0]' (first panel)\, '$.templating.list' (variables)\, '$.annotations.list' (saved dashboard annotation queries/definitions)\, '$.tags' (tags)\, '$.panels[*].targets[*].expr' (all queries). v2 dashboards (see isV2 from get_dashboard_by_uid) use different paths: '$.title'\, '$.elements' (panels\, keyed by name)\, '$.variables' (variables)\, '$.annotations'. Use this instead of get_dashboard_by_uid when you only need specific d

[...]
