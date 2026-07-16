Manage S3 Tables for analytics.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/s3-tables-mcp-server](https://hub.docker.com/repository/docker/mcp/s3-tables-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (16)
Tools provided by this Server|Short Description
-|-
`append_rows_to_table`|Append rows to an Iceberg table using PyIceberg/Daft.|
`create_namespace`|Create a new namespace in an S3 table bucket.|
`create_table`|Create a new S3 table in an S3 table bucket.|
`create_table_bucket`|Creates an S3 table bucket.|
`get_bucket_metadata_config`|Get the metadata table configuration for a regular general purpose S3 bucket.|
`get_maintenance_job_status`|Get the status of a maintenance job for a table.|
`get_table_maintenance_config`|Get details about the maintenance configuration of a table.|
`get_table_metadata_location`|Get the location of the S3 table metadata.|
`import_csv_to_table`|Import data from a CSV file into an S3 table.|
`import_parquet_to_table`|Import data from a Parquet file into an existing S3 table.|
`list_namespaces`|List all namespaces across all S3 table buckets.|
`list_table_buckets`|List all S3 table buckets for your AWS account.|
`list_tables`|List all S3 tables across all table buckets and namespaces.|
`query_database`|Execute SQL queries against S3 Tables using PyIceberg/Daft.|
`rename_table`|Rename an S3 table or move it to a different S3 namespace.|
`update_table_metadata_location`|Update the metadata location for an S3 table.|

---
## Tools Details

#### Tool: **`append_rows_to_table`**
Append rows to an Iceberg table using PyIceberg/Daft.

This tool appends data rows to an existing Iceberg table using the PyIceberg engine.
The rows parameter must be a list of dictionaries, each representing a row.
Check the schema of the table before appending rows.

Example input values:
    warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
    region: 'us-west-2'
    namespace: 'retail_data'
    table_name: 'customers'
    rows: [{"customer_id": 1, "customer_name": "Alice"}, ...]
    uri: 'https://s3tables.us-west-2.amazonaws.com/iceberg'
    catalog_name: 's3tablescatalog'
    rest_signing_name: 's3tables'
    rest_sigv4_enabled: 'true'
Parameters|Type|Description
-|-|-
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`region`|`string`|AWS region for S3Tables/Iceberg REST endpoint
`rows`|`array`|List of rows to append, each as a dict
`table_name`|`string`|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`uri`|`string`|REST URI for Iceberg catalog
`warehouse`|`string`|Warehouse string for Iceberg catalog
`catalog_name`|`string` *optional*|Catalog name
`rest_signing_name`|`string` *optional*|REST signing name
`rest_sigv4_enabled`|`string` *optional*|Enable SigV4 signing

---
#### Tool: **`create_namespace`**
Create a new namespace in an S3 table bucket.

Creates a namespace. A namespace is a logical grouping of tables within your S3 table bucket,
which you can use to organize S3 tables.

Permissions:
You must have the s3tables:CreateNamespace permission to use this operation.
Parameters|Type|Description
-|-|-
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`table_bucket_arn`|`string`|Table bucket ARN
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`create_table`**
Create a new S3 table in an S3 table bucket.

Creates a new S3 table associated with the given S3 namespace in an S3 table bucket.
The S3 table can be configured with specific format and metadata settings. Metadata contains the schema of the table.
Do not use the metadata parameter if the schema is unclear.

Supported Iceberg Primitive Types:
- boolean: True or false
- int: 32-bit signed integers (can promote to long)
- long: 64-bit signed integers
- float: 32-bit IEEE 754 floating point (can promote to double)
- double: 64-bit IEEE 754 floating point
- decimal(P,S): Fixed-point decimal with precision P and scale S (precision must be 38 or less)
- date: Calendar date without timezone or time
- time: Time of day, microsecond precision, without date or timezone
- timestamp: Timestamp, microsecond precision, without timezone (represents date and time regardless of zone)
- timestamptz: Timestamp, microsecond precision, with timezone (stored as UTC)
- string: Arbitrary-length character sequences (UTF-8 encoded)

Note: Binary field types (binary, fixed, uuid) are not supported.

Example of S3 table metadata:
{
    "metadata": {
        "iceberg": {
            "schema": {
                "type": "struct",
                "fields": [
                    {
                        "id": 1,
                        "name": "id",
                        "type": "long",
                        "required": true
                    },
                    {
                        "id": 2,
                        "name": "bool_field",
                        "type": "boolean",
                        "required": false
                    },
                    {
                        "id": 3,
                        "name": "int_field",
                        "type": "int",
                        "required": false
                    },
                    {
                        "id": 4,
                        "name": "long_field",
                        "type": "long",
                        "required": false
                    },
                    {
                        "id": 5,
                        "name": "float_field",
                        "type": "float",
                        "required": false
                    },
                    {
                        "id": 6,
                        "name": "double_field",
                        "type": "double",
                        "required": false
                    },
                    {
                        "id": 7,
                        "name": "decimal_field",
                        "type": "decimal(10,2)",
                        "required": false
                    },
                    {
                        "id": 8,
                        "name": "date_field",
                        "type": "date",
                        "required": false
                    },
                    {
                        "id": 9,
                        "name": "time_field",
                        "type": "time",
                        "required": false
                    },
                    {
                        "id": 10,
                        "name": "timestamp_field",
                        "type": "timestamp",
                        "required": false
                    },
                    {
                        "id": 11,
                        "name": "timestamptz_field",
                        "type": "timestamptz",
                        "required": false
                    },
                    {
                        "id": 12,
                        "name": "string_field",
                        "type": "string",
                        "required": false
                    }
                ]
            },
            "partition-spec": [
                {
                    "source-id": 8,
                    "field-id": 1000,
                    "transform": "month",
                    "name": "date_field_month"
                }
            ],
            "table-properties": {
                "description": "Example table demonstrating supported Iceberg primitive types"
            }
        }
    }
}

Permissions:
You must have the s3tables:CreateTable permission to use this operation.
Parameters|Type|Description
-|-|-
`name`|`string`|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`table_bucket_arn`|`string`|Table bucket ARN
`format`|`string` *optional*|The format for the S3 table.
`metadata`|`string` *optional*|The metadata for the S3 table.
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`create_table_bucket`**
Creates an S3 table bucket.

Permissions:
You must have the s3tables:CreateTableBucket permission to use this operation.
Parameters|Type|Description
-|-|-
`name`|`string`|Name of the table bucket to create. Must be 3-63 characters long and contain only lowercase letters, numbers, and hyphens.
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`get_bucket_metadata_config`**
Get the metadata table configuration for a regular general purpose S3 bucket.

Retrieves the metadata table configuration for a regular general purpose bucket in s3. This configuration
determines how metadata is stored and managed for the bucket.
The response includes:
- S3 Table Bucket ARN
- S3 Table ARN
- S3 Table Name
- S3 Table Namespace

Description:
Amazon S3 Metadata accelerates data discovery by automatically capturing metadata for the objects in your general purpose buckets and storing it in read-only, fully managed Apache Iceberg tables that you can query. These read-only tables are called metadata tables. As objects are added to, updated, and removed from your general purpose buckets, S3 Metadata automatically refreshes the corresponding metadata tables to reflect the latest changes.
By default, S3 Metadata provides three types of metadata:
- System-defined metadata, such as an object's creation time and storage class
- Custom metadata, such as tags and user-defined metadata that was included during object upload
- Event metadata, such as when an object is updated or deleted, and the AWS account that made the request

Metadata table schema:
- bucket: String
- key: String
- sequence_number: String
- record_type: String
- record_timestamp: Timestamp (no time zone)
- version_id: String
- is_delete_marker: Boolean
- size: Long
- last_modified_date: Timestamp (no time zone)
- e_tag: String
- storage_class: String
- is_multipart: Boolean
- encryption_status: String
- is_bucket_key_enabled: Boolean
- kms_key_arn: String
- checksum_algorithm: String
- object_tags: Map<String, String>
- user_metadata: Map<String, String>
- requester: String
- source_ip_address: String
- request_id: String

Permissions:
You must have the s3:GetBucketMetadataConfiguration permission to use this operation.
Parameters|Type|Description
-|-|-
`bucket`|`string`|The name of the S3 bucket to get metadata table configuration for.
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`get_maintenance_job_status`**
Get the status of a maintenance job for a table.

Gets the status of a maintenance job for a table. For more information, see S3 Tables maintenance in the Amazon Simple Storage Service User Guide.

Permissions:
You must have the s3tables:GetTableMaintenanceJobStatus permission to use this operation.
Parameters|Type|Description
-|-|-
`name`|`string`|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`table_bucket_arn`|`string`|Table bucket ARN
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`get_table_maintenance_config`**
Get details about the maintenance configuration of a table.

Gets details about the maintenance configuration of a table. For more information, see S3 Tables maintenance in the Amazon Simple Storage Service User Guide.

Permissions:
You must have the s3tables:GetTableMaintenanceConfiguration permission to use this operation.
Parameters|Type|Description
-|-|-
`name`|`string`|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`table_bucket_arn`|`string`|Table bucket ARN
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`get_table_metadata_location`**
Get the location of the S3 table metadata.

Gets the S3 URI location of the table metadata, which contains the schema and other
table configuration information.

Permissions:
You must have the s3tables:GetTableMetadataLocation permission to use this operation.
Parameters|Type|Description
-|-|-
`name`|`string`|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`table_bucket_arn`|`string`|Table bucket ARN
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`import_csv_to_table`**
Import data from a CSV file into an S3 table.

This tool reads data from a CSV file stored in S3 and imports it into an S3 table.
If the table doesn't exist, it will be created with a schema inferred from the CSV file.
If the table exists, the CSV file schema must be compatible with the table's schema.
The tool will validate the schema before attempting to import the data.
If preserve_case is True, the column names will not be converted to snake_case. Otherwise, the column names will be converted to snake_case.

Returns error dictionary with status and error message if:
    - URL is not a valid S3 URL
    - File is not a CSV file
    - File cannot be accessed
    - Table does not exist
    - CSV headers don't match table schema
    - Any other error occurs

Example input values:
    warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
    region: 'us-west-2'
    namespace: 'retail_data'
    table_name: 'customers'
    s3_url: 's3://bucket-name/path/to/file.csv'
    uri: 'https://s3tables.us-west-2.amazonaws.com/iceberg'
    catalog_name: 's3tablescatalog'
    rest_signing_name: 's3tables'
    rest_sigv4_enabled: 'true'
    preserve_case: False

Permissions:
You must have:
- s3:GetObject permission for the CSV file
- s3tables:GetTable and s3tables:GetTables permissions to access table information
- s3tables:PutTableData permission to write to the table
Parameters|Type|Description
-|-|-
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`region`|`string`|AWS region for S3Tables/Iceberg REST endpoint
`s3_url`|`string`|The S3 URL of the file to preview (format: s3://bucket-name/key)
`table_name`|`string`|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`uri`|`string`|REST URI for Iceberg catalog
`warehouse`|`string`|Warehouse string for Iceberg catalog
`catalog_name`|`string` *optional*|Catalog name
`preserve_case`|`boolean` *optional*|Preserve case of column names
`rest_signing_name`|`string` *optional*|REST signing name
`rest_sigv4_enabled`|`string` *optional*|Enable SigV4 signing

---
#### Tool: **`import_parquet_to_table`**
Import data from a Parquet file into an existing S3 table.

This tool reads data from a Parquet file stored in S3 and imports it into an existing S3 table.
The table must already exist. The Parquet file schema must be compatible with the table's schema.
The tool will validate the schema before attempting to import the data.
If preserve_case is True, the column names will not be converted to snake_case. Otherwise, the column names will be converted to snake_case.

Returns error dictionary with status and error message if:
    - URL is not a valid S3 URL
    - File is not a Parquet file
    - File cannot be accessed
    - Table does not exist
    - Parquet schema is incompatible with existing table schema
    - Any other error occurs

Returns success dictionary with:
    - status: 'success'
    - message: Success message with row count
    - rows_processed: Number of rows imported
    - file_processed: Name of the processed file

Example input values:
    warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
    region: 'us-west-2'
    namespace: 'retail_data'
    table_name: 'customers'
    s3_url: 's3://bucket-name/path/to/file.parquet'
    uri: 'https://s3tables.us-west-2.amazonaws.com/iceberg'
    catalog_name: 's3tablescatalog'
    rest_signing_name: 's3tables'
    rest_sigv4_enabled: 'true'
    preserve_case: False

Permissions:
You must have:
- s3:GetObject permission for the Parquet file
- s3tables:GetTable and s3tables:GetTables permissions to access table information
- s3tables:PutTableData permission to write to the table
Parameters|Type|Description
-|-|-
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`region`|`string`|AWS region for S3Tables/Iceberg REST endpoint
`s3_url`|`string`|The S3 URL of the file to preview (format: s3://bucket-name/key)
`table_name`|`string`|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`uri`|`string`|REST URI for Iceberg catalog
`warehouse`|`string`|Warehouse string for Iceberg catalog
`catalog_name`|`string` *optional*|Catalog name
`preserve_case`|`boolean` *optional*|Preserve case of column names
`rest_signing_name`|`string` *optional*|REST signing name
`rest_sigv4_enabled`|`string` *optional*|Enable SigV4 signing

---
#### Tool: **`list_namespaces`**
List all namespaces across all S3 table buckets.

Permissions:
You must have the s3tables:ListNamespaces permission to use this operation.
Parameters|Type|Description
-|-|-
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`list_table_buckets`**
List all S3 table buckets for your AWS account.

Permissions:
You must have the s3tables:ListTableBuckets permission to use this operation.
Parameters|Type|Description
-|-|-
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`list_tables`**
List all S3 tables across all table buckets and namespaces.

Permissions:
You must have the s3tables:ListTables permission to use this operation.
Parameters|Type|Description
-|-|-
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---
#### Tool: **`query_database`**
Execute SQL queries against S3 Tables using PyIceberg/Daft.

This tool provides a secure interface to run read-only SQL queries against your S3 Tables data using the PyIceberg and Daft engine.
Use a correct region for warehouse, region, and uri.

Example input values:
    warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
    region: 'us-west-2'
    namespace: 'retail_data'
    query: 'SELECT * FROM customers LIMIT 10'
    uri: 'https://s3tables.us-west-2.amazonaws.com/iceberg'
    catalog_name: 's3tablescatalog'
    rest_signing_name: 's3tables'
    rest_sigv4_enabled: 'true'
Parameters|Type|Description
-|-|-
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`region`|`string`|AWS region for S3Tables/Iceberg REST endpoint
`uri`|`string`|REST URI for Iceberg catalog
`warehouse`|`string`|Warehouse string for Iceberg catalog
`catalog_name`|`string` *optional*|Catalog name
`query`|`string` *optional*|Optional SQL query. If not provided, will execute SELECT * FROM table. Must be a read operation.
`rest_signing_name`|`string` *optional*|REST signing name
`rest_sigv4_enabled`|`string` *optional*|Enable SigV4 signing

---
#### Tool: **`rename_table`**
Rename an S3 table or move it to a different S3 namespace.

Renames an S3 table or moves it to a different S3 namespace within the same S3 table bucket.
This operation maintains the table's data and configuration while updating its location.

Permissions:
You must have the s3tables:RenameTable permission to use this operation.
Parameters|Type|Description
-|-|-
`name`|`string`|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`table_bucket_arn`|`string`|Table bucket ARN
`new_name`|`string` *optional*|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`new_namespace_name`|`string` *optional*|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.
`version_token`|`string` *optional*|The version token of the S3 table. Must be 1-2048 characters long.

---
#### Tool: **`update_table_metadata_location`**
Update the metadata location for an S3 table.

Updates the metadata location for an S3 table. The metadata location of an S3 table must be an S3 URI that begins with the S3 table's warehouse location.
The metadata location for an Apache Iceberg S3 table must end with .metadata.json, or if the metadata file is Gzip-compressed, .metadata.json.gz.

Permissions:
You must have the s3tables:UpdateTableMetadataLocation permission to use this operation.
Parameters|Type|Description
-|-|-
`metadata_location`|`string`|The new metadata location for the S3 table. Must be 1-2048 characters long.
`name`|`string`|The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`namespace`|`string`|The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens.
`table_bucket_arn`|`string`|Table bucket ARN
`version_token`|`string`|The version token of the S3 table. Must be 1-2048 characters long.
`region_name`|`string` *optional*|The AWS region name where the operation should be performed.

---

## Screenshots

![AWS S3 Tables screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-s3-tables-1.png)

![AWS S3 Tables screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-s3-tables-2.png)

![AWS S3 Tables screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-s3-tables-3.png)
