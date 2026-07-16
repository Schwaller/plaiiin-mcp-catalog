Image generation server using EverArt's API.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/everart](https://hub.docker.com/repository/docker/mcp/everart)
**Author**|[modelcontextprotocol](https://github.com/modelcontextprotocol)
**Repository**|https://github.com/modelcontextprotocol/servers

## Available Tools (1)
Tools provided by this Server|Short Description
-|-
`generate_image`|Generate images using EverArt Models and returns a clickable link to view the generated image.|

---
## Tools Details

#### Tool: **`generate_image`**
Generate images using EverArt Models and returns a clickable link to view the generated image. The tool will return a URL that can be clicked to view the image in a browser. Available models:
- 5000:FLUX1.1: Standard quality
- 9000:FLUX1.1-ultra: Ultra high quality
- 6000:SD3.5: Stable Diffusion 3.5
- 7000:Recraft-Real: Photorealistic style
- 8000:Recraft-Vector: Vector art style

The response will contain a direct link to view the generated image.
Parameters|Type|Description
-|-|-
`prompt`|`string`|Text description of desired image
`image_count`|`number` *optional*|Number of images to generate
`model`|`string` *optional*|Model ID (5000:FLUX1.1, 9000:FLUX1.1-ultra, 6000:SD3.5, 7000:Recraft-Real, 8000:Recraft-Vector)

---
