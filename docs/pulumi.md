Pulumi MCP server enables AI-powered coding assistants to help you codify cloud architectures and get diffs for infrastructure changes right in your development environment.

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mcp/pulumi](https://hub.docker.com/repository/docker/mcp/pulumi)
**Author**|[pulumi](https://github.com/pulumi)
**Repository**|https://github.com/pulumi/mcp-server
**Dockerfile**|https://github.com/pulumi/mcp-server/blob/main/Dockerfile
**Docker Image built by**|Docker Inc.
**Docker Scout Health Score**| ![Docker Scout Health Score](https://api.scout.docker.com/v1/policy/insights/org-image-score/badge/mcp/pulumi)
**Verify Signature**|`COSIGN_REPOSITORY=mcp/signatures cosign verify mcp/pulumi --key https://raw.githubusercontent.com/docker/keyring/refs/heads/main/public/mcp/latest.pub`
**Licence**|Apache License 2.0

## Available Tools (12)
Tools provided by this Server|Short Description
-|-
`deploy-to-aws`|Deploy application code to AWS by generating Pulumi infrastructure.|
`neo-task-launcher`|Launch a Neo task when user asks Neo to perform a task.|
`pulumi-cli-preview`|Run pulumi preview for a given project and stack|
`pulumi-cli-refresh`|Run pulumi refresh for a given project and stack|
`pulumi-cli-stack-output`|Get the output value(s) of a given stack|
`pulumi-cli-up`|Run pulumi up for a given project and stack|
`pulumi-registry-get-function`|Returns information about a Pulumi Registry function|
`pulumi-registry-get-resource`|Returns information about a Pulumi Registry resource|
`pulumi-registry-get-type`|Get the JSON schema for a specific JSON schema type reference|
`pulumi-registry-list-functions`|List all function types for a given provider and module|
`pulumi-registry-list-resources`|List all resource types for a given provider and module|
`pulumi-resource-search`|Search and analyze Pulumi-managed cloud resources using a strict subset of Lucene query syntax.|

---
## Tools Details

#### Tool: **`deploy-to-aws`**
Deploy application code to AWS by generating Pulumi infrastructure. This tool automatically analyzes your application files and provisions the appropriate AWS resources (S3, Lambda, EC2, etc.) based on what it finds. No prior analysis needed -  just invoke directly.
#### Tool: **`neo-task-launcher`**
Launch a Neo task when user asks Neo to perform a task. Pulumi Neo is a purpose-built cloud infrastructure automation agent.
Parameters|Type|Description
-|-|-
`query`|`string`|The task query to send to Neo (what the user wants Neo to do)
`context`|`string` *optional*|Optional conversation context with details of work done so far. Include: 1) Summary of what the user has been working on, 2) For any files modified, provide git diff format showing the changes, 3) Textual explanation of what was changed and why. Example: "The user has been working on authentication. Files modified: src/auth.ts - Added token support: ```diff\n- function login(user) {\n+ function login(user, token) {\n```\nThis change adds token-based auth for better security."

---
#### Tool: **`pulumi-cli-preview`**
Run pulumi preview for a given project and stack
Parameters|Type|Description
-|-|-
`workDir`|`string`|The working directory of the program.
`stackName`|`string` *optional*|The associated stack name. Defaults to 'dev'.

---
#### Tool: **`pulumi-cli-refresh`**
Run pulumi refresh for a given project and stack
Parameters|Type|Description
-|-|-
`workDir`|`string`|The working directory of the program.
`stackName`|`string` *optional*|The associated stack name. Defaults to 'dev'.

---
#### Tool: **`pulumi-cli-stack-output`**
Get the output value(s) of a given stack
Parameters|Type|Description
-|-|-
`workDir`|`string`|The working directory of the program.
`outputName`|`string` *optional*|The specific stack output name to retrieve.
`stackName`|`string` *optional*|The associated stack name. Defaults to 'dev'.

---
#### Tool: **`pulumi-cli-up`**
Run pulumi up for a given project and stack
Parameters|Type|Description
-|-|-
`workDir`|`string`|The working directory of the program.
`stackName`|`string` *optional*|The associated stack name. Defaults to 'dev'.

---
#### Tool: **`pulumi-registry-get-function`**
Returns information about a Pulumi Registry function
Parameters|Type|Description
-|-|-
`function`|`string`|The function type to query (e.g., 'getBucket', 'getFunction', 'getInstance')
`provider`|`string`|The cloud provider (e.g., 'aws', 'azure', 'gcp', 'random') or github.com/org/repo for Git-hosted components
`module`|`string` *optional*|The module to query (e.g., 's3', 'ec2', 'lambda'). If not specified it will match functions with the given name in any module.
`version`|`string` *optional*|The provider version to use (e.g., '6.0.0'). If not specified, uses the latest available version.

---
#### Tool: **`pulumi-registry-get-resource`**
Returns information about a Pulumi Registry resource
Parameters|Type|Description
-|-|-
`provider`|`string`|The cloud provider (e.g., 'aws', 'azure', 'gcp', 'random') or github.com/org/repo for Git-hosted components
`resource`|`string`|The resource type to query (e.g., 'Bucket', 'Function', 'Instance')
`module`|`string` *optional*|The module to query (e.g., 's3', 'ec2', 'lambda'). If not specified it will match resources with the given name in any module.
`version`|`string` *optional*|The provider version to use (e.g., '6.0.0'). If not specified, uses the latest available version.

---
#### Tool: **`pulumi-registry-get-type`**
Get the JSON schema for a specific JSON schema type reference
Parameters|Type|Description
-|-|-
`name`|`string`|The name of the type to query (e.g., 'BucketGrant', 'FunctionEnvironment', 'InstanceCpuOptions')
`provider`|`string`|The cloud provider (e.g., 'aws', 'azure', 'gcp', 'random') or github.com/org/repo for Git-hosted components
`module`|`string` *optional*|The module to query (e.g., 's3', 'ec2', 'lambda'). Optional for smaller providers, will be 'index by default.
`version`|`string` *optional*|The provider version to use (e.g., '6.0.0'). If not specified, uses the latest available version.

---
#### Tool: **`pulumi-registry-list-functions`**
List all function types for a given provider and module
Parameters|Type|Description
-|-|-
`provider`|`string`|The cloud provider (e.g., 'aws', 'azure', 'gcp', 'random') or github.com/org/repo for Git-hosted components
`module`|`string` *optional*|Optional module to filter by (e.g., 's3', 'ec2', 'lambda')
`version`|`string` *optional*|The provider version to use (e.g., '6.0.0'). If not specified, uses the latest available version.

---
#### Tool: **`pulumi-registry-list-resources`**
List all resource types for a given provider and module
Parameters|Type|Description
-|-|-
`provider`|`string`|The cloud provider (e.g., 'aws', 'azure', 'gcp', 'random') or github.com/org/repo for Git-hosted components
`module`|`string` *optional*|Optional module to filter by (e.g., 's3', 'ec2', 'lambda')
`version`|`string` *optional*|The provider version to use (e.g., '6.0.0'). If not specified, uses the latest available version.

---
#### Tool: **`pulumi-resource-search`**
Search and analyze Pulumi-managed cloud resources using a strict subset of Lucene query syntax.

QUERY SYNTAX RULES:
- The search query syntax is a strict subset of Lucene query syntax
- The documents being searched are Pulumi resources
- The implicit operator is AND
- Parentheses and OR are supported between fields but not within fields
- All resources are returned by default (use empty query "" to get all)
- Wildcard queries are NOT supported (no * allowed)
- Fuzzy queries are NOT supported
- Boosting is NOT supported
- Field grouping is NOT supported
- Whitespace is NOT supported
- field:value produces a match_phrase query
- field:"value" produces a term query
- -field:value produces a bool must_not match_phrase query
- -field:"value" produces a bool must_not term query
- field: produces an existence query
- Resource properties can be queried with leading dot: .property.path:value or .property.path: (existence)
- You absolutely must not produce queries that use fields other than: type, name, id, stack, project, package, modified, provider, provider_urn, team and protected, unless the field is the name of a property.
- You absolutely must not produce queries that use wildcards (e.g., *).
- You absolutely must not produce queries that use field grouping (e.g., type:(a OR b))

AVAILABLE FIELDS:
- type: Pulumi types used for pulumi import operations (e.g., aws:s3/bucket:Bucket)
- name: logical Pulumi resource names
- id: physical Pulumi resource names
- stack: name of the stack the resource belongs to
- project: name of the project the resource belongs to
- created: when the resource was first created (absolute dates only)
- modified: when the resource was last modified (absolute dates only)
- package: package of the resource (e.g., aws, gcp)
- provider: alias for the "package" field
- provider_urn: full URN of the resource's provider
- protected: boolean representing whether a resource is protected
- team: name of a team with access to the resource

IMPORTANT QUERY PATTERNS:
For AWS resources, do not use specific provider prefixes (aws: or aws-native:) in type filters. Instead:
WRONG: type:aws:s3/bucket:Bucket
WRONG: type:aws-native:s3:Bucket
CORRECT: type:"Bucket" (searches across both aws and aws-native providers)
For package filtering, use the generic package name:
CORRECT: package:aws (matches both aws and aws-native packages)
For finding resources by service, prefer the module field when possible:
PREFERRED: module:s3 (finds all S3 resources regardless of provider)
For property existence queries, always use the dot notation:
CORRECT: .tags: (checks if tags property exists)
For property negation queries (finding resources WITHOUT a property):
CORRECT: -.tags: or NOT .tags: (finds resources without tags)
COMMON TRANSLATIONS:
- "untagged resources" → -.tags: or NOT .tags:
- "resources without tags" → -.tags: or NOT .tags:

Supports field filters, boolean operators (AND, OR, NOT), exact matches with quotes, and property searches. The top parameter controls the maximum number of results to return (defaults to 20).

Resources may not have a repository url. This means that there is no available information about the repository that the resource is associated with.
Parameters|Type|Description
-|-|-
`query`|`string`|Lucene query string using strict subset syntax (see tool description for full rules). NO WILDCARDS (*) allowed.
`org`|`string` *optional*|Pulumi organization name (optional, defaults to current default org)
`properties`|`boolean` *optional*|Whether to include resource properties in the response (defaults to false). WARNING: Setting this to true produces significantly more tokens and can cause response size limits to be exceeded. Only set to true when: (1) user explicitly requests properties/details, (2) querying a very small number of specific resources, or (3) user needs property-based analysis. NOT recommended for loose queries (empty query, broad type searches, etc.) that return many resources.
`top`|`number` *optional*|Maximum number of top results to return (defaults to 20)

---
