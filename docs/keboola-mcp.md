Keboola MCP Server is an open-source bridge between your Keboola project and modern AI tools.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/keboola-mcp](https://hub.docker.com/repository/docker/mcp/keboola-mcp)
**Author**|[keboola](https://github.com/keboola)
**Repository**|https://github.com/keboola/mcp-server

## Available Tools (33)
Tools provided by this Server|Short Description
-|-
`add_config_row`|Creates a component configuration row in the specified configuration_id, using the specified name, component ID, configuration JSON, and description.|
`create_config`|Creates a root component configuration using the specified name, component ID, configuration JSON, and description.|
`create_flow`|Creates a new flow configuration in Keboola.|
`create_oauth_url`|Generates an OAuth authorization URL for a Keboola component configuration.|
`create_sql_transformation`|Creates an SQL transformation using the specified name, SQL query following the current SQL dialect, a detailed description, and a list of created table names.|
`docs_query`|Answers a question using the Keboola documentation as a source.|
`find_component_id`|Returns list of component IDs that match the given query.|
`get_bucket`|Gets detailed information about a specific bucket.|
`get_component`|Gets information about a specific component given its ID.|
`get_config`|Gets information about a specific component/transformation configuration.|
`get_config_examples`|Retrieves sample configuration examples for a specific component.|
`get_flow`|Gets detailed information about a specific flow configuration.|
`get_flow_schema`|Returns the JSON schema that defines the structure of Flow configurations.|
`get_job`|Retrieves detailed information about a specific job, identified by the job_id, including its status, parameters, results, and any relevant metadata.|
`get_project_info`|Return structured project information pulled from multiple endpoints.|
`get_sql_dialect`|Gets the name of the SQL dialect used by Keboola project's underlying database.|
`get_table`|Gets detailed information about a specific table including its DB identifier and column information.|
`list_buckets`|Retrieves information about all buckets in the project.|
`list_configs`|Retrieves configurations of components present in the project, optionally filtered by component types or specific component IDs.|
`list_flows`|Retrieves flow configurations from the project.|
`list_jobs`|Retrieves all jobs in the project, or filter jobs by a specific component_id or config_id, with optional status filtering.|
`list_tables`|Retrieves all tables in a specific bucket with their basic information.|
`list_transformations`|Retrieves transformation configurations in the project, optionally filtered by specific transformation IDs.|
`query_data`|Executes an SQL SELECT query to get the data from the underlying database.|
`run_job`|Starts a new job for a given component or transformation.|
`search`|Searches for Keboola items in the production branch of the current project whose names match the given prefixes, potentially narrowed down by item type, limited and paginated.|
`update_bucket_description`|Updates the description for a given Keboola bucket.|
`update_column_description`|Updates the description for a given column in a Keboola table.|
`update_config`|Updates a specific root component configuration using given by component ID, and configuration ID.|
`update_config_row`|Updates a specific component configuration row in the specified configuration_id, using the specified name, component ID, configuration JSON, and description.|
`update_flow`|Updates an existing flow configuration in Keboola.|
`update_sql_transformation`|Updates an existing SQL transformation configuration, optionally updating the description and disabling the configuration.|
`update_table_description`|Updates the description for a given Keboola table.|

---
## Tools Details

#### Tool: **`add_config_row`**
Creates a component configuration row in the specified configuration_id, using the specified name,
component ID, configuration JSON, and description.

CONSIDERATIONS:
- The configuration JSON object must follow the row_configuration_schema of the specified component.
- Make sure the configuration parameters always adhere to the row_configuration_schema,
  which is available via the component_detail tool.
- The configuration JSON object should adhere to the component's configuration examples if found.

USAGE:
- Use when you want to create a new row configuration for a specific component configuration.

EXAMPLES:
- user_input: `Create a new configuration row for component X with these settings`
    - set the component_id, configuration_id and configuration parameters accordingly
    - returns the created component configuration if successful.
Parameters|Type|Description
-|-|-
`component_id`|`string`|The ID of the component for which to create the configuration.
`configuration_id`|`string`|The ID of the configuration for which to create the configuration row.
`description`|`string`|The detailed description of the component configuration explaining its purpose and functionality.
`name`|`string`|A short, descriptive name summarizing the purpose of the component configuration.
`parameters`|`object`|The component row configuration parameters, adhering to the row_configuration_schema
`storage`|`object` *optional*|The table and/or file input / output mapping of the component configuration. It is present only for components that have tables or file input mapping defined

---
#### Tool: **`create_config`**
Creates a root component configuration using the specified name, component ID, configuration JSON, and description.

CONSIDERATIONS:
- The configuration JSON object must follow the root_configuration_schema of the specified component.
- Make sure the configuration parameters always adhere to the root_configuration_schema,
  which is available via the component_detail tool.
- The configuration JSON object should adhere to the component's configuration examples if found.

USAGE:
- Use when you want to create a new root configuration for a specific component.

EXAMPLES:
- user_input: `Create a new configuration for component X with these settings`
    - set the component_id and configuration parameters accordingly
    - returns the created component configuration if successful.
Parameters|Type|Description
-|-|-
`component_id`|`string`|The ID of the component for which to create the configuration.
`description`|`string`|The detailed description of the component configuration explaining its purpose and functionality.
`name`|`string`|A short, descriptive name summarizing the purpose of the component configuration.
`parameters`|`object`|The component configuration parameters, adhering to the root_configuration_schema
`storage`|`object` *optional*|The table and/or file input / output mapping of the component configuration. It is present only for components that have tables or file input mapping defined

---
#### Tool: **`create_flow`**
Creates a new flow configuration in Keboola.
A flow is a special type of Keboola component that orchestrates the execution of other components. It defines
how tasks are grouped and ordered — enabling control over parallelization** and sequential execution.
Each flow is composed of:
- Tasks: individual component configurations (e.g., extractors, writers, transformations).
- Phases: groups of tasks that run in parallel. Phases themselves run in order, based on dependencies.

CONSIDERATIONS:
- The `phases` and `tasks` parameters must conform to the Keboola Flow JSON schema.
- Each task and phase must include at least: `id` and `name`.
- Each task must reference an existing component configuration in the project.
- Items in the `dependsOn` phase field reference ids of other phases.
- Links contained in the response should ALWAYS be presented to the user

USAGE:
Use this tool to automate multi-step data workflows. This is ideal for:
- Creating ETL/ELT orchestration.
- Coordinating dependencies between components.
- Structuring parallel and sequential task execution.

EXAMPLES:
- user_input: Orchestrate all my JIRA extractors.
    - fill `tasks` parameter with the tasks for the JIRA extractors
    - determine dependencies between the JIRA extractors
    - fill `phases` parameter by grouping tasks into phases
Parameters|Type|Description
-|-|-
`description`|`string`|Detailed description of the flow purpose.
`name`|`string`|A short, descriptive name for the flow.
`phases`|`array`|List of phase definitions.
`tasks`|`array`|List of task definitions.

---
#### Tool: **`create_oauth_url`**
Generates an OAuth authorization URL for a Keboola component configuration.

When using this tool, be very concise in your response. Just guide the user to click the
authorization link.

Note that this tool should be called specifically for the OAuth-requiring components after their
configuration is created e.g. keboola.ex-google-analytics-v4 and keboola.ex-gmail.
Parameters|Type|Description
-|-|-
`component_id`|`string`|The component ID to grant access to (e.g., "keboola.ex-google-analytics-v4").
`config_id`|`string`|The configuration ID for the component.

---
#### Tool: **`create_sql_transformation`**
Creates an SQL transformation using the specified name, SQL query following the current SQL dialect, a detailed
description, and a list of created table names.

CONSIDERATIONS:
- By default, SQL transformation must create at least one table to produce a result; omit only if the user
  explicitly indicates that no table creation is needed.
- Each SQL code block must include descriptive name that reflects its purpose and group one or more executable
  semantically related SQL statements.
- Each SQL query statement within a code block must be executable and follow the current SQL dialect, which can be
  retrieved using appropriate tool.
- When referring to the input tables within the SQL query, use fully qualified table names, which can be
  retrieved using appropriate tools.
- When creating a new table within the SQL query (e.g. CREATE TABLE ...), use only the quoted table name without
  fully qualified table name, and add the plain table name without quotes to the `created_table_names` list.
- Unless otherwise specified by user, transformation name and description are generated based on the SQL query
  and user intent.

USAGE:
- Use when you want to create a new SQL transformation.

EXAMPLES:
- user_input: `Can you create a new transformation out of this sql query?`
    - set the sql_code_blocks to the query, and set other parameters accordingly.
    - returns the created SQL transformation configuration if successful.
- user_input: `Generate me an SQL transformation which [USER INTENT]`
    - set the sql_code_blocks to the query based on the [USER INTENT], and set other parameters accordingly.
    - returns the created SQL transformation configuration if successful.
Parameters|Type|Description
-|-|-
`description`|`string`|The detailed description of the SQL transformation capturing the user intent, explaining the SQL query, and the expected output.
`name`|`string`|A short, descriptive name summarizing the purpose of the SQL transformation.
`sql_code_blocks`|`array`|The SQL query code blocks, each containing a descriptive name and a sequence of semantically related independently executable sql_statements written in the current SQL dialect.
`created_table_names`|`array` *optional*|A list of created table names if they are generated within the SQL query statements (e.g., using `CREATE TABLE ...`).

---
#### Tool: **`docs_query`**
Answers a question using the Keboola documentation as a source.
Parameters|Type|Description
-|-|-
`query`|`string`|Natural language query to search for in the documentation.

---
#### Tool: **`find_component_id`**
Returns list of component IDs that match the given query.

USAGE:
- Use when you want to find the component for a specific purpose.

EXAMPLES:
- user_input: `I am looking for a salesforce extractor component`
    - returns a list of component IDs that match the query, ordered by relevance/best match.
Parameters|Type|Description
-|-|-
`query`|`string`|Natural language query to find the requested component.

---
#### Tool: **`get_bucket`**
Gets detailed information about a specific bucket.
Parameters|Type|Description
-|-|-
`bucket_id`|`string`|Unique ID of the bucket.

---
#### Tool: **`get_component`**
Gets information about a specific component given its ID.

USAGE:
- Use when you want to see the details of a specific component to get its documentation, configuration schemas,
  etc. Especially in situation when the users asks to create or update a component configuration.
  This tool is mainly for internal use by the agent.

EXAMPLES:
- user_input: `Create a generic extractor configuration for x`
    - Set the component_id if you know it or find the component_id by find_component_id
      or docs use tool and set it
    - returns the component
Parameters|Type|Description
-|-|-
`component_id`|`string`|ID of the component/transformation

---
#### Tool: **`get_config`**
Gets information about a specific component/transformation configuration.

USAGE:
- Use when you want to see the configuration of a specific component/transformation.

EXAMPLES:
- user_input: `give me details about this configuration`
    - set component_id and configuration_id to the specific component/transformation ID and configuration ID
      if you know it
    - returns the component/transformation configuration pair
Parameters|Type|Description
-|-|-
`component_id`|`string`|ID of the component/transformation
`configuration_id`|`string`|ID of the component/transformation configuration

---
#### Tool: **`get_config_examples`**
Retrieves sample configuration examples for a specific component.

USAGE:
- Use when you want to see example configurations for a specific component.

EXAMPLES:
- user_input: `Show me example configurations for component X`
    - set the component_id parameter accordingly
    - returns a markdown formatted string with configuration examples
Parameters|Type|Description
-|-|-
`component_id`|`string`|The ID of the component to get configuration examples for.

---
#### Tool: **`get_flow`**
Gets detailed information about a specific flow configuration.
Parameters|Type|Description
-|-|-
`configuration_id`|`string`|ID of the flow configuration to retrieve.

---
#### Tool: **`get_flow_schema`**
Returns the JSON schema that defines the structure of Flow configurations.
#### Tool: **`get_job`**
Retrieves detailed information about a specific job, identified by the job_id, including its status, parameters,
results, and any relevant metadata.

EXAMPLES:
- If job_id = "123", then the details of the job with id "123" will be retrieved.
Parameters|Type|Description
-|-|-
`job_id`|`string`|The unique identifier of the job whose details should be retrieved.

---
#### Tool: **`get_project_info`**
Return structured project information pulled from multiple endpoints.
#### Tool: **`get_sql_dialect`**
Gets the name of the SQL dialect used by Keboola project's underlying database.
#### Tool: **`get_table`**
Gets detailed information about a specific table including its DB identifier and column information.
Parameters|Type|Description
-|-|-
`table_id`|`string`|Unique ID of the table.

---
#### Tool: **`list_buckets`**
Retrieves information about all buckets in the project.
#### Tool: **`list_configs`**
Retrieves configurations of components present in the project,
optionally filtered by component types or specific component IDs.
If component_ids are supplied, only those components identified by the IDs are retrieved, disregarding
component_types.

USAGE:
- Use when you want to see components configurations in the project for given component_types.
- Use when you want to see components configurations in the project for given component_ids.

EXAMPLES:
- user_input: `give me all components (in the project)`
    - returns all components configurations in the project
- user_input: `list me all extractor components (in the project)`
    - set types to ["extractor"]
    - returns all extractor components configurations in the project
- user_input: `give me configurations for following component/s` | `give me configurations for this component`
    - set component_ids to list of identifiers accordingly if you know them
    - returns all configurations for the given components in the project
- user_input: `give me configurations for 'specified-id'`
    - set component_ids to ['specified-id']
    - returns the configurations of the component with ID 'specified-id'
Parameters|Type|Description
-|-|-
`component_ids`|`array` *optional*|List of component IDs to retrieve configurations for. If none, return all components.
`component_types`|`array` *optional*|List of component types to filter by. If none, return all components.

---
#### Tool: **`list_flows`**
Retrieves flow configurations from the project.
Parameters|Type|Description
-|-|-
`flow_ids`|`array` *optional*|The configuration IDs of the flows to retrieve.

---
#### Tool: **`list_jobs`**
Retrieves all jobs in the project, or filter jobs by a specific component_id or config_id, with optional status
filtering. Additional parameters support pagination (limit, offset) and sorting (sort_by, sort_order).

USAGE:
- Use when you want to list jobs for a given component_id and optionally for given config_id.
- Use when you want to list all jobs in the project or filter them by status.

EXAMPLES:
- If status = "error", only jobs with status "error" will be listed.
- If status = None, then all jobs with arbitrary status will be listed.
- If component_id = "123" and config_id = "456", then the jobs for the component with id "123" and configuration
  with id "456" will be listed.
- If limit = 100 and offset = 0, the first 100 jobs will be listed.
- If limit = 100 and offset = 100, the second 100 jobs will be listed.
- If sort_by = "endTime" and sort_order = "asc", the jobs will be sorted by the end time in ascending order.
Parameters|Type|Description
-|-|-
`component_id`|`string` *optional*|The optional ID of the component whose jobs you want to list, default = None.
`config_id`|`string` *optional*|The optional ID of the component configuration whose jobs you want to list, default = None.
`limit`|`integer` *optional*|The number of jobs to list, default = 100, max = 500.
`offset`|`integer` *optional*|The offset of the jobs to list, default = 0.
`sort_by`|`string` *optional*|The field to sort the jobs by, default = "startTime".
`sort_order`|`string` *optional*|The order to sort the jobs by, default = "desc".
`status`|`string` *optional*|The optional status of the jobs to filter by, if None then default all.

---
#### Tool: **`list_tables`**
Retrieves all tables in a specific bucket with their basic information.
Parameters|Type|Description
-|-|-
`bucket_id`|`string`|Unique ID of the bucket.

---
#### Tool: **`list_transformations`**
Retrieves transformation configurations in the project, optionally filtered by specific transformation IDs.

USAGE:
- Use when you want to see transformation configurations in the project for given transformation_ids.
- Use when you want to retrieve all transformation configurations, then set transformation_ids to an empty list.

EXAMPLES:
- user_input: `give me all transformations`
    - returns all transformation configurations in the project
- user_input: `give me configurations for following transformation/s` | `give me configurations for
  this transformation`
- set transformation_ids to list of identifiers accordingly if you know the IDs
    - returns all transformation configurations for the given transformations IDs
- user_input: `list me transformations for this transformation component 'specified-id'`
    - set transformation_ids to ['specified-id']
    - returns the transformation configurations with ID 'specified-id'
Parameters|Type|Description
-|-|-
`transformation_ids`|`array` *optional*|List of transformation component IDs to retrieve configurations for.

---
#### Tool: **`query_data`**
Executes an SQL SELECT query to get the data from the underlying database.
* When constructing the SQL SELECT query make sure to check the SQL dialect
  used by the Keboola project's underlying database.
* When referring to tables always use fully qualified table names that include the database name,
  schema name and the table name.
* The fully qualified table name can be found in the table information, use a tool to get the information
  about tables. The fully qualified table name can be found in the response from that tool.
* Always use quoted column names when referring to table columns. The quoted column names can also be found
  in the response from the table information tool.
Parameters|Type|Description
-|-|-
`query_name`|`string`|A concise, human-readable name for this query based on its purpose and what data it retrieves. Use normal words with spaces (e.g., "Customer Orders Last Month", "Top Selling Products", "User Activity Summary").
`sql_query`|`string`|SQL SELECT query to run.

---
#### Tool: **`run_job`**
Starts a new job for a given component or transformation.
Parameters|Type|Description
-|-|-
`component_id`|`string`|The ID of the component or transformation for which to start a job.
`configuration_id`|`string`|The ID of the configuration for which to start a job.

---
#### Tool: **`search`**
Searches for Keboola items in the production branch of the current project whose names match the given prefixes,
potentially narrowed down by item type, limited and paginated. Results are ordered by relevance, then creation time.

Considerations:
- The search is purely name-based, and an item is returned when its name or any word in the name starts with any
  of the "name_prefixes" parameter.
Parameters|Type|Description
-|-|-
`name_prefixes`|`array`|Name prefixes to match against item names.
`item_types`|`array` *optional*|Optional list of keboola item types to filter by.
`limit`|`integer` *optional*|Maximum number of items to return (default: 50, max: 100).
`offset`|`integer` *optional*|Number of matching items to skip, pagination.

---
#### Tool: **`update_bucket_description`**
Updates the description for a given Keboola bucket.
Parameters|Type|Description
-|-|-
`bucket_id`|`string`|The ID of the bucket to update.
`description`|`string`|The new description for the bucket.

---
#### Tool: **`update_column_description`**
Updates the description for a given column in a Keboola table.
Parameters|Type|Description
-|-|-
`column_name`|`string`|The name of the column to update.
`description`|`string`|The new description for the column.
`table_id`|`string`|The ID of the table that contains the column.

---
#### Tool: **`update_config`**
Updates a specific root component configuration using given by component ID, and configuration ID.

CONSIDERATIONS:
- The configuration JSON object must follow the root_configuration_schema of the specified component.
- Make sure the configuration parameters always adhere to the root_configuration_schema,
  which is available via the component_detail tool.
- The configuration JSON object should adhere to the component's configuration examples if found

USAGE:
- Use when you want to update a root configuration of a specific component.

EXAMPLES:
- user_input: `Update a configuration for component X and configuration ID 1234 with these settings`
    - set the component_id, configuration_id and configuration parameters accordingly.
    - set the change_description to the description of the change made to the component configuration.
    - returns the updated component configuration if successful.
Parameters|Type|Description
-|-|-
`change_description`|`string`|Description of the change made to the component configuration.
`component_id`|`string`|The ID of the component the configuration belongs to.
`configuration_id`|`string`|The ID of the configuration to update.
`description`|`string`|The detailed description of the component configuration explaining its purpose and functionality.
`name`|`string`|A short, descriptive name summarizing the purpose of the component configuration.
`parameters`|`object`|The component configuration parameters, adhering to the root_configuration_s

[...]
