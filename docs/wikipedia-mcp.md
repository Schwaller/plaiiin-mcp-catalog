A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/wikipedia-mcp](https://hub.docker.com/repository/docker/mcp/wikipedia-mcp)
**Author**|[Rudra-ravi](https://github.com/Rudra-ravi)
**Repository**|https://github.com/Rudra-ravi/wikipedia-mcp

## Available Tools (22)
Tools provided by this Server|Short Description
-|-
`extract_key_facts`|Extract key facts from a Wikipedia article, optionally focused on a topic.|
`get_article`|Get the full content of a Wikipedia article.|
`get_coordinates`|Get the coordinates of a Wikipedia article.|
`get_links`|Get the links contained within a Wikipedia article.|
`get_related_topics`|Get topics related to a Wikipedia article based on links and categories.|
`get_sections`|Get the sections of a Wikipedia article.|
`get_summary`|Get a summary of a Wikipedia article.|
`search_wikipedia`|Search Wikipedia for articles matching a query.|
`summarize_article_for_query`|Get a summary of a Wikipedia article tailored to a specific query.|
`summarize_article_section`|Get a summary of a specific section of a Wikipedia article.|
`test_wikipedia_connectivity`|Provide diagnostics for Wikipedia API connectivity.|
`wikipedia_extract_key_facts`|Extract key facts from a Wikipedia article, optionally focused on a topic.|
`wikipedia_get_article`|Get the full content of a Wikipedia article.|
`wikipedia_get_coordinates`|Get the coordinates of a Wikipedia article.|
`wikipedia_get_links`|Get the links contained within a Wikipedia article.|
`wikipedia_get_related_topics`|Get topics related to a Wikipedia article based on links and categories.|
`wikipedia_get_sections`|Get the sections of a Wikipedia article.|
`wikipedia_get_summary`|Get a summary of a Wikipedia article.|
`wikipedia_search_wikipedia`|Search Wikipedia for articles matching a query.|
`wikipedia_summarize_article_for_query`|Get a summary of a Wikipedia article tailored to a specific query.|
`wikipedia_summarize_article_section`|Get a summary of a specific section of a Wikipedia article.|
`wikipedia_test_wikipedia_connectivity`|Provide diagnostics for Wikipedia API connectivity.|

---
## Tools Details

#### Tool: **`extract_key_facts`**
Extract key facts from a Wikipedia article, optionally focused on a topic.

Returns a dictionary containing a list of facts.
Parameters|Type|Description
-|-|-
`title`|`string`|
`count`|`integer` *optional*|
`topic_within_article`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`get_article`**
Get the full content of a Wikipedia article.

Returns a dictionary containing article details or an error message
if retrieval fails.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`get_coordinates`**
Get the coordinates of a Wikipedia article.

Returns a dictionary containing coordinate information.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`get_links`**
Get the links contained within a Wikipedia article.

Returns a dictionary with the article title and list of links.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`get_related_topics`**
Get topics related to a Wikipedia article based on links and categories.

Returns a list of related topics up to the specified limit.
Parameters|Type|Description
-|-|-
`title`|`string`|
`limit`|`integer` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`get_sections`**
Get the sections of a Wikipedia article.

Returns a dictionary with the article title and list of sections.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`get_summary`**
Get a summary of a Wikipedia article.

Returns a dictionary with the title and summary string. On error,
includes an error message instead of a summary.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`search_wikipedia`**
Search Wikipedia for articles matching a query.
Parameters|Type|Description
-|-|-
`query`|`string`|The search term to look up on Wikipedia.
`limit`|`integer` *optional*|Maximum number of results to return (1-500).

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`summarize_article_for_query`**
Get a summary of a Wikipedia article tailored to a specific query.

The summary is a snippet around the query within the article text or
summary. The max_length parameter controls the length of the snippet.
Parameters|Type|Description
-|-|-
`query`|`string`|
`title`|`string`|
`max_length`|`integer` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`summarize_article_section`**
Get a summary of a specific section of a Wikipedia article.

Returns a dictionary containing the section summary or an error.
Parameters|Type|Description
-|-|-
`section_title`|`string`|
`title`|`string`|
`max_length`|`integer` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`test_wikipedia_connectivity`**
Provide diagnostics for Wikipedia API connectivity.

Returns the base API URL, language, site information, and response
time in milliseconds. If connectivity fails, status will be 'failed'
with error details.
#### Tool: **`wikipedia_extract_key_facts`**
Extract key facts from a Wikipedia article, optionally focused on a topic.

Returns a dictionary containing a list of facts.
Parameters|Type|Description
-|-|-
`title`|`string`|
`count`|`integer` *optional*|
`topic_within_article`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_get_article`**
Get the full content of a Wikipedia article.

Returns a dictionary containing article details or an error message
if retrieval fails.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_get_coordinates`**
Get the coordinates of a Wikipedia article.

Returns a dictionary containing coordinate information.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_get_links`**
Get the links contained within a Wikipedia article.

Returns a dictionary with the article title and list of links.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_get_related_topics`**
Get topics related to a Wikipedia article based on links and categories.

Returns a list of related topics up to the specified limit.
Parameters|Type|Description
-|-|-
`title`|`string`|
`limit`|`integer` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_get_sections`**
Get the sections of a Wikipedia article.

Returns a dictionary with the article title and list of sections.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_get_summary`**
Get a summary of a Wikipedia article.

Returns a dictionary with the title and summary string. On error,
includes an error message instead of a summary.
Parameters|Type|Description
-|-|-
`title`|`string`|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_search_wikipedia`**
Search Wikipedia for articles matching a query.
Parameters|Type|Description
-|-|-
`query`|`string`|The search term to look up on Wikipedia.
`limit`|`integer` *optional*|Maximum number of results to return (1-500).

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_summarize_article_for_query`**
Get a summary of a Wikipedia article tailored to a specific query.

The summary is a snippet around the query within the article text or
summary. The max_length parameter controls the length of the snippet.
Parameters|Type|Description
-|-|-
`query`|`string`|
`title`|`string`|
`max_length`|`integer` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_summarize_article_section`**
Get a summary of a specific section of a Wikipedia article.

Returns a dictionary containing the section summary or an error.
Parameters|Type|Description
-|-|-
`section_title`|`string`|
`title`|`string`|
`max_length`|`integer` *optional*|

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`wikipedia_test_wikipedia_connectivity`**
Provide diagnostics for Wikipedia API connectivity.

Returns the base API URL, language, site information, and response
time in milliseconds. If connectivity fails, status will be 'failed'
with error details.
