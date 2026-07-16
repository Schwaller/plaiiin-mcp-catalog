Tools for Atlassian products (Confluence and Jira). This integration supports both Atlassian Cloud and Jira Server/Data Center deployments.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/atlassian](https://hub.docker.com/repository/docker/mcp/atlassian)
**Author**|[sooperset](https://github.com/sooperset)
**Repository**|https://github.com/sooperset/mcp-atlassian

## Available Tools (80)
Tools provided by this Server|Short Description
-|-
`confluence_add_comment`|Add Comment|
`confluence_add_inline_comment`|Add Inline Comment|
`confluence_add_label`|Add Label|
`confluence_create_page`|Create Page|
`confluence_delete_attachment`|Delete Attachment|
`confluence_delete_page`|Delete Page|
`confluence_download_attachment`|Download Attachment|
`confluence_download_content_attachments`|Download All Content Attachments|
`confluence_get_attachments`|Get Content Attachments|
`confluence_get_comments`|Get Comments|
`confluence_get_inline_comments`|Get Inline Comments|
`confluence_get_labels`|Get Labels|
`confluence_get_page`|Get Page|
`confluence_get_page_children`|Get Page Children|
`confluence_get_page_diff`|Get Page Version Diff|
`confluence_get_page_history`|Get Page History|
`confluence_get_page_images`|Get Page Images|
`confluence_get_page_views`|Get Page Views|
`confluence_get_space_page_tree`|Get Space Page Tree|
`confluence_move_page`|Move Page|
`confluence_reply_to_comment`|Reply to Comment|
`confluence_search`|Search Content|
`confluence_search_user`|Search User|
`confluence_update_page`|Update Page|
`confluence_update_page_section`|Update Page Section|
`confluence_upload_attachment`|Upload Attachment|
`confluence_upload_attachments`|Upload Multiple Attachments|
`jira_add_comment`|Add Comment|
`jira_add_issues_to_sprint`|Add Issues to Sprint|
`jira_add_watcher`|Add Issue Watcher|
`jira_add_worklog`|Add Worklog|
`jira_assign_issue`|Assign Issue|
`jira_batch_create_issues`|Batch Create Issues|
`jira_batch_create_versions`|Batch Create Versions|
`jira_batch_get_changelogs`|Batch Get Changelogs|
`jira_create_issue`|Create Issue|
`jira_create_issue_link`|Create Issue Link|
`jira_create_remote_issue_link`|Create Remote Issue Link|
`jira_create_sprint`|Create Sprint|
`jira_create_version`|Create Version|
`jira_delete_issue`|Delete Issue|
`jira_download_attachments`|Download Attachments|
`jira_edit_comment`|Edit Comment|
`jira_get_agile_boards`|Get Agile Boards|
`jira_get_all_projects`|Get All Projects|
`jira_get_board_issues`|Get Board Issues|
`jira_get_field_options`|Get Field Options|
`jira_get_issue`|Get Issue|
`jira_get_issue_dates`|Get Issue Dates|
`jira_get_issue_development_info`|Get Issue Development Info|
`jira_get_issue_images`|Get Issue Images|
`jira_get_issue_proforma_forms`|Get Issue Forms|
`jira_get_issue_sla`|Get Issue SLA|
`jira_get_issue_watchers`|Get Issue Watchers|
`jira_get_issues_development_info`|Get Issues Development Info|
`jira_get_link_types`|Get Link Types|
`jira_get_proforma_form_details`|Get Form Details|
`jira_get_project_components`|Get Project Components|
`jira_get_project_fields`|Get Project Fields|
`jira_get_project_issues`|Get Project Issues|
`jira_get_project_versions`|Get Project Versions|
`jira_get_queue_issues`|Get Queue Issues|
`jira_get_service_desk_for_project`|Get Service Desk For Project|
`jira_get_service_desk_queues`|Get Service Desk Queues|
`jira_get_sprint_issues`|Get Sprint Issues|
`jira_get_sprints_from_board`|Get Sprints from Board|
`jira_get_transitions`|Get Transitions|
`jira_get_user_profile`|Get User Profile|
`jira_get_worklog`|Get Worklog|
`jira_link_to_epic`|Link to Epic|
`jira_remove_issue_link`|Remove Issue Link|
`jira_remove_watcher`|Remove Issue Watcher|
`jira_search`|Search Issues|
`jira_search_assignable_users`|Search Assignable Users|
`jira_search_fields`|Search Fields|
`jira_transition_issue`|Transition Issue|
`jira_update_issue`|Update Issue|
`jira_update_proforma_form_answers`|Update Form Answers|
`jira_update_sprint`|Update Sprint|
`jira_update_version`|Update Version|

---
## Tools Details

#### Tool: **`confluence_add_comment`**
Add a comment to a Confluence page.
Parameters|Type|Description
-|-|-
`body`|`string`|The comment content in Markdown format
`page_id`|`string`|The ID of the page to add a comment to

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_add_inline_comment`**
Add an inline comment anchored to a text selection on a page.
Parameters|Type|Description
-|-|-
`body`|`string`|The comment content in Markdown format
`page_id`|`string`|The ID of the page to add the inline comment to
`text_selection`|`string`|The exact text on the page to anchor the inline comment to. Must match text that exists in the page content.
`text_selection_match_count`|`integer` *optional*|Total number of times the selected text appears on the page. Defaults to 1.
`text_selection_match_index`|`integer` *optional*|Zero-based index of which occurrence of the text to anchor to. Defaults to 0 (first occurrence).

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_add_label`**
Add label to Confluence content (pages, blog posts, or attachments).

Useful for:
- Categorizing attachments (e.g., 'screenshot', 'diagram', 'legal-doc')
- Tracking status (e.g., 'approved', 'needs-review', 'archived')
- Filtering content by topic or version
Parameters|Type|Description
-|-|-
`name`|`string`|Label name to add (lowercase, no spaces). Examples: 'draft', 'reviewed', 'confidential', 'v1.0'. Labels help organize and categorize content.
`page_id`|`string`|Confluence content ID to label. For pages/blogs: numeric ID (e.g., '123456789'). For attachments: ID with 'att' prefix (e.g., 'att123456789'). Use get_attachments to find attachment IDs.

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_create_page`**
Create a new Confluence page.
Parameters|Type|Description
-|-|-
`content`|`string`|The content of the page. Format depends on content_format parameter. Can be Markdown (default), wiki markup, storage format, or XHTML storage format
`space_key`|`string`|The key of the space to create the page in (usually a short uppercase code like 'DEV', 'TEAM', or 'DOC')
`title`|`string`|The title of the page
`content_format`|`string` *optional*|(Optional) The format of the content parameter. Options: 'markdown' (default), 'wiki', 'storage', or 'xhtml'. Use 'xhtml' when providing Confluence XHTML storage format (same as 'storage'). Wiki format uses Confluence wiki markup syntax
`emoji`|`string` *optional*|(Optional) Page title emoji (icon shown in navigation). Can be any emoji character like '📝', '🚀', '📚'. Set to null/None to remove.
`enable_heading_anchors`|`boolean` *optional*|(Optional) Whether to enable automatic heading anchor generation. Only applies when content_format is 'markdown'
`include_content`|`boolean` *optional*|(Optional) Whether to include page content in the response. Defaults to false since callers already have the content at create time
`parent_id`|`string` *optional*|(Optional) parent page ID. If provided, this page will be created as a child of the specified page

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_delete_attachment`**
Permanently delete an attachment from Confluence.

**Warning**: This action cannot be undone! The attachment and ALL its versions will be
permanently deleted.

Use this tool to:
- Remove outdated or incorrect attachments
- Clean up duplicate files
- Delete sensitive information that was accidentally uploaded

Best practices:
- Verify the attachment ID before deletion using get_attachments
- Consider downloading the attachment first as a backup
- Check with content owners before deleting shared attachments
Parameters|Type|Description
-|-|-
`attachment_id`|`string`|The ID of the attachment to delete. Attachment IDs can be found using the get_attachments tool. Example: 'att123456789'. **Warning**: This permanently deletes the attachment and all its versions.

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_delete_page`**
Delete an existing Confluence page.
Parameters|Type|Description
-|-|-
`page_id`|`string`|The ID of the page to delete

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_download_attachment`**
Download an attachment from Confluence as an embedded resource.

Returns the attachment content as a base64-encoded embedded resource so
that it is available over the MCP protocol without requiring filesystem
access on the server. Files larger than 50 MB are not downloaded inline;
a descriptive error message is returned instead.
Parameters|Type|Description
-|-|-
`attachment_id`|`string`|The ID of the attachment to download (e.g., 'att123456789'). Find attachment IDs using get_attachments tool. Example workflow: get_attachments(content_id) → use returned ID here.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_download_content_attachments`**
Download all attachments for a Confluence content item as embedded resources.

Returns attachment contents as base64-encoded embedded resources so that
they are available over the MCP protocol without requiring filesystem
access on the server. Files larger than 50 MB are skipped with an error
entry in the summary.
Parameters|Type|Description
-|-|-
`content_id`|`string`|The ID of the Confluence content (page or blog post) to download attachments from. Example: '123456789'

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_attachments`**
List all attachments for a Confluence content item (page or blog post).

Returns metadata about attachments including:
- Attachment ID, title, and file type
- File size and download URL
- Creation/modification dates
- Version information

**Important**: Confluence API returns 'application/octet-stream' as the media type
for most binary files (PNG, JPG, PDF) instead of specific types like 'image/png'.
For filtering by file type, using the 'filename' parameter is more reliable
(e.g., filename='*.png' pattern matching if supported, or exact filename).

Useful for:
- Discovering what files are attached to a page
- Getting attachment IDs for download operations
- Checking if a specific file exists
- Listing images/documents for processing
Parameters|Type|Description
-|-|-
`content_id`|`string`|The ID of the Confluence content (page or blog post) to list attachments for. Example: '123456789'
`filename`|`string` *optional*|(Optional) Filter results to only attachments matching this filename. Exact match only. Example: 'report.pdf'
`limit`|`integer` *optional*|(Optional) Maximum number of attachments to return per request (1-100). Use pagination (start/limit) for large attachment lists. Default: 50
`media_type`|`string` *optional*|(Optional) Filter by MIME type. **Note**: Confluence API returns 'application/octet-stream' for most binary files (PNG, JPG, PDF) instead of specific MIME types like 'image/png'. For more reliable filtering, use the 'filename' parameter. Examples: 'application/octet-stream' (binary files), 'application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' (for .docx)
`start`|`integer` *optional*|(Optional) Starting index for pagination. Use 0 for the first page. To get the next page, add the 'limit' value to 'start'. Default: 0

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_comments`**
Get comments for a specific Confluence page.
Parameters|Type|Description
-|-|-
`page_id`|`string`|Confluence page ID (numeric ID, can be parsed from URL, e.g. from 'https://example.atlassian.net/wiki/spaces/TEAM/pages/123456789/Page+Title' -> '123456789')

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_inline_comments`**
Get all inline comments for a Confluence page.
Parameters|Type|Description
-|-|-
`page_id`|`string`|The ID of the page to get inline comments from

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_labels`**
Get labels for Confluence content (pages, blog posts, or attachments).
Parameters|Type|Description
-|-|-
`page_id`|`string`|Confluence content ID (page, blog post, or attachment). For pages: numeric ID from URL (e.g., '123456789'). For attachments: ID with 'att' prefix (e.g., 'att123456789'). Works with any Confluence content type that supports labels.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_page`**
Get content of a specific Confluence page by its ID, or by its title and space key.
Parameters|Type|Description
-|-|-
`convert_to_markdown`|`boolean` *optional*|Whether to convert page to markdown (true) or keep it in raw HTML format (false). Raw HTML can reveal macros (like dates) not visible in markdown, but CAUTION: using HTML significantly increases token usage in AI responses.
`include_metadata`|`boolean` *optional*|Whether to include page metadata such as creation date, last update, version, and labels.
`page_id`|`string` *optional*|Confluence page ID (numeric ID, can be found in the page URL). For example, in the URL 'https://example.atlassian.net/wiki/spaces/TEAM/pages/123456789/Page+Title', the page ID is '123456789'. Provide this OR both 'title' and 'space_key'. If page_id is provided, title and space_key will be ignored.
`space_key`|`string` *optional*|The key of the Confluence space where the page resides (e.g., 'DEV', 'TEAM'). Required if using 'title'.
`title`|`string` *optional*|The exact title of the Confluence page. Use this with 'space_key' if 'page_id' is not known.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_page_children`**
Get child pages and folders of a specific Confluence page.
Parameters|Type|Description
-|-|-
`parent_id`|`string`|The ID of the parent page whose children you want to retrieve
`convert_to_markdown`|`boolean` *optional*|Whether to convert page content to markdown (true) or keep it in raw HTML format (false). Only relevant if include_content is true.
`expand`|`string` *optional*|Fields to expand in the response (e.g., 'version', 'body.storage')
`include_content`|`boolean` *optional*|Whether to include the page content in the response
`include_folders`|`boolean` *optional*|Whether to include child folders in addition to child pages
`limit`|`integer` *optional*|Maximum number of child items to return (1-50)
`start`|`integer` *optional*|Starting index for pagination (0-based)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_page_diff`**
Get a unified diff between two versions of a Confluence page.
Parameters|Type|Description
-|-|-
`from_version`|`integer`|Source version number
`page_id`|`string`|Confluence page ID (numeric ID, can be found in the page URL). For example, in 'https://example.atlassian.net/wiki/spaces/TEAM/pages/123456789/Page+Title', the page ID is '123456789'.
`to_version`|`integer`|Target version number

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_page_history`**
Get a historical version of a specific Confluence page.
Parameters|Type|Description
-|-|-
`page_id`|`string`|Confluence page ID (numeric ID, can be found in the page URL). For example, in 'https://example.atlassian.net/wiki/spaces/TEAM/pages/123456789/Page+Title', the page ID is '123456789'.
`version`|`integer`|The version number of the page to retrieve
`convert_to_markdown`|`boolean` *optional*|Whether to convert page to markdown (true) or keep it in raw HTML format (false). Raw HTML can reveal macros (like dates) not visible in markdown, but CAUTION: using HTML significantly increases token usage in AI responses.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_page_images`**
Get all images attached to a Confluence page as inline image content.

Filters attachments to images only (PNG, JPEG, GIF, WebP, SVG, BMP)
and returns them as base64-encoded ImageContent that clients can
render directly. Non-image attachments are excluded.

Files with ambiguous MIME types (application/octet-stream) are
detected by filename extension as a fallback. Images larger than
50 MB are skipped with an error entry in the summary.
Parameters|Type|Description
-|-|-
`content_id`|`string`|The ID of the Confluence page or blog post to retrieve images from. Example: '123456789'

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_page_views`**
Get view statistics for a Confluence page.

Note: This tool is only available for Confluence Cloud. Server/Data Center
instances do not support the Analytics API.
Parameters|Type|Description
-|-|-
`page_id`|`string`|Confluence page ID (numeric ID, can be found in the page URL). For example, in 'https://example.atlassian.net/wiki/spaces/TEAM/pages/123456789/Page+Title', the page ID is '123456789'.
`include_title`|`boolean` *optional*|Whether to fetch and include the page title

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_get_space_page_tree`**
Get page hierarchy for a Confluence space as a flat list.

Returns pages with parent_id and depth attributes for token-efficient
processing. Filter by depth to focus on relevant sections, or find
pages by title. Much more efficient than rendering full ASCII trees.

Use this to understand space organization before creating/moving pages.
Parameters|Type|Description
-|-|-
`space_key`|`string`|Space key
`limit`|`integer` *optional*|Max pages to fetch

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_move_page`**
Move a Confluence page to a new parent or space.
Parameters|Type|Description
-|-|-
`page_id`|`string`|ID of the page to move
`position`|`string` *optional*|Position: 'append' (default, move as child of target), 'above' (move before target as sibling), or 'below' (move after target as sibling)
`target_parent_id`|`string` *optional*|Target parent page ID. If omitted with target_space_key, moves to space root.
`target_space_key`|`string` *optional*|Target space key for cross-space moves

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_reply_to_comment`**
Reply to an existing comment thread on a Confluence page.
Parameters|Type|Description
-|-|-
`body`|`string`|The reply content in Markdown format
`comment_id`|`string`|The ID of the parent comment to reply to

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_search`**
Search Confluence content using simple terms or CQL.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query - can be either a simple text (e.g. 'project documentation') or a CQL query string. Simple queries use 'siteSearch' by default, to mimic the WebUI search, with an automatic fallback to 'text' search if not supported. Examples of CQL:
- Basic search: 'type=page AND space=DEV'
- Personal space search: 'space="~username"' (note: personal space keys starting with ~ must be quoted)
- Search by title: 'title~"Meeting Notes"'
- Use siteSearch: 'siteSearch ~ "important concept"'
- Use text search: 'text ~ "important concept"'
- Recent content: 'created >= "2023-01-01"'
- Content with specific label: 'label=documentation'
- Recently modified content: 'lastModified > startOfMonth("-1M")'
- Content modified this year: 'creator = currentUser() AND lastModified > startOfYear()'
- Content you contributed to recently: 'contributor = currentUser() AND lastModified > startOfWeek()'
- Content watched by user: 'watcher = "user@domain.com" AND type = page'
- Exact phrase in content: 'text ~ "\"Urgent Review Required\"" AND label = "pending-approval"'
- Title wildcards: 'title ~ "Minutes*" AND (space = "HR" OR space = "Marketing")'
Note: Special identifiers need proper quoting in CQL: personal space keys (e.g., "~username"), reserved words, numeric IDs, and identifiers with special characters.
`limit`|`integer` *optional*|Maximum number of results (1-50)
`spaces_filter`|`string` *optional*|(Optional) Comma-separated list of space keys to filter results by. Overrides the environment variable CONFLUENCE_SPACES_FILTER if provided. Use empty string to disable filtering.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_search_user`**
Search Confluence users using CQL (Cloud) or group member API (Server/DC).
Parameters|Type|Description
-|-|-
`query`|`string`|Search query - a CQL query string for user search. Examples of CQL:
- Basic user lookup by full name: 'user.fullname ~ "First Last"'
Note: Special identifiers need proper quoting in CQL: personal space keys (e.g., "~username"), reserved words, numeric IDs, and identifiers with special characters.
`group_name`|`string` *optional*|Group to search within on Server/DC instances (default: 'confluence-users'). Ignored on Cloud.
`limit`|`integer` *optional*|Maximum number of results (1-50)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`confluence_update_page`**
Update an existing Confluence page.
Parameters|Type|Description
-|-|-
`content`|`string`|The new content of the page. Format depends on content_format parameter
`page_id`|`string`|The ID of the page to update
`title`|`string`|The new title of the page
`content_format`|`string` *optional*|(Optional) The format of the content parameter. Options: 'markdown' (default), 'wiki', 'storage', or 'xhtml'. Use 'xhtml' when providing Confluence XHTML storage format (same as 'storage'). Wiki format uses Confluence wiki markup syntax
`emoji`|`string` *optional*|(Optional) Page title emoji (icon shown in navigation). Can be any emoji character like '📝', '🚀', '📚'. Set to null/None to remove.
`enable_heading_anchors`|`boolean` *optional*|(Optional) Whether to enable automatic heading anchor generation. Only applies when content_format is 'markdown'
`include_content`|`boolean` *optional*|(Optional) Whether to include page content in the response. Defaults to false since callers already have the content at update time
`is_minor_edit`|`boolean` *optional*|Whether this is a minor edit
`parent_id`|`string` *optional*|Optional the new parent page ID
`version_comment`|`string` *optional*|Optional comment for this version

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_update_page_section`**
Update a single section of a Confluence page without affecting the rest.

Replaces only the content beneath a named heading, leaving all other
sections, macros, layouts, and Confluence-specific elements completely
intact. This avoids the data loss that occurs when a full page is
downloaded as Markdown, edited, and re-uploaded.
Parameters|Type|Description
-|-|-
`heading_text`|`string`|Exact text of the heading that starts the section to replace. Matching is case-sensitive. Use confluence_get_page with convert_to_markdown=false to inspect exact heading text when unsure.
`new_content`|`string`|Replacement content for the section body. Do NOT include the heading itself — only the body beneath it. Format is controlled by content_format.
`page_id`|`string`|The ID of the page to update
`content_format`|`string` *optional*|(Optional) Format of new_content. Options: 'markdown' (default) or 'storage' (raw Confluence storage XML). Use 'storage' to insert macros or elements that markdown cannot express.
`is_minor_edit`|`boolean` *optional*|Whether this is a minor edit
`version_comment`|`string` *optional*|Optional comment for this version

*This tool may perform destructive updates.*

---
#### Tool: **`confluence_upload_attachment`**
Upload an attachment to Confluence content (page or blog post).

If the attachment already exists (same filename), a new version is created.
This is useful for:
- Attaching documents, images, or files to a page
- Updating existing attachments with new versions
- Adding supporting materials to documentation
Parameters|Type|Description
-|-|-
`content_id`|`string`|The ID of the Confluence content (page or blog post) to attach the file to. Page IDs can be found in the page URL or by using the search/get_page tools. Example: '123456789'
`file_path

[...]
