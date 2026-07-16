IAM user, role, group, and policy management.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/iam-mcp-server](https://hub.docker.com/repository/docker/mcp/iam-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (29)
Tools provided by this Server|Short Description
-|-
`add_user_to_group`|Add a user to an IAM group.|
`attach_group_policy`|Attach a managed policy to an IAM group.|
`attach_user_policy`|Attach a managed policy to an IAM user.|
`create_access_key`|Create a new access key for an IAM user.|
`create_group`|Create a new IAM group.|
`create_role`|Create a new IAM role.|
`create_user`|Create a new IAM user.|
`delete_access_key`|Delete an access key for an IAM user.|
`delete_group`|Delete an IAM group.|
`delete_role_policy`|Delete an inline policy from an IAM role.|
`delete_user`|Delete an IAM user.|
`delete_user_policy`|Delete an inline policy from an IAM user.|
`detach_group_policy`|Detach a managed policy from an IAM group.|
`detach_user_policy`|Detach a managed policy from an IAM user.|
`get_group`|Get detailed information about a specific IAM group.|
`get_managed_policy_document`|Retrieve the policy document for a managed policy.|
`get_role_policy`|Retrieve an inline policy for an IAM role.|
`get_user`|Get detailed information about a specific IAM user.|
`get_user_policy`|Retrieve an inline policy for an IAM user.|
`list_groups`|List IAM groups in the account.|
`list_policies`|List IAM policies in the account.|
`list_role_policies`|List all inline policies for an IAM role.|
`list_roles`|List IAM roles in the account.|
`list_user_policies`|List all inline policies for an IAM user.|
`list_users`|List IAM users in the account.|
`put_role_policy`|Create or update an inline policy for an IAM role.|
`put_user_policy`|Create or update an inline policy for an IAM user.|
`remove_user_from_group`|Remove a user from an IAM group.|
`simulate_principal_policy`|Simulate IAM policy evaluation for a principal.|

---
## Tools Details

#### Tool: **`add_user_to_group`**
Add a user to an IAM group.
Parameters|Type|Description
-|-|-
`group_name`|`string`|The name of the IAM group
`user_name`|`string`|The name of the IAM user
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`attach_group_policy`**
Attach a managed policy to an IAM group.
Parameters|Type|Description
-|-|-
`group_name`|`string`|The name of the IAM group
`policy_arn`|`string`|The ARN of the policy to attach
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`attach_user_policy`**
Attach a managed policy to an IAM user.
Parameters|Type|Description
-|-|-
`policy_arn`|`string`|The ARN of the policy to attach
`user_name`|`string`|The name of the IAM user
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`create_access_key`**
Create a new access key for an IAM user.
Parameters|Type|Description
-|-|-
`user_name`|`string`|The name of the IAM user
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`create_group`**
Create a new IAM group.

This tool creates a new IAM group in your AWS account. The group will be created
without any permissions by default - you'll need to attach policies separately.

## Security Best Practices:
- Use descriptive group names that indicate the group's purpose
- Set appropriate paths for organizational structure
- Follow the principle of least privilege when assigning permissions later
Parameters|Type|Description
-|-|-
`group_name`|`string`|The name of the new IAM group
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation
`path`|`string` *optional*|The path for the group

---
#### Tool: **`create_role`**
Create a new IAM role.
Parameters|Type|Description
-|-|-
`assume_role_policy_document`|`string`|The trust policy document in JSON format (string or dict)
`role_name`|`string`|The name of the new IAM role
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation
`description`|`string` *optional*|Description of the role
`max_session_duration`|`integer` *optional*|Maximum session duration in seconds (3600-43200)
`path`|`string` *optional*|The path for the role
`permissions_boundary`|`string` *optional*|ARN of the permissions boundary policy

---
#### Tool: **`create_user`**
Create a new IAM user.

This tool creates a new IAM user in your AWS account. The user will be created
without any permissions by default - you'll need to attach policies separately.

## Security Best Practices:
- Use descriptive user names that indicate the user's role or purpose
- Set appropriate paths for organizational structure
- Consider using permissions boundaries to limit maximum permissions
- Follow the principle of least privilege when assigning permissions later
Parameters|Type|Description
-|-|-
`ctx`|`string`|MCP context for error reporting
`user_name`|`string`|The name of the new IAM user
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation
`path`|`string` *optional*|The path for the user
`permissions_boundary`|`string` *optional*|ARN of the permissions boundary policy

---
#### Tool: **`delete_access_key`**
Delete an access key for an IAM user.
Parameters|Type|Description
-|-|-
`access_key_id`|`string`|The access key ID to delete
`user_name`|`string`|The name of the IAM user
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`delete_group`**
Delete an IAM group.
Parameters|Type|Description
-|-|-
`group_name`|`string`|The name of the IAM group to delete
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation
`force`|`boolean` *optional*|Force delete by removing all members and policies first

---
#### Tool: **`delete_role_policy`**
Delete an inline policy from an IAM role.

This tool removes an inline policy from the specified role. The policy document
will be permanently deleted and cannot be recovered.
Parameters|Type|Description
-|-|-
`policy_name`|`string`|The name of the inline policy to delete
`role_name`|`string`|The name of the IAM role
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`delete_user`**
Delete an IAM user.
Parameters|Type|Description
-|-|-
`user_name`|`string`|The name of the IAM user to delete
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation
`force`|`boolean` *optional*|Force delete user by removing all attached policies, groups, and access keys first

---
#### Tool: **`delete_user_policy`**
Delete an inline policy from an IAM user.

This tool removes an inline policy from the specified user. The policy document
will be permanently deleted and cannot be recovered.
Parameters|Type|Description
-|-|-
`policy_name`|`string`|The name of the inline policy to delete
`user_name`|`string`|The name of the IAM user
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`detach_group_policy`**
Detach a managed policy from an IAM group.
Parameters|Type|Description
-|-|-
`group_name`|`string`|The name of the IAM group
`policy_arn`|`string`|The ARN of the policy to detach
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`detach_user_policy`**
Detach a managed policy from an IAM user.
Parameters|Type|Description
-|-|-
`policy_arn`|`string`|The ARN of the policy to detach
`user_name`|`string`|The name of the IAM user
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`get_group`**
Get detailed information about a specific IAM group.

This tool retrieves comprehensive information about an IAM group including
group members, attached policies, and inline policies. Use this to get
a complete picture of a group's configuration and membership.

## Usage Tips:
- Use this after list_groups to get detailed information about specific groups
- Review attached policies to understand group permissions
- Check group members to see who has these permissions
Parameters|Type|Description
-|-|-
`group_name`|`string`|The name of the IAM group to retrieve

---
#### Tool: **`get_managed_policy_document`**
Retrieve the policy document for a managed policy.

This tool retrieves the policy document for a specific managed policy version.
Use this to examine the actual permissions and wildcards in managed policies.
Parameters|Type|Description
-|-|-
`policy_arn`|`string`|The ARN of the managed policy
`version_id`|`string` *optional*|The version ID of the policy (defaults to current version)

---
#### Tool: **`get_role_policy`**
Retrieve an inline policy for an IAM role.

This tool retrieves the policy document for a specific inline policy attached to a role.
Parameters|Type|Description
-|-|-
`policy_name`|`string`|The name of the inline policy
`role_name`|`string`|The name of the IAM role

---
#### Tool: **`get_user`**
Get detailed information about a specific IAM user.

This tool retrieves comprehensive information about an IAM user including
attached policies, group memberships, and access keys. Use this to get
a complete picture of a user's permissions and configuration.

## Usage Tips:
- Use this after list_users to get detailed information about specific users
- Review attached policies to understand user permissions
- Check access keys to identify potential security issues
Parameters|Type|Description
-|-|-
`ctx`|`string`|MCP context for error reporting
`user_name`|`string`|The name of the IAM user to retrieve

---
#### Tool: **`get_user_policy`**
Retrieve an inline policy for an IAM user.

This tool retrieves the policy document for a specific inline policy attached to a user.
Parameters|Type|Description
-|-|-
`policy_name`|`string`|The name of the inline policy
`user_name`|`string`|The name of the IAM user

---
#### Tool: **`list_groups`**
List IAM groups in the account.

This tool retrieves a list of IAM groups from your AWS account with optional filtering.
Use this to get an overview of all groups or find specific groups by path prefix.

## Usage Tips:
- Use path_prefix to filter groups by organizational structure
- Adjust max_items to control response size for large accounts
- Results may be paginated for accounts with many groups
Parameters|Type|Description
-|-|-
`max_items`|`integer` *optional*|Maximum number of groups to return
`path_prefix`|`string` *optional*|Path prefix to filter groups (e.g., "/division_abc/")

---
#### Tool: **`list_policies`**
List IAM policies in the account.
Parameters|Type|Description
-|-|-
`max_items`|`integer` *optional*|Maximum number of policies to return
`only_attached`|`boolean` *optional*|Only return policies that are attached to a user, group, or role
`path_prefix`|`string` *optional*|Path prefix to filter policies
`scope`|`string` *optional*|Scope of policies to list: "All", "AWS", or "Local"

---
#### Tool: **`list_role_policies`**
List all inline policies for an IAM role.

This tool retrieves the names of all inline policies attached to the specified role.
Parameters|Type|Description
-|-|-
`role_name`|`string`|The name of the IAM role

---
#### Tool: **`list_roles`**
List IAM roles in the account.
Parameters|Type|Description
-|-|-
`max_items`|`integer` *optional*|Maximum number of roles to return
`path_prefix`|`string` *optional*|Path prefix to filter roles (e.g., "/service-role/")

---
#### Tool: **`list_user_policies`**
List all inline policies for an IAM user.

This tool retrieves the names of all inline policies attached to the specified user.
Parameters|Type|Description
-|-|-
`user_name`|`string`|The name of the IAM user

---
#### Tool: **`list_users`**
List IAM users in the account.

This tool retrieves a list of IAM users from your AWS account with optional filtering.
Use this to get an overview of all users or find specific users by path prefix.

## Usage Tips:
- Use path_prefix to filter users by organizational structure
- Adjust max_items to control response size for large accounts
- Results may be paginated for accounts with many users
Parameters|Type|Description
-|-|-
`ctx`|`string`|MCP context for error reporting
`max_items`|`integer` *optional*|Maximum number of users to return
`path_prefix`|`string` *optional*|Path prefix to filter users (e.g., "/division_abc/")

---
#### Tool: **`put_role_policy`**
Create or update an inline policy for an IAM role.

This tool creates a new inline policy or updates an existing one for the specified role.
Inline policies are directly embedded in a single user, role, or group and have a one-to-one
relationship with the identity.
Parameters|Type|Description
-|-|-
`policy_document`|`string`|The policy document in JSON format (string or dict)
`policy_name`|`string`|The name of the inline policy
`role_name`|`string`|The name of the IAM role
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`put_user_policy`**
Create or update an inline policy for an IAM user.

This tool creates a new inline policy or updates an existing one for the specified user.
Inline policies are directly embedded in a single user, role, or group and have a one-to-one
relationship with the identity.

## Security Best Practices:
- Follow the principle of least privilege when creating policies
- Use managed policies for common permissions that can be reused
- Regularly review and audit inline policies
- Test policies using simulate_principal_policy before applying
Parameters|Type|Description
-|-|-
`policy_document`|`string`|The policy document in JSON format (string or dict)
`policy_name`|`string`|The name of the inline policy
`user_name`|`string`|The name of the IAM user
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`remove_user_from_group`**
Remove a user from an IAM group.
Parameters|Type|Description
-|-|-
`group_name`|`string`|The name of the IAM group
`user_name`|`string`|The name of the IAM user
`confirmed`|`boolean` *optional*|Must be true to confirm this write operation

---
#### Tool: **`simulate_principal_policy`**
Simulate IAM policy evaluation for a principal.
Parameters|Type|Description
-|-|-
`action_names`|`array`|List of actions to simulate
`policy_source_arn`|`string`|ARN of the user or role to simulate
`context_entries`|`string` *optional*|Context entries for the simulation
`resource_arns`|`string` *optional*|List of resource ARNs to test against

---

## Screenshots

![AWS IAM screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-iam-1.png)

![AWS IAM screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-iam-2.png)

![AWS IAM screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-iam-3.png)
