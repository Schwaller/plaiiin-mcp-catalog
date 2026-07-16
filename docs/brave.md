Search the Web for pages, images, news, videos, and more using the Brave Search API.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/brave-search](https://hub.docker.com/repository/docker/mcp/brave-search)
**Author**|[brave](https://github.com/brave)
**Repository**|https://github.com/brave/brave-search-mcp-server

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`brave_image_search`|Brave Image Search|
`brave_llm_context`|Brave LLM Context|
`brave_local_search`|Brave Local Search|
`brave_news_search`|Brave News Search|
`brave_place_search`|Brave Place Search|
`brave_summarizer`|Brave Summarizer|
`brave_video_search`|Brave Video Search|
`brave_web_search`|Brave Web Search|

---
## Tools Details

#### Tool: **`brave_image_search`**
Performs an image search using the Brave Search API. Helpful for when you need pictures of people, places, things, graphic design ideas, art inspiration, and more. When relaying results in a markdown environment, it may be helpful to include images in the results (e.g., ![image.title](image.properties.url)).
Parameters|Type|Description
-|-|-
`query`|`string`|The user's search query. Query cannot be empty. Limited to 400 characters and 50 words.
`count`|`integer` *optional*|Number of results (1-200, default 50). Combine this parameter with `offset` to paginate search results.
`country`|`string` *optional*|Search query country, where the results come from. The country string is limited to 2 character country codes of supported countries.
`safesearch`|`string` *optional*|Filters search results for adult content. The following values are supported: 'off' - No filtering. 'strict' - Drops all adult content from search results.
`search_lang`|`string` *optional*|Search language preference. The 2 or more character language code for which the search results are provided.
`spellcheck`|`boolean` *optional*|Whether to spellcheck provided query.

*This tool interacts with external entities.*

---
#### Tool: **`brave_llm_context`**
Retrieves pre-extracted, relevance-ranked web content using Brave's LLM Context API, optimized for AI agents, LLM grounding, and RAG pipelines. Unlike a traditional web search that returns links and short descriptions, this tool returns the actual substance of matching pages — text chunks, tables, code blocks, and structured data — so the model can reason over it directly.

    When to use:
        - Grounding answers in fresh, relevant web content (RAG)
        - Giving an AI agent ready-to-use page content from a single search call
        - Question answering and fact-checking against current sources
        - Gathering source material for research without manually fetching pages
        - When you need the contents of pages, not just titles, descriptions, and URLs

    When relaying results in markdown-supporting environments, cite the source URLs from the "sources" map.
Parameters|Type|Description
-|-|-
`query`|`string`|The user's search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.
`accept`|`string` *optional*|The default supported media type is application/json.
`api-version`|`string` *optional*|The API version to use. This is denoted by the format YYYY-MM-DD. Default is the latest that is available. Read more about API versioning at https://api-dashboard.search.brave.com/documentation/guides/versioning.
`cache-control`|`string` *optional*|Brave Search will return cached content by default. To prevent caching set the Cache-Control header to no-cache. This is currently done as best effort.
`context_threshold_mode`|`string` *optional*|The mode to use to determine the threshold for including content in context. Default is balanced.
`count`|`integer` *optional*|The maximum number of search results considered to select the LLM context data. The default is 20 and the maximum is 50.
`country`|`string` *optional*|The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries.
`enable_local`|`boolean` *optional*|Whether to enable local recall. Not setting this value means auto-detect and uses local recall if any of the localization headers are provided.
`enable_source_metadata`|`boolean` *optional*|Enable source metadata enrichment (site_name, favicon) in the sources attribute of the response.
`freshness`|`string` *optional*|Filters search results by when they were discovered. The following values are supported: 'pd' - Discovered within the last 24 hours. 'pw' - Discovered within the last 7 days. 'pm' - Discovered within the last 31 days. 'py' - Discovered within the last 365 days. 'YYYY-MM-DDtoYYYY-MM-DD' - Timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30.
`goggles`|`string` *optional*|Goggles act as a custom re-ranking on top of Brave's search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. Multiple goggle URLs and/or definitions can be provided in an array. For more details, refer to the Goggles repository (i.e., https://github.com/brave/goggles-quickstart).
`maximum_number_of_snippets`|`integer` *optional*|Maximum number of different snippets (or chunks of text) to include in LLM context. The default is 50 and maximum is 256.
`maximum_number_of_snippets_per_url`|`integer` *optional*|Maximum number of snippets to include per URL. The default is 50 and maximum is 100.
`maximum_number_of_tokens`|`integer` *optional*|Approximate maximum number of tokens to include in context. The default is 8192 and maximum is 32768.
`maximum_number_of_tokens_per_url`|`integer` *optional*|Maximum number of tokens to include per URL. The default is 4096 and maximum is 8192.
`maximum_number_of_urls`|`integer` *optional*|Maximum number of different URLs to include in LLM context.
`search_lang`|`string` *optional*|The search language preference. The 2 or more character language code for which the search results are provided.
`spellcheck`|`boolean` *optional*|Whether to enable spellcheck on the query.
`user-agent`|`string` *optional*|The user agent originating the request. Brave search can utilize the user agent to provide a different experience depending on the device as described by the string. The user agent should follow the commonly used browser agent strings on each platform. For more information on curating user agents, see RFC 9110.
`x-loc-city`|`string` *optional*|The generic name of the client city
`x-loc-country`|`string` *optional*|The two letter country code for the client’s country. For a list of country codes, see ISO 3166-1 alpha-2
`x-loc-lat`|`number` *optional*|The latitude of the client's geographical location in degrees, to provide relevant local results. The latitude must be greater than or equal to -90.0 degrees and less than or equal to +90.0 degrees.
`x-loc-long`|`number` *optional*|The longitude of the client's geographical location in degrees, to provide relevant local results. The longitude must be greater than or equal to -180.0 and less than or equal to +180.0 degrees.
`x-loc-postal-code`|`string` *optional*|The client’s postal code
`x-loc-state`|`string` *optional*|A code which could be up to three characters, that represent the client's state/region. The region is the first-level subdivision (the broadest or least specific) of the ISO 3166-2 code.
`x-loc-state-name`|`string` *optional*|The name of the client’s state/region. The region is the first-level subdivision (the broadest or least specific) of the ISO 3166-2 code.

*This tool interacts with external entities.*

---
#### Tool: **`brave_local_search`**
Brave Local Search API provides enrichments for location search results. Access to this API is available only through the Brave Search API Pro plans; confirm the user's plan before using this tool (if the user does not have a Pro plan, use the brave_web_search tool). Searches for local businesses and places using Brave's Local Search API. Best for queries related to physical locations, businesses, restaurants, services, etc.

    Returns detailed information including:
        - Business names and addresses
        - Ratings and review counts
        - Phone numbers and opening hours

    Use this when the query implies 'near me', 'in my area', or mentions specific locations (e.g., 'in San Francisco'). This tool automatically falls back to brave_web_search if no local results are found.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query (max 400 chars, 50 words)
`count`|`integer` *optional*|Number of results (1-20, default 10). Applies only to web search results (i.e., has no effect on locations, news, videos, etc.)
`country`|`string` *optional*|Search query country, where the results come from. The country string is limited to 2 character country codes of supported countries.
`extra_snippets`|`boolean` *optional*|A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans.
`freshness`|`string` *optional*|Filters search results by when they were discovered. The following values are supported: 'pd' - Discovered within the last 24 hours. 'pw' - Discovered within the last 7 days. 'pm' - Discovered within the last 31 days. 'py' - Discovered within the last 365 days. 'YYYY-MM-DDtoYYYY-MM-DD' - Timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30.
`goggles`|`string` *optional*|Goggles act as a custom re-ranking on top of Brave's search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. Multiple goggle URLs and/or definitions can be provided in an array. For more details, refer to the Goggles repository (i.e., https://github.com/brave/goggles-quickstart).
`offset`|`integer` *optional*|Pagination offset (max 9, default 0)
`result_filter`|`array` *optional*|Result filter (default ['web', 'query'])
`safesearch`|`string` *optional*|Filters search results for adult content. The following values are supported: 'off' - No filtering. 'moderate' - Filters explicit content (e.g., images and videos), but allows adult domains in search results. 'strict' - Drops all adult content from search results. The default value is 'moderate'.
`search_lang`|`string` *optional*|Search language preference. The 2 or more character language code for which the search results are provided.
`spellcheck`|`boolean` *optional*|Whether to spellcheck the provided query.
`summary`|`boolean` *optional*|This parameter enables summary key generation in web search results. This is required for summarizer to be enabled.
`text_decorations`|`boolean` *optional*|Whether display strings (e.g. result snippets) should include decoration markers (e.g. highlighting characters).
`ui_lang`|`string` *optional*|The language of the UI. The 2 or more character language code for which the search results are provided.
`units`|`string` *optional*|The measurement units. If not provided, units are derived from search country.

*This tool interacts with external entities.*

---
#### Tool: **`brave_news_search`**
This tool searches for news articles using Brave's News Search API based on the user's query. Use it when you need current news information, breaking news updates, or articles about specific topics, events, or entities.

    When to use:
        - Finding recent news articles on specific topics
        - Getting breaking news updates
        - Researching current events or trending stories
        - Gathering news sources and headlines for analysis

    Returns a JSON list of news-related results with title, url, and description. Some results may contain snippets of text from the article.

    When relaying results in markdown-supporting environments, always cite sources with hyperlinks.

    Examples:
        - "According to [Reuters](https://www.reuters.com/technology/china-bans/), China bans uncertified and recalled power banks on planes".
        - "The [New York Times](https://www.nytimes.com/2025/06/27/us/technology/ev-sales.html) reports that Tesla's EV sales have increased by 20%".
        - "According to [BBC News](https://www.bbc.com/news/world-europe-65910000), the UK government has announced a new policy to support renewable energy".
Parameters|Type|Description
-|-|-
`query`|`string`|Search query (max 400 chars, 50 words)
`count`|`integer` *optional*|Number of results (1-50, default 20)
`country`|`string` *optional*|Search query country, where the results come from. The country string is limited to 2 character country codes of supported countries.
`extra_snippets`|`boolean` *optional*|A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans.
`freshness`|`string` *optional*|Filters search results by when they were discovered. The following values are supported: 'pd' - Discovered within the last 24 hours. 'pw' - Discovered within the last 7 Days. 'pm' - Discovered within the last 31 Days. 'py' - Discovered within the last 365 Days. 'YYYY-MM-DDtoYYYY-MM-DD' - Timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30.
`goggles`|`string` *optional*|Goggles act as a custom re-ranking on top of Brave's search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. Multiple goggle URLs and/or definitions can be provided in an array. For more details, refer to the Goggles repository (i.e., https://github.com/brave/goggles-quickstart).
`offset`|`integer` *optional*|Pagination offset (max 9, default 0)
`safesearch`|`string` *optional*|Filters search results for adult content. The following values are supported: 'off' - No filtering. 'moderate' - Filter out explicit content. 'strict' - Filter out explicit and suggestive content. The default value is 'moderate'.
`search_lang`|`string` *optional*|Search language preference. The 2 or more character language code for which the search results are provided.
`spellcheck`|`boolean` *optional*|Whether to spellcheck provided query.
`ui_lang`|`string` *optional*|User interface language preferred in response. Usually of the format <language_code>-<country_code>. For more, see RFC 9110.

*This tool interacts with external entities.*

---
#### Tool: **`brave_place_search`**
Searches Brave's Place Search API. A single call may populate any combination of 'results' (POIs), 'cities', 'addresses', 'streets', and 'location' (the resolved search area), depending on the query's shape.

    When to use:
        - POIs near coordinates or a named area (e.g. "coffee shops in Paris") -> 'results', each with structured business data (postal address, hours, contact, ratings, photos, categories, timezone).
        - Browsing general POIs (omit 'query'; supply 'latitude'+'longitude' or 'location').
        - Disambiguating a bare city name (e.g. "springfield") -> 'cities'.
        - Resolving a specific address (e.g. "350 5th avenue" with NYC coords) -> 'addresses' (often plus 'streets').
        - Looking up a street by name (e.g. "michigan avenue" with Chicago coords) -> 'streets'.

    Inputs:
        - Anchor the search via 'latitude'+'longitude' or 'location' (or both). With neither, 'query' is required.
        - 'addresses' / 'streets' only surface when the query is address-/street-shaped AND geographically anchored.
        - 'location' format: US -- '<city> <state> <country>' (e.g. 'san francisco ca united states'); non-US -- '<city> <country>' (e.g. 'tokyo japan'). Capitalization and commas don't matter.
        - 'count' caps results (max 50, default 20). 'radius' (meters) biases toward closer results; it does NOT hard-limit the search area.
Parameters|Type|Description
-|-|-
`accept`|`string` *optional*|The default supported media type is application/json.
`api-version`|`string` *optional*|The API version to use. This is denoted by the format YYYY-MM-DD. Default is the latest that is available. Read more about API versioning at https://api-dashboard.search.brave.com/documentation/guides/versioning.
`cache-control`|`string` *optional*|Brave Search will return cached content by default. To prevent caching set the Cache-Control header to no-cache. This is currently done as best effort.
`count`|`integer` *optional*|Number of results to return. Maximum is 50. Default is 20.
`country`|`string` *optional*|Two-letter country code (ISO 3166-1 alpha-2) used to scope the search. Defaults to 'US'.
`geoloc`|`string` *optional*|Optional geolocation token used to refine results.
`latitude`|`number` *optional*|Latitude of the geographical coordinates around which to search, in degrees (-90 to 90). Typically paired with `longitude`.
`location`|`string` *optional*|Location string to search around, used as an alternative to `latitude` and `longitude`. For US locations prefer the form '<city> <state> <country name>' (e.g. 'san francisco ca united states'); for non-US locations use '<city> <country name>' (e.g. 'tokyo japan'). No commas or special characters needed; capitalization does not matter.
`longitude`|`number` *optional*|Longitude of the geographical coordinates around which to search, in degrees (-180 to 180). Typically paired with `latitude`.
`query`|`string` *optional*|Query string. Shape influences the response: POI-like queries -> `results`; bare/ambiguous city names -> `cities`; address- or street-shaped queries with a geographic anchor -> `addresses` and/or `streets`. If omitted, returns general POIs in the supplied area.
`radius`|`number` *optional*|Bias toward results closer to the supplied coordinates, in meters. NOT a hard cutoff -- the API may still return more distant results. If omitted, the search is performed globally.
`safesearch`|`string` *optional*|Safe search level for the query results. 'off' - No filtering. 'moderate' - Filter out explicit content. 'strict' - Filter out explicit and suggestive content. Defaults to 'strict'.
`search_lang`|`string` *optional*|Language for the search results. Defaults to 'en'.
`spellcheck`|`boolean` *optional*|Whether to apply spellcheck before executing the search. Defaults to true.
`ui_lang`|`string` *optional*|User interface language for the response, usually of the form '<language>-<region>'. Defaults to 'en-US'.
`units`|`string` *optional*|Units of measurement for distance values. Defaults to 'metric'.
`user-agent`|`string` *optional*|The user agent originating the request. Brave Search can utilize the user agent to provide a different experience depending on the device as described by the string. The user agent should follow the commonly used browser agent strings on each platform. For more information on curating user agents, see RFC 9110.

*This tool interacts with external entities.*

---
#### Tool: **`brave_summarizer`**
Retrieves AI-generated summaries of web search results using Brave's Summarizer API. This tool processes search results to create concise, coherent summaries of information gathered from multiple sources.

    When to use:

    - When you need a concise overview of complex topics from multiple sources
    - For quick fact-checking or getting key points without reading full articles
    - When providing users with summarized information that synthesizes various perspectives
    - For research tasks requiring distilled information from web searches

    Returns a text summary that consolidates information from the search results. Optional features include inline references to source URLs and additional entity information.

    Requirements: Must first perform a web search using brave_web_search with summary=true parameter. Requires a Pro AI subscription to access the summarizer functionality.
Parameters|Type|Description
-|-|-
`key`|`string`|The key is equal to value of field key as part of the Summarizer response model.
`entity_info`|`boolean` *optional*|Returns extra entities info with the summary response.
`inline_references`|`boolean` *optional*|Adds inline references to the summary response.

*This tool interacts with external entities.*

---
#### Tool: **`brave_video_search`**
Searches for videos using Brave's Video Search API and returns structured video results with metadata.

    When to use:
        - When you need to find videos related to a specific topic, keyword, or query.
        - Useful for discovering video content, getting video metadata, or finding videos from specific creators/publishers.

    Returns a JSON list of video-related results with title, url, description, duration, and thumbnail_url.
Parameters|Type|Description
-|-|-
`query`|`string`|The user's search query. Query cannot be empty. Limited to 400 characters and 50 words.
`count`|`integer` *optional*|Number of results (1-50, default 20). Combine this parameter with `offset` to paginate search results.
`country`|`string` *optional*|Search query country, where the results come from. The country string is limited to 2 character country codes of supported countries.
`freshness`|`string` *optional*|Filters search results by when they were discovered. The following values are supported: 'pd' - Discovered within the last 24 hours. 'pw' - Discovered within the last 7 days. 'pm' - Discovered within the last 31 days. 'py' - Discovered within the last 365 days. 'YYYY-MM-DDtoYYYY-MM-DD' - timeframe is also supported by specifying the date range (e.g. '2022-04-01to2022-07-30').
`offset`|`integer` *optional*|Pagination offset (max 9, default 0). Combine this parameter with `count` to paginate search results.
`safesearch`|`string` *optional*|Filters search results for adult content. The following values are supported: 'off' - No filtering. 'moderate' - Filter out explicit content. 'strict' - Filter out explicit and suggestive content. The default value is 'moderate'.
`search_lang`|`string` *optional*|Search language preference. The 2 or more character language code for which the search results are provided.
`spellcheck`|`boolean` *optional*|Whether to spellcheck provided query.
`ui_lang`|`string` *optional*|User interface language preferred in response. Usually of the format <language_code>-<country_code>. For more, see RFC 9110.

*This tool interacts with external entities.*

---
#### Tool: **`brave_web_search`**
Performs web searches using the Brave Search API and returns comprehensive search results with rich metadata.

    When to use:
        - General web searches for information, facts, or current topics
        - Location-based queries (restaurants, businesses, points of interest)
        - News searches for recent events or breaking stories
        - Finding videos, discussions, or FAQ content
        - Research requiring diverse result types (web pages, images, reviews, etc.)

    Returns a JSON list of web results with title, description, and URL.

    When the "results_filter" parameter is empty, JSON results may also contain FAQ, Discussions, News, and Video results.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query (max 400 chars, 50 words)
`count`|`integer` *optional*|Number of results (1-20, default 10). Applies only to web search results (i.e., has no effect on locations, news, videos, etc.)
`country`|`string` *optional*|Search query country, where the results come from. The country string is limited to 2 character country codes of supported countries.
`extra_snippets`|`boolean` *optional*|A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans.
`freshness`|`string` *optional*|Filters search results by when they were discovered. The following values are supported: 'pd' - Discovered within the last 24 hours. 'pw' - Discovered within the last 7 days. 'pm' - Discovered within the last 31 days. 'py' - Discovered within the last 365 days. 'YYYY-MM-DDtoYYYY-MM-DD' - Timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30.
`goggles`|`string` *optional*|Goggles act as a cust

[...]
