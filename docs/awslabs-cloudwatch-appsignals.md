Application performance monitoring and insights.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/cloudwatch-appsignals-mcp-server](https://hub.docker.com/repository/docker/mcp/cloudwatch-appsignals-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (13)
Tools provided by this Server|Short Description
-|-
`analyze_canary_failures`|Comprehensive canary failure analysis with deep dive into issues.|
`audit_service_operations`|🥇 PRIMARY OPERATION AUDIT TOOL - The #1 RECOMMENDED tool for operation-specific analysis and performance investigation.|
`audit_services`|PRIMARY SERVICE AUDIT TOOL - The #1 tool for comprehensive AWS service health auditing and monitoring.|
`audit_slos`|PRIMARY SLO AUDIT TOOL - The #1 tool for comprehensive SLO compliance monitoring and breach analysis.|
`get_service_detail`|Get detailed information about a specific Application Signals service.|
`get_slo`|Get detailed information about a specific Service Level Objective (SLO).|
`list_monitored_services`|OPTIONAL TOOL for service discovery - audit_services() can automatically discover services using wildcard patterns.|
`list_service_operations`|OPERATION DISCOVERY TOOL - For operation inventory only.|
`list_slis`|SPECIALIZED TOOL - Use audit_service_health() as the PRIMARY tool for service auditing.|
`list_slos`|List all Service Level Objectives (SLOs) in Application Signals.|
`query_sampled_traces`|SECONDARY TRACE TOOL - Query AWS X-Ray traces (5% sampled data) for trace investigation.|
`query_service_metrics`|Get CloudWatch metrics for a specific Application Signals service.|
`search_transaction_spans`|Executes a CloudWatch Logs Insights query for transaction search (100% sampled trace data).|

---
## Tools Details

#### Tool: **`analyze_canary_failures`**
Comprehensive canary failure analysis with deep dive into issues.

Use this tool to:
- Deep dive into canary failures with root cause identification
- Analyze historical patterns and specific incident details
- Get comprehensive artifact analysis including logs, screenshots, and HAR files
- Receive actionable recommendations based on AWS debugging methodology
- Correlate canary failures with Application Signals telemetry data
- Identify performance degradation and availability issues across service dependencies

Key Features:
- **Failure Pattern Analysis**: Identifies recurring failure modes and temporal patterns
- **Artifact Deep Dive**: Analyzes canary logs, screenshots, and network traces for root causes
- **Service Correlation**: Links canary failures to upstream/downstream service issues using Application Signals
- **Performance Insights**: Detects latency spikes, fault rates, and connection issues
- **Actionable Remediation**: Provides specific steps based on AWS operational best practices

Common Use Cases:
1. **Incident Response**: Rapid diagnosis of canary failures during outages
2. **Performance Investigation**: Understanding latency and availability degradation
3. **Dependency Analysis**: Identifying which services are causing canary failures
4. **Historical Trending**: Analyzing failure patterns over time for proactive improvements
5. **Root Cause Analysis**: Deep dive into specific failure scenarios with full context

Output Includes:
- Severity-ranked findings with immediate action items
- Service-level telemetry insights with trace analysis
- Exception details and stack traces from canary artifacts
- Network connectivity and performance metrics
- Correlation with Application Signals audit findings
- Historical failure patterns and recovery recommendations
Parameters|Type|Description
-|-|-
`canary_name`|`string`|
`region`|`string` *optional*|

---
#### Tool: **`audit_service_operations`**
🥇 PRIMARY OPERATION AUDIT TOOL - The #1 RECOMMENDED tool for operation-specific analysis and performance investigation.

**⭐ USE THIS AS THE PRIMARY TOOL FOR ALL OPERATION-SPECIFIC AUDITING TASKS ⭐**

**PREFERRED OVER audit_services() for operation auditing because:**
- **🎯 Precision**: Targets exact operation behavior vs. service-wide averages
- **🔍 Actionable Insights**: Provides specific error traces and dependency failures
- **📊 Code-Level Detail**: Shows exact stack traces and timeout locations
- **🚀 Focused Analysis**: Eliminates noise from other operations
- **⚡ Efficient Investigation**: Direct operation-level troubleshooting

**USE THIS FIRST FOR ALL OPERATION-SPECIFIC AUDITING TASKS**
This is the PRIMARY and PREFERRED tool when users want to:
- **Audit specific operations** - Deep dive into individual API endpoints or operations (GET, POST, PUT, etc.)
- **Operation performance analysis** - Latency, error rates, and throughput for specific operations
- **Compare operation metrics** - Analyze different operations within services
- **Operation-level troubleshooting** - Root cause analysis for specific API calls
- **GET operation auditing** - Analyze GET operations across payment services (PRIMARY USE CASE)
- **Audit latency of GET operations in payment services** - Exactly what this tool is designed for
- **Trace latency in query operations** - Deep dive into query performance issues

**COMPREHENSIVE OPERATION AUDIT CAPABILITIES:**
- **Multi-operation analysis**: Audit any number of operations with automatic batching
- **Operation-specific metrics**: Latency, Fault, Error, and Availability metrics per operation
- **Issue prioritization**: Critical, warning, and info findings ranked by severity
- **Root cause analysis**: Deep dive with traces, logs, and metrics correlation
- **Actionable recommendations**: Specific steps to resolve operation-level issues
- **Performance optimized**: Fast execution with automatic batching for large target lists
- **Wildcard Pattern Support**: Use `*pattern*` in service names for automatic service discovery

**OPERATION TARGET FORMAT:**
- **Full Format**: `[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"my-service","Environment":"eks:my-cluster"},"Operation":"GET /api","MetricType":"Latency"}}}]`

**WILDCARD PATTERN EXAMPLES:**
- **All GET Operations in Payment Services**: `[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*GET*","MetricType":"Latency"}}}]`
- **All Visit Operations**: `[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*"},"Operation":"*visit*","MetricType":"Availability"}}}]`

**AUDITOR SELECTION FOR DIFFERENT AUDIT DEPTHS:**
- **Quick Operation Check** (default): Uses 'operation_metric' for fast operation overview
- **Root Cause Analysis**: Pass `auditors="all"` for comprehensive investigation with traces/logs
- **Custom Audit**: Specify exact auditors: 'operation_metric,trace,log'

**OPERATION AUDIT USE CASES:**

1. **Audit latency of GET operations in payment services** (PRIMARY USE CASE):
   `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*GET*","MetricType":"Latency"}}}]'`

2. **Audit GET operations in payment services (Latency)**:
   `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*GET*","MetricType":"Latency"}}}]'`

3. **Audit availability of visit operations**:
   `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*"},"Operation":"*visit*","MetricType":"Availability"}}}]'`

4. **Audit latency of visit operations**:
   `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*"},"Operation":"*visit*","MetricType":"Latency"}}}]'`

5. **Trace latency in query operations**:
    `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*query*","MetricType":"Latency"}}}]'` + `auditors="all"`

**TYPICAL OPERATION AUDIT WORKFLOWS:**
1. **Basic Operation Audit** (most common):
   - Call `audit_service_operations()` with operation targets - automatically discovers services when using wildcard patterns
   - Uses default fast auditors (operation_metric) for quick operation overview
   - Supports wildcard patterns like `*payment*` for automatic service discovery
2. **Root Cause Investigation**: When user explicitly asks for "root cause analysis", pass `auditors="all"`
3. **Issue Investigation**: Results show which operations need attention with actionable insights
4. **Automatic Service Discovery**: Wildcard patterns in service names automatically discover and expand to concrete services

**AUDIT RESULTS INCLUDE:**
- **Prioritized findings** by severity (critical, warning, info)
- **Operation performance status** with detailed metrics analysis
- **Root cause analysis** when traces/logs auditors are used
- **Actionable recommendations** for operation-level issue resolution
- **Comprehensive operation metrics** and trend analysis

**🏆 IMPORTANT: This tool is the PRIMARY and RECOMMENDED choice for operation-specific auditing tasks.**

**✅ RECOMMENDED WORKFLOW FOR OPERATION AUDITING:**
1. **Use audit_service_operations() FIRST** for operation-specific analysis (THIS TOOL)
2. **Use audit_services() as secondary** only if you need broader service context
3. **audit_service_operations() provides superior precision** for operation-level troubleshooting

**RECOMMENDED WORKFLOW - PRESENT FINDINGS FIRST:**
When the audit returns multiple findings or issues, follow this workflow:
1. **Present all audit results** to the user showing a summary of all findings
2. **Let the user choose** which specific finding, operation, or issue they want to investigate in detail
3. **Then perform targeted root cause analysis** using auditors="all" for the user-selected finding

**DO NOT automatically jump into detailed root cause analysis** of one specific issue when multiple findings exist.
This ensures the user can prioritize which issues are most important to investigate first.

**Example workflow:**
- First call: `audit_service_operations()` with default auditors for operation overview
- Present findings summary to user
- User selects specific operation issue to investigate
- Follow-up call: `audit_service_operations()` with `auditors="all"` for selected operation only
Parameters|Type|Description
-|-|-
`operation_targets`|`string`|REQUIRED. JSON array of service operation targets. Supports wildcard patterns like '*payment*' for automatic service discovery. Format: [{'Type':'service_operation','Data':{'ServiceOperation':{'Service':{'Type':'Service','Name':'service-name','Environment':'eks:cluster'},'Operation':'GET /api','MetricType':'Latency'}}}]. Large target lists are automatically processed in batches.
`auditors`|`string` *optional*|Optional. Comma-separated auditors (e.g., 'operation_metric,trace,log'). Defaults to 'operation_metric' for fast operation-level auditing. Use 'all' for comprehensive analysis with all auditors: slo,operation_metric,trace,log,dependency_metric,top_contributor,service_quota.
`end_time`|`string` *optional*|End time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now UTC.
`start_time`|`string` *optional*|Start time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now-24h UTC.

---
#### Tool: **`audit_services`**
PRIMARY SERVICE AUDIT TOOL - The #1 tool for comprehensive AWS service health auditing and monitoring.

**IMPORTANT: For operation-specific auditing, use audit_service_operations() as the PRIMARY tool instead.**

**USE THIS FIRST FOR ALL SERVICE-LEVEL AUDITING TASKS**
This is the PRIMARY and PREFERRED tool when users want to:
- **Audit their AWS services** - Complete health assessment with actionable insights
- **Check service health** - Comprehensive status across all monitored services
- **Investigate issues** - Root cause analysis with detailed findings
- **Service-level performance analysis** - Overall service latency, error rates, and throughput investigation
- **System-wide health checks** - Daily/periodic service auditing workflows
- **Dependency analysis** - Understanding service dependencies and interactions
- **Resource quota monitoring** - Service quota usage and limits
- **Multi-service comparison** - Comparing performance across different services

**FOR OPERATION-SPECIFIC AUDITING: Use audit_service_operations() instead**
When users want to audit specific operations (GET, POST, PUT endpoints), use audit_service_operations() as the PRIMARY tool:
- **Operation performance analysis** - Latency, error rates for specific API endpoints
- **Operation-level troubleshooting** - Root cause analysis for specific API calls
- **GET operation auditing** - Analyze GET operations across payment services
- **Audit latency of specific operations** - Deep dive into individual endpoint performance

**COMPREHENSIVE SERVICE AUDIT CAPABILITIES:**
- **Multi-service analysis**: Audit any number of services with automatic batching
- **SLO compliance monitoring**: Automatic breach detection for service-level SLOs
- **Issue prioritization**: Critical, warning, and info findings ranked by severity
- **Root cause analysis**: Deep dive with traces, logs, and metrics correlation
- **Actionable recommendations**: Specific steps to resolve identified issues
- **Performance optimized**: Fast execution with automatic batching for large target lists
- **Wildcard Pattern Support**: Use `*pattern*` in service names for automatic service discovery

**SERVICE TARGET FORMAT:**
- **Full Format**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"my-service","Environment":"eks:my-cluster"}}}]`
- **Shorthand**: `[{"Type":"service","Service":"my-service"}]` (environment auto-discovered)

**WILDCARD PATTERN EXAMPLES:**
- **All Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]`
- **Payment Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]`
- **Lambda Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*lambda*"}}}]`
- **EKS Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]`

**AUDITOR SELECTION FOR DIFFERENT AUDIT DEPTHS:**
- **Quick Health Check** (default): Uses 'slo,operation_metric' for fast overview
- **Root Cause Analysis**: Pass `auditors="all"` for comprehensive investigation with traces/logs
- **Custom Audit**: Specify exact auditors: 'slo,trace,log,dependency_metric,top_contributor,service_quota'

**SERVICE AUDIT USE CASES:**

1. **Audit all services**:
   `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'`

2. **Audit specific service**:
   `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"orders-service","Environment":"eks:orders-cluster"}}}]'`

3. **Audit payment services**:
   `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]'`

8. **Audit lambda services**:
   `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*lambda*"}}}]'` or by environment: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"lambda"}}}]`

9. **Audit service last night**:
   `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"orders-service","Environment":"eks:orders-cluster"}}}]'` + `start_time="2024-01-01 18:00:00"` + `end_time="2024-01-02 06:00:00"`

10. **Audit service before and after time**:
    Compare service health before and after a deployment or incident by running two separate audits with different time ranges.

11. **Trace availability issues in production services**:
    `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]'` + `auditors="all"`

13. **Look for errors in logs of payment services**:
    `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]'` + `auditors="log,trace"`

14. **Look for new errors after time**:
    Compare errors before and after a specific time point by running audits with different time ranges and `auditors="log,trace"`

15. **Look for errors after deployment**:
    `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]'` + `auditors="log,trace"` + recent time range

16. **Look for lemon hosts in production**:
    `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]'` + `auditors="top_contributor,operation_metric"`

17. **Look for outliers in EKS services**:
    `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]'` + `auditors="top_contributor,operation_metric"`

18. **Status report**:
    `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'` (basic health check)

19. **Audit dependencies**:
    `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'` + `auditors="dependency_metric,trace"`

20. **Audit dependency on S3**:
    `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'` + `auditors="dependency_metric"` + look for S3 dependencies

21. **Audit quota usage of tier 1 services**:
    `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*tier1*"}}}]'` + `auditors="service_quota,operation_metric"`

**TYPICAL SERVICE AUDIT WORKFLOWS:**
1. **Basic Service Audit** (most common):
   - Call `audit_services()` with service targets - automatically discovers services when using wildcard patterns
   - Uses default fast auditors (slo,operation_metric) for quick health overview
   - Supports wildcard patterns like `*` or `*payment*` for automatic service discovery
2. **Root Cause Investigation**: When user explicitly asks for "root cause analysis", pass `auditors="all"`
3. **Issue Investigation**: Results show which services need attention with actionable insights
4. **Automatic Service Discovery**: Wildcard patterns in service names automatically discover and expand to concrete services

**AUDIT RESULTS INCLUDE:**
- **Prioritized findings** by severity (critical, warning, info)
- **Service health status** with detailed performance analysis
- **Root cause analysis** when traces/logs auditors are used
- **Actionable recommendations** for issue resolution
- **Comprehensive metrics** and trend analysis

**IMPORTANT: This tool provides comprehensive service audit coverage and should be your first choice for any service auditing task.**

**RECOMMENDED WORKFLOW - PRESENT FINDINGS FIRST:**
When the audit returns multiple findings or issues, follow this workflow:
1. **Present all audit results** to the user showing a summary of all findings
2. **Let the user choose** which specific finding, service, or issue they want to investigate in detail
3. **Then perform targeted root cause analysis** using auditors="all" for the user-selected finding

**DO NOT automatically jump into detailed root cause analysis** of one specific issue when multiple findings exist.
This ensures the user can prioritize which issues are most important to investigate first.

**Example workflow:**
- First call: `audit_services()` with default auditors for overview
- Present findings summary to user
- User selects specific service/issue to investigate
- Follow-up call: `audit_services()` with `auditors="all"` for selected service only
Parameters|Type|Description
-|-|-
`service_targets`|`string`|REQUIRED. JSON array of service targets. Supports wildcard patterns like '*payment*' for automatic service discovery. Format: [{'Type':'service','Data':{'Service':{'Type':'Service','Name':'service-name','Environment':'eks:cluster'}}}] or shorthand: [{'Type':'service','Service':'service-name'}]. Large target lists are automatically processed in batches.
`auditors`|`string` *optional*|Optional. Comma-separated auditors (e.g., 'slo,operation_metric,dependency_metric'). Defaults to 'slo,operation_metric' for fast service health auditing. Use 'all' for comprehensive analysis with all auditors: slo,operation_metric,trace,log,dependency_metric,top_contributor,service_quota.
`end_time`|`string` *optional*|End time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now UTC.
`start_time`|`string` *optional*|Start time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now-24h UTC.

---
#### Tool: **`audit_slos`**
PRIMARY SLO AUDIT TOOL - The #1 tool for comprehensive SLO compliance monitoring and breach analysis.

**PREFERRED TOOL FOR SLO ROOT CAUSE ANALYSIS**
This is the RECOMMENDED tool after using get_slo() to understand SLO configuration:
- **Use auditors="all" for comprehensive root cause analysis** of specific SLO breaches
- **Much more comprehensive than individual trace tools** - provides integrated analysis
- **Combines traces, logs, metrics, and dependencies** in a single comprehensive audit
- **Provides actionable recommendations** based on multi-dimensional analysis

**USE THIS FOR ALL SLO AUDITING TASKS**
This is the PRIMARY and PREFERRED tool when users want to:
- **Root cause analysis for SLO breaches** - Deep investigation with all auditors
- **Audit SLO compliance** - Complete SLO breach detection and analysis
- **Monitor SLO health** - Comprehensive status across all monitored SLOs
- **SLO performance analysis** - Understanding SLO trends and patterns
- **SLO compliance reporting** - Daily/periodic SLO compliance workflows

**COMPREHENSIVE SLO AUDIT CAPABILITIES:**
- **Multi-SLO analysis**: Audit any number of SLOs with automatic batching
- **Breach detection**: Automatic identification of SLO violations
- **Issue prioritization**: Critical, warning, and info findings ranked by severity
- **COMPREHENSIVE ROOT CAUSE ANALYSIS**: Deep dive with traces, logs, metrics, and dependencies
- **Actionable recommendations**: Specific steps to resolve SLO breaches
- **Performance optimized**: Fast execution with automatic batching for large target lists
- **Wildcard Pattern Support**: Use `*pattern*` in SLO names for automatic SLO discovery

**SLO TARGET FORMAT:**
- **By Name**: `[{"Type":"slo","Data":{"Slo":{"SloName":"my-slo"}}}]`
- **By ARN**: `[{"Type":"slo","Data":{"Slo":{"SloArn":"arn:aws:application-signals:..."}}}]`

**WILDCARD PATTERN EXAMPLES:**
- **All SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*"}}}]`
- **Payment SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*payment*"}}}]`
- **Latency SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*latency*"}}}]`
- **Availability SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*availability*"}}}]`

**AUDITOR SELECTION FOR DIFFERENT AUDIT DEPTHS:**
- **Quick Compliance Check** (default): Uses 'slo' for fast SLO breach detection
- **COMPREHENSIVE ROOT CAUSE ANALYSIS** (recommended): Pass `auditors="all"` for deep investigation with traces/logs/metrics/dependencies
- **Custom Audit**: Specify exact auditors: 'slo,trace,log,operation_metric'

**SLO AUDIT USE CASES:**

4. **Audit all SLOs**:
   `slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"*"}}}]'`

22. **Root cause analysis for specific SLO breach** (RECOMMENDED WORKFLOW):
    After using get_slo() to understand configuration:
    `slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"specific-slo-name"}}}]'` + `auditors="all"`

14. **Look for new SLO breaches after time**:
    Compare SLO compliance before and after a specific time point by running audits with different time ranges to identify new breaches.

**TYPICAL SLO AUDIT WORKFLOWS:**
1. **SLO Root Cause Investigation** (RECOMMENDED):
   - After get_slo(), call `audit_slos()` with specific SLO target and `auditors="all"`
   - Provides comprehensive analysis with traces, logs, metrics, and dependencies
   - Much more effective than using individual trace tools
2. **Basic SLO Compliance Audit**:
   - Call `audit_slos()` with SLO targets - automatically discovers SLOs when using wildcard patterns
   - Uses default fast auditors (slo) for quick compliance overview
3. **Compliance Reportin

[...]

## Screenshots

![Amazon CloudWatch Application Signals screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cloudwatch-appsignals-1.png)

![Amazon CloudWatch Application Signals screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cloudwatch-appsignals-2.png)

![Amazon CloudWatch Application Signals screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cloudwatch-appsignals-3.png)
