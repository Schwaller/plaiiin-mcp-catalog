Postman's MCP server connects AI agents, assistants, and chatbots directly to your APIs on Postman. Use natural language to prompt AI to automate work across your Postman collections, environments, workspaces, and more.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/postman](https://hub.docker.com/repository/docker/mcp/postman)
**Author**|[postmanlabs](https://github.com/postmanlabs)
**Repository**|https://github.com/postmanlabs/postman-mcp-server

## Available Tools (42)
Tools provided by this Server|Short Description
-|-
`createCollection`|Creates a collection using the [Postman Collection v2.1.0 schema format](https://schema.postman.com/collection/json/v2.1.0/draft-07/docs/index.html).|
`createCollectionRequest`|Creates a request in a collection. For a complete list of properties, refer to the **Request** entry in the [Postman Collection Format documentation](https://schema.postman.com/collection/json/v2.1.0/draft-07/docs/index.html).|
`createCollectionResponse`|Creates a request response in a collection. For a complete list of request body properties, refer to the **Response** entry in the [Postman Collection Format documentation](https://schema.postman.com/collection/json/v2.1.0/draft-07/docs/index.html).|
`createEnvironment`|Creates an environment.|
`createMock`|Creates a mock server in a collection.|
`createSpec`|Creates an API specification in Postman's [Spec Hub](https://learning.postman.com/docs/design-apis/specifications/overview/). Specifications can be single or multi-file.|
`createSpecFile`|Creates a file for an OpenAPI or a protobuf 2 or 3 specification.|
`createWorkspace`|Creates a new [workspace](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/).|
`duplicateCollection`|Creates a duplicate of the given collection in another workspace.|
`generateCollection`|Creates a collection from the given API specification.|
`generateSpecFromCollection`|Generates an OpenAPI 2.0, 3.0, or 3.1 specification for the given collection. The response contains a polling link to the task status.|
`getAllSpecs`|Gets all API specifications in a workspace.|
`getAuthenticatedUser`|Gets information about the authenticated user.|
`getCollection`|Get Collection (map by default)|
`getCollections`|The workspace ID query is required for this endpoint. If not provided, the LLM should ask the user to provide it.|
`getDuplicateCollectionTaskStatus`|Gets the status of a collection duplication task.|
`getEnabledTools`|Get Enabled Tools|
`getEnvironment`|Gets information about an environment.|
`getEnvironments`|Gets information about all of your [environments](https://learning.postman.com/docs/sending-requests/managing-environments/).|
`getGeneratedCollectionSpecs`|Gets the API specification generated for the given collection.|
`getMock`|Gets information about a mock server.|
`getMocks`|Gets all active mock servers. By default, returns only mock servers you created across all workspaces.|
`getSpec`|Gets information about an API specification.|
`getSpecCollections`|Gets all of an API specification's generated collections.|
`getSpecDefinition`|Gets the complete contents of an OpenAPI or AsyncAPI specification's definition.|
`getSpecFile`|Gets the contents of an API specification's file.|
`getSpecFiles`|Gets all the files in an API specification.|
`getTaggedEntities`|**Requires an Enterprise plan.** Tagging is only available on Postman Enterprise plans. This tool returns a 404 error on Free, Basic, and Professional accounts.|
`getWorkspace`|Gets information about a workspace.|
`getWorkspaces`|Gets all workspaces you have access to.|
`publishMock`|Publishes a mock server. Publishing a mock server sets its **Access Control** configuration setting to public.|
`putCollection`|Replaces the contents of a collection using the [Postman Collection v2.1.0 schema format](https://schema.postman.com/collection/json/v2.1.0/draft-07/docs/index.html). Include the collection's ID values in the request body. If you do not, the endpoint removes the existing items and creates new items.|
`putEnvironment`|Replaces all the contents of an environment with the given information.|
`runCollection`|Run Postman Collection|
`searchPostmanElements`|Search for Postman entities (requests, collections, workspaces, specs, flows, environments, mocks).|
`syncCollectionWithSpec`|Syncs a collection generated from an API specification. This is an asynchronous endpoint that returns an HTTP \`202 Accepted\` response.|
`syncSpecWithCollection`|Syncs an API specification linked to a collection. This is an asynchronous endpoint that returns an HTTP \`202 Accepted\` response.|
`updateCollectionRequest`|Updates a request in a collection. For a complete list of properties, refer to the **Request** entry in the [Postman Collection Format documentation](https://schema.postman.com/collection/json/v2.1.0/draft-07/docs/index.html).|
`updateMock`|Updates a mock server.|
`updateSpecFile`|Updates a file for an OpenAPI or protobuf 2 or 3 specification.|
`updateSpecProperties`|Updates an API specification's properties, such as its name.|
`updateWorkspace`|Updates a workspace's property, such as its name or visibility.|

---
## Tools Details

#### Tool: **`createCollection`**
Creates a collection using the [Postman Collection v2.1.0 schema format](https://schema.postman.com/collection/json/v2.1.0/draft-07/docs/index.html).

**Note:**

If you do not include the \`workspace\` query parameter, the system creates the collection in the oldest personal Internal workspace you own.
Parameters|Type|Description
-|-|-
`workspace`|`string`|The workspace's ID.
`collection`|`object` *optional*|

---
#### Tool: **`createCollectionRequest`**
Creates a request in a collection. For a complete list of properties, refer to the **Request** entry in the [Postman Collection Format documentation](https://schema.postman.com/collection/json/v2.1.0/draft-07/docs/index.html).

**Note:**

It is recommended that you pass the \`name\` property in the request body. If you do not, the system uses a null value. As a result, this creates a request with a blank name.
Parameters|Type|Description
-|-|-
`collectionId`|`string`|The collection's ID.
`auth`|`string` *optional*|The request's authentication information.
`data`|`string` *optional*|The request body's form data.
`dataMode`|`string` *optional*|The request body's data mode.
`dataOptions`|`string` *optional*|Additional configurations and options set for the request body's various data modes.
`description`|`string` *optional*|The request's description.
`events`|`string` *optional*|A list of scripts configured to run when specific events occur.
`folderId`|`string` *optional*|The folder ID in which to create the request. By default, the system will create the request at the collection level.
`graphqlModeData`|`string` *optional*|The request body's GraphQL mode data.
`headerData`|`array` *optional*|The request's headers.
`method`|`string` *optional*|The request's HTTP method.
`name`|`string` *optional*|The request's name. It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a request with a blank name.
`queryParams`|`array` *optional*|The request's query parameters.
`rawModeData`|`string` *optional*|The request body's raw mode data.
`url`|`string` *optional*|The request's URL.

---
#### Tool: **`createCollectionResponse`**
Creates a request response in a collection. For a complete list of request body properties, refer to the **Response** entry in the [Postman Collection Format documentation](https://schema.postman.com/collection/json/v2.1.0/draft-07/docs/index.html).

**Note:**

It is recommended that you pass the \`name\` property in the request body. If you do not, the system uses a null value. As a result, this creates a response with a blank name.
Parameters|Type|Description
-|-|-
`collectionId`|`string`|The collection's ID.
`request`|`string`|The parent request's ID.
`cookies`|`string` *optional*|The response's cookie data.
`dataMode`|`string` *optional*|The associated request body's data mode.
`dataOptions`|`string` *optional*|Additional configurations and options set for the request body's various data modes.
`description`|`string` *optional*|The response's description.
`headers`|`array` *optional*|A list of headers.
`language`|`string` *optional*|The response body's language type.
`method`|`string` *optional*|The request's HTTP method.
`mime`|`string` *optional*|The response's MIME type.
`name`|`string` *optional*|The response's name. It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a response with a blank name.
`rawDataType`|`string` *optional*|The response's raw data type.
`rawModeData`|`string` *optional*|The associated request body's raw mode data.
`requestObject`|`string` *optional*|A JSON-stringified representation of the associated request.
`responseCode`|`object` *optional*|The response's HTTP response code information.
`status`|`string` *optional*|The response's HTTP status text.
`text`|`string` *optional*|The raw text of the response body.
`time`|`string` *optional*|The time taken by the request to complete, in milliseconds.
`url`|`string` *optional*|The associated request's URL.

---
#### Tool: **`createEnvironment`**
Creates an environment.

**Note:**

- The request body size cannot exceed the maximum allowed size of 30MB.
- If you receive an HTTP \`411 Length Required\` error response, manually pass the \`Content-Length\` header and its value in the request header.
- If you do not include the \`workspace\` query parameter, the system creates the environment in the oldest personal Internal workspace you own.
Parameters|Type|Description
-|-|-
`workspace`|`string`|The workspace's ID.
`environment`|`object` *optional*|Information about the environment.

---
#### Tool: **`createMock`**
Creates a mock server in a collection.

- Pass the collection UID (ownerId-collectionId), not the bare collection ID.
- If you only have a \`collectionId\`, resolve the UID first:
  1) Prefer GET \`/collections/{collectionId}\` and read \`uid\`, or
  2) Construct \`{ownerId}-{collectionId}\` using ownerId from GET \`/me\`:
    - For team-owned collections: \`ownerId = me.teamId\`
    - For personal collections: \`ownerId = me.user.id\`
- Use the \`workspace\` query to place the mock in a specific workspace. Prefer explicit workspace scoping.
Parameters|Type|Description
-|-|-
`workspace`|`string`|The workspace's ID.
`mock`|`object` *optional*|

---
#### Tool: **`createSpec`**
Creates an API specification in Postman's [Spec Hub](https://learning.postman.com/docs/design-apis/specifications/overview/). Specifications can be single or multi-file.

**Note:**
- Postman supports OpenAPI (2.0, 3.0, and 3.1), AsyncAPI (2.0 and 3.0), protobuf (2 and 3), GraphQL, and Smithy specifications.
- If the file path contains a \`/\` (forward slash) character, then a folder is created. For example, if the path is the \`components/schemas.json\` value, then a \`components\` folder is created with the \`schemas.json\` file inside.
- Multi-file specifications can only have one root file.
- Files cannot exceed a maximum of 12 MB in size.
Parameters|Type|Description
-|-|-
`files`|`array`|A list of the specification's files and their contents.
`name`|`string`|The specification's name.
`type`|`string`|The type of API specification.
`workspaceId`|`string`|The workspace's ID.

---
#### Tool: **`createSpecFile`**
Creates a file for an OpenAPI or a protobuf 2 or 3 specification.

**Note:**

- If the file path contains a \`/\` (forward slash) character, then a folder is created. For example, if the path is the \`components/schemas.json\` value, then a \`components\` folder is created with the \`schemas.json\` file inside.
- Creating a spec file assigns it the \`DEFAULT\` file type.
- Multi-file specifications can only have one root file.
- Files cannot exceed a maximum of 10 MB in size.
Parameters|Type|Description
-|-|-
`content`|`string`|The file's stringified contents.
`path`|`string`|The file's path. Accepts JSON or YAML files.
`specId`|`string`|The spec's ID.

---
#### Tool: **`createWorkspace`**
Creates a new [workspace](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/).

**Note:**

- This endpoint returns a 403 \`Forbidden\` response if the user does not have permission to create workspaces. [Admins and Super Admins](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles) can configure workspace permissions to restrict users and/or user groups from creating workspaces or require approvals for the creation of team workspaces.
- Private and [Partner Workspaces](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) are available on Postman [**Team** and **Enterprise** plans](https://www.postman.com/pricing).
- There are rate limits when publishing public workspaces.
- Public team workspace names must be unique.
- The \`teamId\` property must be passed in the request body if [Postman Organizations](https://learning.postman.com/docs/administration/onboarding-checklist) is enabled.
Parameters|Type|Description
-|-|-
`workspace`|`object` *optional*|Information about the workspace.

---
#### Tool: **`duplicateCollection`**
Creates a duplicate of the given collection in another workspace.

Use the GET \`/collection-duplicate-tasks/{taskId}\` endpoint to get the duplication task's current status.
Parameters|Type|Description
-|-|-
`collectionId`|`string`|The collection's unique ID.
`workspace`|`string`|The workspace ID in which to duplicate the collection.
`suffix`|`string` *optional*|An optional suffix to append to the duplicated collection's name.

---
#### Tool: **`generateCollection`**
Creates a collection from the given API specification.
The specification must already exist or be created before it can be used to generate a collection.
The response contains a polling link to the task status.
Parameters|Type|Description
-|-|-
`elementType`|`string`|The `collection` element type.
`name`|`string`|The generated collection's name.
`options`|`object`|The advanced creation options and their values. For more details, see Postman's [OpenAPI to Postman Collection Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive.
`specId`|`string`|The spec's ID.

---
#### Tool: **`generateSpecFromCollection`**
Generates an OpenAPI 2.0, 3.0, or 3.1 specification for the given collection. The response contains a polling link to the task status.
Parameters|Type|Description
-|-|-
`collectionUid`|`string`|The collection's unique ID.
`elementType`|`string`|The `spec` value.
`format`|`string`|The format of the API specification.
`name`|`string`|The API specification's name.
`type`|`string`|The specification's type.

---
#### Tool: **`getAllSpecs`**
Gets all API specifications in a workspace.
Parameters|Type|Description
-|-|-
`workspaceId`|`string`|The workspace's ID.
`cursor`|`string` *optional*|The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter.
`limit`|`integer` *optional*|The maximum number of rows to return in the response.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getAuthenticatedUser`**
Gets information about the authenticated user.
- This endpoint provides “current user” context (\`user.id\`, \`username\`, \`teamId\`, roles).
- When a user asks for “my …” (e.g., “my workspaces, my information, etc.”), call this first to resolve the user ID.
#### Tool: **`getCollection`**
Get information about a collection. By default this tool returns the lightweight collection map (metadata + recursive itemRefs).
Use the model parameter to opt in to Postman's full API responses:
- model=minimal — root-level folder/request IDs only
- model=full — full Postman collection payload.
Parameters|Type|Description
-|-|-
`collectionId`|`string`|The collection ID must be in the form <OWNER_ID>-<UUID> (e.g. 12345-33823532ab9e41c9b6fd12d0fd459b8b).
`access_key`|`string` *optional*|A collection's read-only access key. Using this query parameter does not require an API key to call the endpoint.
`model`|`string` *optional*|Optional response shape override. Omit to receive the lightweight collection map. Set to `minimal` for the Postman minimal model or `full` for the complete collection payload.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getCollections`**
The workspace ID query is required for this endpoint. If not provided, the LLM should ask the user to provide it.
Parameters|Type|Description
-|-|-
`workspace`|`string`|The workspace's ID.
`limit`|`integer` *optional*|The maximum number of rows to return in the response.
`name`|`string` *optional*|Filter results by collections whose name exactly matches the given value. Partial or substring matches are not supported.
`offset`|`integer` *optional*|The zero-based offset of the first item to return.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getDuplicateCollectionTaskStatus`**
Gets the status of a collection duplication task.
Parameters|Type|Description
-|-|-
`taskId`|`string`|The task's unique ID.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getEnabledTools`**
IMPORTANT: Run this tool first when a requested tool is unavailable. Returns information about which tools are enabled in the full and minimal tool sets, helping you identify available alternatives.
#### Tool: **`getEnvironment`**
Gets information about an environment.
Parameters|Type|Description
-|-|-
`environmentId`|`string`|The environment's ID.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getEnvironments`**
Gets information about all of your [environments](https://learning.postman.com/docs/sending-requests/managing-environments/).
Parameters|Type|Description
-|-|-
`workspace`|`string` *optional*|The workspace's ID.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getGeneratedCollectionSpecs`**
Gets the API specification generated for the given collection.
Parameters|Type|Description
-|-|-
`collectionUid`|`string`|The collection's unique ID.
`elementType`|`string`|The `spec` value.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getMock`**
Gets information about a mock server.
- Resource: Mock server entity. Response includes the associated \`collection\` UID and \`mockUrl\`.
- Use the \`collection\` UID to navigate back to the source collection.
Parameters|Type|Description
-|-|-
`mockId`|`string`|The mock's ID.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getMocks`**
Gets all active mock servers. By default, returns only mock servers you created across all workspaces.

- Always pass either the \`workspace\` or \`teamId\` query to scope results. Prefer \`workspace\` when known.
- If you need team-scoped results, set \`teamId\` from the current user: call GET \`/me\` and use \`me.teamId\`.
- If both \`teamId\` and \`workspace\` are passed, only \`workspace\` is used.
Parameters|Type|Description
-|-|-
`teamId`|`string` *optional*|Return only results that belong to the given team ID.
- For team-scoped requests, set this from GET `/me` (`me.teamId`).

`workspace`|`string` *optional*|Return only results found in the given workspace ID.
- Prefer this parameter when the user mentions a specific workspace.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getSpec`**
Gets information about an API specification.
Parameters|Type|Description
-|-|-
`specId`|`string`|The spec's ID.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getSpecCollections`**
Gets all of an API specification's generated collections.
Parameters|Type|Description
-|-|-
`elementType`|`string`|The `collection` element type.
`specId`|`string`|The spec's ID.
`cursor`|`string` *optional*|The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter.
`limit`|`integer` *optional*|The maximum number of rows to return in the response.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getSpecDefinition`**
Gets the complete contents of an OpenAPI or AsyncAPI specification's definition.
Parameters|Type|Description
-|-|-
`specId`|`string`|The spec's ID.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getSpecFile`**
Gets the contents of an API specification's file.
Parameters|Type|Description
-|-|-
`filePath`|`string`|The path to the file.
`specId`|`string`|The spec's ID.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getSpecFiles`**
Gets all the files in an API specification.
Parameters|Type|Description
-|-|-
`specId`|`string`|The spec's ID.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getTaggedEntities`**
**Requires an Enterprise plan.** Tagging is only available on Postman Enterprise plans. This tool returns a 404 error on Free, Basic, and Professional accounts.

Gets Postman elements (entities) by a given tag. Tags enable you to organize and search workspaces, APIs, and collections that contain shared tags.
Parameters|Type|Description
-|-|-
`slug`|`string`|The tag's ID within a team or individual (non-team) user scope.
`cursor`|`string` *optional*|The cursor to get the next set of results in the paginated response. If you pass an invalid value, the API only returns the first set of results.
`direction`|`string` *optional*|The ascending (`asc`) or descending (`desc`) order to sort the results by, based on the time of the entity's tagging.
`entityType`|`string` *optional*|Filter results for the given entity type.
`limit`|`integer` *optional*|The maximum number of tagged elements to return in a single call.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getWorkspace`**
Gets information about a workspace.

**Note:**

This endpoint's response contains the \`visibility\` field. [Visibility](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility) determines who can access the workspace:
- \`personal\` — Only you can access the workspace.
- \`team\` — All team members can access the workspace.
- \`private\` — Only invited team members can access the workspace ([**Team** and **Enterprise** plans only](https://www.postman.com/pricing)).
- \`public\` — Everyone can access the workspace.
- \`partner\` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Team** and **Enterprise** plans only](https://www.postman.com/pricing)).
Parameters|Type|Description
-|-|-
`workspaceId`|`string`|The workspace's ID.
`include`|`string` *optional*|Include the following information in the endpoint's response:
- `mocks:deactivated` — Include all deactivated mock servers in the response.
- `scim` — Return the SCIM user IDs of the workspace creator and who last modified it.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`getWorkspaces`**
Gets all workspaces you have access to.
- For “my …” requests, first call GET \`/me\` and pass \`createdBy={me.user.id}\`.
- This endpoint's response contains the visibility field. Visibility determines who can access the workspace:
  - \`personal\` — Only you can access the workspace.
  - \`team\` — All team members can access the workspace.
  - \`private\` — Only invited team members can access the workspace (Professional and Enterprise).
  - \`public\` — Everyone can access the workspace.
  - \`partner\` — Invited team members and partners (Professional and Enterprise).
- For tools that require the

[...]
