Advanced data structures with Valkey.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/valkey-mcp-server](https://hub.docker.com/repository/docker/mcp/valkey-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (105)
Tools provided by this Server|Short Description
-|-
`bitmap_count`|Count the number of set bits (1) in a range.|
`bitmap_get`|Get the bit value at offset.|
`bitmap_pos`|Find positions of bits set to a specific value.|
`bitmap_set`|Set the bit at offset to value.|
`client_list`|Get a list of connected clients to the Valkey server.|
`dbsize`|Get the number of keys stored in the Valkey database.|
`delete`|Delete a Valkey key.|
`expire`|Set an expiration time for a Redis key.|
`hash_exists`|Check if field exists in hash.|
`hash_get`|Get field from hash.|
`hash_get_all`|Get all fields and values from hash.|
`hash_increment`|Increment field value in hash.|
`hash_keys`|Get all field names from hash.|
`hash_length`|Get number of fields in hash.|
`hash_random_field`|Get random field(s) from hash.|
`hash_random_field_with_values`|Get random field(s) with their values from hash.|
`hash_set`|Set field in hash.|
`hash_set_if_not_exists`|Set field in hash only if it does not exist.|
`hash_set_multiple`|Set multiple fields in hash.|
`hash_strlen`|Get length of field value in hash.|
`hash_values`|Get all values from hash.|
`hll_add`|Add one element to a HyperLogLog.|
`hll_count`|Get the estimated cardinality of a HyperLogLog.|
`info`|Get Valkey server information and statistics.|
`json_arrappend`|Append values to the array at path.|
`json_arrindex`|Get the index of value in array at path.|
`json_arrlen`|Get the length of array at path.|
`json_arrpop`|Pop a value from the array at path and index.|
`json_arrtrim`|Trim array at path to include only elements within range.|
`json_clear`|Clear container at path (array or object).|
`json_del`|Delete value at path.|
`json_get`|Get the JSON value at path.|
`json_numincrby`|Increment the number at path by value.|
`json_nummultby`|Multiply the number at path by value.|
`json_objkeys`|Get the keys in the object at path.|
`json_objlen`|Get the number of keys in the object at path.|
`json_set`|Set the JSON value at path.|
`json_strappend`|Append a string to the string at path.|
`json_strlen`|Get the length of string at path.|
`json_toggle`|Toggle boolean value at path.|
`json_type`|Get the type of JSON value at path.|
`list_append`|Append value to list.|
`list_append_multiple`|Append multiple values to list.|
`list_get`|Get value at index from list.|
`list_insert_after`|Insert value after pivot in list.|
`list_insert_before`|Insert value before pivot in list.|
`list_length`|Get length of list.|
`list_move`|Move element from one list to another.|
`list_pop_left`|Pop value(s) from left of list.|
`list_pop_right`|Pop value(s) from right of list.|
`list_position`|Find position(s) of value in list.|
`list_prepend`|Prepend value to list.|
`list_prepend_multiple`|Prepend multiple values to list.|
`list_range`|Get range of values from list.|
`list_remove`|Remove occurrences of value from list.|
`list_set`|Set value at index in list.|
`list_trim`|Trim list to specified range.|
`rename`|Renames a Redis key from old_key to new_key.|
`set_add`|Add member to set.|
`set_cardinality`|Get number of members in set.|
`set_contains`|Check if member exists in set.|
`set_members`|Get all members in set.|
`set_move`|Move member from one set to another.|
`set_pop`|Remove and return random member(s) from set.|
`set_random_member`|Get random member(s) from set without removing.|
`set_remove`|Remove member from set.|
`sorted_set_add`|Add member-score pairs to sorted set.|
`sorted_set_add_incr`|Add member to sorted set or increment its score.|
`sorted_set_cardinality`|Get number of members in sorted set.|
`sorted_set_popmax`|Remove and return members with highest scores.|
`sorted_set_popmin`|Remove and return members with lowest scores.|
`sorted_set_range`|Get range of members from sorted set.|
`sorted_set_range_by_lex`|Get range of members by lexicographical order.|
`sorted_set_range_by_score`|Get range of members by score.|
`sorted_set_rank`|Get rank of member in sorted set.|
`sorted_set_remove`|Remove member(s) from sorted set.|
`sorted_set_remove_by_lex`|Remove members by lexicographical range.|
`sorted_set_remove_by_rank`|Remove members by rank range.|
`sorted_set_remove_by_score`|Remove members by score range.|
`sorted_set_score`|Get score of member in sorted set.|
`stream_add`|Add entry to stream.|
`stream_delete`|Delete entries from stream.|
`stream_group_create`|Create consumer group.|
`stream_group_delete_consumer`|Delete consumer from group.|
`stream_group_destroy`|Destroy consumer group.|
`stream_group_set_id`|Set consumer group's last delivered ID.|
`stream_info`|Get information about stream.|
`stream_info_consumers`|Get information about consumers in group.|
`stream_info_groups`|Get information about consumer groups.|
`stream_length`|Get length of stream.|
`stream_range`|Get range of entries from stream.|
`stream_read`|Read entries from stream.|
`stream_read_group`|Read entries from stream as part of consumer group.|
`stream_trim`|Trim stream to specified length.|
`string_append`|Append to string value.|
`string_decrement`|Decrement integer value.|
`string_get`|Get string value.|
`string_get_range`|Get substring.|
`string_get_set`|Set new value and return old value.|
`string_increment`|Increment integer value.|
`string_increment_float`|Increment float value.|
`string_length`|Get string length.|
`string_set`|Set string value.|
`string_set_range`|Overwrite part of string.|
`type`|Returns the string representation of the type of the value stored at key.|

---
## Tools Details

#### Tool: **`bitmap_count`**
Count the number of set bits (1) in a range.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the bitmap key
`end`|`string` *optional*|End offset (inclusive, optional)
`start`|`string` *optional*|Start offset (inclusive, optional)

---
#### Tool: **`bitmap_get`**
Get the bit value at offset.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the bitmap key
`offset`|`integer`|The bit offset (0-based)

---
#### Tool: **`bitmap_pos`**
Find positions of bits set to a specific value.
Parameters|Type|Description
-|-|-
`bit`|`integer`|Bit value to search for (0 or 1)
`key`|`string`|The name of the bitmap key
`count`|`string` *optional*|Maximum number of positions to return (optional)
`end`|`string` *optional*|End offset (inclusive, optional)
`start`|`string` *optional*|Start offset (inclusive, optional)

---
#### Tool: **`bitmap_set`**
Set the bit at offset to value.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the bitmap key
`offset`|`integer`|The bit offset (0-based)
`value`|`integer`|The bit value (0 or 1)

---
#### Tool: **`client_list`**
Get a list of connected clients to the Valkey server.
#### Tool: **`dbsize`**
Get the number of keys stored in the Valkey database.
#### Tool: **`delete`**
Delete a Valkey key.
Parameters|Type|Description
-|-|-
`key`|`string`|

---
#### Tool: **`expire`**
Set an expiration time for a Redis key.
Parameters|Type|Description
-|-|-
`expire_seconds`|`integer`|Time in seconds after which the key should expire.
`name`|`string`|The Redis key.

---
#### Tool: **`hash_exists`**
Check if field exists in hash.
Parameters|Type|Description
-|-|-
`field`|`string`|The field name
`key`|`string`|The name of the key

---
#### Tool: **`hash_get`**
Get field from hash.
Parameters|Type|Description
-|-|-
`field`|`string`|The field name
`key`|`string`|The name of the key

---
#### Tool: **`hash_get_all`**
Get all fields and values from hash.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key

---
#### Tool: **`hash_increment`**
Increment field value in hash.
Parameters|Type|Description
-|-|-
`field`|`string`|The field name
`key`|`string`|The name of the key
`amount`|`string` *optional*|Amount to increment by (default: 1)

---
#### Tool: **`hash_keys`**
Get all field names from hash.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key

---
#### Tool: **`hash_length`**
Get number of fields in hash.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key

---
#### Tool: **`hash_random_field`**
Get random field(s) from hash.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`count`|`string` *optional*|Number of fields to return (optional)

---
#### Tool: **`hash_random_field_with_values`**
Get random field(s) with their values from hash.
Parameters|Type|Description
-|-|-
`count`|`integer`|Number of field-value pairs to return
`key`|`string`|The name of the key

---
#### Tool: **`hash_set`**
Set field in hash.
Parameters|Type|Description
-|-|-
`field`|`string`|The field name
`key`|`string`|The name of the key
`value`|`string`|The value to set

---
#### Tool: **`hash_set_if_not_exists`**
Set field in hash only if it does not exist.
Parameters|Type|Description
-|-|-
`field`|`string`|The field name
`key`|`string`|The name of the key
`value`|`string`|The value to set

---
#### Tool: **`hash_set_multiple`**
Set multiple fields in hash.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`mapping`|`object`|Dictionary of field-value pairs

---
#### Tool: **`hash_strlen`**
Get length of field value in hash.
Parameters|Type|Description
-|-|-
`field`|`string`|The field name
`key`|`string`|The name of the key

---
#### Tool: **`hash_values`**
Get all values from hash.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key

---
#### Tool: **`hll_add`**
Add one element to a HyperLogLog.
Parameters|Type|Description
-|-|-
`element`|`string`|One element to add
`key`|`string`|The name of the HyperLogLog key

---
#### Tool: **`hll_count`**
Get the estimated cardinality of a HyperLogLog.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the HyperLogLog key

---
#### Tool: **`info`**
Get Valkey server information and statistics.
Parameters|Type|Description
-|-|-
`section`|`string` *optional*|The section of the info command (default, memory, cpu, etc.).

---
#### Tool: **`json_arrappend`**
Append values to the array at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document
`values`|`string`|

---
#### Tool: **`json_arrindex`**
Get the index of value in array at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document
`value`|`string`|The value to search for
`start`|`string` *optional*|Start offset (optional)
`stop`|`string` *optional*|Stop offset (optional)

---
#### Tool: **`json_arrlen`**
Get the length of array at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document

---
#### Tool: **`json_arrpop`**
Pop a value from the array at path and index.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document
`index`|`integer` *optional*|The index to pop from (-1 for last element)

---
#### Tool: **`json_arrtrim`**
Trim array at path to include only elements within range.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document
`start`|`integer`|Start index (inclusive)
`stop`|`integer`|Stop index (inclusive)

---
#### Tool: **`json_clear`**
Clear container at path (array or object).
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document

---
#### Tool: **`json_del`**
Delete value at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document

---
#### Tool: **`json_get`**
Get the JSON value at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`indent`|`string` *optional*|Number of spaces for indentation (optional)
`newline`|`string` *optional*|Add newlines in formatted output (optional)
`path`|`string` *optional*|The path in the JSON document (optional, defaults to root)
`space`|`string` *optional*|Add spaces in formatted output (optional)

---
#### Tool: **`json_numincrby`**
Increment the number at path by value.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document
`value`|`string`|The increment value (integer or float)

---
#### Tool: **`json_nummultby`**
Multiply the number at path by value.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document
`value`|`string`|The multiplier value (integer or float)

---
#### Tool: **`json_objkeys`**
Get the keys in the object at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document

---
#### Tool: **`json_objlen`**
Get the number of keys in the object at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document

---
#### Tool: **`json_set`**
Set the JSON value at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document (e.g., "$.name" or "." for root)
`value`|`string`|The value to set
`nx`|`boolean` *optional*|Only set if path doesn't exist
`xx`|`boolean` *optional*|Only set if path exists

---
#### Tool: **`json_strappend`**
Append a string to the string at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document
`value`|`string`|The string to append

---
#### Tool: **`json_strlen`**
Get the length of string at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document

---
#### Tool: **`json_toggle`**
Toggle boolean value at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string`|The path in the JSON document

---
#### Tool: **`json_type`**
Get the type of JSON value at path.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`path`|`string` *optional*|The path in the JSON document (optional, defaults to root)

---
#### Tool: **`list_append`**
Append value to list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`value`|`string`|The value to append

---
#### Tool: **`list_append_multiple`**
Append multiple values to list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`values`|`array`|List of values to append

---
#### Tool: **`list_get`**
Get value at index from list.
Parameters|Type|Description
-|-|-
`index`|`integer`|The index (0-based, negative indices supported)
`key`|`string`|The name of the key

---
#### Tool: **`list_insert_after`**
Insert value after pivot in list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`pivot`|`string`|The pivot value
`value`|`string`|The value to insert

---
#### Tool: **`list_insert_before`**
Insert value before pivot in list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`pivot`|`string`|The pivot value
`value`|`string`|The value to insert

---
#### Tool: **`list_length`**
Get length of list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key

---
#### Tool: **`list_move`**
Move element from one list to another.
Parameters|Type|Description
-|-|-
`destination`|`string`|Destination list key
`source`|`string`|Source list key
`wherefrom`|`string` *optional*|Where to pop from ("LEFT" or "RIGHT")
`whereto`|`string` *optional*|Where to push to ("LEFT" or "RIGHT")

---
#### Tool: **`list_pop_left`**
Pop value(s) from left of list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`count`|`string` *optional*|Number of values to pop (optional)

---
#### Tool: **`list_pop_right`**
Pop value(s) from right of list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`count`|`string` *optional*|Number of values to pop (optional)

---
#### Tool: **`list_position`**
Find position(s) of value in list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`value`|`string`|Value to search for
`count`|`string` *optional*|Return this many matches (optional)
`maxlen`|`string` *optional*|Limit search to first N elements (optional)
`rank`|`string` *optional*|Match the Nth occurrence (optional)

---
#### Tool: **`list_prepend`**
Prepend value to list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`value`|`string`|The value to prepend

---
#### Tool: **`list_prepend_multiple`**
Prepend multiple values to list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`values`|`array`|List of values to prepend

---
#### Tool: **`list_range`**
Get range of values from list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`start`|`integer` *optional*|Start index (inclusive, default 0)
`stop`|`integer` *optional*|Stop index (inclusive, default -1 for end)

---
#### Tool: **`list_remove`**
Remove occurrences of value from list.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`value`|`string`|Value to remove
`count`|`integer` *optional*|Number of occurrences to remove (0 for all, positive for left-to-right, negative for right-to-left)

---
#### Tool: **`list_set`**
Set value at index in list.
Parameters|Type|Description
-|-|-
`index`|`integer`|The index (0-based, negative indices supported)
`key`|`string`|The name of the key
`value`|`string`|The value to set

---
#### Tool: **`list_trim`**
Trim list to specified range.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`start`|`integer`|Start index (inclusive)
`stop`|`integer`|Stop index (inclusive)

---
#### Tool: **`rename`**
Renames a Redis key from old_key to new_key.
Parameters|Type|Description
-|-|-
`new_key`|`string`|
`old_key`|`string`|

---
#### Tool: **`set_add`**
Add member to set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`member`|`string`|Member to add

---
#### Tool: **`set_cardinality`**
Get number of members in set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key

---
#### Tool: **`set_contains`**
Check if member exists in set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`member`|`string`|Member to check

---
#### Tool: **`set_members`**
Get all members in set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key

---
#### Tool: **`set_move`**
Move member from one set to another.
Parameters|Type|Description
-|-|-
`destination`|`string`|Destination set key
`member`|`string`|Member to move
`source`|`string`|Source set key

---
#### Tool: **`set_pop`**
Remove and return random member(s) from set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`count`|`string` *optional*|Number of members to pop (optional)

---
#### Tool: **`set_random_member`**
Get random member(s) from set without removing.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`count`|`string` *optional*|Number of members to return (optional)

---
#### Tool: **`set_remove`**
Remove member from set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`member`|`string`|Member to remove

---
#### Tool: **`sorted_set_add`**
Add member-score pairs to sorted set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`mapping`|`object`|Dictionary of member-score pairs

---
#### Tool: **`sorted_set_add_incr`**
Add member to sorted set or increment its score.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`member`|`string`|The member to add/update
`score`|`number`|Score to add to existing score (or initial score)

---
#### Tool: **`sorted_set_cardinality`**
Get number of members in sorted set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`max_score`|`string` *optional*|Maximum score (optional)
`min_score`|`string` *optional*|Minimum score (optional)

---
#### Tool: **`sorted_set_popmax`**
Remove and return members with highest scores.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`count`|`string` *optional*|Number of members to pop (optional)

---
#### Tool: **`sorted_set_popmin`**
Remove and return members with lowest scores.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`count`|`string` *optional*|Number of members to pop (optional)

---
#### Tool: **`sorted_set_range`**
Get range of members from sorted set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`reverse`|`boolean` *optional*|Return results in reverse order
`start`|`integer` *optional*|Start index (inclusive)
`stop`|`integer` *optional*|Stop index (inclusive)
`withscores`|`boolean` *optional*|Include scores in result

---
#### Tool: **`sorted_set_range_by_lex`**
Get range of members by lexicographical order.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`max_lex`|`string`|Maximum value (inclusive)
`min_lex`|`string`|Minimum value (inclusive)
`count`|`string` *optional*|Maximum number of members to return
`offset`|`string` *optional*|Number of members to skip
`reverse`|`boolean` *optional*|Return results in reverse order

---
#### Tool: **`sorted_set_range_by_score`**
Get range of members by score.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`max_score`|`number`|Maximum score (inclusive)
`min_score`|`number`|Minimum score (inclusive)
`count`|`string` *optional*|Maximum number of members to return
`offset`|`string` *optional*|Number of members to skip
`reverse`|`boolean` *optional*|Return results in reverse order
`withscores`|`boolean` *optional*|Include scores in result

---
#### Tool: **`sorted_set_rank`**
Get rank of member in sorted set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`member`|`string`|The member to get rank for
`reverse`|`boolean` *optional*|If True, get rank in reverse order (highest first)

---
#### Tool: **`sorted_set_remove`**
Remove member(s) from sorted set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`members`|`string`|

---
#### Tool: **`sorted_set_remove_by_lex`**
Remove members by lexicographical range.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`max_lex`|`string`|Maximum value (inclusive)
`min_lex`|`string`|Minimum value (inclusive)

---
#### Tool: **`sorted_set_remove_by_rank`**
Remove members by rank range.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`start`|`integer`|Start rank (inclusive)
`stop`|`integer`|Stop rank (inclusive)

---
#### Tool: **`sorted_set_remove_by_score`**
Remove members by score range.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`max_score`|`number`|Maximum score (inclusive)
`min_score`|`number`|Minimum score (inclusive)

---
#### Tool: **`sorted_set_score`**
Get score of member in sorted set.
Parameters|Type|Description
-|-|-
`key`|`string`|The name of the key
`member`|`string`|The member to get score for

---
#### Tool: **`stream_add`**
Add entry to stream.
Parameters|Type|Description
-|-|-
`field_dict`|`object`|Dictionary of field-value pairs
`key`|`string`|The name of the key
`approximate`|`boolean` *optional*|Whether maxlen is approximate
`id`|`string` *optional*|Entry ID (default "*" for auto-generation)
`maxlen`|`string` *optional*|Maximum length of stream (optional)

---
#### Tool: **`stream_delete`**
Delete entries from stream.
Parameters|Type|Description
-|-|-
`id`|`string`|Entry ID to delete
`key`|`string`|The name of the key

---
#### Tool: **`stream_group_create`**
Create consumer group.
Parameters|Type|Description
-|-|-
`group_name`|`string`|Name of consumer group
`key`|`string`|The name of the key
`id`|`string` *optional*|ID to start reading from (default "$" for new entries only)
`mkstream`|`boolean` *optional*|Create stream if it doesn't exist

---
#### Tool: **`stream_group_delete_consumer`**
Delete consumer from group.
Parameters|Type|Description
-|-|-
`consumer_name`|`string`|Name of consumer to delete
`group_na

[...]

## Screenshots

![Amazon ElastiCache/MemoryDB for Valkey screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/awslabs-valkey-1.png)

![Amazon ElastiCache/MemoryDB for Valkey screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/awslabs-valkey-2.png)

![Amazon ElastiCache/MemoryDB for Valkey screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/awslabs-valkey-3.png)
