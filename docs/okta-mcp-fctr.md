Secure Okta identity and access management via Model Context Protocol (MCP). Access Okta users, groups, applications, logs, and policies through AI assistants with enterprise-grade security.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/okta-mcp-fctr](https://hub.docker.com/repository/docker/mcp/okta-mcp-fctr)
**Author**|[fctr-id](https://github.com/fctr-id)
**Repository**|https://github.com/fctr-id/okta-mcp-server

## Available Tools (20)
Tools provided by this Server|Short Description
-|-
`analyze_login_risk`|Comprehensive login risk analysis for users.|
`analyze_user_app_access`|Comprehensive access analysis for users and applications.|
`get_current_time`|Get the current date and time in UTC, formatted for Okta API usage.|
`get_okta_application`|Get detailed information about a specific Okta application.|
`get_okta_event_logs`|Get Okta system log events with comprehensive filtering and full pagination for complete audit trails.|
`get_okta_group`|Get detailed information about a specific Okta group.|
`get_okta_policy_rule`|Get detailed information about a specific Okta policy rule.|
`get_okta_user`|Get detailed information about a specific Okta user.|
`list_okta_application_groups`|List all groups assigned to a specific Okta application with full pagination.|
`list_okta_application_users`|List all users assigned to a specific Okta application with full pagination.|
`list_okta_applications`|List all applications in the Okta organization with pagination and filtering.|
`list_okta_group_users`|List all users in a specific Okta group with full pagination for complete results.|
`list_okta_groups`|List Okta groups with filtering - limited to 50 groups by default for context efficiency.|
`list_okta_network_zones`|List all network zones defined in the Okta organization.|
`list_okta_policy_rules`|List all rules for a specific Okta policy.|
`list_okta_user_applications`|List all application links (assigned applications) for a specific Okta user.|
`list_okta_user_factors`|List all authentication factors enrolled for a specific Okta user.|
`list_okta_user_groups`|List all groups that a specific Okta user belongs to.|
`list_okta_users`|List Okta users with filtering - returns first 50 users by default due to LLM context limitations.|
`parse_relative_time`|Parse natural language time expressions into Okta API-compatible timestamps.|

---
## Tools Details

#### Tool: **`analyze_login_risk`**
Comprehensive login risk analysis for users.

SPECIAL TOOL: Collects last 10 login events (policy.evaluate_sign_on) including location patterns, 
device fingerprints, user agents, ISPs, network zones, and behavioral indicators. Returns comprehensive 
raw data for LLM risk assessment without making risk decisions.

The LLM MUST analyze the returned data and provide clear risk assessment with reasoning based on 
login patterns, location consistency, device familiarity, and behavioral anomalies while protecting PII.

Parameters:
- user_identifier: User email, login, or Okta ID (REQUIRED)

Returns comprehensive login behavior data including:
• User details: status, profile information
• Login events: Last 10 policy.evaluate_sign_on events with full context
• Location patterns: Geographic information for each login event
• Network data: ISP, proxy detection, network organization details
• Device fingerprints: Unique device identifiers and consistency analysis
• Behavioral analysis: Okta's risk scoring and anomaly detection
• Baseline patterns: User's typical behavior patterns for comparison

The tool collects raw data only - risk decisions must be made by analyzing:
1. CRITICAL: VPN/Tor/Proxy usage in network data (immediate HIGH RISK)
2. CRITICAL: threat_suspected field (if true, immediate HIGH RISK)
3. Geographic impossibility (multiple distant locations in short timeframes)
4. Location consistency across events
5. Network/ISP consistency patterns
6. Device fingerprint familiarity
7. User agent (OS/browser) stability
8. Okta's behavioral risk scores and flags
9. Authentication timing and outcome patterns

Examples:
• analyze_login_risk(user_identifier="john@company.com")
• analyze_login_risk(user_identifier="john.smith")
• analyze_login_risk(user_identifier="00u1abc2def3ghi4jk5")
Parameters|Type|Description
-|-|-
`user_identifier`|`string`|User email, login, or Okta ID (required)

---
#### Tool: **`analyze_user_app_access`**
Comprehensive access analysis for users and applications.

SPECIAL TOOL: Collects ALL access-related data including user details, assignments, 
application info, policy rules, MFA factors, and network zones. Returns comprehensive 
raw data for LLM analysis without making access decisions.

The LLM MUST analyze the returned data and provide clear access determination with 
specific reasoning based on user status, application assignments, and policy rule evaluation.

Parameters:
- app_identifier: Application name, label, or Okta ID (REQUIRED)
- user_identifier: User email, login, or ID (optional if group provided)
- group_identifier: Group name or ID (optional if user provided)

Note: Either user_identifier OR group_identifier must be provided.

Returns comprehensive analysis data including:
• User details (if user specified): status, profile, MFA factors
• Group details (if group specified): name, description, type
• Application details: status, sign-on mode, access policy
• Assignment status: direct or group-based assignments
• Policy rules: access conditions, network zones, MFA requirements with detailed zone/user/group info
• Network zones: IP ranges, gateway details for policy evaluation

The tool collects raw data only - access decisions must be made by analyzing:
1. User/Group must be ACTIVE
2. User/Group must be assigned to application (directly or via group)
3. All policy rules must be satisfied (network zones, MFA, etc.)

Examples:
• analyze_user_app_access(app_identifier="Salesforce", user_identifier="john@company.com")
• analyze_user_app_access(app_identifier="Office 365", group_identifier="Sales Team")
• analyze_user_app_access(app_identifier="0oa1bc2def3ghi4jk5l6", user_identifier="00u1abc2def3ghi4jk5")
Parameters|Type|Description
-|-|-
`app_identifier`|`string`|Application name, label, or Okta ID (required)
`group_identifier`|`string` *optional*|Group name or Okta ID (optional if user_identifier provided)
`user_identifier`|`string` *optional*|User email, login, or Okta ID (optional if group_identifier provided)

---
#### Tool: **`get_current_time`**
Get the current date and time in UTC, formatted for Okta API usage.

Returns current UTC timestamp in ISO 8601 format with microseconds and Z suffix,
suitable for Okta API date parameters and filtering.

Buffer Hours:
Use buffer_hours to get times in the past (negative) or future (positive):
• buffer_hours=0: Current time
• buffer_hours=-24: 24 hours ago  
• buffer_hours=-168: 1 week ago (7*24 hours)
• buffer_hours=24: 24 hours from now

Output Format:
Returns timestamp in format: YYYY-MM-DDTHH:MM:SS.ffffffZ
Example: 2024-06-23T14:30:15.123456Z

Use Cases:
• Log event filtering: since="2024-06-22T00:00:00.000Z"
• User creation filters: lastUpdated gt "timestamp"
• Application audit queries with time ranges
• Policy rule time-based conditions

Perfect for constructing Okta API queries that require precise timestamps.
Parameters|Type|Description
-|-|-
`buffer_hours`|`integer` *optional*|Optional number of hours to add/subtract from current time

---
#### Tool: **`get_okta_application`**
Get detailed information about a specific Okta application.

Returns comprehensive application details including:
• Basic information: name, label, status, description
• Sign-on configuration: mode, credentials, authentication settings
• User assignment settings and policies
• Group assignment configuration
• Application-specific settings and features
• Provisioning configuration (if applicable)
• Application URLs and endpoints
• Custom attributes and profile mappings

Application Status Values:
• ACTIVE - Application is active and available to users
• INACTIVE - Application is disabled and not available

Sign-On Modes:
• SAML_2_0 - SAML 2.0 federation
• OPENID_CONNECT - OpenID Connect/OAuth 2.0
• SECURE_PASSWORD_STORE - Password-based with secure storage
• AUTO_LOGIN - Automatic login with stored credentials
• BOOKMARK - Simple bookmark/link application
• BASIC_AUTH - HTTP Basic Authentication
• BROWSER_PLUGIN - Browser plugin required
• WS_FEDERATION - WS-Federation protocol

Use this tool to get complete application configuration details for troubleshooting,
auditing, or configuration review purposes.
Parameters|Type|Description
-|-|-
`app_id`|`string`|The ID of the application to retrieve

---
#### Tool: **`get_okta_event_logs`**
Get Okta system log events with comprehensive filtering and full pagination for complete audit trails.

Returns detailed log events from Okta system logs including authentication, user management,
application access, policy changes, and administrative actions with complete audit information.

Time Parameters:
• since - Start time in ISO 8601 format: "2024-06-01T00:00:00.000Z"
• until - End time in ISO 8601 format: "2024-06-23T23:59:59.999Z"
• Use datetime tools to generate proper timestamps: parse_relative_time("24 hours ago")

Filter Parameter:
Uses Okta expression language for precise event filtering:
• eventType eq "user.authentication.auth" - Authentication events
• eventType eq "user.lifecycle.create" - User creation events
• eventType eq "user.lifecycle.activate" - User activation events
• eventType eq "user.lifecycle.suspend" - User suspension events
• eventType eq "application.lifecycle.create" - App creation events
• outcome.result eq "SUCCESS" - Successful events only
• outcome.result eq "FAILURE" - Failed events only
• actor.id eq "user_id" - Events by specific user
• target.id eq "target_id" - Events targeting specific resource

Common Event Types:
• user.authentication.auth - User login attempts
• user.authentication.sso - SSO authentication
• user.session.start - Session initiation
• user.session.end - Session termination
• user.lifecycle.create - User creation
• user.lifecycle.activate - User activation
• user.lifecycle.suspend - User suspension
• user.lifecycle.unsuspend - User reactivation
• user.lifecycle.deactivate - User deactivation
• application.user_membership.add - App assignment
• application.user_membership.remove - App removal
• group.user_membership.add - Group membership addition
• group.user_membership.remove - Group membership removal
• policy.lifecycle.create - Policy creation
• policy.lifecycle.update - Policy modification

Search Parameter:
Free-text search across event data:
• Search for usernames, email addresses, application names
• Search for IP addresses, client information
• Search for error messages or specific text in events

Sort Order:
• DESCENDING - Most recent events first (default)
• ASCENDING - Oldest events first

Example Filters:
• Authentication failures: 'eventType eq "user.authentication.auth" and outcome.result eq "FAILURE"'
• User lifecycle changes: 'eventType sw "user.lifecycle"'
• Application events: 'eventType sw "application"'
• Admin actions: 'actor.type eq "User" and eventType sw "policy"'
• Specific user activity: 'actor.alternateId eq "user@company.com"'

This tool uses full pagination to return complete audit trails for compliance,
security analysis, and forensic investigation purposes.

Use for security monitoring, compliance auditing, troubleshooting authentication
issues, and comprehensive log analysis.
Parameters|Type|Description
-|-|-
`filter_string`|`string` *optional*|Filter expression for log events
`q`|`string` *optional*|Search term for log events
`since`|`string` *optional*|Starting time for log events (ISO 8601 format)
`sort_order`|`string` *optional*|Order of results (ASCENDING or DESCENDING)
`until`|`string` *optional*|Ending time for log events (ISO 8601 format)

---
#### Tool: **`get_okta_group`**
Get detailed information about a specific Okta group.

Returns comprehensive group information including:
• Group profile (name, description, custom attributes)
• Group type and classification
• Membership statistics
• Creation and modification timestamps
• Group settings and configuration

Group Information Includes:
• Basic details (ID, name, description)
• Group type (OKTA_GROUP, BUILT_IN, APP_GROUP)
• Profile attributes and custom fields
• Administrative metadata
• Object class and schema information

Group Types:
• OKTA_GROUP - Standard organizational groups
• BUILT_IN - System groups like "Everyone"
• APP_GROUP - Application-specific groups

Common Use Cases:
• Verify group configuration
• Audit group settings and metadata
• Get group details for membership operations
• Compliance and access reviews
• Troubleshoot group-related issues
Parameters|Type|Description
-|-|-
`group_id`|`string`|The ID of the group to retrieve

---
#### Tool: **`get_okta_policy_rule`**
Get detailed information about a specific Okta policy rule.

Returns comprehensive rule configuration including:
• Authentication methods and requirements
• Network zone constraints and IP restrictions
• User and group targeting conditions
• Device and platform requirements
• Session management behaviors
• Risk assessment criteria

Rule Details Include:
• Rule identification (ID, name, description)
• Activation status and priority
• Condition expressions and logic
• Action specifications and behaviors
• Administrative metadata

Authentication Rule Information:
• Required MFA factors and methods
• Factor sequencing and fallbacks
• Enrollment requirements
• Verification policies

Network Zone Constraints:
• Allowed/blocked IP ranges
• Geographic restrictions
• Proxy and VPN handling
• Dynamic zone evaluation

Access Control Actions:
• Grant/deny decisions
• Step-up authentication triggers
• Session duration and management
• Redirect behaviors

Risk and Context Factors:
• Device trust requirements
• Location-based rules
• Behavioral analysis integration
• Threat intelligence inputs

Common Use Cases:
• Detailed rule configuration review
• Security policy troubleshooting
• Compliance audit requirements
• Rule modification planning
• Access control verification
Parameters|Type|Description
-|-|-
`policy_id`|`string`|The ID of the policy that contains the rule
`rule_id`|`string`|The ID of the specific rule to retrieve

---
#### Tool: **`get_okta_user`**
Get detailed information about a specific Okta user.
Parameters|Type|Description
-|-|-
`user_id`|`string`|Enter the login of the user to retrieve details for

---
#### Tool: **`list_okta_application_groups`**
List all groups assigned to a specific Okta application with full pagination.

Returns complete list of all groups assigned to the application including:
• Group information (ID, name, description, type)
• Assignment details and configuration
• Group assignment scope and permissions
• Application-specific group attributes
• Assignment timestamps and metadata

Group Assignment Types:
• Direct assignment - Group explicitly assigned to application
• Inherited assignment - Group assigned via policy or rule

Group Types:
• OKTA_GROUP - Standard Okta group
• APP_GROUP - Application-imported group
• BUILT_IN - Built-in Okta group (Everyone, etc.)

Assignment Scope:
• USER - Group assignment applies to user access
• GROUP - Group assignment for group-level permissions

This tool uses full pagination to return ALL assigned groups, ensuring complete
visibility into group-based application access for security reviews and auditing.

Use for application access governance, group assignment reviews, and troubleshooting
group-based access issues.
Parameters|Type|Description
-|-|-
`app_id`|`string`|The ID of the application

---
#### Tool: **`list_okta_application_users`**
List all users assigned to a specific Okta application with full pagination.

Returns complete list of all users assigned to the application including:
• User profile information (ID, email, name, status)
• Assignment details (scope, credentials, profile)
• Assignment timestamps and metadata
• Application-specific user attributes
• User status within the application context

Assignment Types:
• Direct assignment - User assigned directly to application
• Group assignment - User assigned via group membership
• Rule-based assignment - User assigned via assignment rules

User Assignment Status:
• PROVISIONED - User is provisioned and active in application
• STAGED_FOR_PROVISIONING - User staged for provisioning
• DEPROVISIONED - User removed from application
• SUSPENDED - User temporarily suspended in application

This tool uses full pagination to return ALL assigned users, which may take longer
for applications with many users but ensures complete data for compliance and auditing.

Use for application access reviews, user assignment audits, and troubleshooting
user access issues.
Parameters|Type|Description
-|-|-
`app_id`|`string`|The ID of the application

---
#### Tool: **`list_okta_applications`**
List all applications in the Okta organization with pagination and filtering.

OAuth 2.0 scopes: okta.apps.read

Lists all apps in the org with pagination. A subset of apps can be returned that match 
a supported filter expression or query. The results are paginated according to the 
limit parameter. If there are multiple pages of results, the header contains a next link.

Note: To list all of a member's assigned app links, use the List all assigned app 
links endpoint in the User Resources API.

Query Parameters:

q (string): Searches for apps with name or label properties that starts with the q 
value using the startsWith operation.
Example: q=Okta

filter (string): Filters apps by status, user.id, group.id, credentials.signing.kid 
or name expression that supports the eq operator.

Filter Examples:
• Filter for active apps: status eq "ACTIVE"
• Filter for apps with specific name: name eq "okta_org2org"
• Filter for apps using a specific key: credentials.signing.kid eq "SIMcCQNY3uwXoW3y0vf6VxiBb5n9pf8L2fK8d-F1bm4"
• Filter by user assignment: user.id eq "00u1emaK22p5pX0123d7"
• Filter by group assignment: group.id eq "00g1emaK22p5pX0123d7"

limit (integer): Specifies the number of results per page (1-200, default 50).
Use the after cursor to request additional pages when more results are available.

after (string): Specifies the pagination cursor for the next page of results. 
Treat this as an opaque value obtained through the next link relationship.

use_optimization (boolean): Specifies whether to use query optimization. If true, 
the response contains a subset of app instance properties for better performance.

include_non_deleted (boolean): Specifies whether to include non-active, but not 
deleted apps in the results.

expand (string): An optional parameter for link expansion to embed more resources 
in the response. Only supports expand=user/{userId} and must be used with the 
user.id eq "{userId}" filter query for the same user.

Application Status Values:
• ACTIVE - Application is active and available to users
• INACTIVE - Application is disabled and not available

Common Sign-On Modes:
• SAML_2_0, OPENID_CONNECT, SECURE_PASSWORD_STORE, AUTO_LOGIN
• BOOKMARK, BASIC_AUTH, BROWSER_PLUGIN, WS_FEDERATION

Returns application details including ID, name, label, status, and sign-on configuration.
Parameters|Type|Description
-|-|-
`after`|`string` *optional*|Pagination cursor for the next page of results
`expand`|`string` *optional*|Link expansion to embed more resources (supports expand=user/{userId})
`filter`|`string` *optional*|Filters apps by status, user.id, group.id, credentials.signing.kid or name
`include_non_deleted`|`boolean` *optional*|Include non-active, but not deleted apps
`limit`|`integer` *optional*|Maximum applications to return per page (1-200, default 50)
`q`|`string` *optional*|Searches for apps with name or label properties that start with the q value
`use_optimization`|`boolean` *optional*|Use query optimization for subset of app properties

---
#### Tool: **`list_okta_group_users`**
List all users in a specific Okta group with full pagination for complete results.

Returns complete group membership including:
• All users currently in the group
• User profile information
• Membership timestamps and details
• User status and account information

Pagination Handling:
This tool automatically handles pagination to return ALL users in the group,
not just the first page. For large groups, this ensures complete membership visibility.

User Information Includes:
• Basic user profile (name, email, username)
• User status (ACTIVE, SUSPENDED, etc.)
• User ID for further operations
• Profile attributes relevant to group membership

Group Membership Details:
• Current active memberships only
• No historical membership data
• Real-time membership status
• Direct group membership (not inherited)

Performance Considerations:
• Large groups may take longer to process
• Automatic rate limiting to prevent API throttling
• Progress reporting for long-running operations
• Graceful handling of pagination errors

Common Use Cases:
• Complete group membership audit
• User access reviews and compliance
• Group cleanup and optimization
• Security group verification
• Bulk user operations on group members
Parameters|Type|Description
-|-|-
`group_id`|`string`|The ID of the group to list users for

---
#### Tool: **`list_okta_groups`**
List Okta groups with filtering - limited to 50 groups by default for context efficiency.

IMPORTANT LIMITATIONS:
Limited to 50 groups by default (max 100) to stay within LLM context limits.
Use search filters to find specific groups rather than browsing all groups.

Search Parameters (priority order):
1. search - SCIM filter syntax (recommended for precise filtering)
2. query - Simple text search against group name
3. filter_type - Basic type/status filtering

SCIM Filter Syntax (search parameter):
Uses SCIM filter expressions for precise group filtering.

Supported Operators:
• eq (equals), ne (not equals), gt (greater than), lt (less than)
• ge (greater than or equal), le (less than or equal)
• sw (starts with), co (contains), pr (present)
• and (logical AND), or (logical OR)

Common Group Profile Fields:
• profile.name - Group name
• profile.description - Group description
• type - Group type (OKTA_GROUP, BUILT_IN, etc.)
• created, lastUpdated, lastMembershipUpdated
• Custom profile attributes

Example SCIM Filters:
• Engineering groups: 'profile.name co "Engineering"'
• Groups starting with Admin: 'profile.name sw "Admin"'
• Multiple departments: 'profile.name co "Engineering" or profile.name co "Sales"'
• Built-in groups: 'type eq "BUILT_IN"'
• Groups with descriptions: 'profile.description pr'
• Recent groups: 'created gt "2024-01-01T00:00:00.000Z"'

Query Parameter:
Simple text search that matches against group name.
Use when you want broad matching without specific SCIM syntax.

Filter Type Parameter:
Basic filtering for type or status. Examples: 'type eq "OKTA_GROUP"'

Group Types:
• OKTA_GROUP - Standard Okta groups
• BUILT_IN - System built-in groups (Everyone, etc.)
• APP_GROUP - Application-specific groups

Common Use Cases:
• Find department or team groups
• Audit security and admin groups
• Locate application-specific groups
• Review group membership structures
• Compliance and access reviews
Parameters|Type|Description
-|-|-
`filter_type`|`string` *optional*|Filter type (type, status, etc.)
`max_results`|`integer` *optional*|Maximum groups to return (1-100). Limited for LLM context window.
`query`|`string` *optional*|Simple text search matched against group name
`search`|`string` *optional*|SCIM filter syntax - see docstring for complete syntax

---
#### Tool: **`list_okta_network_zones`**
List all network zones defined in the Okta organization.

Return

[...]

## Screenshots

![Okta screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/okta-mcp-fctr-1.gif)

![Okta screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/okta-mcp-fctr-2.png)
