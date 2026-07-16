A Model Context Protocol (MCP) server that provides access to Hacker News stories, comments, and user data, with support for search and content retrieval.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/hackernews-mcp](https://hub.docker.com/repository/docker/mcp/hackernews-mcp)
**Author**|[AayushBahukhandi](https://github.com/AayushBahukhandi)
**Repository**|https://github.com/AayushBahukhandi/hackernews-mcp

## Available Tools (4)
Tools provided by this Server|Short Description
-|-
`get_stories`|Get stories from Hacker News.|
`get_story_info`|Get detailed story info from Hacker News, including the comments|
`get_user_info`|Get user info from Hacker News, including the stories they've submitted|
`search_stories`|Search stories from Hacker News.|

---
## Tools Details

#### Tool: **`get_stories`**
Get stories from Hacker News. The options are `top`, `new`, `ask_hn`, `show_hn` for types of stories. This doesn't include the comments. Use `get_story_info` to get the comments.
Parameters|Type|Description
-|-|-
`num_stories`|`integer` *optional*|Number of stories to get
`story_type`|`string` *optional*|Type of stories to get, one of: `top`, `new`, `ask_hn`, `show_hn`

---
#### Tool: **`get_story_info`**
Get detailed story info from Hacker News, including the comments
Parameters|Type|Description
-|-|-
`story_id`|`integer`|Story ID

---
#### Tool: **`get_user_info`**
Get user info from Hacker News, including the stories they've submitted
Parameters|Type|Description
-|-|-
`user_name`|`string`|Username of the user
`num_stories`|`integer` *optional*|Number of stories to get, defaults to 10

---
#### Tool: **`search_stories`**
Search stories from Hacker News. It is generally recommended to use simpler queries to get a broader set of results (less than 5 words). Very targeted queries may not return any results.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query
`num_results`|`integer` *optional*|Number of results to get
`search_by_date`|`boolean` *optional*|Search by date, defaults to false. If this is false, then we search by relevance, then points, then number of comments.

---
