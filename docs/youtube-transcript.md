Retrieves transcripts for given YouTube video URLs.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/youtube-transcript](https://hub.docker.com/repository/docker/mcp/youtube-transcript)
**Author**|[jkawamoto](https://github.com/jkawamoto)
**Repository**|https://github.com/jkawamoto/mcp-youtube-transcript

## Available Tools (4)
Tools provided by this Server|Short Description
-|-
`get_available_languages`|Retrieves the available languages for the video.|
`get_timed_transcript`|Retrieves the transcript of a YouTube video with timestamps.|
`get_transcript`|Retrieves the transcript of a YouTube video.|
`get_video_info`|Retrieves the video information.|

---
## Tools Details

#### Tool: **`get_available_languages`**
Retrieves the available languages for the video.
Parameters|Type|Description
-|-|-
`url`|`string`|The URL of the YouTube video

---
#### Tool: **`get_timed_transcript`**
Retrieves the transcript of a YouTube video with timestamps.
Parameters|Type|Description
-|-|-
`url`|`string`|The URL of the YouTube video
`lang`|`string` *optional*|The preferred language for the transcript
`next_cursor`|`string` *optional*|Cursor to retrieve the next page of the transcript

---
#### Tool: **`get_transcript`**
Retrieves the transcript of a YouTube video.
Parameters|Type|Description
-|-|-
`url`|`string`|The URL of the YouTube video
`lang`|`string` *optional*|The preferred language for the transcript
`next_cursor`|`string` *optional*|Cursor to retrieve the next page of the transcript

---
#### Tool: **`get_video_info`**
Retrieves the video information.
Parameters|Type|Description
-|-|-
`url`|`string`|The URL of the YouTube video

---
