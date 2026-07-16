Connect your AI workflows to the ThingsBoard IoT Platform through this MCP server. 
Enables LLMs to query device telemetry, manage IoT entities (devices, assets, customers),
and analyze sensor data - all through natural language.

Perfect for building AI-powered IoT monitoring, predictive maintenance, and automated
device management workflows. Supports both ThingsBoard Community Edition and Professional Edition.
.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/thingsboard](https://hub.docker.com/repository/docker/mcp/thingsboard)
**Author**|[thingsboard](https://github.com/thingsboard)
**Repository**|https://github.com/thingsboard/thingsboard-mcp

## Available Tools (62)
Tools provided by this Server|Short Description
-|-
`findByFrom`|Returns list of relation objects for the specified entity by the 'from' direction.|
`findByFromWithRelationType`|Returns list of relation objects for the specified entity by the 'from' direction and relation type.|
`findByTo`|Returns list of relation objects for the specified entity by the 'to' direction.|
`findByToWithRelationType`|Returns list of relation objects for the specified entity by the 'to' direction and relation type.|
`findInfoByFrom`|Returns list of relation info objects for the specified entity by the 'from' direction.|
`findInfoByTo`|Returns list of relation info objects for the specified entity by the 'to' direction.|
`getAdminSettings`|Get the Administration Settings object using specified string key.|
`getAlarmById`|Get the Alarm object based on the provided alarm id.|
`getAlarmInfoById`|Get the Alarm info object based on the provided alarm id.|
`getAlarmTypes`|Get a set of unique alarm types based on alarms that are either owned by tenant or assigned to the customer which user is performing the request.|
`getAlarms`|Get a page of alarms for the selected entity.|
`getAllAlarms`|Get a page of alarms that belongs to the current user owner.|
`getAllCustomerUsers`|Returns a page of users for the current tenant with authority 'CUSTOMER_USER'.|
`getAssetById`|Get the Asset object based on the provided Asset Id.|
`getAssetsByEntityGroupId`|Returns a page of asset objects that belongs to specified Entity Group Id.|
`getAssetsByIds`|Get Assets By Ids.|
`getAttributeKeys`|Returns a set of unique attribute key names for the selected entity.|
`getAttributeKeysByScope`|Returns a set of unique attribute key names for the selected entity and attributes scope: * SERVER_SCOPE - supported for all entity types; * CLIENT_SCOPE - supported for devices; * SHARED_SCOPE - supported for devices.|
`getAttributes`|Returns all attributes that belong to specified entity.|
`getAttributesByScope`|Returns all attributes of a specified scope that belong to specified entity.|
`getCustomerAssets`|Returns a page of assets objects assigned to customer.|
`getCustomerById`|Get the Customer object based on the provided Customer Id.|
`getCustomerDevices`|Returns a page of devices objects assigned to customer.|
`getCustomerUsers`|Returns a page of users assigned to the specified customer.|
`getCustomers`|Returns a page of customers owned by tenant.|
`getCustomersByEntityGroupId`|Returns a page of Customer objects that belongs to specified Entity Group Id.|
`getDeviceById`|Fetch the Device object based on the provided Device Id.|
`getDeviceCredentialsByDeviceId`|Get device credentials by device id.|
`getDevicesByEntityGroupId`|Returns a page of device objects that belongs to specified Entity Group Id.|
`getDevicesByIds`|Get Devices By Ids.|
`getEntityGroupById`|Fetch the Entity Group object based on the provided Entity Group Id.|
`getEntityGroupByOwnerAndNameAndType`|Fetch the Entity Group object based on the provided owner, type and name.|
`getEntityGroupsByIds`|Fetch the list of Entity Group Info objects based on the provided entity group ids list.|
`getEntityGroupsByOwnerAndType`|Fetch the list of Entity Group Info objects based on the provided Owner Id and Entity Type.|
`getEntityGroupsByType`|Fetch the list of Entity Group Info objects based on the provided Entity Type.|
`getEntityGroupsForEntity`|Returns a list of groups that contain the specified Entity Id.|
`getHighestAlarmSeverity`|Get highest alarm severity by originator ('entityType' and 'entityId') and optional 'status' and 'searchStatus' filters and returns the highest AlarmSeverity(CRITICAL, MAJOR, MINOR, WARNING or INDETERMINATE).Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error.|
`getLatestTimeseries`|Returns all time series that belong to specified entity.|
`getRelation`|Returns relation object between two specified entities if present.|
`getSecuritySettings`|Get the Security settings object that contains password policy, lockout limits, notification email, mobile secret key length, and TTL values for activation & password-reset tokens (1–24 hours).|
`getSystemInfo`|Get main information about system.|
`getTenantAdmins`|Returns a page of tenant administrator users assigned to the specified tenant.|
`getTenantAsset`|Get tenant asset.|
`getTenantAssets`|Returns a page of assets owned by tenant.|
`getTenantCustomer`|Get the Customer using Customer Title.|
`getTenantDevice`|Requested device must be owned by tenant that the user belongs to.|
`getTenantDevices`|Returns a page of devices owned by tenant.|
`getTimeseries`|Returns a range of time series values for specified entity.|
`getTimeseriesKeys`|Returns a set of unique time series key names for the selected entity.|
`getUsageInfo`|Retrieves usage statistics for the current tenant, including number of devices, assets, customers, users, dashboards, edges, transportMessages, jsExecutions, tbelExecutions, emails, sms, alarms.|
`getUserAssets`|Returns a page of assets objects available for the current user.|
`getUserById`|Fetch the User object based on the provided User Id.|
`getUserCustomers`|Returns a page of customers available for the user.|
`getUserDevices`|Returns a page of device objects available for the current user.|
`getUsers`|Returns a page of users owned by tenant or customer.|
`getUsersByEntityGroupId`|Returns a page of user objects that belongs to specified Entity Group Id.|
`getUsersForAssign`|Returns page of user data objects that can be assigned to provided alarmId.|
`saveDeviceAttributes`|Creates or updates the device attributes based on device id and specified attribute scope.|
`saveEntityAttributesV1`|Creates or updates the entity attributes based on Entity Id and the specified attribute scope.|
`saveEntityAttributesV2`|Creates or updates the entity attributes based on Entity Id and the specified attribute scope.|
`saveEntityTelemetry`|Creates or updates the entity time series data based on the Entity Id and request payload.The request payload is a JSON document with three possible formats: Simple format without timestamp.|
`saveEntityTelemetryWithTTL`|Creates or updates the entity time series data based on the Entity Id and request payload.The request payload is a JSON document with three possible formats: Simple format without timestamp.|

---
## Tools Details

#### Tool: **`findByFrom`**
Returns list of relation objects for the specified entity by the 'from' direction. 

If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.
Parameters|Type|Description
-|-|-
`strFromId`|`string`|A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`strFromType`|`string`|A string value representing the entity type. For example, 'DEVICE'
`strRelationTypeGroup`|`string` *optional*|A string value representing relation type group. For example, 'COMMON'

---
#### Tool: **`findByFromWithRelationType`**
Returns list of relation objects for the specified entity by the 'from' direction and relation type. 

If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.
Parameters|Type|Description
-|-|-
`relationType`|`string`|A string value representing relation type between entities. For example, 'Contains', 'Manages'. It can be any string value.
`strFromId`|`string`|A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`strFromType`|`string`|A string value representing the entity type. For example, 'DEVICE'
`strRelationTypeGroup`|`string` *optional*|A string value representing relation type group. For example, 'COMMON'

---
#### Tool: **`findByTo`**
Returns list of relation objects for the specified entity by the 'to' direction. 

If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.
Parameters|Type|Description
-|-|-
`strToId`|`string`|A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`strToType`|`string`|A string value representing the entity type. For example, 'DEVICE'
`strRelationTypeGroup`|`string` *optional*|A string value representing relation type group. For example, 'COMMON'

---
#### Tool: **`findByToWithRelationType`**
Returns list of relation objects for the specified entity by the 'to' direction and relation type. 

If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.
Parameters|Type|Description
-|-|-
`relationType`|`string`|A string value representing relation type between entities. For example, 'Contains', 'Manages'. It can be any string value.
`strToId`|`string`|A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`strToType`|`string`|A string value representing the entity type. For example, 'DEVICE'
`strRelationTypeGroup`|`string` *optional*|A string value representing relation type group. For example, 'COMMON'

---
#### Tool: **`findInfoByFrom`**
Returns list of relation info objects for the specified entity by the 'from' direction. 

If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names.
Parameters|Type|Description
-|-|-
`strFromId`|`string`|A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`strFromType`|`string`|A string value representing the entity type. For example, 'DEVICE'
`strRelationTypeGroup`|`string` *optional*|A string value representing relation type group. For example, 'COMMON'

---
#### Tool: **`findInfoByTo`**
Returns list of relation info objects for the specified entity by the 'to' direction. 

If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names.
Parameters|Type|Description
-|-|-
`strToId`|`string`|A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`strToType`|`string`|A string value representing the entity type. For example, 'DEVICE'
`strRelationTypeGroup`|`string` *optional*|A string value representing relation type group. For example, 'COMMON'

---
#### Tool: **`getAdminSettings`**
Get the Administration Settings object using specified string key. Referencing non-existing key will cause an error. 

Available for users with 'SYS_ADMIN' authority.
Parameters|Type|Description
-|-|-
`key`|`string`|A string value of the key (e.g. 'general', 'mail', 'notifications', 'sms', 'entitiesVersionControl', 'connectivity', 'jwt', etc

---
#### Tool: **`getAlarmById`**
Get the Alarm object based on the provided alarm id. If the user has the authority of 'Tenant Administrator', the server checks that the originator of alarm is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the originator of alarm belongs to the customer.
Parameters|Type|Description
-|-|-
`alarmId`|`string`|A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'

---
#### Tool: **`getAlarmInfoById`**
Get the Alarm info object based on the provided alarm id. If the user has the authority of 'Tenant Administrator', the server checks that the originator of alarm is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the originator of alarm belongs to the customer. Alarm Info is an extension of the default Alarm object that also contains name of the alarm originator.

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.
Parameters|Type|Description
-|-|-
`alarmId`|`string`|A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'

---
#### Tool: **`getAlarmTypes`**
Get a set of unique alarm types based on alarms that are either owned by tenant or assigned to the customer which user is performing the request. 

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.
Parameters|Type|Description
-|-|-
`page`|`integer`|Sequence number of page starting from 0
`pageSize`|`integer`|Maximum amount of entities in a one page
`sortOrder`|`string` *optional*|Sort order. ASC (ASCENDING) or DESC (DESCENDING)
`textSearch`|`string` *optional*|The case insensitive 'substring' filter based on of next alarm fields: type, severity or status

---
#### Tool: **`getAlarms`**
Get a page of alarms for the selected entity. Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. 

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.
Parameters|Type|Description
-|-|-
`entityId`|`string`|A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`entityType`|`string`|A string value representing the entity type. For example, 'DEVICE'
`page`|`integer`|Sequence number of page starting from 0
`pageSize`|`integer`|Maximum amount of entities in a one page
`endTs`|`integer` *optional*|The end timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'.
`fetchOriginator`|`boolean` *optional*|A boolean value to specify if the alarm originator name will be filled in the AlarmInfo object  field: 'originatorName' or will returns as null.
`searchStatus`|`string` *optional*|A string value representing one of the AlarmSearchStatus enumeration value. Allowed values: 'ANY', 'ACTIVE', 'CLEARED', 'ACK', 'UNACK'
`sortOrder`|`string` *optional*|Sort order. ASC (ASCENDING) or DESC (DESCENDING)
`sortProperty`|`string` *optional*|Property of entity to sort by. Allowed values: 'createdTime', 'startTs', 'endTs', 'ackTs', 'clearTs', 'severity', 'status'
`startTs`|`integer` *optional*|The start timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'.
`status`|`string` *optional*|A string value representing one of the AlarmStatus enumeration value. Allowed values: 'ACTIVE_UNACK', 'ACTIVE_ACK', 'CLEARED_UNACK', 'CLEARED_ACK'
`textSearch`|`string` *optional*|The case insensitive 'substring' filter based on of next alarm fields: type, severity or status

---
#### Tool: **`getAllAlarms`**
Get a page of alarms that belongs to the current user owner. If the user has the authority of 'Tenant Administrator', the server returns alarms that belongs to the tenant of current user. If the user has the authority of 'Customer User', the server returns alarms that belongs to the customer of current user. Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. 

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.
Parameters|Type|Description
-|-|-
`page`|`integer`|Sequence number of page starting from 0
`pageSize`|`integer`|Maximum amount of entities in a one page
`assigneeId`|`string` *optional*|A string value representing the assignee user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`endTs`|`integer` *optional*|The end timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'.
`fetchOriginator`|`boolean` *optional*|A boolean value to specify if the alarm originator name will be filled in the AlarmInfo object  field: 'originatorName' or will returns as null.
`searchStatus`|`string` *optional*|A string value representing one of the AlarmSearchStatus enumeration value. Allowed values: 'ANY', 'ACTIVE', 'CLEARED', 'ACK', 'UNACK'
`sortOrder`|`string` *optional*|Sort order. ASC (ASCENDING) or DESC (DESCENDING)
`sortProperty`|`string` *optional*|Property of entity to sort by. Allowed values: 'createdTime', 'startTs', 'endTs', 'ackTs', 'clearTs', 'severity', 'status'
`startTs`|`integer` *optional*|The start timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'.
`status`|`string` *optional*|A string value representing one of the AlarmStatus enumeration value. Allowed values: 'ACTIVE_UNACK', 'ACTIVE_ACK', 'CLEARED_UNACK', 'CLEARED_ACK'
`textSearch`|`string` *optional*|The case insensitive 'substring' filter based on of next alarm fields: type, severity or status

---
#### Tool: **`getAllCustomerUsers`**
Returns a page of users for the current tenant with authority 'CUSTOMER_USER'. Available only in Professional edition (PE). You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. 

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).
Parameters|Type|Description
-|-|-
`page`|`integer`|Sequence number of page starting from 0
`pageSize`|`integer`|Maximum amount of entities in a one page
`sortOrder`|`string` *optional*|Sort order. ASC (ASCENDING) or DESC (DESCENDING)
`sortProperty`|`string` *optional*|Property of entity to sort by. Allowed values: 'createdTime', 'firstName', 'lastName', 'email'
`textSearch`|`string` *optional*|The case insensitive 'substring' filter based on the customer title.

---
#### Tool: **`getAssetById`**
Get the Asset object based on the provided Asset Id. If the user has the authority of 'Tenant Administrator', the server checks that the asset is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the asset is assigned to the same customer.

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.
Parameters|Type|Description
-|-|-
`assetId`|`string`|A string value representing the asset id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'

---
#### Tool: **`getAssetsByEntityGroupId`**
Returns a page of asset objects that belongs to specified Entity Group Id. Available only in Professional edition (PE). You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. 

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.
Parameters|Type|Description
-|-|-
`entityGroupId`|`string`|A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`page`|`integer`|Sequence number of page starting from 0
`pageSize`|`integer`|Maximum amount of entities in a one page
`sortOrder`|`string` *optional*|Sort order. ASC (ASCENDING) or DESC (DESCENDING)
`sortProperty`|`string` *optional*|Property of entity to sort by. Allowed values: 'createdTime', 'firstName', 'lastName', 'email'
`textSearch`|`string` *optional*|The case insensitive 'substring' filter based on the customer title.

---
#### Tool: **`getAssetsByIds`**
Get Assets By Ids. Requested assets must be owned by tenant or assigned to customer which user is performing the request. 

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.
Parameters|Type|Description
-|-|-
`assetIds`|`array`|A list of assets ids, separated by comma ','

---
#### Tool: **`getAttributeKeys`**
Returns a set of unique attribute key names for the selected entity. The response will include merged key names set for all attribute scopes:

 * SERVER_SCOPE - supported for all entity types;
 * CLIENT_SCOPE - supported for devices;
 * SHARED_SCOPE - supported for devices. 

Referencing a non-existing entity Id or invalid entity type will cause an error. 

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.
Parameters|Type|Description
-|-|-
`entityIdStr`|`string`|A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`entityType`|`string`|A string value representing the entity type. For example, 'DEVICE'

---
#### Tool: **`getAttributeKeysByScope`**
Returns a set of unique attribute key names for the selected entity and attributes scope: 

 * SERVER_SCOPE - supported for all entity types;
 * CLIENT_SCOPE - supported for devices;
 * SHARED_SCOPE - supported for devices. 

Referencing a non-existing entity Id or invalid entity type will cause an error. 

Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.
Parameters|Type|Description
-|-|-
`entityIdStr`|`string`|A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
`entityType`|`string`|A string value representing the entity type. For example, 'DEVICE'
`scope`|`string`|A string value representing the attributes scope. For example, 'SERVER_SCOPE'. Allowable values: 'SERVER_SCOPE', 'SHARED_SCOPE', 'CLIENT_SCOPE'

---
#### Tool: **`getAttributes`**
Returns all attributes that belong to specified entity. Use optional 'keys' parameter to return specific attributes.
 Example of the result: 

```json
[
  {"key": "stringAttributeKey", "value": "value", "lastUpdateTs": 1609459200000},
  {"key": "booleanAttributeKey", "value": false, "lastUpdateTs": 1609459200001},
  {"key": "doubleAttributeKey", "value": 42.2, "lastUpdateTs": 1609459200002},
  {"key": "longKeyExample", "value": 73, "lastUpdateTs": 1609459200003},
  {"key": "json

[...]

## Screenshots

![ThingsBoard screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/thingsboard-1.png)

![ThingsBoard screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/thingsboard-2.png)

![ThingsBoard screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/thingsboard-3.png)
