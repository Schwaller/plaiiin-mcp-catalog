This server provides AI agents with tools to fetch, post and search on Reddit.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/reddit-mcp](https://hub.docker.com/repository/docker/mcp/reddit-mcp)
**Author**|[KrishnaRandad2023](https://github.com/KrishnaRandad2023)
**Repository**|https://github.com/KrishnaRandad2023/mcp-reddit

## Available Tools (6)
Tools provided by this Server|Short Description
-|-
`fetchPosts`|Fetch hot posts from a subreddit|
`getComments`|Get comments for a specific Reddit post|
`getSubredditInfo`|Get information about a subreddit|
`postComment`|Post a comment on a Reddit post|
`postToSubreddit`|Create a new post in a subreddit|
`searchPosts`|Search for posts within a subreddit|

---
## Tools Details

#### Tool: **`fetchPosts`**
Fetch hot posts from a subreddit
Parameters|Type|Description
-|-|-
`subreddit`|`string`|Name of the subreddit
`limit`|`integer` *optional*|Number of posts to fetch (1-100)

---
#### Tool: **`getComments`**
Get comments for a specific Reddit post
Parameters|Type|Description
-|-|-
`post_id`|`string`|Reddit post ID (without 't3_' prefix)

---
#### Tool: **`getSubredditInfo`**
Get information about a subreddit
Parameters|Type|Description
-|-|-
`subreddit`|`string`|Name of the subreddit

---
#### Tool: **`postComment`**
Post a comment on a Reddit post
Parameters|Type|Description
-|-|-
`comment_text`|`string`|Comment text to post
`post_id`|`string`|Reddit post ID (without 't3_' prefix)

---
#### Tool: **`postToSubreddit`**
Create a new post in a subreddit
Parameters|Type|Description
-|-|-
`subreddit`|`string`|Name of the subreddit
`title`|`string`|Post title
`content`|`string` *optional*|Post content (for text posts)
`url`|`string` *optional*|URL (for link posts)

---
#### Tool: **`searchPosts`**
Search for posts within a subreddit
Parameters|Type|Description
-|-|-
`query`|`string`|Search query
`subreddit`|`string`|Name of the subreddit
`limit`|`integer` *optional*|Number of results to return (1-100)

---
