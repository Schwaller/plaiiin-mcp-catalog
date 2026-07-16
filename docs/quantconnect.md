The QuantConnect MCP Server is a bridge for AIs (such as Claude and OpenAI o3 Pro) to interact with our cloud platform. When equipped with our MCP, the AI can perform tasks on your behalf through our API such as updating projects, writing strategies, backtesting, and deploying strategies to production live-trading.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/quantconnect](https://hub.docker.com/repository/docker/mcp/quantconnect)
**Author**|[QuantConnect](https://github.com/QuantConnect)
**Repository**|https://github.com/QuantConnect/mcp-server

## Available Tools (64)
Tools provided by this Server|Short Description
-|-
`abort_optimization`|Abort optimization|
`authorize_connection`|Authorize external connection|
`broadcast_live_command`|Broadcast live command|
`check_initialization_errors`|Check initialization errors|
`check_syntax`|Check syntax|
`complete_code`|Complete code|
`create_backtest`|Create backtest|
`create_compile`|Create compile|
`create_file`|Create file|
`create_live_algorithm`|Create live algorithm|
`create_live_command`|Create live command|
`create_optimization`|Create optimization|
`create_project`|Create project|
`create_project_collaborator`|Create project collaborator|
`delete_backtest`|Delete backtest|
`delete_file`|Delete file|
`delete_object`|Delete Object Store file|
`delete_optimization`|Delete optimization|
`delete_project`|Delete project|
`delete_project_collaborator`|Delete project collaborator|
`enhance_error_message`|Enhance error message|
`estimate_optimization_time`|Estimate optimization time|
`liquidate_live_algorithm`|Liquidate live algorithm|
`list_backtests`|List backtests|
`list_live_algorithms`|List live algorithms|
`list_object_store_files`|List Object Store files|
`list_optimizations`|List optimizations|
`list_projects`|List projects|
`lock_project_with_collaborators`|Lock project with collaborators|
`patch_file`|Patch file|
`read_account`|Read account|
`read_backtest`|Read backtest|
`read_backtest_chart`|Read backtest chart|
`read_backtest_insights`|Read backtest insights|
`read_backtest_orders`|Read backtest orders|
`read_compile`|Read compile|
`read_file`|Read file|
`read_latest_mcp_server_version`|Read latest QC MCP Server version|
`read_lean_versions`|Read LEAN versions|
`read_live_algorithm`|Read live algorithm|
`read_live_chart`|Read live chart|
`read_live_insights`|Read live insights|
`read_live_logs`|Read live logs|
`read_live_orders`|Read live orders|
`read_live_portfolio`|Read live portfolio|
`read_mcp_server_version`|Read QC MCP Server version|
`read_object_properties`|Read Object Store file properties|
`read_object_store_file_download_url`|Read Object Store file download URL|
`read_object_store_file_job_id`|Read Object Store file job Id|
`read_optimization`|Read optimization|
`read_project`|Read project|
`read_project_collaborators`|Read project collaborators|
`read_project_nodes`|Read project nodes|
`search_quantconnect`|Search QuantConnect|
`stop_live_algorithm`|Stop live algorithm|
`update_backtest`|Update backtest|
`update_code_to_pep8`|Update code to PEP8|
`update_file_contents`|Update file contents|
`update_file_name`|Update file name|
`update_optimization`|Update optimization|
`update_project`|Update project|
`update_project_collaborator`|Update project collaborator|
`update_project_nodes`|Update project nodes|
`upload_object`|Upload Object Store file|

---
## Tools Details

#### Tool: **`abort_optimization`**
Abort an optimization.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`authorize_connection`**
Authorize an external connection with a live brokerage or 
        data provider.

        This tool automatically opens your browser for you to complete
        the authentication flow. For the flow to work, you must be 
        logged into your QuantConnect account on the browser that opens.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`broadcast_live_command`**
Broadcast a live command to all live algorithms in an 
        organization.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`check_initialization_errors`**
Run a backtest for a few seconds to initialize the algorithm 
        and get inialization errors if any.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`check_syntax`**
Check the syntax of a code.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`complete_code`**
Show the code completion for a specific text input.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`create_backtest`**
Create a new backtest request and get the backtest Id.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`create_compile`**
Asynchronously create a compile job request for a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`create_file`**
Add a file to a given project.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`create_live_algorithm`**
Create a live algorithm.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`create_live_command`**
Send a command to a live trading algorithm.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`create_optimization`**
Create an optimization with the specified parameters.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`create_project`**
Create a new project in your default organization.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`create_project_collaborator`**
Add a collaborator to a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`delete_backtest`**
Delete a backtest from a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`delete_file`**
Delete a file in a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`delete_object`**
Delete the Object Store file of a specific organization and 
        key.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`delete_optimization`**
Delete an optimization.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`delete_project`**
Delete a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`delete_project_collaborator`**
Remove a collaborator from a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`enhance_error_message`**
Show additional context and suggestions for error messages.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`estimate_optimization_time`**
Estimate the execution time of an optimization with the 
        specified parameters.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`liquidate_live_algorithm`**
Liquidate and stop a live algorithm.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`list_backtests`**
List all the backtests for the project.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_live_algorithms`**
List all your past and current live trading deployments.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`list_object_store_files`**
List the Object Store files under a specific directory in 
        an organization.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_optimizations`**
List all the optimizations for a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_projects`**
List the details of all projects.
#### Tool: **`lock_project_with_collaborators`**
Lock a project so you can edit it. 

        This is necessary when the project has collaborators or when an 
        LLM is editing files on your behalf via our MCP Server.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`patch_file`**
Apply a patch (unified diff) to a file in a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`read_account`**
Read the organization account status.
#### Tool: **`read_backtest`**
Read the results of a backtest.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_backtest_chart`**
Read a chart from a backtest.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_backtest_insights`**
Read out the insights of a backtest.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_backtest_orders`**
Read out the orders of a backtest.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_compile`**
Read a compile packet job result.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_file`**
Read a file from a project, or all files in the project if 
        no file name is provided.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_latest_mcp_server_version`**
Returns the latest version of the QC MCP Server released.
#### Tool: **`read_lean_versions`**
Returns a list of LEAN versions with basic information for 
        each version.
#### Tool: **`read_live_algorithm`**
Read details of a live algorithm.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`read_live_chart`**
Read a chart from a live algorithm.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`read_live_insights`**
Read out the insights of a live algorithm.

        The snapshot updates about every 10 minutes.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`read_live_logs`**
Get the logs of a live algorithm.

        The snapshot updates about every 5 minutes.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`read_live_orders`**
Read out the orders of a live algorithm.

        The snapshot updates about every 10 minutes.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`read_live_portfolio`**
Read out the portfolio state of a live algorithm.

        The snapshot updates about every 10 minutes.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`read_mcp_server_version`**
Returns the version of the QC MCP Server that's running.
#### Tool: **`read_object_properties`**
Get Object Store properties of a specific organization and 
        key. 

        It doesn't work if the key is a directory in the Object Store.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_object_store_file_download_url`**
Get the URL for downloading files from the Object Store.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_object_store_file_job_id`**
Create a job to download files from the Object Store and 
        then read the job Id.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`read_optimization`**
Read an optimization.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_project`**
List the details of a project or a set of recent projects.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_project_collaborators`**
List all collaborators on a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`read_project_nodes`**
Read the available and selected nodes of a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`search_quantconnect`**
Search for content in QuantConnect.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`stop_live_algorithm`**
Stop a live algorithm.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`update_backtest`**
Update the name or note of a backtest.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`update_code_to_pep8`**
Update Python code to follow PEP8 style.
Parameters|Type|Description
-|-|-
`model`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`update_file_contents`**
Update the contents of a file.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`update_file_name`**
Update the name of a file.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`update_optimization`**
Update the name of an optimization.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`update_project`**
Update a project's name or description.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`update_project_collaborator`**
Update collaborator information in a project.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`update_project_nodes`**
Update the active state of the given nodes to true.

        If you don't provide any nodes, all the nodes become inactive 
        and autoSelectNode is true.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
#### Tool: **`upload_object`**
Upload files to the Object Store.
Parameters|Type|Description
-|-|-
`model`|`string`|

---
