High-speed caching with Memcached.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/memcached-mcp-server](https://hub.docker.com/repository/docker/mcp/memcached-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (22)
Tools provided by this Server|Short Description
-|-
`cache_add`|Add a value to the cache only if the key doesn't exist.|
`cache_append`|Append a string to an existing value.|
`cache_cas`|Set a value using CAS (Check And Set).|
`cache_decr`|Decrement a counter in the cache.|
`cache_delete`|Delete a value from the cache.|
`cache_delete_many`|Delete multiple values from the cache.|
`cache_delete_multi`|Delete multiple values from the cache (alias for delete_many).|
`cache_flush_all`|Flush all cache entries.|
`cache_get`|Get a value from the cache.|
`cache_get_many`|Get multiple values from the cache.|
`cache_get_multi`|Get multiple values from the cache (alias for get_many).|
`cache_gets`|Get a value and its CAS token from the cache.|
`cache_incr`|Increment a counter in the cache.|
`cache_prepend`|Prepend a string to an existing value.|
`cache_quit`|Close the connection to the cache server.|
`cache_replace`|Replace a value in the cache only if the key exists.|
`cache_set`|Set a value in the cache.|
`cache_set_many`|Set multiple values in the cache.|
`cache_set_multi`|Set multiple values in the cache (alias for set_many).|
`cache_stats`|Get cache statistics.|
`cache_touch`|Update the expiration time for a key.|
`cache_version`|Get the version of the cache server.|

---
## Tools Details

#### Tool: **`cache_add`**
Add a value to the cache only if the key doesn't exist.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to add
`value`|`string`|The value to store
`expire`|`string` *optional*|Optional expiration time in seconds

---
#### Tool: **`cache_append`**
Append a string to an existing value.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to append to
`value`|`string`|String to append

---
#### Tool: **`cache_cas`**
Set a value using CAS (Check And Set).
Parameters|Type|Description
-|-|-
`cas`|`integer`|CAS token from gets()
`key`|`string`|The key to set
`value`|`string`|The value to store
`expire`|`string` *optional*|Optional expiration time in seconds

---
#### Tool: **`cache_decr`**
Decrement a counter in the cache.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to decrement
`value`|`integer` *optional*|Amount to decrement by (default 1)

---
#### Tool: **`cache_delete`**
Delete a value from the cache.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to delete

---
#### Tool: **`cache_delete_many`**
Delete multiple values from the cache.
Parameters|Type|Description
-|-|-
`keys`|`array`|List of keys to delete

---
#### Tool: **`cache_delete_multi`**
Delete multiple values from the cache (alias for delete_many).
Parameters|Type|Description
-|-|-
`keys`|`array`|List of keys to delete

---
#### Tool: **`cache_flush_all`**
Flush all cache entries.
Parameters|Type|Description
-|-|-
`delay`|`integer` *optional*|Optional delay in seconds before flushing

---
#### Tool: **`cache_get`**
Get a value from the cache.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to retrieve

---
#### Tool: **`cache_get_many`**
Get multiple values from the cache.
Parameters|Type|Description
-|-|-
`keys`|`array`|List of keys to retrieve

---
#### Tool: **`cache_get_multi`**
Get multiple values from the cache (alias for get_many).
Parameters|Type|Description
-|-|-
`keys`|`array`|List of keys to retrieve

---
#### Tool: **`cache_gets`**
Get a value and its CAS token from the cache.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to retrieve

---
#### Tool: **`cache_incr`**
Increment a counter in the cache.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to increment
`value`|`integer` *optional*|Amount to increment by (default 1)

---
#### Tool: **`cache_prepend`**
Prepend a string to an existing value.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to prepend to
`value`|`string`|String to prepend

---
#### Tool: **`cache_quit`**
Close the connection to the cache server.

Returns:
    Success message or error message
#### Tool: **`cache_replace`**
Replace a value in the cache only if the key exists.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to replace
`value`|`string`|The new value
`expire`|`string` *optional*|Optional expiration time in seconds

---
#### Tool: **`cache_set`**
Set a value in the cache.
Parameters|Type|Description
-|-|-
`key`|`string`|The key to set
`value`|`string`|The value to store
`expire`|`string` *optional*|Optional expiration time in seconds

---
#### Tool: **`cache_set_many`**
Set multiple values in the cache.
Parameters|Type|Description
-|-|-
`mapping`|`object`|Dictionary of key-value pairs
`expire`|`string` *optional*|Optional expiration time in seconds

---
#### Tool: **`cache_set_multi`**
Set multiple values in the cache (alias for set_many).
Parameters|Type|Description
-|-|-
`mapping`|`object`|Dictionary of key-value pairs
`expire`|`string` *optional*|Optional expiration time in seconds

---
#### Tool: **`cache_stats`**
Get cache statistics.
Parameters|Type|Description
-|-|-
`args`|`string` *optional*|Args:

---
#### Tool: **`cache_touch`**
Update the expiration time for a key.
Parameters|Type|Description
-|-|-
`expire`|`integer`|New expiration time in seconds
`key`|`string`|The key to update

---
#### Tool: **`cache_version`**
Get the version of the cache server.

Returns:
    Version string or error message

## Screenshots

![Amazon ElastiCache for Memcached screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-memcached-1.png)

![Amazon ElastiCache for Memcached screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-memcached-2.png)

![Amazon ElastiCache for Memcached screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-memcached-3.png)
