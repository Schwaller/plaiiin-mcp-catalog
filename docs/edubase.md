The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/edubase](https://hub.docker.com/repository/docker/mcp/edubase)
**Author**|[EduBase](https://github.com/EduBase)
**Repository**|https://github.com/EduBase/MCP

## Available Tools (165)
Tools provided by this Server|Short Description
-|-
`edubase_delete_class_members`|Remove user(s) from a class|
`edubase_delete_class_permission`|Remove a user permission from a class|
`edubase_delete_class_tag`|Remove a tag attachment from a class|
`edubase_delete_course_permission`|Remove a user permission from a course|
`edubase_delete_course_tag`|Remove a tag attachment from a course|
`edubase_delete_event_permission`|Remove a user permission from an event|
`edubase_delete_event_tag`|Remove a tag attachment from an event|
`edubase_delete_exam`|Remove/archive exam|
`edubase_delete_exam_branding`|Remove branding from an exam|
`edubase_delete_exam_permission`|Remove a user permission from an exam|
`edubase_delete_exam_tag`|Remove a tag attachment from an exam|
`edubase_delete_exam_users`|Remove user(s) from an exam|
`edubase_delete_filebin_upload`|Delete an uploaded file and/or temporary file upload link|
`edubase_delete_integration`|Remove integration|
`edubase_delete_integration_permission`|Remove a user permission from an integration|
`edubase_delete_integration_tag`|Remove a tag attachment from an integration|
`edubase_delete_organization`|Remove organization|
`edubase_delete_organization_members`|Remove user(s) from an organization|
`edubase_delete_organization_permission`|Remove a user permission from an organization|
`edubase_delete_organization_tag`|Remove a tag attachment from an organization|
`edubase_delete_organization_webhook`|Remove organizational webhook|
`edubase_delete_question`|Permanently delete a Quiz question|
`edubase_delete_quiz`|Remove/archive Quiz set|
`edubase_delete_quiz_permission`|Remove a user permission from a quiz|
`edubase_delete_quiz_questions`|Remove question(s) from a Quiz set, or one of its question group|
`edubase_delete_quiz_tag`|Remove a tag attachment from a Quiz|
`edubase_delete_scorm_permission`|Remove a user permission from a SCORM learning material|
`edubase_delete_scorm_tag`|Remove a tag attachment from a SCORM learning material|
`edubase_delete_tag_permission`|Remove a user permission from a tag|
`edubase_delete_user`|Delete user|
`edubase_delete_user_assume`|Revoke assume token|
`edubase_delete_user_classes`|Remove user from class(es)|
`edubase_delete_user_login`|Delete a previously generated login link|
`edubase_delete_user_organizations`|Remove user from organization(s)|
`edubase_delete_video_permission`|Remove a user permission from a video|
`edubase_delete_video_tag`|Remove a tag attachment from a video|
`edubase_filebin`|Upload file to EduBase temporary file storage|
`edubase_get_class`|Get/check class|
`edubase_get_class_assignments`|List all assignments in a class|
`edubase_get_class_members`|List all members in a class|
`edubase_get_class_permission`|Check if a user has permission on a class|
`edubase_get_class_tag`|Check if tag is attached to a class|
`edubase_get_class_tags`|List all attached tags of a class|
`edubase_get_classes`|List owned and managed classes|
`edubase_get_course_permission`|Check if a user has permission on a course|
`edubase_get_course_tag`|Check if tag is attached to a course|
`edubase_get_course_tags`|List all attached tags of a course|
`edubase_get_event_permission`|Check if a user has permission on an event|
`edubase_get_event_tag`|Check if tag is attached to an event|
`edubase_get_event_tags`|List all attached tags of an event|
`edubase_get_exam`|Get/check exam|
`edubase_get_exam_branding`|Get exam branding configuration|
`edubase_get_exam_certificates_user`|Get (the latest) certificate details for a specific exam and user|
`edubase_get_exam_permission`|Check if a user has permission on an exam|
`edubase_get_exam_results_raw`|Get raw results for a specific exam|
`edubase_get_exam_results_user`|Get user results for a specific exam|
`edubase_get_exam_tag`|Check if tag is attached to an exam|
`edubase_get_exam_tags`|List all attached tags of an exam|
`edubase_get_exam_users`|List all users on an exam|
`edubase_get_exams`|List owned and managed exams|
`edubase_get_integration`|Get/check integration|
`edubase_get_integration_keys`|Get integration keys/secrets|
`edubase_get_integration_permission`|Check if a user has permission on an integration|
`edubase_get_integration_tag`|Check if tag is attached to an integration|
`edubase_get_integration_tags`|List all attached tags of an integration|
`edubase_get_integrations`|List owned and managed integrations|
`edubase_get_organization`|Get/check organization|
`edubase_get_organization_members`|List all members in an organization|
`edubase_get_organization_permission`|Check if a user has permission on an organization|
`edubase_get_organization_tag`|Check if tag is attached to an organization|
`edubase_get_organization_tags`|List all attached tags of an organization|
`edubase_get_organization_webhook`|Get/check webhook configured in organization|
`edubase_get_organizations`|List owned and managed organizations|
`edubase_get_question`|Check existing question|
`edubase_get_question_id`|Get external unique question identifier by question identification string|
`edubase_get_questions`|List owned and managed Quiz questions|
`edubase_get_quiz`|Get/check Quiz set|
`edubase_get_quiz_permission`|Check if a user has permission on a quiz|
`edubase_get_quiz_questions`|List all questions and question groups in a Quiz set|
`edubase_get_quiz_results_play`|Get detailed results for a specific Quiz play|
`edubase_get_quiz_results_user`|Get user results for a specific Quiz set|
`edubase_get_quiz_tag`|Check if tag is attached to a Quiz|
`edubase_get_quiz_tags`|List all attached tags of a Quiz|
`edubase_get_quizes`|List owned and managed Quiz sets|
`edubase_get_scorm_permission`|Check if a user has permission on a SCORM learning material|
`edubase_get_scorm_tag`|Check if tag is attached to a SCORM learning material|
`edubase_get_scorm_tags`|List all attached tags of a SCORM learning material|
`edubase_get_tag`|Get/check tag|
`edubase_get_tag_permission`|Check if a user has permission on a tag|
`edubase_get_tags`|List owned and managed tags|
`edubase_get_user`|Get/check user|
`edubase_get_user_classes`|List all classes a user is member of|
`edubase_get_user_group`|Get user's group|
`edubase_get_user_login`|Get latest valid login link for user|
`edubase_get_user_me`|Get/check current user|
`edubase_get_user_name`|Get user's name|
`edubase_get_user_organizations`|List all organizations a user is member of|
`edubase_get_user_search`|Lookup user by email, username or code|
`edubase_get_users`|List managed, non-generated users|
`edubase_get_video_permission`|Check if a user has permission on a video|
`edubase_get_video_tag`|Check if tag is attached to a video|
`edubase_get_video_tags`|List all attached tags of a video|
`edubase_mcp_server_api`|Get MCP Server API URL|
`edubase_mcp_server_version`|Get MCP Server Version|
`edubase_patch_integration`|Update integration|
`edubase_patch_organization`|Update organization|
`edubase_patch_organization_webhook`|Update organizational webhook|
`edubase_patch_user`|Update user|
`edubase_post_class_members`|Assign user(s) to a class|
`edubase_post_class_permission`|Create new permission for a user on a class|
`edubase_post_class_tag`|Attach tag to a class|
`edubase_post_class_transfer`|Transfer class to user|
`edubase_post_classes_members`|Assign user(s) to class(es)|
`edubase_post_course_permission`|Create new permission for a user on a course|
`edubase_post_course_tag`|Attach tag to a course|
`edubase_post_course_transfer`|Transfer course to user|
`edubase_post_event_permission`|Create new permission for a user on an event|
`edubase_post_event_tag`|Attach tag to an event|
`edubase_post_event_transfer`|Transfer event to user|
`edubase_post_exam`|Create a new exam from an existing Quiz set|
`edubase_post_exam_branding`|Configure or update exam branding|
`edubase_post_exam_certificates_user_download`|Generate download link for the latest user exam certificate|
`edubase_post_exam_permission`|Create new permission for a user on an exam|
`edubase_post_exam_summary`|Submit a new AI exam summary|
`edubase_post_exam_tag`|Attach tag to an exam|
`edubase_post_exam_transfer`|Transfer exam to user|
`edubase_post_exam_users`|Assign user(s) to an exam|
`edubase_post_filebin_upload`|Generate upload link for a temporary file storage|
`edubase_post_integration`|Create a new API or LMS integration|
`edubase_post_integration_keys`|Rotate integration keys/secrets|
`edubase_post_integration_permission`|Create new permission for a user on an integration|
`edubase_post_integration_tag`|Attach tag to an integration|
`edubase_post_integration_transfer`|Transfer integration to user|
`edubase_post_metrics_custom`|Update a custom metric|
`edubase_post_organization`|Create an organization|
`edubase_post_organization_members`|Assign user(s) to an organization|
`edubase_post_organization_permission`|Create new permission for a user on an organization|
`edubase_post_organization_tag`|Attach tag to an organization|
`edubase_post_organization_transfer`|Transfer organization to user|
`edubase_post_organization_webhook`|Create a webhook for an organization|
`edubase_post_organization_webhook_trigger`|Trigger an organizational webhook call with optional custom payload|
`edubase_post_organizations_members`|Assign user(s) to organization(s)|
`edubase_post_question`|Publish or update a question|
`edubase_post_question_export`|Generate download link for exporting the question (in JSON format)|
`edubase_post_question_id`|Set external unique question identifier for question identified by a question identification string|
`edubase_post_quiz`|Create a new Quiz set|
`edubase_post_quiz_permission`|Create new permission for a user on a quiz|
`edubase_post_quiz_questions`|Assign question(s) to a Quiz set, or one of its question group|
`edubase_post_quiz_tag`|Attach tag to a Quiz|
`edubase_post_quiz_transfer`|Transfer Quiz to user|
`edubase_post_scorm_permission`|Create new permission for a user on a SCORM learning material|
`edubase_post_scorm_tag`|Attach tag to a SCORM learning material|
`edubase_post_scorm_transfer`|Transfer SCORM to user|
`edubase_post_tag_permission`|Create new permission for a user on a tag|
`edubase_post_tag_transfer`|Transfer tag to user|
`edubase_post_user`|Create new EduBase user account|
`edubase_post_user_assume`|Assume user for next requests with assume token|
`edubase_post_user_classes`|Assign user to class(es)|
`edubase_post_user_group`|Update a user's group|
`edubase_post_user_login`|Generate login link|
`edubase_post_user_name`|Update a user's name|
`edubase_post_user_organizations`|Assign user to organization(s)|
`edubase_post_video_permission`|Create new permission for a user on a video|
`edubase_post_video_tag`|Attach tag to a video|
`edubase_post_video_transfer`|Transfer video to user|

---
## Tools Details

#### Tool: **`edubase_delete_class_members`**
Remove user(s) from a class.
Parameters|Type|Description
-|-|-
`class`|`string`|class identification string
`users`|`string`|comma-separated list of user identification strings

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_class_permission`**
Remove a user permission from a class.
Parameters|Type|Description
-|-|-
`class`|`string`|class identification string
`permission`|`string`|permission level (view / report / control / modify / grant / admin)
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_class_tag`**
Remove a tag attachment from a class.
Parameters|Type|Description
-|-|-
`class`|`string`|class identification string
`tag`|`string`|tag identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_course_permission`**
Remove a user permission from a course.
Parameters|Type|Description
-|-|-
`course`|`string`|course identification string
`permission`|`string`|permission level (view / report / control / modify / grant / admin)
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_course_tag`**
Remove a tag attachment from a course.
Parameters|Type|Description
-|-|-
`course`|`string`|course identification string
`tag`|`string`|tag identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_event_permission`**
Remove a user permission from an event.
Parameters|Type|Description
-|-|-
`event`|`string`|event identification string
`permission`|`string`|permission level (view / report / control / modify / finances / grant / admin)
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_event_tag`**
Remove a tag attachment from an event.
Parameters|Type|Description
-|-|-
`event`|`string`|event identification string
`tag`|`string`|tag identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_exam`**
Remove/archive exam.
Parameters|Type|Description
-|-|-
`exam`|`string`|exam identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_exam_branding`**
Remove branding from an exam.
Parameters|Type|Description
-|-|-
`exam`|`string`|exam identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_exam_permission`**
Remove a user permission from an exam.
Parameters|Type|Description
-|-|-
`exam`|`string`|exam identification string
`permission`|`string`|permission level (view / report / control / modify / grant / admin)
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_exam_tag`**
Remove a tag attachment from an exam.
Parameters|Type|Description
-|-|-
`exam`|`string`|exam identification string
`tag`|`string`|tag identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_exam_users`**
Remove user(s) from an exam.
Parameters|Type|Description
-|-|-
`exam`|`string`|exam identification string
`users`|`string`|comma-separated list of user identification strings

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_filebin_upload`**
Delete an uploaded file and/or temporary file upload link.
Parameters|Type|Description
-|-|-
`id`|`string`|external unique filebin identifier of the uploaded file or temporary file upload link

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_integration`**
Remove integration.
Parameters|Type|Description
-|-|-
`integration`|`string`|integration identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_integration_permission`**
Remove a user permission from an integration.
Parameters|Type|Description
-|-|-
`integration`|`string`|integration identification string
`permission`|`string`|permission level (view / report / control / modify / grant / admin)
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_integration_tag`**
Remove a tag attachment from an integration.
Parameters|Type|Description
-|-|-
`integration`|`string`|integration identification string
`tag`|`string`|tag identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_organization`**
Remove organization.
Parameters|Type|Description
-|-|-
`organization`|`string`|organization identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_organization_members`**
Remove user(s) from an organization.
Parameters|Type|Description
-|-|-
`organization`|`string`|organization identification string
`users`|`string`|comma-separated list of user identification strings

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_organization_permission`**
Remove a user permission from an organization.
Parameters|Type|Description
-|-|-
`organization`|`string`|organization identification string
`permission`|`string`|permission level (view / report / control / modify / grant / admin)
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_organization_tag`**
Remove a tag attachment from an organization.
Parameters|Type|Description
-|-|-
`organization`|`string`|organization identification string
`tag`|`string`|tag identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_organization_webhook`**
Remove organizational webhook.
Parameters|Type|Description
-|-|-
`organization`|`string`|organization identification string
`webhook`|`string`|webhook identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_question`**
Permanently delete a Quiz question.
Parameters|Type|Description
-|-|-
`id`|`string`|external unique question identifier

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_quiz`**
Remove/archive Quiz set.
Parameters|Type|Description
-|-|-
`quiz`|`string`|Quiz identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_quiz_permission`**
Remove a user permission from a quiz.
Parameters|Type|Description
-|-|-
`permission`|`string`|permission level (view / report / control / modify / grant / admin)
`quiz`|`string`|Quiz identification string
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_quiz_questions`**
Remove question(s) from a Quiz set, or one of its question group.
Parameters|Type|Description
-|-|-
`questions`|`string`|comma-separated list of question identification strings
`quiz`|`string`|Quiz identification string
`group`|`string` *optional*|question group title

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_quiz_tag`**
Remove a tag attachment from a Quiz.
Parameters|Type|Description
-|-|-
`quiz`|`string`|Quiz identification string
`tag`|`string`|tag identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_scorm_permission`**
Remove a user permission from a SCORM learning material.
Parameters|Type|Description
-|-|-
`permission`|`string`|permission level (view / report / control / modify / grant / admin)
`scorm`|`string`|SCORM identification string
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_scorm_tag`**
Remove a tag attachment from a SCORM learning material.
Parameters|Type|Description
-|-|-
`scorm`|`string`|SCORM identification string
`tag`|`string`|tag identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_tag_permission`**
Remove a user permission from a tag.
Parameters|Type|Description
-|-|-
`permission`|`string`|permission level (view / report / control / modify / grant / admin)
`tag`|`string`|tag identification string
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_user`**
Delete user.
Parameters|Type|Description
-|-|-
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_user_assume`**
Revoke assume token.
Parameters|Type|Description
-|-|-
`token`|`string`|assume token

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`edubase_delete_user_classes`**
Remove user from class(es).
Parameters|Type|Description
-|-|-
`classes`|`string`|comma-separated list of class identification strings
`user`|`string`|user identification string

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same 

[...]

## Screenshots

![EduBase screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/edubase-1.gif)

![EduBase screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/edubase-2.png)

![EduBase screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/edubase-3.jpg)
