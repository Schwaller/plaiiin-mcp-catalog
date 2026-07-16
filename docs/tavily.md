The Tavily MCP server provides seamless interaction with the tavily-search and tavily-extract tools, real-time web search capabilities through the tavily-search tool and Intelligent data extraction from web pages via the tavily-extract tool.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/tavily](https://hub.docker.com/repository/docker/mcp/tavily)
**Author**|[tavily-ai](https://github.com/tavily-ai)
**Repository**|https://github.com/tavily-ai/tavily-mcp

## Available Tools (5)
Tools provided by this Server|Short Description
-|-
`tavily_crawl`|Crawl a website starting from a URL.|
`tavily_extract`|Extract content from URLs.|
`tavily_map`|Map a website's structure.|
`tavily_research`|Perform comprehensive research on a given topic or question.|
`tavily_search`|Search the web for current information on any topic.|

---
## Tools Details

#### Tool: **`tavily_crawl`**
Crawl a website starting from a URL. Extracts content from pages with configurable depth and breadth.
Parameters|Type|Description
-|-|-
`url`|`string`|The root URL to begin the crawl
`allow_external`|`boolean` *optional*|Whether to return external links in the final response
`extract_depth`|`string` *optional*|Advanced extraction retrieves more data, including tables and embedded content, with higher success but may increase latency
`format`|`string` *optional*|The format of the extracted web page content. markdown returns content in markdown format. text returns plain text and may increase latency.
`include_favicon`|`boolean` *optional*|Whether to include the favicon URL for each result
`instructions`|`string` *optional*|Natural language instructions for the crawler. Instructions specify which types of pages the crawler should return.
`limit`|`integer` *optional*|Total number of links the crawler will process before stopping
`max_breadth`|`integer` *optional*|Max number of links to follow per level of the tree (i.e., per page)
`max_depth`|`integer` *optional*|Max depth of the crawl. Defines how far from the base URL the crawler can explore.
`select_domains`|`array` *optional*|Regex patterns to restrict crawling to specific domains or subdomains (e.g., ^docs\.example\.com$)
`select_paths`|`array` *optional*|Regex patterns to select only URLs with specific path patterns (e.g., /docs/.*, /api/v1.*)

---
#### Tool: **`tavily_extract`**
Extract content from URLs. Returns raw page content in markdown or text format.
Parameters|Type|Description
-|-|-
`urls`|`array`|List of URLs to extract content from
`extract_depth`|`string` *optional*|Use 'advanced' for LinkedIn, protected sites, or tables/embedded content
`format`|`string` *optional*|Output format
`include_favicon`|`boolean` *optional*|Include favicon URLs
`include_images`|`boolean` *optional*|Include images from pages
`query`|`string` *optional*|Query to rerank content chunks by relevance

---
#### Tool: **`tavily_map`**
Map a website's structure. Returns a list of URLs found starting from the base URL.
Parameters|Type|Description
-|-|-
`url`|`string`|The root URL to begin the mapping
`allow_external`|`boolean` *optional*|Whether to return external links in the final response
`instructions`|`string` *optional*|Natural language instructions for the crawler
`limit`|`integer` *optional*|Total number of links the crawler will process before stopping
`max_breadth`|`integer` *optional*|Max number of links to follow per level of the tree (i.e., per page)
`max_depth`|`integer` *optional*|Max depth of the mapping. Defines how far from the base URL the crawler can explore
`select_domains`|`array` *optional*|Regex patterns to restrict crawling to specific domains or subdomains (e.g., ^docs\.example\.com$)
`select_paths`|`array` *optional*|Regex patterns to select only URLs with specific path patterns (e.g., /docs/.*, /api/v1.*)

---
#### Tool: **`tavily_research`**
Perform comprehensive research on a given topic or question. Use this tool when you need to gather information from multiple sources to answer a question or complete a task. Returns a detailed response based on the research findings. Rate limit: 20 requests per minute.
Parameters|Type|Description
-|-|-
`input`|`string`|A comprehensive description of the research task
`model`|`string` *optional*|Defines the degree of depth of the research. 'mini' is good for narrow tasks with few subtopics. 'pro' is good for broad tasks with many subtopics. 'auto' automatically selects the best model.

---
#### Tool: **`tavily_search`**
Search the web for current information on any topic. Use for news, facts, or data beyond your knowledge cutoff. Returns snippets and source URLs.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query
`country`|`string` *optional*|Boost search results from a specific country. Must be a full country name (e.g., 'United States', 'Japan', 'Germany'). ISO country codes (e.g., 'us', 'jp') are not supported. Available only if topic is general. See https://docs.tavily.com/documentation/api-reference/search for the full list of supported countries.
`end_date`|`string` *optional*|Will return all results before the specified end date. Required to be written in the format YYYY-MM-DD
`exact_match`|`boolean` *optional*|Only return results containing the exact phrase(s) in quotes in your query
`exclude_domains`|`array` *optional*|List of domains to specifically exclude, if the user asks to exclude a domain set this to the domain of the site
`include_domains`|`array` *optional*|A list of domains to specifically include in the search results, if the user asks to search on specific sites set this to the domain of the site
`include_favicon`|`boolean` *optional*|Whether to include the favicon URL for each result
`include_image_descriptions`|`boolean` *optional*|Include a list of query-related images and their descriptions in the response
`include_images`|`boolean` *optional*|Include a list of query-related images in the response
`include_raw_content`|`boolean` *optional*|Include the cleaned and parsed HTML content of each search result
`max_results`|`number` *optional*|The maximum number of search results to return
`search_depth`|`string` *optional*|The depth of the search. 'basic' for generic results, 'advanced' for more thorough search, 'fast' for optimized low latency with high relevance, 'ultra-fast' for prioritizing latency above all else
`start_date`|`string` *optional*|Will return all results after the specified start date. Required to be written in the format YYYY-MM-DD.
`time_range`|`string` *optional*|The time range back from the current date to include in the search results
`topic`|`string` *optional*|The category of the search. This will determine which of our agents will be used for the search

---
