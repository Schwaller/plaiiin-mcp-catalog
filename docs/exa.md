Exa MCP for web search and web crawling!.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/exa](https://hub.docker.com/repository/docker/mcp/exa)
**Author**|[exa-labs](https://github.com/exa-labs)
**Repository**|https://github.com/exa-labs/exa-mcp-server

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`web_fetch_exa`|Read a webpage's full content as clean markdown.|
`web_search_exa`|Search the web for any topic and get clean, ready-to-use content.|

---
## Tools Details

#### Tool: **`web_fetch_exa`**
Read a webpage's full content as clean markdown. Use after web_search_exa when highlights are insufficient or to read any URL.

Best for: Extracting full content from known URLs. Batch multiple URLs in one call.
Returns: Clean text content and metadata from the page(s).
Parameters|Type|Description
-|-|-
`urls`|`array`|URLs to read. Batch multiple URLs in one call.
`maxCharacters`|`number` *optional*|Maximum characters to extract per page (default: 3000)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`web_search_exa`**
Search the web for any topic and get clean, ready-to-use content.

      Best for: Finding current information, news, facts, people, companies, or answering questions about any topic.
      Returns: Clean text content from top search results.

      Query tips:
      describe the ideal page, not keywords. "blog post comparing React and Vue performance" not "React vs Vue".
      Use category:people / category:company to search through Linkedin profiles / companies respectively.
      If highlights are insufficient, follow up with web_fetch_exa on the best URLs.
Parameters|Type|Description
-|-|-
`query`|`string`|Natural language search query. Should be a semantically rich description of the ideal page, not just keywords. Optionally include category:<type> (company, people) to focus results — e.g. 'category:people John Doe software engineer'.
`numResults`|`number` *optional*|Number of search results to return (default: 10).

*This tool is read-only. It does not modify its environment.*

---
