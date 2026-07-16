Pref Editor is a tool for viewing and editing Android app preferences during development.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/pref-editor](https://hub.docker.com/repository/docker/mcp/pref-editor)
**Author**|[charlesmuchene](https://github.com/charlesmuchene)
**Repository**|https://github.com/charlesmuchene/pref-editor-mcp-server

## Available Tools (7)
Tools provided by this Server|Short Description
-|-
`add_preference`|Adds a new preference given the name, value and type.|
`change_preference`|Changes the value of an existing preference|
`delete_preference`|Delete an existing preference|
`devices`|Lists connected Android devices|
`list_apps`|Lists apps installed on device|
`list_files`|Lists preference files for an app|
`read_preferences`|Reads all user preferences in a file|

---
## Tools Details

#### Tool: **`add_preference`**
Adds a new preference given the name, value and type.
Parameters|Type|Description
-|-|-
`appId`|`string`|The application's package name.
`deviceId`|`string`|The device's serial number.
`filename`|`string`|The filename with or without the extension.
`name`|`string`|The name/key of the user preference
`type`|`string`|The type of the preference value: integer, boolean, float, double, long or string
`value`|`string`|The value of user preference

---
#### Tool: **`change_preference`**
Changes the value of an existing preference
Parameters|Type|Description
-|-|-
`appId`|`string`|The application's package name.
`deviceId`|`string`|The device's serial number.
`filename`|`string`|The filename with or without the extension.
`name`|`string`|The name/key of the user preference
`value`|`string`|The value of user preference

---
#### Tool: **`delete_preference`**
Delete an existing preference
Parameters|Type|Description
-|-|-
`appId`|`string`|The application's package name.
`deviceId`|`string`|The device's serial number.
`filename`|`string`|The filename with or without the extension.
`name`|`string`|The name/key of the user preference

---
#### Tool: **`devices`**
Lists connected Android devices
#### Tool: **`list_apps`**
Lists apps installed on device
Parameters|Type|Description
-|-|-
`deviceId`|`string`|The device's serial number.

---
#### Tool: **`list_files`**
Lists preference files for an app
Parameters|Type|Description
-|-|-
`appId`|`string`|The application's package name.
`deviceId`|`string`|The device's serial number.

---
#### Tool: **`read_preferences`**
Reads all user preferences in a file
Parameters|Type|Description
-|-|-
`appId`|`string`|The application's package name.
`deviceId`|`string`|The device's serial number.
`filename`|`string`|The filename with or without the extension.

---

## Screenshots

![Pref Editor screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/pref-editor-1.png)

![Pref Editor screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/pref-editor-2.png)

![Pref Editor screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/pref-editor-3.png)
