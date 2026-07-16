A comprehensive MCP server for Metabase with 70+ tools.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/metabase](https://hub.docker.com/repository/docker/mcp/metabase)
**Author**|[easecloudio](https://github.com/easecloudio)
**Repository**|https://github.com/easecloudio/mcp-metabase-server

## Available Tools (28)
Tools provided by this Server|Short Description
-|-
`add_card_to_dashboard`|Add a card to a dashboard with positioning|
`create_card`|Create a new Metabase question (card)|
`create_collection`|Create a new Metabase collection|
`create_dashboard`|Create a new Metabase dashboard|
`create_database_connection`|Create a new database connection|
`create_permission_group`|Create a new permission group|
`create_user`|Create a new Metabase user|
`delete_card`|Delete a Metabase question (card)|
`delete_dashboard`|Delete a Metabase dashboard|
`execute_card`|Execute a Metabase question/card and get results|
`execute_query`|Execute a SQL query against a Metabase database|
`get_dashboard_cards`|Get all cards in a dashboard|
`get_database_schema`|Get the schema information for a database|
`get_database_sync_status`|Get database schema sync status|
`get_database_tables`|Get all tables in a database|
`list_cards`|List all questions/cards in Metabase|
`list_collections`|List all collections in Metabase|
`list_dashboards`|List all dashboards in Metabase|
`list_databases`|List all databases in Metabase|
`list_permission_groups`|List all permission groups|
`list_users`|List all users in Metabase|
`remove_card_from_dashboard`|Remove a card from a dashboard|
`search_content`|Search across all Metabase content|
`sync_database_schema`|Sync database schema metadata|
`test_database_connection`|Test a database connection|
`update_card`|Update an existing Metabase question (card)|
`update_dashboard`|Update an existing Metabase dashboard|
`update_dashboard_card`|Update card position, size, and settings on a dashboard|

---
## Tools Details

#### Tool: **`add_card_to_dashboard`**
Add a card to a dashboard with positioning
Parameters|Type|Description
-|-|-
`card_id`|`number`|ID of the card to add
`dashboard_id`|`number`|ID of the dashboard
`col`|`number` *optional*|Column position (0-based)
`parameter_mappings`|`array` *optional*|Parameter mappings between dashboard and card
`row`|`number` *optional*|Row position (0-based)
`size_x`|`number` *optional*|Width in grid units
`size_y`|`number` *optional*|Height in grid units
`visualization_settings`|`object` *optional*|Visualization settings for the card on this dashboard

---
#### Tool: **`create_card`**
Create a new Metabase question (card)
Parameters|Type|Description
-|-|-
`dataset_query`|`object`|The query for the card (e.g., MBQL or native query)
`display`|`string`|Display type (e.g., 'table', 'line', 'bar')
`name`|`string`|Name of the card
`visualization_settings`|`object`|Settings for the visualization
`collection_id`|`number` *optional*|Optional ID of the collection to save the card in
`description`|`string` *optional*|Optional description for the card

---
#### Tool: **`create_collection`**
Create a new Metabase collection
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the collection
`color`|`string` *optional*|Color of the collection
`description`|`string` *optional*|Description of the collection
`parent_id`|`number` *optional*|Parent collection ID (null for root level)

---
#### Tool: **`create_dashboard`**
Create a new Metabase dashboard
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the dashboard
`collection_id`|`number` *optional*|Optional ID of the collection to save the dashboard in
`description`|`string` *optional*|Optional description for the dashboard
`parameters`|`array` *optional*|Optional parameters for the dashboard

---
#### Tool: **`create_database_connection`**
Create a new database connection
Parameters|Type|Description
-|-|-
`details`|`object`|Connection details (host, port, dbname, user, etc.)
`engine`|`string`|Database engine (e.g., 'postgres', 'mysql', 'h2')
`name`|`string`|Name of the database connection
`auto_run_queries`|`boolean` *optional*|Whether to auto-run queries
`is_full_sync`|`boolean` *optional*|Whether to perform full schema sync

---
#### Tool: **`create_permission_group`**
Create a new permission group
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the permission group

---
#### Tool: **`create_user`**
Create a new Metabase user
Parameters|Type|Description
-|-|-
`email`|`string`|User's email address
`first_name`|`string`|User's first name
`last_name`|`string`|User's last name
`group_ids`|`array` *optional*|Array of group IDs to assign user to
`password`|`string` *optional*|User's password

---
#### Tool: **`delete_card`**
Delete a Metabase question (card)
Parameters|Type|Description
-|-|-
`card_id`|`number`|ID of the card to delete
`hard_delete`|`boolean` *optional*|Set to true for hard delete, false (default) for archive

---
#### Tool: **`delete_dashboard`**
Delete a Metabase dashboard
Parameters|Type|Description
-|-|-
`dashboard_id`|`number`|ID of the dashboard to delete
`hard_delete`|`boolean` *optional*|Set to true for hard delete, false (default) for archive

---
#### Tool: **`execute_card`**
Execute a Metabase question/card and get results
Parameters|Type|Description
-|-|-
`card_id`|`number`|ID of the card/question to execute
`parameters`|`object` *optional*|Optional parameters for the query

---
#### Tool: **`execute_query`**
Execute a SQL query against a Metabase database
Parameters|Type|Description
-|-|-
`database_id`|`number`|ID of the database to query
`query`|`string`|SQL query to execute
`native_parameters`|`array` *optional*|Optional parameters for the query

---
#### Tool: **`get_dashboard_cards`**
Get all cards in a dashboard
Parameters|Type|Description
-|-|-
`dashboard_id`|`number`|ID of the dashboard

---
#### Tool: **`get_database_schema`**
Get the schema information for a database
Parameters|Type|Description
-|-|-
`database_id`|`number`|ID of the database

---
#### Tool: **`get_database_sync_status`**
Get database schema sync status
Parameters|Type|Description
-|-|-
`database_id`|`number`|ID of the database

---
#### Tool: **`get_database_tables`**
Get all tables in a database
Parameters|Type|Description
-|-|-
`database_id`|`number`|ID of the database

---
#### Tool: **`list_cards`**
List all questions/cards in Metabase
#### Tool: **`list_collections`**
List all collections in Metabase
Parameters|Type|Description
-|-|-
`archived`|`boolean` *optional*|Include archived collections

---
#### Tool: **`list_dashboards`**
List all dashboards in Metabase
#### Tool: **`list_databases`**
List all databases in Metabase
#### Tool: **`list_permission_groups`**
List all permission groups
#### Tool: **`list_users`**
List all users in Metabase
Parameters|Type|Description
-|-|-
`include_deactivated`|`boolean` *optional*|Include deactivated users

---
#### Tool: **`remove_card_from_dashboard`**
Remove a card from a dashboard
Parameters|Type|Description
-|-|-
`dashboard_id`|`number`|ID of the dashboard
`dashcard_id`|`number`|ID of the dashboard card (not the card itself)

---
#### Tool: **`search_content`**
Search across all Metabase content
Parameters|Type|Description
-|-|-
`query`|`string`|Search query
`models`|`array` *optional*|Filter by content types

---
#### Tool: **`sync_database_schema`**
Sync database schema metadata
Parameters|Type|Description
-|-|-
`database_id`|`number`|ID of the database to sync

---
#### Tool: **`test_database_connection`**
Test a database connection
Parameters|Type|Description
-|-|-
`connection_details`|`object` *optional*|Connection details to test (optional)
`database_id`|`number` *optional*|ID of the database to test

---
#### Tool: **`update_card`**
Update an existing Metabase question (card)
Parameters|Type|Description
-|-|-
`card_id`|`number`|ID of the card to update
`archived`|`boolean` *optional*|Set to true to archive the card
`collection_id`|`number` *optional*|New collection ID
`dataset_query`|`object` *optional*|New query for the card
`description`|`string` *optional*|New description
`display`|`string` *optional*|New display type
`name`|`string` *optional*|New name for the card
`visualization_settings`|`object` *optional*|New visualization settings

---
#### Tool: **`update_dashboard`**
Update an existing Metabase dashboard
Parameters|Type|Description
-|-|-
`dashboard_id`|`number`|ID of the dashboard to update
`archived`|`boolean` *optional*|Set to true to archive the dashboard
`collection_id`|`number` *optional*|New collection ID
`description`|`string` *optional*|New description for the dashboard
`name`|`string` *optional*|New name for the dashboard
`parameters`|`array` *optional*|New parameters for the dashboard

---
#### Tool: **`update_dashboard_card`**
Update card position, size, and settings on a dashboard
Parameters|Type|Description
-|-|-
`dashboard_id`|`number`|ID of the dashboard
`dashcard_id`|`number`|ID of the dashboard card
`col`|`number` *optional*|New column position
`parameter_mappings`|`array` *optional*|Updated parameter mappings
`row`|`number` *optional*|New row position
`size_x`|`number` *optional*|New width in grid units
`size_y`|`number` *optional*|New height in grid units
`visualization_settings`|`object` *optional*|Updated visualization settings

---
