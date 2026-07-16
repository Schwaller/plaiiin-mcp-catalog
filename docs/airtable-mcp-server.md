Provides AI assistants with direct access to Airtable bases, allowing them to read schemas, query records, and interact with your Airtable data. Supports listing bases, retrieving table structures, and searching through records to help automate workflows and answer questions about your organized data.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/airtable-mcp-server](https://hub.docker.com/repository/docker/mcp/airtable-mcp-server)
**Author**|[domdomegg](https://github.com/domdomegg)
**Repository**|https://github.com/domdomegg/airtable-mcp-server

## Available Tools (16)
Tools provided by this Server|Short Description
-|-
`create_comment`|Create a comment on a record|
`create_field`|Create a new field in a table|
`create_record`|Create a new record in a table|
`create_table`|Create a new table in a base|
`delete_records`|Delete records from a table|
`describe_table`|Get detailed information about a specific table|
`get_record`|Get a specific record by ID|
`list_bases`|List all accessible Airtable bases|
`list_comments`|List comments on a record|
`list_records`|List records from a table|
`list_tables`|List all tables in a specific base|
`search_records`|Search for records containing specific text|
`update_field`|Update a field's name or description|
`update_records`|Update up to 10 records in a table|
`update_table`|Update a table's name or description|
`upload_attachment`|Upload a file directly to an attachment field on an existing record using Airtable's upload API.|

---
## Tools Details

#### Tool: **`create_comment`**
Create a comment on a record
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`recordId`|`string`|The ID of the record
`tableId`|`string`|The ID or name of the table
`text`|`string`|The comment text
`parentCommentId`|`string` *optional*|Optional parent comment ID for threaded replies

---
#### Tool: **`create_field`**
Create a new field in a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`nested`|`object`|
`tableId`|`string`|The ID or name of the table

---
#### Tool: **`create_record`**
Create a new record in a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`fields`|`object`|The fields for the new record
`tableId`|`string`|The ID or name of the table

---
#### Tool: **`create_table`**
Create a new table in a base
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`fields`|`array`|Array of field definitions
`name`|`string`|The name of the table
`description`|`string` *optional*|Optional description for the table

---
#### Tool: **`delete_records`**
Delete records from a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`recordIds`|`array`|Array of record IDs to delete
`tableId`|`string`|The ID or name of the table

*This tool may perform destructive updates.*

---
#### Tool: **`describe_table`**
Get detailed information about a specific table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`tableId`|`string`|The ID or name of the table
`detailLevel`|`string` *optional*|Detail level for table information:
- tableIdentifiersOnly: table IDs and names
- identifiersOnly: table, field, and view IDs and names
- full: complete details including field types, descriptions, and configurations

Note for LLMs: To optimize context window usage, request the minimum detail level needed:
- Use 'tableIdentifiersOnly' when you only need to list or reference tables
- Use 'identifiersOnly' when you need to work with field or view references
- Only use 'full' when you need field types, descriptions, or other detailed configuration

If you only need detailed information on a few tables in a base with many complex tables, it might be more efficient for you to use list_tables with tableIdentifiersOnly, then describe_table with full on the specific tables you want.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_record`**
Get a specific record by ID
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`recordId`|`string`|The ID of the record
`tableId`|`string`|The ID or name of the table

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_bases`**
List all accessible Airtable bases
#### Tool: **`list_comments`**
List comments on a record
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`recordId`|`string`|The ID of the record
`tableId`|`string`|The ID or name of the table
`offset`|`string` *optional*|Offset for pagination
`pageSize`|`number` *optional*|Number of comments to return (max 100, default 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_records`**
List records from a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`tableId`|`string`|The ID or name of the table
`filterByFormula`|`string` *optional*|A formula used to filter records
`maxRecords`|`number` *optional*|The maximum total number of records that will be returned
`sort`|`array` *optional*|A list of sort objects that specifies how the records will be ordered
`view`|`string` *optional*|The name or ID of a view in the table

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_tables`**
List all tables in a specific base
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`detailLevel`|`string` *optional*|Detail level for table information:
- tableIdentifiersOnly: table IDs and names
- identifiersOnly: table, field, and view IDs and names
- full: complete details including field types, descriptions, and configurations

Note for LLMs: To optimize context window usage, request the minimum detail level needed:
- Use 'tableIdentifiersOnly' when you only need to list or reference tables
- Use 'identifiersOnly' when you need to work with field or view references
- Only use 'full' when you need field types, descriptions, or other detailed configuration

If you only need detailed information on a few tables in a base with many complex tables, it might be more efficient for you to use list_tables with tableIdentifiersOnly, then describe_table with full on the specific tables you want.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`search_records`**
Search for records containing specific text
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`searchTerm`|`string`|The text to search for
`tableId`|`string`|The ID or name of the table
`fieldIds`|`array` *optional*|Optional array of field IDs to search in
`maxRecords`|`number` *optional*|The maximum total number of records that will be returned
`view`|`string` *optional*|The name or ID of a view in the table

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`update_field`**
Update a field's name or description
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`fieldId`|`string`|The ID of the field
`tableId`|`string`|The ID or name of the table
`description`|`string` *optional*|New description for the field
`name`|`string` *optional*|New name for the field

*This tool may perform destructive updates.*

---
#### Tool: **`update_records`**
Update up to 10 records in a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`records`|`array`|Array of records to update (max 10)
`tableId`|`string`|The ID or name of the table

*This tool may perform destructive updates.*

---
#### Tool: **`update_table`**
Update a table's name or description
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`tableId`|`string`|The ID or name of the table
`description`|`string` *optional*|New description for the table
`name`|`string` *optional*|New name for the table

*This tool may perform destructive updates.*

---
#### Tool: **`upload_attachment`**
Upload a file directly to an attachment field on an existing record using Airtable's upload API. Supports files up to 5 MB. For larger files, use create_record or update_records with a public URL. The record must already exist.
Parameters|Type|Description
-|-|-
`attachmentFieldIdOrName`|`string`|The ID or name of the attachment field (e.g. fldXXXXXXXXXXXXXX or "Images")
`baseId`|`string`|The ID of the base
`contentType`|`string`|MIME type of the file (e.g. "image/jpeg", "image/png", "application/pdf")
`file`|`string`|Raw base64-encoded file content (no data URL prefix)
`filename`|`string`|Filename for the attachment (e.g. "image.jpg")
`recordId`|`string`|The ID of the existing record (e.g. recXXXXXXXXXXXXXX)

---
