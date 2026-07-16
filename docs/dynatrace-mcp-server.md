This MCP Server allows interaction with the Dynatrace observability platform, brining real-time observability data directly into your development workflow.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/dynatrace-mcp-server](https://hub.docker.com/repository/docker/mcp/dynatrace-mcp-server)
**Author**|[dynatrace-oss](https://github.com/dynatrace-oss)
**Repository**|https://github.com/dynatrace-oss/dynatrace-mcp

## Available Tools (18)
Tools provided by this Server|Short Description
-|-
`chat_with_davis_copilot`|Use this tool to ask any Dynatrace related question, in case no other more specific tool is available.|
`create_dynatrace_notebook`|Create a new notebook in the Dynatrace platform (NOT a Jupyter notebook) to share your analysis and findings with colleagues.|
`execute_davis_analyzer`|Execute a Davis Analyzer with custom input parameters.|
`execute_dql`|Get data like Logs, Metrics, Spans, Events, or Entity Data from Dynatrace Grail by executing a Dynatrace Query Language (DQL) statement.|
`explain_dql_in_natural_language`|Explain Dynatrace Query Language (DQL) statements in natural language using Davis CoPilot AI.|
`find_entity_by_name`|Find the entityId and type of a monitored entity (service, host, process-group, application, kubernetes-node, custom-app, ...) within the topology on Dynatrace, based on the name of the entity.|
`generate_dql_from_natural_language`|Convert natural language queries to Dynatrace Query Language (DQL) using Davis CoPilot AI.|
`get_environment_info`|Get information about the connected Dynatrace Environment (Tenant) and verify the connection and authentication.|
`get_kubernetes_events`|Get all events from a specific Kubernetes (K8s) cluster|
`list_davis_analyzers`|List all available Davis Analyzers in Dynatrace (forecast, anomaly detection, correlation analyzers, and more)|
`list_exceptions`|List all exceptions known on Dynatrace starting with the most recent.|
`list_problems`|List all problems (based on "fetch dt.davis.problems") known on Dynatrace, sorted by their recency.|
`list_vulnerabilities`|Retrieve all active (non-muted) vulnerabilities from Dynatrace.|
`reset_grail_budget`|Reset the Grail query budget after it was exhausted, allowing new queries to be executed.|
`send_email`|Send an email using the Dynatrace Email API.|
`send_event`|Send a custom event to Dynatrace using the Events API v2.|
`send_slack_message`|Sends a Slack message to a dedicated Slack Channel via Slack Connector on Dynatrace|
`verify_dql`|Syntactically verify a Dynatrace Query Language (DQL) statement on Dynatrace GRAIL before executing it.|

---
## Tools Details

#### Tool: **`chat_with_davis_copilot`**
Use this tool to ask any Dynatrace related question, in case no other more specific tool is available.
Parameters|Type|Description
-|-|-
`text`|`string`|Your question or request for Davis CoPilot
`context`|`string` *optional*|Optional context to provide additional information (like problem details, vulnerability details, entity information)
`instruction`|`string` *optional*|Optional instruction for how to format the response

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`create_dynatrace_notebook`**
Create a new notebook in the Dynatrace platform (NOT a Jupyter notebook) to share your analysis and findings with colleagues.
Parameters|Type|Description
-|-|-
`content`|`array`|The Dynatrace notebook content, containing DQL statements and text (multi-line markdown is possible) relevant for the analysis. Do NOT use Jupyter notebook format.
`name`|`string`|The name of the notebook (e.g., "Performance Analysis for <entity-name>" or "Error Investigation Dashboard for <problem-name>")
`description`|`string` *optional*|Optional description of the Dynatrace notebook (could include the purpose, scope, the original prompt, or just a summary based on the initial prompt)

*This tool may perform destructive updates.*

---
#### Tool: **`execute_davis_analyzer`**
Execute a Davis Analyzer with custom input parameters. Use "list_davis_analyzers" first to see available analyzers and their names.
Parameters|Type|Description
-|-|-
`analyzerName`|`string`|The name of the Davis Analyzer to execute (e.g., "dt.statistics.GenericForecastAnalyzer")
`input`|`object` *optional*|Input parameters for the analyzer as a JSON object
`timeframeEnd`|`string` *optional*|End time for the analysis (default: now)
`timeframeStart`|`string` *optional*|Start time for the analysis (default: now-1h)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`execute_dql`**
Get data like Logs, Metrics, Spans, Events, or Entity Data from Dynatrace Grail by executing a Dynatrace Query Language (DQL) statement. Use the "generate_dql_from_natural_language" tool upfront to generate or refine a DQL statement based on your request. To learn about possible fields available for filtering, use the query "fetch dt.semantic_dictionary.models | filter data_object == \"logs\"". IMPORTANT: The MCP App UI will automatically render the query results as an interactive table and chart. Do NOT generate Mermaid diagrams, ASCII charts, markdown tables, or any other visual representation of the data — the MCP App is solely responsible for rendering.
Parameters|Type|Description
-|-|-
`dqlStatement`|`string`|DQL Statement (Ex: "fetch [logs, spans, events, ...], from: now()-4h, to: now() [| filter <some-filter>] [| summarize count(), by:{some-fields}]", or for metrics: "metrics [from: now()-4h] [to: now()] [| filter: {<filter>}]" or "timeseries { avg(<metric-name>), value.A = avg(<metric-name>, scalar: true) }", or for entities via smartscape: "smartscapeNodes \"[*, HOST, PROCESS, ...]\" [| filter id == \"<ENTITY-ID>\"]"). When querying data for a specific entity, call the `find_entity_by_name` tool first to get an appropriate filter like `dt.entity.service == "SERVICE-1234"` or `dt.entity.host == "HOST-1234"` to be used in the DQL statement. Note: `dt.entity.*` filters only work in `fetch` queries (logs, metrics, spans, etc.). For `smartscapeNodes`, filter by `id == toSmartscapeId("<ENTITY-ID>")` or simply `id == "<ENTITY-ID>"` (raw string). For `smartscapeEdges`, use `source_id == toSmartscapeId("<ENTITY-ID>")` or `target_id == toSmartscapeId("<ENTITY-ID>")`. String functions like `contains()` or `startsWith()` do NOT work on smartscape `id` fields. 
`recordLimit`|`number` *optional*|Maximum number of records to return (default: 100)
`recordSizeLimitMB`|`number` *optional*|Maximum size of the returned records in MB (default: 1MB)

*This tool interacts with external entities.*

---
#### Tool: **`explain_dql_in_natural_language`**
Explain Dynatrace Query Language (DQL) statements in natural language using Davis CoPilot AI.
Parameters|Type|Description
-|-|-
`dql`|`string`|The DQL statement to explain

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`find_entity_by_name`**
Find the entityId and type of a monitored entity (service, host, process-group, application, kubernetes-node, custom-app, ...) within the topology on Dynatrace, based on the name of the entity. Run this before querying data like logs, metrics, problems, events. If no entity name is known, make an educated guess with common identifiers like package.json `id`/`name`, helm chart names, kubernetes manifest names, and alike.
Parameters|Type|Description
-|-|-
`entityNames`|`array`|Names of the entities to search for - try with one name at first (identifiers like package.json id), and only try with multiple names if the first search was unsuccessful
`extendedSearch`|`boolean` *optional*|Set this to true if you want a comprehensive search over all available entity types.
`maxEntitiesToDisplay`|`number` *optional*|Maximum number of entities to display in the response.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`generate_dql_from_natural_language`**
Convert natural language queries to Dynatrace Query Language (DQL) using Davis CoPilot AI. You can ask for problem events, security issues, logs, metrics, spans, and custom data.
Parameters|Type|Description
-|-|-
`text`|`string`|Natural language description of what you want to query. Be specific and include time ranges, entities, and metrics of interest.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_environment_info`**
Get information about the connected Dynatrace Environment (Tenant) and verify the connection and authentication.
#### Tool: **`get_kubernetes_events`**
Get all events from a specific Kubernetes (K8s) cluster
Parameters|Type|Description
-|-|-
`clusterId`|`string` *optional*|The Kubernetes Cluster Id, referred to as k8s.cluster.uid, usually seen when using "kubectl" - this is NOT the Dynatrace environment and not the Dynatrace Kubernetes Entity Id. Leave empty if you don't know the Cluster Id.
`eventType`|`string` *optional*|
`kubernetesEntityId`|`string` *optional*|The Dynatrace Kubernetes Entity Id, referred to as dt.entity.kubernetes_cluster. Leave empty if you don't know the Entity Id, or use the "find_entity_by_name" tool to find the cluster by name.
`maxEventsToDisplay`|`number` *optional*|Maximum number of events to display in the response.
`timeframe`|`string` *optional*|Timeframe to query events (e.g., "12h", "24h", "7d", "30d"). Default: "24h". Supports hours (h) and days (d).

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_davis_analyzers`**
List all available Davis Analyzers in Dynatrace (forecast, anomaly detection, correlation analyzers, and more)
#### Tool: **`list_exceptions`**
List all exceptions known on Dynatrace starting with the most recent.
Parameters|Type|Description
-|-|-
`additionalFilter`|`string` *optional*|Additional DQL filter for user.events - filter by error id like 'error.id == "<error.id>"', application id like 'dt.rum.application.id == "<dt.rum.application.id>"', application entity like 'dt.rum.application.entity == "<dt.rum.application.entity>"' or operating system name like 'os.name == "<os.name>"'. Leave empty to get all exceptions within the timeframe.
`maxExceptionsToDisplay`|`number` *optional*|Maximum number of exceptions to display in the response.
`timeframe`|`string` *optional*|Timeframe to query problems (e.g., "12h", "24h", "7d", "30d", "30m"). Default: "24h". Supports days (d), hours (h) and minutes (m).

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_problems`**
List all problems (based on "fetch dt.davis.problems") known on Dynatrace, sorted by their recency.
Parameters|Type|Description
-|-|-
`additionalFilter`|`string` *optional*|Additional DQL filter for dt.davis.problems - filter by entity type (preferred), like 'dt.entity.<service|host|application|$type> == "<entity-id>"', or by entity tags 'entity_tags == array("dt.owner:team-foobar", "tag:tag")'
`maxProblemsToDisplay`|`number` *optional*|Maximum number of problems to display in the response.
`status`|`string` *optional*|Fitler problems by their status. "ACTIVE": only active problems (those without an end time set), "CLOSED": only closed problems (those with an end time set), "ALL": active and closed problems (default)
`timeframe`|`string` *optional*|Timeframe to query problems (e.g., "12h", "24h", "7d", "30d"). Default: "24h". Supports hours (h) and days (d).

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_vulnerabilities`**
Retrieve all active (non-muted) vulnerabilities from Dynatrace. An additional filter can be provided using DQL filter (filter for a specific entity type and id).
Parameters|Type|Description
-|-|-
`additionalFilter`|`string` *optional*|Additional DQL-based filter for accessing vulnerabilities, e.g., by entity type (preferred), like 'dt.entity.<service|host|application|$type> == "<entity-id>"', by entity name (not recommended) 'affected_entity.name contains "<entity-name>"' , or by tags 'entity_tags == array("dt.owner:team-foobar", "tag:tag")'. You can also filter by vulnerability details like 'vulnerability.stack == "CODE_LIBRARY"' or 'vulnerability.risk.level == "CRITICAL"' or 'vulnerability.davis_assessment.exposure_status == "PUBLIC_NETWORK"'
`maxVulnerabilitiesToDisplay`|`number` *optional*|Maximum number of vulnerabilities to display in the response.
`riskScore`|`number` *optional*|Minimum risk score of vulnerabilities to list (default: 8.0)
`timeframe`|`string` *optional*|Timeframe to query vulnerabilities (e.g., "12h", "24h", "7d", "30d", "90d"). Default: "30d". Supports hours (h) and days (d).

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`reset_grail_budget`**
Reset the Grail query budget after it was exhausted, allowing new queries to be executed. This clears all tracked bytes scanned in the current session.
#### Tool: **`send_email`**
Send an email using the Dynatrace Email API. The sender will be no-reply@apps.dynatrace.com. Maximum 10 recipients total across TO, CC, and BCC.
Parameters|Type|Description
-|-|-
`body`|`string`|Body content of the email (plain text only). Avoid sending sensitive data like log lines. Focus on context, insights, links, and summaries.
`subject`|`string`|Subject line of the email
`toRecipients`|`array`|Array of email addresses for TO recipients
`bccRecipients`|`array` *optional*|Array of email addresses for BCC recipients
`ccRecipients`|`array` *optional*|Array of email addresses for CC recipients

*This tool interacts with external entities.*

---
#### Tool: **`send_event`**
Send a custom event to Dynatrace using the Events API v2. Use this to ingest custom events for alerting, tracking deployments, configuration changes, or any custom business events.
Parameters|Type|Description
-|-|-
`eventType`|`string`|Type of event to send. Common types: CUSTOM_INFO for general information, CUSTOM_DEPLOYMENT for deployments, CUSTOM_ALERT for alerts, ERROR_EVENT for errors.
`title`|`string`|Title of the event (max 500 characters). Should be descriptive and concise.
`endTime`|`number` *optional*|End timestamp of the event in UTC milliseconds. If not set, current time is used.
`entitySelector`|`string` *optional*|Entity selector to associate the event with specific Dynatrace entities. Example: "type(HOST),entityId(HOST-1234567890ABCDEF)" or "type(SERVICE),tag(environment:production)"
`properties`|`object` *optional*|Custom properties as key-value pairs to include with the event. Example: {"version": "1.2.3", "environment": "production"}
`startTime`|`number` *optional*|Start timestamp of the event in UTC milliseconds. If not set, current time is used.

*This tool may perform destructive updates.*

---
#### Tool: **`send_slack_message`**
Sends a Slack message to a dedicated Slack Channel via Slack Connector on Dynatrace
Parameters|Type|Description
-|-|-
`channel`|`string`|
`message`|`string`|Slack markdown supported. Avoid sending sensitive data like log lines. Focus on context, insights, links, and summaries.

---
#### Tool: **`verify_dql`**
Syntactically verify a Dynatrace Query Language (DQL) statement on Dynatrace GRAIL before executing it. Recommended for generated DQL statements. Skip for statements created by `generate_dql_from_natural_language` tool, as well as from documentation.
Parameters|Type|Description
-|-|-
`dqlStatement`|`string`|

*This tool is read-only. It does not modify its environment.*

---

## Screenshots

![Dynatrace screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/dynatrace-mcp-server-1.png)
