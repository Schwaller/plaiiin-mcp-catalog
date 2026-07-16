AI image generation using Amazon Nova Canvas.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/nova-canvas-mcp-server](https://hub.docker.com/repository/docker/mcp/nova-canvas-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`generate_image`|Generate an image using Amazon Nova Canvas with text prompt.|
`generate_image_with_colors`|Generate an image using Amazon Nova Canvas with color guidance.|

---
## Tools Details

#### Tool: **`generate_image`**
Generate an image using Amazon Nova Canvas with text prompt.

This tool uses Amazon Nova Canvas to generate images based on a text prompt.
The generated image will be saved to a file and the path will be returned.

IMPORTANT FOR ASSISTANT: Always send the current workspace directory when calling this tool!
The workspace_dir parameter should be set to the directory where the user is currently working
so that images are saved to a location accessible to the user.

## Prompt Best Practices

An effective prompt often includes short descriptions of:
1. The subject
2. The environment
3. (optional) The position or pose of the subject
4. (optional) Lighting description
5. (optional) Camera position/framing
6. (optional) The visual style or medium ("photo", "illustration", "painting", etc.)

Do not use negation words like "no", "not", "without" in your prompt. Instead, use the
negative_prompt parameter to specify what you don't want in the image.

You should always include "people, anatomy, hands, low quality, low resolution, low detail" in your negative_prompt

## Example Prompts

- "realistic editorial photo of female teacher standing at a blackboard with a warm smile"
- "whimsical and ethereal soft-shaded story illustration: A woman in a large hat stands at the ship's railing looking out across the ocean"
- "drone view of a dark river winding through a stark Iceland landscape, cinematic quality"

Returns:
    McpImageGenerationResponse: A response containing the generated image paths.
Parameters|Type|Description
-|-|-
`prompt`|`string`|The text description of the image to generate (1-1024 characters)
`cfg_scale`|`number` *optional*|How strongly the image adheres to the prompt (1.1-10.0)
`filename`|`string` *optional*|The name of the file to save the image to (without extension)
`height`|`integer` *optional*|The height of the generated image (320-4096, divisible by 16)
`negative_prompt`|`string` *optional*|Text to define what not to include in the image (1-1024 characters)
`number_of_images`|`integer` *optional*|The number of images to generate (1-5)
`quality`|`string` *optional*|The quality of the generated image ("standard" or "premium")
`seed`|`string` *optional*|Seed for generation (0-858,993,459)
`width`|`integer` *optional*|The width of the generated image (320-4096, divisible by 16)
`workspace_dir`|`string` *optional*|The current workspace directory where the image should be saved.
        CRITICAL: Assistant must always provide the current IDE workspace directory parameter to save images to the user's current project.

---
#### Tool: **`generate_image_with_colors`**
Generate an image using Amazon Nova Canvas with color guidance.

This tool uses Amazon Nova Canvas to generate images based on a text prompt and color palette.
The generated image will be saved to a file and the path will be returned.

IMPORTANT FOR Assistant: Always send the current workspace directory when calling this tool!
The workspace_dir parameter should be set to the directory where the user is currently working
so that images are saved to a location accessible to the user.

## Prompt Best Practices

An effective prompt often includes short descriptions of:
1. The subject
2. The environment
3. (optional) The position or pose of the subject
4. (optional) Lighting description
5. (optional) Camera position/framing
6. (optional) The visual style or medium ("photo", "illustration", "painting", etc.)

Do not use negation words like "no", "not", "without" in your prompt. Instead, use the
negative_prompt parameter to specify what you don't want in the image.

## Example Colors

- ["#FF5733", "#33FF57", "#3357FF"] - A vibrant color scheme with red, green, and blue
- ["#000000", "#FFFFFF"] - A high contrast black and white scheme
- ["#FFD700", "#B87333"] - A gold and bronze color scheme

Returns:
    McpImageGenerationResponse: A response containing the generated image paths.
Parameters|Type|Description
-|-|-
`colors`|`array`|List of up to 10 hexadecimal color values (e.g., "#FF9800")
`prompt`|`string`|The text description of the image to generate (1-1024 characters)
`cfg_scale`|`number` *optional*|How strongly the image adheres to the prompt (1.1-10.0)
`filename`|`string` *optional*|The name of the file to save the image to (without extension)
`height`|`integer` *optional*|The height of the generated image (320-4096, divisible by 16)
`negative_prompt`|`string` *optional*|Text to define what not to include in the image (1-1024 characters)
`number_of_images`|`integer` *optional*|The number of images to generate (1-5)
`quality`|`string` *optional*|The quality of the generated image ("standard" or "premium")
`seed`|`string` *optional*|Seed for generation (0-858,993,459)
`width`|`integer` *optional*|The width of the generated image (320-4096, divisible by 16)
`workspace_dir`|`string` *optional*|The current workspace directory where the image should be saved. CRITICAL: Assistant must always provide this parameter to save images to the user's current project.

---

## Screenshots

![AWS Labs Nova Canvas screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-nova-canvas-1.png)

![AWS Labs Nova Canvas screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-nova-canvas-2.png)

![AWS Labs Nova Canvas screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/awslabs-nova-canvas-3.png)
