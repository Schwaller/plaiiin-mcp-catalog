Model Context Protocol (MCP) Server for Handwriting OCR .

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/handwriting-ocr](https://hub.docker.com/repository/docker/mcp/handwriting-ocr)
**Author**|[Handwriting-OCR](https://github.com/Handwriting-OCR)
**Repository**|https://github.com/Handwriting-OCR/handwriting-ocr-mcp-server

## Available Tools (3)
Tools provided by this Server|Short Description
-|-
`check_status`|Check the status of a document|
`get_text`|Retrieve the transcribed text from a document|
`upload_document`|Upload a document to Handwriting OCR API for transcription|

---
## Tools Details

#### Tool: **`check_status`**
Check the status of a document
Parameters|Type|Description
-|-|-
`id`|`string`|Document ID

---
#### Tool: **`get_text`**
Retrieve the transcribed text from a document
Parameters|Type|Description
-|-|-
`id`|`string`|Document ID

---
#### Tool: **`upload_document`**
Upload a document to Handwriting OCR API for transcription
Parameters|Type|Description
-|-|-
`file`|`string`|Path to the document (PDF, JPG, PNG, etc.)
`delete_after`|`integer` *optional*|Seconds until auto-deletion (optional)
`extractor_id`|`string` *optional*|Extractor ID (required if action is extractor, will be ignored)
`prompt_id`|`string` *optional*|Prompt ID (requires Enterprise subscription, will be ignored)

---
