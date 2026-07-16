CloudFormation resource management via Cloud Control API.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/cfn-mcp-server](https://hub.docker.com/repository/docker/mcp/cfn-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`create_resource`|Create an AWS resource.|
`create_template`|Create a CloudFormation template from existing resources using the IaC Generator API.|
`delete_resource`|Delete an AWS resource.|
`get_resource`|Get details of a specific AWS resource.|
`get_resource_request_status`|Get the status of a long running operation with the request token.|
`get_resource_schema_information`|Get schema information for an AWS resource.|
`list_resources`|List AWS resources of a specified type.|
`update_resource`|Update an AWS resource.|

---
## Tools Details

#### Tool: **`create_resource`**
Create an AWS resource.

Parameters:
    resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
    properties: A dictionary of properties for the resource
    region: AWS region to use (e.g., "us-east-1", "us-west-2")

Returns:
    Information about the created resource with a consistent structure:
    {
        "status": Status of the operation ("SUCCESS", "PENDING", "FAILED", etc.)
        "resource_type": The AWS resource type
        "identifier": The resource identifier
        "is_complete": Boolean indicating whether the operation is complete
        "status_message": Human-readable message describing the result
        "request_token": A token that allows you to track long running operations via the get_resource_request_status tool
        "resource_info": Optional information about the resource properties
    }
Parameters|Type|Description
-|-|-
`properties`|`object`|A dictionary of properties for the resource
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`create_template`**
Create a CloudFormation template from existing resources using the IaC Generator API.

This tool allows you to generate CloudFormation templates from existing AWS resources
that are not already managed by CloudFormation. The template generation process is
asynchronous, so you can check the status of the process and retrieve the template
once it's complete. You can pass up to 500 resources at a time.

Examples:
1. Start template generation for an S3 bucket:
   create_template(
       template_name="my-template",
       resources=[{"ResourceType": "AWS::S3::Bucket", "ResourceIdentifier": {"BucketName": "my-bucket"}}],
       deletion_policy="RETAIN",
       update_replace_policy="RETAIN"
   )

2. Check status of template generation:
   create_template(template_id="arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/abcdef12-3456-7890-abcd-ef1234567890")

3. Retrieve and save generated template:
   create_template(
       template_id="arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/abcdef12-3456-7890-abcd-ef1234567890",
       save_to_file="/path/to/template.yaml",
       output_format="YAML"
   )
Parameters|Type|Description
-|-|-
`deletion_policy`|`string` *optional*|Default DeletionPolicy for resources in the template (RETAIN, DELETE, or SNAPSHOT)
`output_format`|`string` *optional*|Output format for the template (JSON or YAML)
`region`|`string` *optional*|The AWS region that the operation should be performed in
`resources`|`string` *optional*|List of resources to include in the template, each with 'ResourceType' and 'ResourceIdentifier'
`save_to_file`|`string` *optional*|Path to save the generated template to a file
`template_id`|`string` *optional*|ID of an existing template generation process to check status or retrieve template
`template_name`|`string` *optional*|Name for the generated template
`update_replace_policy`|`string` *optional*|Default UpdateReplacePolicy for resources in the template (RETAIN, DELETE, or SNAPSHOT)

---
#### Tool: **`delete_resource`**
Delete an AWS resource.

Parameters:
    resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
    identifier: The primary identifier of the resource to delete (e.g., bucket name for S3 buckets)
    region: AWS region to use (e.g., "us-east-1", "us-west-2")

Returns:
    Information about the deletion operation with a consistent structure:
    {
        "status": Status of the operation ("SUCCESS", "PENDING", "FAILED", "NOT_FOUND", etc.)
        "resource_type": The AWS resource type
        "identifier": The resource identifier
        "is_complete": Boolean indicating whether the operation is complete
        "status_message": Human-readable message describing the result
        "request_token": A token that allows you to track long running operations via the get_resource_request_status tool
    }
Parameters|Type|Description
-|-|-
`identifier`|`string`|The primary identifier of the resource to get (e.g., bucket name for S3 buckets)
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`get_resource`**
Get details of a specific AWS resource.

Parameters:
    resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
    identifier: The primary identifier of the resource to get (e.g., bucket name for S3 buckets)
    region: AWS region to use (e.g., "us-east-1", "us-west-2")

Returns:
    Detailed information about the specified resource with a consistent structure:
    {
        "identifier": The resource identifier,
        "properties": The detailed information about the resource
    }
Parameters|Type|Description
-|-|-
`identifier`|`string`|The primary identifier of the resource to get (e.g., bucket name for S3 buckets)
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`get_resource_request_status`**
Get the status of a long running operation with the request token.
Parameters|Type|Description
-|-|-
`request_token`|`string`|The request_token returned from the long running operation
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`get_resource_schema_information`**
Get schema information for an AWS resource.

Parameters:
    resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")

Returns:
    The resource schema information
Parameters|Type|Description
-|-|-
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`list_resources`**
List AWS resources of a specified type.

Parameters:
    resource_type: The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
    region: AWS region to use (e.g., "us-east-1", "us-west-2")

Returns:
    A list of resource identifiers
Parameters|Type|Description
-|-|-
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`region`|`string` *optional*|The AWS region that the operation should be performed in

---
#### Tool: **`update_resource`**
Update an AWS resource.

Parameters:
    resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
    identifier: The primary identifier of the resource to update
    patch_document: A list of RFC 6902 JSON Patch operations to apply
    region: AWS region to use (e.g., "us-east-1", "us-west-2")

Returns:
    Information about the updated resource with a consistent structure:
    {
        "status": Status of the operation ("SUCCESS", "PENDING", "FAILED", etc.)
        "resource_type": The AWS resource type
        "identifier": The resource identifier
        "is_complete": Boolean indicating whether the operation is complete
        "status_message": Human-readable message describing the result
        "request_token": A token that allows you to track long running operations via the get_resource_request_status tool
        "resource_info": Optional information about the resource properties
    }
Parameters|Type|Description
-|-|-
`identifier`|`string`|The primary identifier of the resource to get (e.g., bucket name for S3 buckets)
`resource_type`|`string`|The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
`patch_document`|`array` *optional*|A list of RFC 6902 JSON Patch operations to apply
`region`|`string` *optional*|The AWS region that the operation should be performed in

---

## Screenshots

![AWS CloudFormation screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cfn-1.png)

![AWS CloudFormation screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cfn-2.png)

![AWS CloudFormation screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-cfn-3.png)
