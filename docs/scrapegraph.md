ScapeGraph MCP Server.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/scrapegraph](https://hub.docker.com/repository/docker/mcp/scrapegraph)
**Author**|[ScrapeGraphAI](https://github.com/ScrapeGraphAI)
**Repository**|https://github.com/ScrapeGraphAI/scrapegraph-mcp

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`agentic_scrapper`|Execute complex multi-step web scraping workflows with AI-powered automation.|
`markdownify`|Convert a webpage into clean, formatted markdown.|
`scrape`|Fetch raw page content from any URL with optional JavaScript rendering.|
`searchscraper`|Perform AI-powered web searches with structured data extraction.|
`sitemap`|Extract and discover the complete sitemap structure of any website.|
`smartcrawler_fetch_results`|Retrieve the results of an asynchronous SmartCrawler operation.|
`smartcrawler_initiate`|Initiate an asynchronous multi-page web crawling operation with AI extraction or markdown conversion.|
`smartscraper`|Extract structured data from a webpage, HTML, or markdown using AI-powered extraction.|

---
## Tools Details

#### Tool: **`agentic_scrapper`**
Execute complex multi-step web scraping workflows with AI-powered automation.

This tool runs an intelligent agent that can navigate websites, interact with forms and buttons,
follow multi-step workflows, and extract structured data. Ideal for complex scraping scenarios
requiring user interaction simulation, form submissions, or multi-page navigation flows.
Supports custom output schemas and step-by-step instructions. Variable credit cost based on
complexity. Can perform actions on the website (non-read-only, non-idempotent).

The agent accepts flexible input formats for steps (list or JSON string) and output_schema
(dict or JSON string) to accommodate different client implementations.
Parameters|Type|Description
-|-|-
`url`|`string`|
`ai_extraction`|`string` *optional*|
`output_schema`|`string` *optional*|
`persistent_session`|`string` *optional*|
`steps`|`string` *optional*|
`timeout_seconds`|`string` *optional*|
`user_prompt`|`string` *optional*|

---
#### Tool: **`markdownify`**
Convert a webpage into clean, formatted markdown.

This tool fetches any webpage and converts its content into clean, readable markdown format.
Useful for extracting content from documentation, articles, and web pages for further processing.
Costs 2 credits per page. Read-only operation with no side effects.
Parameters|Type|Description
-|-|-
`website_url`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`scrape`**
Fetch raw page content from any URL with optional JavaScript rendering.

This tool performs basic web scraping to retrieve the raw HTML content of a webpage.
Optionally enable JavaScript rendering for Single Page Applications (SPAs) and sites with
heavy client-side rendering. Lower cost than AI extraction (1 credit/page).
Read-only operation with no side effects.
Parameters|Type|Description
-|-|-
`website_url`|`string`|
`render_heavy_js`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`searchscraper`**
Perform AI-powered web searches with structured data extraction.

This tool searches the web based on your query and uses AI to extract structured information
from the search results. Ideal for research, competitive analysis, and gathering information
from multiple sources. Each website searched costs 10 credits (default 3 websites = 30 credits).
Read-only operation but results may vary over time (non-idempotent).
Parameters|Type|Description
-|-|-
`user_prompt`|`string`|
`num_results`|`string` *optional*|
`number_of_scrolls`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`sitemap`**
Extract and discover the complete sitemap structure of any website.

This tool automatically discovers all accessible URLs and pages within a website, providing
a comprehensive map of the site's structure. Useful for understanding site architecture before
crawling or for discovering all available content. Very cost-effective at 1 credit per request.
Read-only operation with no side effects.
Parameters|Type|Description
-|-|-
`website_url`|`string`|

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`smartcrawler_fetch_results`**
Retrieve the results of an asynchronous SmartCrawler operation.

This tool fetches the results from a previously initiated crawling operation using the request_id.
The crawl request processes asynchronously in the background. Keep polling this endpoint until
the status field indicates 'completed'. While processing, you'll receive status updates.
Read-only operation that safely retrieves results without side effects.
Parameters|Type|Description
-|-|-
`request_id`|`string`|The unique request ID returned by smartcrawler_initiate. Use this to retrieve the crawling results. Keep polling until status is 'completed'. Example: 'req_abc123xyz'

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`smartcrawler_initiate`**
Initiate an asynchronous multi-page web crawling operation with AI extraction or markdown conversion.

This tool starts an intelligent crawler that discovers and processes multiple pages from a starting URL.
Choose between AI Extraction Mode (10 credits/page) for structured data or Markdown Mode (2 credits/page)
for content conversion. The operation is asynchronous - use smartcrawler_fetch_results to retrieve results.
Creates a new crawl request (non-idempotent, non-read-only).

SmartCrawler supports two modes:
- AI Extraction Mode: Extracts structured data based on your prompt from every crawled page
- Markdown Conversion Mode: Converts each page to clean markdown format
Parameters|Type|Description
-|-|-
`url`|`string`|
`depth`|`string` *optional*|
`extraction_mode`|`string` *optional*|
`max_pages`|`string` *optional*|
`prompt`|`string` *optional*|
`same_domain_only`|`string` *optional*|

---
#### Tool: **`smartscraper`**
Extract structured data from a webpage, HTML, or markdown using AI-powered extraction.

    This tool uses advanced AI to understand your natural language prompt and extract specific
    structured data from web content. Supports three input modes: URL scraping, local HTML processing,
    or local markdown processing. Ideal for extracting product information, contact details,
    article metadata, or any structured content. Costs 10 credits per page. Read-only operation.
Parameters|Type|Description
-|-|-
`user_prompt`|`string`|
`number_of_scrolls`|`string` *optional*|
`output_schema`|`string` *optional*|
`render_heavy_js`|`string` *optional*|
`stealth`|`string` *optional*|
`total_pages`|`string` *optional*|
`website_html`|`string` *optional*|
`website_markdown`|`string` *optional*|
`website_url`|`string` *optional*|

*This tool is read-only. It does not modify its environment.*

---

## Screenshots

![ScrapeGraph screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/scrapegraph-1.png)
