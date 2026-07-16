Tigris is a globally distributed S3-compatible object storage service that provides low latency anywhere in the world, enabling developers to store and access any amount of data for a wide range of use cases.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/tigris](https://hub.docker.com/repository/docker/mcp/tigris)
**Author**|[tigrisdata](https://github.com/tigrisdata)
**Repository**|https://github.com/tigrisdata/tigris-mcp-server

## Available Tools (10)
Tools provided by this Server|Short Description
-|-
`tigris_create_bucket`|Create a Tigris bucket in your account|
`tigris_delete_bucket`|Delete a Tigris bucket in your account|
`tigris_delete_object`|Delete an object in a bucket|
`tigris_get_object`|Get an object in a bucket|
`tigris_get_signed_url_object`|Get an signed url of an object from a bucket|
`tigris_list_buckets`|List all Tigris buckets in your account|
`tigris_list_objects`|List all objects in a buckets|
`tigris_put_object`|Creates an object in bucket|
`tigris_put_object_from_path`|Creates an object in bucket from a path on the filesystem|
`tigris_upload_file_and_get_url`|Upload a file and get a public url for it|

---
## Tools Details

#### Tool: **`tigris_create_bucket`**
Create a Tigris bucket in your account
Parameters|Type|Description
-|-|-
`bucketName`|`string`|Name of the bucket to create
`isPublic`|`boolean` *optional*|Set your bucket as public or private

---
#### Tool: **`tigris_delete_bucket`**
Delete a Tigris bucket in your account
Parameters|Type|Description
-|-|-
`bucketName`|`string`|Name of the bucket to delete

---
#### Tool: **`tigris_delete_object`**
Delete an object in a bucket
Parameters|Type|Description
-|-|-
`bucketName`|`string`|Name of the bucket
`key`|`string`|Key of the object to put

---
#### Tool: **`tigris_get_object`**
Get an object in a bucket
Parameters|Type|Description
-|-|-
`bucketName`|`string`|Name of the bucket
`key`|`string`|Key of the object to delete

---
#### Tool: **`tigris_get_signed_url_object`**
Get an signed url of an object from a bucket
Parameters|Type|Description
-|-|-
`bucketName`|`string`|Name of the bucket
`key`|`string`|Key of the object to get signed url
`expiresIn`|`number` *optional*|Expiration time in seconds

---
#### Tool: **`tigris_list_buckets`**
List all Tigris buckets in your account
#### Tool: **`tigris_list_objects`**
List all objects in a buckets
Parameters|Type|Description
-|-|-
`bucketName`|`string`|Name of the bucket

---
#### Tool: **`tigris_put_object`**
Creates an object in bucket
Parameters|Type|Description
-|-|-
`bucketName`|`string`|Name of the bucket
`content`|`string`|Content to store in the object
`key`|`string`|Key of the object to put
`contentType`|`string` *optional*|Optional MIME type of the content

---
#### Tool: **`tigris_put_object_from_path`**
Creates an object in bucket from a path on the filesystem
Parameters|Type|Description
-|-|-
`bucketName`|`string`|Name of the bucket
`key`|`string`|Key of the object to put
`path`|`string`|Absolute path to the file to upload

---
#### Tool: **`tigris_upload_file_and_get_url`**
Upload a file and get a public url for it
Parameters|Type|Description
-|-|-
`bucketName`|`string`|Name of the bucket
`expiresIn`|`number`|Expiration time in seconds
`key`|`string`|Key of the object to upload
`path`|`string`|Absolute path to the file to upload

---
