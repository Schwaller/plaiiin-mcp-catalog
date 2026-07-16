Python server implementing Model Context Protocol (MCP) for ROS2.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/ros2](https://hub.docker.com/repository/docker/mcp/ros2)
**Author**|[wise-vision](https://github.com/wise-vision)
**Repository**|https://github.com/wise-vision/mcp_server_ros_2

## Available Tools (14)
Tools provided by this Server|Short Description
-|-
`ros2_action_request_result`|Wait for the RESULT of a ROS 2 action (GetResult) for a given goal_id.|
`ros2_action_subscribe_feedback`|Subscribe to feedback messages of a ROS 2 action.|
`ros2_action_subscribe_status`|Subscribe to '/<action>/_action/status' (action_msgs/msg/GoalStatusArray) and return a snapshot of status frames over a time window.|
`ros2_cancel_action_goal`|Cancel a ROS 2 action goal via '/<action>/cancel_goal' (action_msgs/srv/CancelGoal).|
`ros2_get_message_fields`|Returns the fields of a given ROS2 message type.|
`ros2_get_messages_stored_in_influx_data_base`|Calls the ROS2 ‘/get_messages’ service to retrieve past messages from a topic for data which is stored in InfluxDB.|
`ros2_interface_list`|Returns a list of available ROS 2 interfaces.|
`ros2_list_actions`|List all available ROS 2 actions with their types and request fields.|
`ros2_send_action_goal`|Send a goal to a ROS 2 action by name and action type using provided goal fields.|
`ros2_service_call`|Call a ROS 2 service by name and type using provided fields.|
`ros2_service_list`|Returns a list of available ROS 2 services and their request fields.|
`ros2_topic_list`|Returns a list of available ROS 2 topics and their types.|
`ros2_topic_publish`|Publish a message to a ROS 2 topic by name and message type using provided field values.|
`ros2_topic_subscribe`|Subscribe to a ROS 2 topic by name collecting messages for a given time or count limit.|

---
## Tools Details

#### Tool: **`ros2_action_request_result`**
Wait for the RESULT of a ROS 2 action (GetResult) for a given goal_id. Before **every** use of this tool, the agent should ensure the target action exists (e.g., by calling 'ros2_list_actions').
Parameters|Type|Description
-|-|-
`action_name`|`string`|Action name, e.g. '/fibonacci'
`action_type`|`string`|Full action type, e.g. 'example_interfaces/action/Fibonacci' or 'pkg/ActionName'
`goal_id_hex`|`string`|32-char UUID hex of the goal (no dashes).
`timeout_sec`|`string` *optional*|Seconds to wait for GetResult; null → wait indefinitely.
`wait_for_service_sec`|`number` *optional*|Seconds to wait for the GetResult service to appear.

---
#### Tool: **`ros2_action_subscribe_feedback`**
Subscribe to feedback messages of a ROS 2 action. Optionally filter by goal_id_hex. Collects feedback for a fixed duration or until a maximum number of messages is received. Each message contains goal_id, feedback payload, and receive timestamp.
Parameters|Type|Description
-|-|-
`action_name`|`string`|Action name, e.g. '/fibonacci'
`action_type`|`string`|Full action type, e.g. 'example_interfaces/action/Fibonacci' or 'pkg/ActionName'
`duration_sec`|`number` *optional*|How many seconds to keep spinning and collecting feedback.
`goal_id_hex`|`string` *optional*|Optional 32-char UUID hex of the goal (no dashes) to filter feedbacks.
`max_messages`|`integer` *optional*|Maximum number of feedback messages to collect.

---
#### Tool: **`ros2_action_subscribe_status`**
Subscribe to '/<action>/_action/status' (action_msgs/msg/GoalStatusArray) and return a snapshot of status frames over a time window. Each frame contains goal_id, accept_stamp, status_code and status text.
Parameters|Type|Description
-|-|-
`action_name`|`string`|Action name, e.g. '/fibonacci'
`duration_sec`|`number` *optional*|How many seconds to collect status frames.
`max_messages`|`integer` *optional*|Max number of individual statuses to collect in total.

---
#### Tool: **`ros2_cancel_action_goal`**
Cancel a ROS 2 action goal via '/<action>/cancel_goal' (action_msgs/srv/CancelGoal). You can cancel a specific goal by goal_id_hex or cancel all matching goals using cancel_all=True. Optionally limit cancellation to goals accepted before a given stamp (sec/nanosec). Before **every** use of this tool, the agent should ensure the target action exists (e.g., by calling 'ros2_list_actions').
Parameters|Type|Description
-|-|-
`action_name`|`string`|Action name, e.g. '/fibonacci' or '/navigate_to_pose'
`cancel_all`|`boolean` *optional*|If true, send zero-UUID to cancel all matching goals.
`goal_id_hex`|`string` *optional*|32-char UUID hex of the goal (no dashes). Omit when cancel_all=True.
`stamp_nanosec`|`integer` *optional*|Nanoseconds part for the acceptance time filter.
`stamp_sec`|`integer` *optional*|Cancel goals accepted BEFORE this sec (default 0 → usually all).
`wait_timeout_sec`|`number` *optional*|Timeout (seconds) to wait for the service and response.

---
#### Tool: **`ros2_get_message_fields`**
Returns the fields of a given ROS2 message type.
Parameters|Type|Description
-|-|-
`message_type`|`string`|Full ROS2 message type, e.g., std_msgs/msg/String

---
#### Tool: **`ros2_get_messages_stored_in_influx_data_base`**
Calls the ROS2 ‘/get_messages’ service to retrieve past messages from a topic for data which is stored in InfluxDB.
            Check if the /get_messages service is available before calling.
Parameters|Type|Description
-|-|-
`message_type`|`string`|Full ROS2 message type used for decoding
`topic_name`|`string`|Name of the topic to retrieve messages from.
`number_of_messages`|`integer` *optional*|Number of messages to fetch.
`time_end`|`string` *optional*|ISO8601 timestamp string to filter messages before a point in time.
`time_start`|`string` *optional*|ISO8601 timestamp string to filter messages after a point in time.

---
#### Tool: **`ros2_interface_list`**
Returns a list of available ROS 2 interfaces.
#### Tool: **`ros2_list_actions`**
List all available ROS 2 actions with their types and request fields.
            This tool queries the current ROS graph to discover active action servers and
            returns a structured description for each action.
#### Tool: **`ros2_send_action_goal`**
Send a goal to a ROS 2 action by name and action type using provided goal fields. Before **every** use of this tool, the agent must call 'ros2_list_actions' and 'ros2_interface_list' to ensure the latest available actions and types are known. Optionally wait for the result with a timeout.
Parameters|Type|Description
-|-|-
`action_name`|`string`|Action name, e.g. '/fibonacci' or '/navigate_to_pose'
`action_type`|`string`|Full action type, e.g. 'example_interfaces/action/Fibonacci' or 'pkg/ActionName'
`goal_fields`|`object`|Dictionary with goal message fields (1st section of .action file)
`timeout_sec`|`number` *optional*|Timeout (seconds) for waiting on the result when wait_for_result=true
`wait_for_result`|`boolean` *optional*|If true, wait for GetResult and include final status/result

---
#### Tool: **`ros2_service_call`**
Call a ROS 2 service by name and type using provided fields.
            Will ask the user to confirm if some fields are missing unless 'force_call' is set to True.
            Before **every** use of this tool, the agent must call 'ros2 service list' and 'ros2 interface list' to ensure the latest interface information is available.
Parameters|Type|Description
-|-|-
`fields`|`object`|Dictionary of fields to send in the service request.
`service_name`|`string`|Name of the service to call
`service_type`|`string`|Full ROS 2 service type, before pass, check service type using tool ros2_service_list
`force_call`|`boolean` *optional*|Whether to call the service even if some fields are missing

---
#### Tool: **`ros2_service_list`**
Returns a list of available ROS 2 services and their request fields.
#### Tool: **`ros2_topic_list`**
Returns a list of available ROS 2 topics and their types.
#### Tool: **`ros2_topic_publish`**
Publish a message to a ROS 2 topic by name and message type using provided field values.
            Supports single publish (default) or continuous publishing at a specified frequency for a duration.
            Before **every** use of this tool, the agent must call 'ros2_topic_list' and 'ros2_interface_list'
            to ensure the latest available topics and message types are known.
Parameters|Type|Description
-|-|-
`data`|`object`|Dictionary containing the message fields and values
`message_type`|`string`|Full ROS 2 message type, e.g., 'std_msgs/msg/String'
`topic_name`|`string`|Name of the topic to publish to
`duration`|`number` *optional*|Optional: Duration in seconds for continuous publishing. Must be used with frequency parameter.
`frequency`|`number` *optional*|Optional: Publish frequency in Hz (messages per second). If provided with duration, publishes repeatedly.

---
#### Tool: **`ros2_topic_subscribe`**
Subscribe to a ROS 2 topic by name collecting messages for a given time or count limit.
            Before **every** use of this tool, the agent must call 'ros2_topic_list'
            to ensure it has the latest available topics
Parameters|Type|Description
-|-|-
`topic_name`|`string`|Name of the topic to subscribe to
`duration`|`number` *optional*|If provided, collects messages for this many seconds.
`message_limit`|`integer` *optional*|If provided, stops after receiving this number of messages.

---

## Screenshots

![WiseVision ROS2 screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/ros2-1.gif)

![WiseVision ROS2 screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/ros2-2.gif)

![WiseVision ROS2 screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/ros2-3.gif)
