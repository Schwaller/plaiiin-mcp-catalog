This adds a border to an image and returns base64 encoded image.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/schogini_mcp_image_border](https://hub.docker.com/repository/docker/mcp/schogini_mcp_image_border)
**Author**|[schogini](https://github.com/schogini)
**Repository**|https://github.com/schogini/schogini_mcp_image_border

## Available Tools (3)
Tools provided by this Server|Short Description
-|-
`add-two-numbers`|A simple tool to add two numbers.|
`image-border`|Add a colored border to an image from a URL|
`image-meta`|Get image metadata from a public image URL.|

---
## Tools Details

#### Tool: **`add-two-numbers`**
A simple tool to add two numbers.
Parameters|Type|Description
-|-|-
`num1`|`string`|First number to add
`num2`|`string`|Second number to add

---
#### Tool: **`image-border`**
Add a colored border to an image from a URL
Parameters|Type|Description
-|-|-
`border_color`|`string`|e.g., black, red, #FF0000
`border_thickness`|`integer`|
`image_url`|`string`|Public image URL

---
#### Tool: **`image-meta`**
Get image metadata from a public image URL. Returns width, height, file size in bytes, image mode (e.g., RGB), and image format (e.g., PNG, JPEG).
Parameters|Type|Description
-|-|-
`image_url`|`string`|The public URL of the image.

---
