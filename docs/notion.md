Official Notion MCP Server.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/notion](https://hub.docker.com/repository/docker/mcp/notion)
**Author**|[makenotion](https://github.com/makenotion)
**Repository**|https://github.com/makenotion/notion-mcp-server

## Available Tools (24)
Tools provided by this Server|Short Description
-|-
`API-create-a-comment`|Create A Comment|
`API-create-a-data-source`|Create A Data Source|
`API-delete-a-block`|Delete A Block|
`API-get-block-children`|Get Block Children|
`API-get-self`|Get Self|
`API-get-user`|Get User|
`API-get-users`|Get Users|
`API-list-data-source-templates`|List Data Source Templates|
`API-move-page`|Move Page|
`API-patch-block-children`|Patch Block Children|
`API-patch-page`|Patch Page|
`API-post-page`|Post Page|
`API-post-search`|Post Search|
`API-query-data-source`|Query Data Source|
`API-retrieve-a-block`|Retrieve A Block|
`API-retrieve-a-comment`|Retrieve A Comment|
`API-retrieve-a-data-source`|Retrieve A Data Source|
`API-retrieve-a-database`|Retrieve A Database|
`API-retrieve-a-page`|Retrieve A Page|
`API-retrieve-a-page-property`|Retrieve A Page Property|
`API-retrieve-page-markdown`|Retrieve Page Markdown|
`API-update-a-block`|Update A Block|
`API-update-a-data-source`|Update A Data Source|
`API-update-page-markdown`|Update Page Markdown|

---
## Tools Details

#### Tool: **`API-create-a-comment`**
Notion | Create comment
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`parent`|`string`|
`rich_text`|`array`|

*This tool may perform destructive updates.*

---
#### Tool: **`API-create-a-data-source`**
Notion | Create a data source
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`parent`|`string`|
`properties`|`string`|
`title`|`array` *optional*|

*This tool may perform destructive updates.*

---
#### Tool: **`API-delete-a-block`**
Notion | Delete a block
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`block_id`|`string`|Identifier for a Notion block

*This tool may perform destructive updates.*

---
#### Tool: **`API-get-block-children`**
Notion | Retrieve block children
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`block_id`|`string`|Identifier for a [block](ref:block)
`page_size`|`integer` *optional*|The number of items from the full list desired in the response. Maximum: 100
`start_cursor`|`string` *optional*|If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-get-self`**
Notion | Retrieve your token's bot user
Error Responses:
400: Bad request
#### Tool: **`API-get-user`**
Notion | Retrieve a user
Error Responses:
400: 400
Parameters|Type|Description
-|-|-
`user_id`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-get-users`**
Notion | List all users
Error Responses:
400: 400
Parameters|Type|Description
-|-|-
`page_size`|`integer` *optional*|The number of items from the full list desired in the response. Maximum: 100
`start_cursor`|`string` *optional*|If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-list-data-source-templates`**
Notion | List templates in a data source
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`data_source_id`|`string`|Identifier for a Notion data source
`page_size`|`integer` *optional*|
`start_cursor`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-move-page`**
Notion | Move a page
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`page_id`|`string`|Identifier for a Notion page
`parent`|`string`|

*This tool may perform destructive updates.*

---
#### Tool: **`API-patch-block-children`**
Notion | Append block children
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`block_id`|`string`|Identifier for a [block](ref:block). Also accepts a [page](ref:page) ID.
`children`|`array`|Child content to append to a container block as an array of [block objects](ref:block)
`after`|`string` *optional*|The ID of the existing block that the new block should be appended after.

*This tool may perform destructive updates.*

---
#### Tool: **`API-patch-page`**
Notion | Update page properties
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`page_id`|`string`|The identifier for the Notion page to be updated.
`archived`|`boolean` *optional*|
`cover`|`string` *optional*|
`icon`|`string` *optional*|
`in_trash`|`boolean` *optional*|Set to true to delete a block. Set to false to restore a block.
`properties`|`string` *optional*|

*This tool may perform destructive updates.*

---
#### Tool: **`API-post-page`**
Notion | Create a page
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`parent`|`string`|
`properties`|`string`|
`children`|`array` *optional*|The content to be rendered on the new page, represented as an array of [block objects](https://developers.notion.com/reference/block).
`cover`|`string` *optional*|The cover image of the new page, represented as a [file object](https://developers.notion.com/reference/file-object).
`icon`|`string` *optional*|The icon of the new page. Either an [emoji object](https://developers.notion.com/reference/emoji-object) or an [external file object](https://developers.notion.com/reference/file-object)..

*This tool may perform destructive updates.*

---
#### Tool: **`API-post-search`**
Notion | Search by title
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`filter`|`string` *optional*|
`page_size`|`integer` *optional*|The number of items from the full list to include in the response. Maximum: `100`.
`query`|`string` *optional*|The text that the API compares page and database titles against.
`sort`|`string` *optional*|
`start_cursor`|`string` *optional*|A `cursor` value returned in a previous response that If supplied, limits the response to results starting after the `cursor`. If not supplied, then the first page of results is returned. Refer to [pagination](https://developers.notion.com/reference/intro#pagination) for more details.

*This tool may perform destructive updates.*

---
#### Tool: **`API-query-data-source`**
Notion | Query a data source
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`data_source_id`|`string`|Identifier for a Notion data source (database)
`archived`|`boolean` *optional*|
`filter`|`string` *optional*|
`filter_properties`|`array` *optional*|A list of page property value IDs to limit the response
`in_trash`|`boolean` *optional*|
`page_size`|`integer` *optional*|
`sorts`|`array` *optional*|
`start_cursor`|`string` *optional*|

*This tool may perform destructive updates.*

---
#### Tool: **`API-retrieve-a-block`**
Notion | Retrieve a block
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`block_id`|`string`|Identifier for a Notion block

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-retrieve-a-comment`**
Notion | Retrieve comments
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`block_id`|`string`|Identifier for a Notion block or page
`page_size`|`integer` *optional*|The number of items from the full list desired in the response. Maximum: 100
`start_cursor`|`string` *optional*|If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-retrieve-a-data-source`**
Notion | Retrieve a data source
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`data_source_id`|`string`|Identifier for a Notion data source

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-retrieve-a-database`**
Notion | Retrieve a database
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`database_id`|`string`|Identifier for a Notion database

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-retrieve-a-page`**
Notion | Retrieve a page
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`page_id`|`string`|Identifier for a Notion page
`filter_properties`|`string` *optional*|A list of page property value IDs associated with the page. Use this param to limit the response to a specific page property value or values. To retrieve multiple properties, specify each page property ID. For example: `?filter_properties=iAk8&filter_properties=b7dh`.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-retrieve-a-page-property`**
Notion | Retrieve a page property item
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`page_id`|`string`|Identifier for a Notion page
`property_id`|`string`|Identifier for a page [property](https://developers.notion.com/reference/page#all-property-values)
`page_size`|`integer` *optional*|For paginated properties. The max number of property item objects on a page. The default size is 100
`start_cursor`|`string` *optional*|For paginated properties.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-retrieve-page-markdown`**
Notion | Retrieve a page as Markdown
Error Responses:
400: Bad request
403: The integration lacks the read/update content capability required for this page.
404: Page not found or not shared with the integration.
429: Rate limited.
Parameters|Type|Description
-|-|-
`page_id`|`string`|Identifier for a Notion page (or block) to read or update as markdown.
`include_transcript`|`boolean` *optional*|Whether to include meeting note transcripts. When false (default), a placeholder with the meeting note URL is shown instead of the full transcript.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`API-update-a-block`**
Notion | Update a block
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`block_id`|`string`|Identifier for a Notion block
`archived`|`boolean` *optional*|Set to true to archive (delete) a block. Set to false to un-archive (restore) a block.
`type`|`string` *optional*|

*This tool may perform destructive updates.*

---
#### Tool: **`API-update-a-data-source`**
Notion | Update a data source
Error Responses:
400: Bad request
Parameters|Type|Description
-|-|-
`data_source_id`|`string`|Identifier for a Notion data source
`description`|`array` *optional*|
`properties`|`string` *optional*|
`title`|`array` *optional*|

*This tool may perform destructive updates.*

---
#### Tool: **`API-update-page-markdown`**
Notion | Update a page's content as Markdown
Error Responses:
400: Bad request
403: The integration lacks the read/update content capability required for this page.
404: Page not found or not shared with the integration.
409: Conflict (e.g. row limit exceeded).
429: Rate limited.
Parameters|Type|Description
-|-|-
`page_id`|`string`|Identifier for a Notion page (or block) to read or update as markdown.
`type`|`string`|The kind of edit to apply. Prefer `replace_content` (overwrite the whole page) or `update_content` (targeted find-and-replace). `insert_content` and `replace_content_range` are deprecated.
`insert_content`|`string` *optional*|
`replace_content`|`string` *optional*|
`replace_content_range`|`string` *optional*|
`update_content`|`string` *optional*|

*This tool may perform destructive updates.*

---

## Screenshots

![Notion screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/notion-1.png)

![Notion screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/notion-2.png)

![Notion screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/notion-3.png)
