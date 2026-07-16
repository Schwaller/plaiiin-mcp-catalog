Tools to interact with the Camunda 7 Community Edition Engine using the Model Context Protocol (MCP). Whether you're automating workflows, querying process instances, or integrating with external systems, Camunda MCP Server is your agentic solution for seamless interaction with Camunda.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/camunda](https://hub.docker.com/repository/docker/mcp/camunda)
**Author**|[lepoco](https://github.com/lepoco)
**Repository**|https://github.com/lepoco/mcp-camunda

## Available Tools (12)
Tools provided by this Server|Short Description
-|-
`complete_user_task`|Complete a user task in the Camunda process engine.|
`count_incidents`|Count incidents for a specific BPMN process instance in the Camunda process engine.|
`count_instances`|Count active instances for a specific BPMN process definition in the Camunda process engine.|
`count_user_tasks`|Count user tasks for a specific BPMN process instance in the Camunda process engine.|
`count_variables`|Count variables for a specific BPMN process in the Camunda process engine.|
`list_definitions`|Retrieve all BPMN process definitions available in the Camunda BPM process engine.|
`list_incidents`|List incidents for a specific BPMN process instance in the Camunda process engine.|
`list_instances`|Retrieve the list of active instances for a specific BPMN process definition in the Camunda process engine.|
`list_user_tasks`|List user tasks for a specific BPMN process instance in the Camunda process engine.|
`list_variables`|Retrieve the list of variables for a specific BPMN process in the Camunda process engine.|
`resolve_incident`|Requests the Cmaunda BPM process engine to resolve an incident.|
`send_message`|Send a message to a specific BPMN process instance in the Camunda process engine.|

---
## Tools Details

#### Tool: **`complete_user_task`**
Complete a user task in the Camunda process engine. The task is identified by its unique task id.
Parameters|Type|Description
-|-|-
`taskId`|`string`|The unique task id of the user task to complete.

---
#### Tool: **`count_incidents`**
Count incidents for a specific BPMN process instance in the Camunda process engine. The process is identified by its process instance id or the business key.
Parameters|Type|Description
-|-|-
`processInstanceIdOrBusinessKey`|`string`|The unique process instance id or business key of the BPMN process.

---
#### Tool: **`count_instances`**
Count active instances for a specific BPMN process definition in the Camunda process engine. The process is identified by its key. The response includes information about the number of active instances associated with the process definition.
Parameters|Type|Description
-|-|-
`processKey`|`string`|The unique key of the BPMN process definition.

---
#### Tool: **`count_user_tasks`**
Count user tasks for a specific BPMN process instance in the Camunda process engine. The process is identified by its process instance id or the business key.
Parameters|Type|Description
-|-|-
`processInstanceIdOrBusinessKey`|`string`|The unique process instance id or business key of the BPMN process.

---
#### Tool: **`count_variables`**
Count variables for a specific BPMN process in the Camunda process engine. The process is identified by its process instance id or the business key. The response information about the number of variables associated with the process instance.
Parameters|Type|Description
-|-|-
`processInstanceIdOrBusinessKey`|`string`|The unique process instance if of the BPMN process definition. Business key may belong to multiple processes.

---
#### Tool: **`list_definitions`**
Retrieve all BPMN process definitions available in the Camunda BPM process engine. The response includes details such as tenant, version, deployment ID, and other metadata for each process definition. Allows narrowing down results by providing parts of the process key or name, and limiting the number of results returned.
Parameters|Type|Description
-|-|-
`camundaAddress`|`string`|Optional, the address of the Camunda process engine. If not provided, the default address will be used.
`maxResults`|`string`|Optional, max results to fetch provided as integer.
`processKeyLike`|`string`|Optional, part of the BPMN process definiton unique key.
`processNameLike`|`string`|Optional, part of the BPMN process definition name in human readable form.

---
#### Tool: **`list_incidents`**
List incidents for a specific BPMN process instance in the Camunda process engine. The process is identified by its process instance id or the business key.
Parameters|Type|Description
-|-|-
`maxResults`|`string`|Optional, max results to fetch provided as integer.
`processInstanceIdOrBusinessKey`|`string`|The unique process instance id or business key of the BPMN process.

---
#### Tool: **`list_instances`**
Retrieve the list of active instances for a specific BPMN process definition in the Camunda process engine. The process is identified by its key. The response includes details such as tenant, key, business key, process instance id, and other metadata for each process instance.
Parameters|Type|Description
-|-|-
`maxResults`|`string`|Optional, max results to fetch provided as integer.
`processKey`|`string`|The unique key of the BPMN process definition.

---
#### Tool: **`list_user_tasks`**
List user tasks for a specific BPMN process instance in the Camunda process engine. The process is identified by its process instance id or the business key.
Parameters|Type|Description
-|-|-
`maxResults`|`string`|Optional, max results to fetch provided as integer.
`processInstanceIdOrBusinessKey`|`string`|The unique process instance id or business key of the BPMN process.

---
#### Tool: **`list_variables`**
Retrieve the list of variables for a specific BPMN process in the Camunda process engine. The process is identified by its process instance id or the business key. The response includes details such as tenant, key, business key, process instance id, and other metadata for each process instance.
Parameters|Type|Description
-|-|-
`maxResults`|`string`|Optional, max results to fetch provided as integer.
`processInstanceIdOrBusinessKey`|`string`|The unique process instance if of the BPMN process definition. Business key may belong to multiple processes.

---
#### Tool: **`resolve_incident`**
Requests the Cmaunda BPM process engine to resolve an incident. Resolving an incident allows the process instance to continue its execution.
Parameters|Type|Description
-|-|-
`incidentId`|`string`|The unique identifier of the incident to resolve. This ID is typically generated by the Camunda process engine when an incident occurs.

---
#### Tool: **`send_message`**
Send a message to a specific BPMN process instance in the Camunda process engine. The process is identified by its process instance id or the business key.
Parameters|Type|Description
-|-|-
`messageName`|`string`|The name of the message to send.
`processInstanceIdOrBusinessKey`|`string`|The unique process instance id or business key of the BPMN process.

---
