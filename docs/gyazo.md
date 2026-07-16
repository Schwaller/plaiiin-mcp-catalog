Official Model Context Protocol server for Gyazo.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/gyazo](https://hub.docker.com/repository/docker/mcp/gyazo)
**Author**|[nota](https://github.com/nota)
**Repository**|https://github.com/nota/gyazo-mcp-server

## Available Tools (4)
Tools provided by this Server|Short Description
-|-
`gyazo_image`|Fetch image content and metadata from Gyazo|
`gyazo_latest_image`|Fetch latest uploaded image content and metadata from Gyazo|
`gyazo_search`|Full-text search for captures uploaded by users on Gyazo|
`gyazo_upload`|Upload an image to Gyazo|

---
## Tools Details

#### Tool: **`gyazo_image`**
Fetch image content and metadata from Gyazo
Parameters|Type|Description
-|-|-
`id_or_url`|`string`|ID or URL of the image on Gyazo

---
#### Tool: **`gyazo_latest_image`**
Fetch latest uploaded image content and metadata from Gyazo
Parameters|Type|Description
-|-|-
`name`|`string`|

---
#### Tool: **`gyazo_search`**
Full-text search for captures uploaded by users on Gyazo
Parameters|Type|Description
-|-|-
`query`|`string`|Search keyword (max length: 200 characters). example: 'cat', 'title:cat', 'app:"Google Chrome"', 'url:google.com', 'cat since:2024-01-01 until:2024-12-31' NOTE: If you cannot find an appropriate capture, try rephrasing the search query to capture the user's intent and repeat the search several times
`page`|`integer` *optional*|Page number for pagination
`per`|`integer` *optional*|Number of results per page (max: 100)

---
#### Tool: **`gyazo_upload`**
Upload an image to Gyazo
Parameters|Type|Description
-|-|-
`imageData`|`string`|Base64 encoded image data
`app`|`string` *optional*|Application name for the image (optional).
`description`|`string` *optional*|Description for the image (optional)
`refererUrl`|`string` *optional*|Source URL for the image (optional).
`title`|`string` *optional*|Title for the image (optional)

---
