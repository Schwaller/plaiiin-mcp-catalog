ONLYOFFICE DocSpace is a room-based collaborative platform which allows organizing a clear file structure depending on users' needs or project goals.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/onlyoffice-docspace](https://hub.docker.com/repository/docker/mcp/onlyoffice-docspace)
**Author**|[ONLYOFFICE](https://github.com/ONLYOFFICE)
**Repository**|https://github.com/ONLYOFFICE/docspace-mcp

## Available Tools (23)
Tools provided by this Server|Short Description
-|-
`archive_room`|Archive a room.|
`copy_batch_items`|Copy to a folder.|
`create_folder`|Create a folder.|
`create_room`|Create a room.|
`delete_file`|Delete a file.|
`delete_folder`|Delete a folder.|
`download_file_as_text`|Download a file as text.|
`get_all_people`|Get all people.|
`get_file_info`|Get file information.|
`get_folder_content`|Get content of a folder.|
`get_folder_info`|Get folder information.|
`get_my_folder`|Get the 'My Documents' folder.|
`get_room_access_levels`|Get a list of available room invitation access levels.|
`get_room_info`|Get room information.|
`get_room_security_info`|Get a list of users with their access levels to a room.|
`get_room_types`|Get a list of available room types.|
`get_rooms_folder`|Get the 'Rooms' folder.|
`move_batch_items`|Move to a folder.|
`rename_folder`|Rename a folder.|
`set_room_security`|Invite or remove users from a room.|
`update_file`|Update a file.|
`update_room`|Update a room.|
`upload_file`|Upload a file.|

---
## Tools Details

#### Tool: **`archive_room`**
Archive a room.
Parameters|Type|Description
-|-|-
`roomId`|`number`|The ID of the room to archive.

*This tool may perform destructive updates.*

---
#### Tool: **`copy_batch_items`**
Copy to a folder.
Parameters|Type|Description
-|-|-
`destFolderId`|`string` *optional*|The ID of the destination folder to copy the items to.
`fileIds`|`array` *optional*|The IDs of the files to copy.
`folderIds`|`array` *optional*|The IDs of the folders to copy.

*This tool may perform destructive updates.*

---
#### Tool: **`create_folder`**
Create a folder.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the folder creation. Use them to reduce the size of the response.
`parentId`|`number`|The ID of the room or folder to create the folder in.
`title`|`string`|The title of the folder to create.

*This tool may perform destructive updates.*

---
#### Tool: **`create_room`**
Create a room.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the room creation.
`roomType`|`number`|The type of the room to create.

1 - Form Filling Room. Upload PDF forms into the room. Invite members and guests to fill out a PDF form. Review completed forms and analyze data automatically collected in a spreadsheet.
2 - Collaboration room. Collaborate on one or multiple documents with your team.
5 - Custom room. Apply your own settings to use this room for any custom purpose.
6 - Public room. Share documents for viewing, editing, commenting, or reviewing without registration. You can also embed this room into any web interface.
8 - Virtual Data Room. Use VDR for advanced file security and transparency. Set watermarks, automatically index and track all content, restrict downloading and copying.
`title`|`string`|The title of the room to create.

*This tool may perform destructive updates.*

---
#### Tool: **`delete_file`**
Delete a file.
Parameters|Type|Description
-|-|-
`fileId`|`number`|The ID of the file to delete.

*This tool may perform destructive updates.*

---
#### Tool: **`delete_folder`**
Delete a folder.
Parameters|Type|Description
-|-|-
`folderId`|`number`|The ID of the folder to delete.

*This tool may perform destructive updates.*

---
#### Tool: **`download_file_as_text`**
Download a file as text.
Parameters|Type|Description
-|-|-
`fileId`|`number`|The ID of the file to download as text.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_all_people`**
Get all people.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the list of people. Use them to reduce the size of the response.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_file_info`**
Get file information.
Parameters|Type|Description
-|-|-
`fileId`|`number`|The ID of the file to get info for.
`filters`|`object`|The filters to apply to the file info. Use them to reduce the size of the response.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_folder_content`**
Get content of a folder.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the contents of the folder. Use them to reduce the size of the response.
`folderId`|`number`|The ID of the folder to get.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_folder_info`**
Get folder information.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the folder info. Use them to reduce the size of the response.
`folderId`|`number`|The ID of the folder to get info for.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_my_folder`**
Get the 'My Documents' folder.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the My Documents folder. Use them to reduce the size of the response.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_room_access_levels`**
Get a list of available room invitation access levels.
Parameters|Type|Description
-|-|-
`roomId`|`number`|The ID of the room to get the invitation access for.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_room_info`**
Get room information.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the room info.
`roomId`|`number`|The ID of the room to get info for.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_room_security_info`**
Get a list of users with their access levels to a room.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the room security info.
`roomId`|`number`|The ID of the room to get a list of users with their access level for.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_room_types`**
Get a list of available room types.
#### Tool: **`get_rooms_folder`**
Get the 'Rooms' folder.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the rooms folder.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`move_batch_items`**
Move to a folder.
Parameters|Type|Description
-|-|-
`destFolderId`|`string` *optional*|The ID of the destination folder to move the items to.
`fileIds`|`array` *optional*|The IDs of the files to move.
`folderIds`|`array` *optional*|The IDs of the folders to move items to.

*This tool may perform destructive updates.*

---
#### Tool: **`rename_folder`**
Rename a folder.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the folder renaming. Use them to reduce the size of the response.
`folderId`|`number`|The ID of the folder to rename.
`title`|`string`|The new title of the folder to set.

*This tool may perform destructive updates.*

---
#### Tool: **`set_room_security`**
Invite or remove users from a room.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the room security info.
`invitations`|`array`|The invitations or removals to perform.
`roomId`|`number`|The ID of the room to invite or remove users from.
`culture`|`string` *optional*|The languages to use for the invitation.
`message`|`string` *optional*|The message to use for the invitation.
`notify`|`boolean` *optional*|Whether to notify the user.

*This tool may perform destructive updates.*

---
#### Tool: **`update_file`**
Update a file.
Parameters|Type|Description
-|-|-
`fileId`|`number`|The ID of the file to update.
`title`|`string`|The new title of the file to set.

*This tool may perform destructive updates.*

---
#### Tool: **`update_room`**
Update a room.
Parameters|Type|Description
-|-|-
`filters`|`object`|The filters to apply to the room update.
`roomId`|`number`|The ID of the room to update.
`title`|`string` *optional*|The new title of the room to set.

*This tool may perform destructive updates.*

---
#### Tool: **`upload_file`**
Upload a file.
Parameters|Type|Description
-|-|-
`content`|`string`|The content of the file to upload.
`filename`|`string`|The file name with an extension to upload.
`parentId`|`number`|The ID of the room or folder to upload the file to.

*This tool may perform destructive updates.*

---
