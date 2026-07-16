Manage applications powered by AWS AppSync.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-appsync-mcp-server](https://hub.docker.com/repository/docker/mcp/aws-appsync-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (10)
Tools provided by this Server|Short Description
-|-
`create_api`|Create AppSync API|
`create_api_cache`|Create API Cache|
`create_api_key`|Create API Key|
`create_channel_namespace`|Create Channel Namespace|
`create_datasource`|Create Data Source|
`create_domain_name`|Create Domain Name|
`create_function`|Create Function|
`create_graphql_api`|Create GraphQL API|
`create_resolver`|Create Resolver|
`create_schema`|Create Schema|

---
## Tools Details

#### Tool: **`create_api`**
Creates a new AppSync API.

        This operation creates a new AppSync API with the specified configuration.
        The API will be created with default settings and can be further configured
        using additional AppSync operations.
Parameters|Type|Description
-|-|-
`name`|`string`|The name of the API
`event_config`|`string` *optional*|The event configuration for the API
`owner_contact`|`string` *optional*|The owner contact information for the API
`tags`|`string` *optional*|A map of tags to assign to the resource

---
#### Tool: **`create_api_cache`**
Creates a cache for the GraphQL API.

        This operation creates an API cache for the specified GraphQL API. Caching improves
        performance by storing frequently requested data and reducing the number of requests
        to data sources.
Parameters|Type|Description
-|-|-
`api_caching_behavior`|`string`|Caching behavior. Valid values: FULL_REQUEST_CACHING, PER_RESOLVER_CACHING
`api_id`|`string`|The GraphQL API ID
`ttl`|`integer`|TTL in seconds for entries in the API cache. Valid values are 1-3600 seconds
`type`|`string`|The cache instance type. Valid values: SMALL, MEDIUM, LARGE, XLARGE, LARGE_2X, LARGE_4X, LARGE_8X, LARGE_12X
`at_rest_encryption_enabled`|`string` *optional*|At-rest encryption flag for cache
`health_metrics_config`|`string` *optional*|The health metrics configuration. Valid values: ENABLED, DISABLED
`transit_encryption_enabled`|`string` *optional*|Transit encryption flag when connecting to cache

---
#### Tool: **`create_api_key`**
Creates a unique key that you can distribute to clients who invoke your API.

        This operation creates an API key for the specified GraphQL API. API keys are used
        to authenticate requests when the API uses API_KEY authentication type.
Parameters|Type|Description
-|-|-
`api_id`|`string`|The ID for the GraphQL API
`description`|`string` *optional*|A description of the purpose of the API key
`expires`|`string` *optional*|From the creation time, the time after which the API key expires (Unix timestamp)

---
#### Tool: **`create_channel_namespace`**
Creates a ChannelNamespace for an Api.

        This operation creates a channel namespace for the specified GraphQL API.
        Channel namespaces provide a way to organize and manage real-time subscriptions
        in AppSync APIs, enabling event-driven architectures and real-time data updates.
Parameters|Type|Description
-|-|-
`api_id`|`string`|The ID of the Api associated with the ChannelNamespace
`name`|`string`|The name of the ChannelNamespace
`code_handlers`|`string` *optional*|The event handler functions that run custom business logic to process published events and subscribe requests
`handler_configs`|`string` *optional*|Configuration for event handlers that process published events and subscribe requests
`publish_auth_modes`|`string` *optional*|The authorization mode to use for publishing messages on the channel namespace
`subscribe_auth_modes`|`string` *optional*|The authorization mode to use for subscribing to messages on the channel namespace
`tags`|`string` *optional*|A map of tags to assign to the resource

---
#### Tool: **`create_datasource`**
Creates a DataSource object for a GraphQL API.

        This operation creates a data source for the specified GraphQL API. Data sources
        connect your GraphQL API to various backend services like DynamoDB, Lambda,
        HTTP endpoints, and more.
Parameters|Type|Description
-|-|-
`api_id`|`string`|The API ID for the GraphQL API for the DataSource
`name`|`string`|A user-supplied name for the DataSource
`type`|`string`|The type of the DataSource. Valid values: AWS_LAMBDA, AMAZON_DYNAMODB, AMAZON_ELASTICSEARCH, HTTP, NONE, RELATIONAL_DATABASE, AMAZON_EVENTBRIDGE, AMAZON_OPENSEARCH_SERVICE
`description`|`string` *optional*|A description of the DataSource
`dynamodb_config`|`string` *optional*|Amazon DynamoDB settings
`elasticsearch_config`|`string` *optional*|Amazon OpenSearch Service settings
`event_bridge_config`|`string` *optional*|Amazon EventBridge settings
`http_config`|`string` *optional*|HTTP endpoint settings
`lambda_config`|`string` *optional*|AWS Lambda settings
`metrics_config`|`string` *optional*|Enables or disables enhanced DataSource metrics. Valid values: ENABLED, DISABLED
`open_search_service_config`|`string` *optional*|Amazon OpenSearch Service settings
`relational_database_config`|`string` *optional*|Relational database settings
`service_role_arn`|`string` *optional*|The AWS IAM service role ARN for the data source. Format: arn:aws:iam::ACCOUNT-ID:role/ROLE-NAME

---
#### Tool: **`create_domain_name`**
Creates a custom domain name for use with AppSync APIs.

        This operation creates a custom domain name that can be associated with
        AppSync APIs, allowing you to use your own domain instead of the default
        AppSync domain. Requires an SSL certificate from AWS Certificate Manager.
Parameters|Type|Description
-|-|-
`certificate_arn`|`string`|The ARN of the certificate from AWS Certificate Manager
`domain_name`|`string`|The domain name to create (e.g., api.example.com)
`description`|`string` *optional*|A description of the domain name
`tags`|`string` *optional*|A map of tags to assign to the resource

---
#### Tool: **`create_function`**
Creates a Function object for a GraphQL API.

        This operation creates a function for the specified GraphQL API. Functions
        are reusable pieces of resolver logic that can be attached to multiple fields
        in your GraphQL schema.
Parameters|Type|Description
-|-|-
`api_id`|`string`|The GraphQL API ID
`data_source_name`|`string`|The Function DataSource name
`name`|`string`|The Function name
`code`|`string` *optional*|The function code that contains the request and response functions
`description`|`string` *optional*|The Function description
`function_version`|`string` *optional*|The version of the request mapping template. Currently, the supported value is 2018-05-29
`max_batch_size`|`string` *optional*|The maximum batching size for a resolver
`request_mapping_template`|`string` *optional*|The Function request mapping template
`response_mapping_template`|`string` *optional*|The Function response mapping template
`runtime`|`string` *optional*|Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function
`sync_config`|`string` *optional*|Describes a Sync configuration for a resolver

---
#### Tool: **`create_graphql_api`**
Creates a GraphQL API.

        This operation creates a new GraphQL API with the specified configuration.
        The API will be created with the authentication type and other settings provided.
        Supports various authentication types including API_KEY, AWS_IAM, AMAZON_COGNITO_USER_POOLS,
        OPENID_CONNECT, and AWS_LAMBDA.

        When authentication_type is API_KEY, an API key is automatically created with a 7-day expiry.
Parameters|Type|Description
-|-|-
`authentication_type`|`string`|The authentication type: API_KEY, AWS_IAM, AMAZON_COGNITO_USER_POOLS, OPENID_CONNECT, AWS_LAMBDA
`name`|`string`|A user-supplied name for the GraphQL API
`additional_authentication_providers`|`string` *optional*|A list of additional authentication providers
`api_type`|`string` *optional*|The value that indicates whether the GraphQL API is a standard API (GRAPHQL) or merged API (MERGED)
`enhanced_metrics_config`|`string` *optional*|The enhancedMetricsConfig object
`introspection_config`|`string` *optional*|Sets the value of the GraphQL API to enable (ENABLED) or disable (DISABLED) introspection
`lambda_authorizer_config`|`string` *optional*|Configuration for AWS Lambda function authorization
`log_config`|`string` *optional*|The Amazon CloudWatch Logs configuration
`merged_api_execution_role_arn`|`string` *optional*|The Identity and Access Management service role ARN for a merged API
`open_id_connect_config`|`string` *optional*|The OpenID Connect configuration
`owner_contact`|`string` *optional*|The owner contact information for an API resource
`query_depth_limit`|`string` *optional*|The maximum depth a query can have in a single request
`resolver_count_limit`|`string` *optional*|The maximum number of resolvers that can be invoked in a single request
`tags`|`string` *optional*|A TagMap object
`user_pool_config`|`string` *optional*|The Amazon Cognito user pool configuration
`visibility`|`string` *optional*|Sets the value of the GraphQL API to public (GLOBAL) or private (PRIVATE)
`xray_enabled`|`string` *optional*|A flag indicating whether to enable X-Ray tracing

---
#### Tool: **`create_resolver`**
Creates a resolver for a GraphQL field in an AppSync API.

        A resolver is the bridge between your GraphQL schema and your data sources.
        It defines how to fetch or modify data for a specific field in your schema.
        Resolvers can be unit resolvers (attached to a single data source) or
        pipeline resolvers (composed of multiple functions).
Parameters|Type|Description
-|-|-
`api_id`|`string`|The API ID for the GraphQL API
`field_name`|`string`|The name of the field to attach the resolver to
`type_name`|`string`|The name of the type (e.g., Query, Mutation, Subscription)
`caching_config`|`string` *optional*|Caching configuration for the resolver
`code`|`string` *optional*|The resolver code for JavaScript/TypeScript resolvers
`data_source_name`|`string` *optional*|The name of the data source (required for unit resolvers)
`kind`|`string` *optional*|The resolver kind: UNIT or PIPELINE
`max_batch_size`|`string` *optional*|Maximum batch size for batch operations
`metrics_config`|`string` *optional*|Metrics configuration: ENABLED or DISABLED
`pipeline_config`|`string` *optional*|Pipeline configuration for PIPELINE resolvers with functions list
`request_mapping_template`|`string` *optional*|The request mapping template in VTL (Velocity Template Language)
`response_mapping_template`|`string` *optional*|The response mapping template in VTL (Velocity Template Language)
`runtime`|`string` *optional*|Runtime configuration (name and runtimeVersion)
`sync_config`|`string` *optional*|Sync configuration for conflict resolution

---
#### Tool: **`create_schema`**
Creates a GraphQL schema for an AppSync API and polls until completion.

        This tool starts the schema creation process and automatically polls for the status
        until the operation completes (either SUCCESS or FAILED). The schema defines the
        structure of your GraphQL API, including types, queries, mutations, and subscriptions.
Parameters|Type|Description
-|-|-
`api_id`|`string`|The API ID for the GraphQL API
`definition`|`string`|The schema definition in GraphQL Schema Definition Language (SDL)

---

## Screenshots

![AWS AppSync screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-appsync-1.png)

![AWS AppSync screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-appsync-2.png)

![AWS AppSync screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-appsync-3.png)
