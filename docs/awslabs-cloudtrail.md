AWS CloudTrail audit logging and monitoring.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/cloudtrail-mcp-server](https://hub.docker.com/repository/docker/mcp/cloudtrail-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (5)
Tools provided by this Server|Short Description
-|-
`get_query_results`|Get the results of a completed CloudTrail Lake query with pagination support.|
`get_query_status`|Get the status of a CloudTrail Lake query.|
`lake_query`|Execute a SQL query against CloudTrail Lake for complex analytics and filtering.|
`list_event_data_stores`|List available CloudTrail Lake Event Data Stores with their capabilities and event selectors.|
`lookup_events`|Look up CloudTrail events based on various criteria.|

---
## Tools Details

#### Tool: **`get_query_results`**
Get the results of a completed CloudTrail Lake query with pagination support.

This tool retrieves the results of a previously executed CloudTrail Lake query. It supports
pagination for large result sets, allowing you to fetch results in chunks.

Usage: Use this tool to get the results of a query that has completed (status = 'FINISHED').
For large result sets, use the next_token to fetch subsequent pages of results.

Pagination workflow:
1. Call get_query_results with just the query_id to get the first page
2. If next_token is returned, call again with the same query_id and the next_token
3. Repeat until next_token is null/empty

Returns:
--------
QueryResult containing:
    - query_id: The query identifier
    - query_status: Current status of the query
    - query_result_rows: Results for this page
    - next_token: Token for next page (null if no more pages)
    - query_statistics: Performance statistics for the query
Parameters|Type|Description
-|-|-
`query_id`|`string`|The ID of the query to get results for
`max_results`|`string` *optional*|Maximum number of results to return per page (1-50, default: 50)
`next_token`|`string` *optional*|Token for pagination to fetch the next page of results. Use the next_token returned from a previous call to get successive pages.
`region`|`string` *optional*|AWS region to query. Defaults to us-east-1.

---
#### Tool: **`get_query_status`**
Get the status of a CloudTrail Lake query.

This tool checks the status of a previously started CloudTrail Lake query. Use this
when you need to check if a long-running query has completed or if you want to get
details about query execution.

Usage: Use this tool to monitor the progress of CloudTrail Lake queries, especially
long-running ones that may take time to complete.

Returns:
--------
QueryStatus containing:
    - query_id: The query identifier
    - query_status: Current status (QUEUED, RUNNING, FINISHED, FAILED, CANCELLED, TIMED_OUT)
    - query_statistics: Performance and execution statistics
    - error_message: Error details if the query failed
Parameters|Type|Description
-|-|-
`query_id`|`string`|The ID of the query to check status for
`region`|`string` *optional*|AWS region to query. Defaults to us-east-1.

---
#### Tool: **`lake_query`**
Execute a SQL query against CloudTrail Lake for complex analytics and filtering.

CloudTrail Lake allows you to run SQL queries against your CloudTrail events for advanced
analysis. This is more powerful than the basic lookup functions and allows for complex
filtering, aggregation, and analysis.

PAGINATION WORKFLOW:
For large result sets, you have two options:
1. Use wait_for_completion=False to get the query_id immediately, then use get_query_results with pagination
2. Use wait_for_completion=True (default) to get first page of results, then use get_query_results with next_token for additional pages

IMPORTANT LIMITATIONS:
- CloudTrail Lake only supports SELECT statements using Trino-compatible SQL syntax
- INSERT, UPDATE, DELETE, CREATE, DROP, and other DDL/DML operations are not supported
- Do not use Common Table Expression (CTE)
- Your SQL query MUST include a valid Event Data Store (EDS) ID in the FROM clause
- Use the list_event_data_stores tool first to get available EDS IDs, then reference the EDS ID
  directly in your FROM clause
- Always use a start and end time using eventtime or have a limit on total output by default

CLOUDTRAIL EVENT SCHEMA:
All CloudTrail events contain these key fields that you can query:

Core Fields (Always Present):
- eventTime: UTC timestamp when request completed
- eventVersion: Log format version (current: 1.11)
- eventSource: AWS service name (e.g., "s3.amazonaws.com")
- eventName: API action name
- awsRegion: AWS region where request was made
- sourceIPAddress: IP address of requester
- eventID: Unique GUID for this event
- eventType: AwsApiCall, AwsServiceEvent, AwsConsoleAction, AwsConsoleSignIn, AwsVpceEvent
- eventCategory: Management, Data, NetworkActivity, Insight

UserIdentity Object (Always Present):
- userIdentity.type: Root, IAMUser, AssumedRole, Role, FederatedUser, Directory, AWSAccount, AWSService, IdentityCenterUser, SAMLUser, WebIdentityUser, Unknown
- userIdentity.principalId: Unique identifier for the entity
- userIdentity.arn: ARN of the principal
- userIdentity.accountId: Account that owns the entity
- userIdentity.accessKeyId: Access key used (may be empty for security)
- userIdentity.userName: Friendly name (when available)
- userIdentity.invokedBy: AWS service that made the request
- userIdentity.identityProvider: External identity provider (SAML/Web)
- userIdentity.credentialId: Bearer token credential ID
- userIdentity.sessionContext: For temporary credentials (AssumedRole, FederatedUser)
  - sessionIssuer.type: Source type (Root, IAMUser, Role)
  - sessionIssuer.principalId: Internal ID of issuer
  - sessionIssuer.arn: ARN of issuer
  - sessionIssuer.accountId: Account of issuer
  - sessionIssuer.userName: Name of credential issuer
  - attributes.mfaAuthenticated: "true"/"false" if MFA was used
  - attributes.creationDate: When credentials were issued (ISO 8601)
  - webIdFederationData.federatedProvider: Identity provider name
  - webIdFederationData.attributes: Provider-specific attributes
  - sourceIdentity: Original user identity for role chaining
  - ec2RoleDelivery: "1.0" or "2.0" for IMDS version
  - assumedRoot: True for AssumeRoot sessions
- userIdentity.onBehalfOf: IAM Identity Center user info
  - userId: Identity Center user ID
  - identityStoreArn: Identity store ARN
- userIdentity.inScopeOf: Service scope information
  - sourceArn: Invoking resource ARN
  - sourceAccount: Source account ID
  - issuerType: Credential issuer type
  - credentialsIssuedTo: Credential target resource

Optional Fields (Conditionally Present):
- userAgent: Client that made the request (max 1KB)
- errorCode: AWS service error code if request failed (max 1KB)
- errorMessage: Error description if request failed (max 1KB)
- requestParameters: Request parameters (object, max 100KB)
- responseElements: Response elements for write operations (object, max 100KB)
- additionalEventData: Additional event data (object, max 28KB)
- requestID: Service-generated request identifier (max 1KB)
- apiVersion: API version for AwsApiCall events
- managementEvent: True if management event
- readOnly: true/false if read-only operation
- resources: Array of resources accessed
  - resources[].type: Resource type (e.g., "AWS::S3::Object", "AWS::DynamoDB::Table")
  - resources[].ARN: Resource ARN
  - resources[].accountId: Resource owner account
- recipientAccountId: Account that received the event
- serviceEventDetails: Service event details (object, max 100KB)
- sharedEventID: Shared GUID for cross-account events
- vpcEndpointId: VPC endpoint identifier (for network events)
- vpcEndpointAccountId: VPC endpoint owner account
- addendum: Information about delayed/updated events
  - reason: Why event was delayed (DELIVERY_DELAY, UPDATED_DATA, SERVICE_OUTAGE)
  - updatedFields: Event record fields updated by addendum
  - originalRequestID: Original unique ID of request
  - originalEventID: Original event ID
- sessionCredentialFromConsole: "true" if from console session
- eventContext: Enriched event context (tags, IAM conditions)
  - requestContext: IAM condition keys evaluated during authorization
  - tagContext: Tags associated with resources and IAM principals
    - resourceTags: Array of resource tag information
      - resourceTags[].arn: ARN of the tagged resource
      - resourceTags[].tags: Object containing tag key-value pairs
    - principalTags: Tags associated with the IAM principal making the request
- edgeDeviceDetails: Edge device information (object, max 28KB)
- tlsDetails: TLS connection information
  - tlsVersion: TLS version used
  - cipherSuite: Cipher suite used
  - clientProvidedHostHeader: Client-provided hostname

Example SQL queries:
- SELECT eventname, count(*) FROM eds-id WHERE eventtime > '2025-01-01 00:00:00' GROUP BY eventname
- SELECT errorcode, errormessage, eventname FROM eds-id WHERE errorcode IS NOT NULL OR errormessage IS NOT NULL LIMIT 10
- SELECT eventname, resources FROM eds-id WHERE any_match(resources, x -> x.type = 'AWS::S3::Object') LIMIT 10
- SELECT useridentity.sessioncontext.sessionissuer.username FROM eds-id WHERE useridentity.type = 'AssumedRole' LIMIT 10
- SELECT sourceipaddress, count(*) FROM eds-id WHERE eventname = 'ConsoleLogin' GROUP BY sourceipaddress LIMIT 10
- SELECT eventname, filter(resources, x -> x.type = 'AWS::Lambda::Function') as lambda_resources FROM eds-id WHERE cardinality(filter(resources, x -> x.type = 'AWS::Lambda::Function')) > 0 LIMIT 5

Returns:
--------
QueryResult containing:
    - query_id: Unique identifier for the query
    - query_status: Current status of the query
    - query_result_rows: Results if query completed successfully (only when wait_for_completion=True)
    - next_token: Token for pagination (only when wait_for_completion=True and results are paginated)
    - query_statistics: Performance statistics for the query
Parameters|Type|Description
-|-|-
`sql`|`string`|SQL query to execute against CloudTrail Lake. IMPORTANT: You must include a valid Event Data Store (EDS) ID in the FROM clause of your SQL query. Use list_event_data_stores tool to get available EDS IDs first. CloudTrail Lake only supports SELECT statements using Trino-compatible SQL syntax. Example: SELECT * FROM 0233062b-51c6-4d18-8dec-a8c90da840d9 WHERE eventname = 'ConsoleLogin'
`region`|`string` *optional*|AWS region to query. Defaults to us-east-1.
`wait_for_completion`|`boolean` *optional*|Whether to wait for query completion and return results. If False, returns immediately with query_id for manual result fetching using get_query_results. Default: True

---
#### Tool: **`list_event_data_stores`**
List available CloudTrail Lake Event Data Stores with their capabilities and event selectors.

Event Data Stores are the storage and query engines for CloudTrail Lake. This tool helps you
understand which Event Data Stores are available and their configurations.

Usage: Use this tool to understand which Event Data Stores are available and their
configurations. This information is needed when executing CloudTrail Lake queries.

Returns:
--------
List of available Event Data Stores with their configurations
Parameters|Type|Description
-|-|-
`include_details`|`boolean` *optional*|Whether to include detailed event selector information (default: true)
`region`|`string` *optional*|AWS region to query. Defaults to us-east-1.

---
#### Tool: **`lookup_events`**
Look up CloudTrail events based on various criteria.

This tool searches CloudTrail events using the LookupEvents API, which provides access to the
last 90 days of management events. You can filter by time range and search for specific
attribute values.

Usage: Use this tool to find CloudTrail events by various attributes like username, event name,
resource name, etc. This is useful for security investigations, troubleshooting, and audit trails.

IMPORTANT PAGINATION REQUIREMENTS:
- AWS CloudTrail requires pagination tokens to be used with exactly the same parameters as the original request
- When using next_token, you must provide the exact same start_time, end_time, attribute_key, and attribute_value
- Use the 'query_params' returned in the response for subsequent paginated requests

Returns:
--------
Dictionary containing:
    - events: List of CloudTrail events matching the criteria with exact CloudTrail schema
    - next_token: Token for pagination if more results available
    - query_params: Parameters used for the query (includes pagination parameters when next_token is present)
Parameters|Type|Description
-|-|-
`attribute_key`|`string` *optional*|Attribute to search by
`attribute_value`|`string` *optional*|Value to search for in the specified attribute
`end_time`|`string` *optional*|End time for event lookup (ISO format or relative like "1 hour ago"). IMPORTANT: When using pagination (next_token), you must provide the exact same end_time as the original request.
`max_results`|`string` *optional*|Maximum number of events to return (1-50, default: 10)
`next_token`|`string` *optional*|Token for pagination to fetch the next page of events. IMPORTANT: When using this token, all other parameters (start_time, end_time, attribute_key, attribute_value) must match exactly the original request that generated this token.
`region`|`string` *optional*|AWS region to query. Defaults to us-east-1.
`start_time`|`string` *optional*|Start time for event lookup (ISO format or relative like "1 day ago"). IMPORTANT: When using pagination (next_token), you must provide the exact same start_time as the original request.

---

## Screenshots

![AWS CloudTrail screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cloudtrail-1.png)

![AWS CloudTrail screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cloudtrail-2.png)

![AWS CloudTrail screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cloudtrail-3.png)
