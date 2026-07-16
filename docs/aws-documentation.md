Tools to access AWS documentation, search for content, and get recommendations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-documentation](https://hub.docker.com/repository/docker/mcp/aws-documentation)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (4)
Tools provided by this Server|Short Description
-|-
`read_documentation`|Fetch and convert an AWS documentation page to markdown format.|
`read_sections`|Extract specific sections from AWS documentation pages by title.|
`recommend`|Get content recommendations for an AWS documentation page.|
`search_documentation`|Search AWS documentation using the official AWS Documentation Search API.|

---
## Tools Details

#### Tool: **`read_documentation`**
Fetch and convert an AWS documentation page to markdown format.

## Usage

This tool retrieves the content of an AWS documentation page and converts it to markdown format.
For long documents, you can make multiple calls with different start_index values to retrieve
the entire content in chunks.

## URL Requirements

- Must be from the docs.aws.amazon.com domain
- Must end with .html

## Example URLs

- https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html

## Output Format

The output is formatted as markdown text with:
- Preserved headings and structure
- Code blocks for examples
- Lists and tables converted to markdown format

## Handling Long Documents

If the response indicates the document was truncated, you have several options:

1. **Continue Reading**: Make another call with start_index set to the end of the previous response
2. **Stop Early**: For very long documents (>30,000 characters), if you've already found the specific information needed, you can stop reading
Parameters|Type|Description
-|-|-
`url`|`string`|URL of the AWS documentation page to read
`max_length`|`integer` *optional*|Maximum number of characters to return.
`start_index`|`integer` *optional*|On return output starting at this character index, useful if a previous fetch was truncated and more content is required.

---
#### Tool: **`read_sections`**
Extract specific sections from AWS documentation pages by title.

Retrieves a page, converts to markdown, and returns only matching sections.
Section matching is case-insensitive and handles whitespace differences.

## URL Requirements
- Must end with .html

## Read Sections Tips

- Use exact section titles from search results 'sections' field when available
- Section matching is case-insensitive and handles whitespace differences
- Include multiple related sections in one call for comprehensive coverage

## Example Usage

```
# If query is about S3 bucket naming rules:
# Available sections: ['General purpose buckets naming rules', 'Example general purpose bucket names', 'Best practices', 'Creating a bucket that uses a GUID in the bucket name']
# Read these specific sections:
read_sections(
    url='https://docs.aws.amazon.com/s3/latest/userguide/bucketnamingrules.html',
    section_titles=['General purpose buckets naming rules', 'Best practices'],
)

# If query is about Python Lambda function examples:
# Available sections: ['Example Python Lambda function code', 'Handler naming conventions', 'Using the Lambda event object', 'Accessing and using the Lambda context object'. 'Valid handler signatures for Python handlers', 'Returning a value', 'Using the AWS SDK for Python (Boto3) in your handler', 'Accessing environment variables, 'Code best practices for Python Lambda functions']
# Read these specific sections:
read_sections(
    url='https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html',
    section_titles=[
        'Example Python Lambda function code',
        'Code best practices for Python Lambda functions',
    ],
)
```
Parameters|Type|Description
-|-|-
`section_titles`|`array`|List of section titles to extract from the documentation
`url`|`string`|URL of the AWS documentation page to read

---
#### Tool: **`recommend`**
Get content recommendations for an AWS documentation page.

## Usage

This tool provides recommendations for related AWS documentation pages based on a given URL.
Use it to discover additional relevant content that might not appear in search results.

## Recommendation Types

The recommendations include four categories:

1. **Highly Rated**: Popular pages within the same AWS service
2. **New**: Recently added pages within the same AWS service - useful for finding newly released features
3. **Similar**: Pages covering similar topics to the current page
4. **Journey**: Pages commonly viewed next by other users

## When to Use

- After reading a documentation page to find related content
- When exploring a new AWS service to discover important pages
- To find alternative explanations of complex concepts
- To discover the most popular pages for a service
- To find newly released information by using a service's welcome page URL and checking the **New** recommendations

## Finding New Features

To find newly released information about a service:
1. Find any page belong to that service, typically you can try the welcome page
2. Call this tool with that URL
3. Look specifically at the **New** recommendation type in the results

## Result Interpretation

Each recommendation includes:
- url: The documentation page URL
- title: The page title
- context: A brief description (if available)
Parameters|Type|Description
-|-|-
`url`|`string`|URL of the AWS documentation page to get recommendations for

---
#### Tool: **`search_documentation`**
Search AWS documentation using the official AWS Documentation Search API.

## Usage

This tool searches across all AWS documentation for pages matching your search phrase.
Use it to find relevant documentation when you don't have a specific URL.

## Search Tips

- Use specific technical terms rather than general phrases
- Include service names to narrow results (e.g., "S3 bucket versioning" instead of just "versioning")
- Use quotes for exact phrase matching (e.g., "AWS Lambda function URLs")
- Include abbreviations and alternative terms to improve results
- Use guide_type and product_type filters found from a SearchResponse's "facets" property:
    - Filter only for broad search queries with patterns:
        - "What is [service]?" -> product_types: ["Amazon Simple Storage Service"]
        - "How to use <service 1> with <service 2>?" -> product_types: [<service 1>, <service 2>]
        - "[service] getting started" -> product_types: [<service>] + guide_types: ["User Guide, "Developer Guide"]
        - "API reference for [service]" -> product_types: [<service>] + guide_types: ["API Reference"]

## Result Interpretation

Each SearchResponse includes:
- search_results: List of documentation pages, each with:
    - rank_order: The relevance ranking (lower is more relevant)
    - url: The documentation page URL
    - title: The page title
    - context: A brief excerpt or summary (if available)
    - recommended_sections: A subset of section titles ranked as most relevant to the query, in rank order (when available) - Pass these directly to read_sections for targeted content extraction
    - sections: All available section titles for this page (when available) - individual titles can be used with the read_sections tool for targeted content extraction
    - metadata: Optional per-result context (when available). May include:
        - additional_urls: Other doc URLs related to the same result `{url, section_title, section_anchor}` - pass `section_title` to read_sections to fetch content; use `url#section_anchor` when citing
- facets: Available filters (product_types, guide_types) for refining searches
- query_id: Unique identifier for this search session
- metadata: Optional response-level context (when available). May include:
    - discovered_services: AWS services inferred from the query that may be relevant beyond the top results
    - related_tasks: Related operations or workflows the user may want to follow up on, each with its own doc URLs
    - relationships: Named connections between information in the search results, useful for understanding how the returned topics relate to each other
Parameters|Type|Description
-|-|-
`search_phrase`|`string`|Search phrase to use
`guide_types`|`string` *optional*|Filter results by guide type (e.g., ["User Guide", "API Reference", "Developer Guide"])
`limit`|`integer` *optional*|Maximum number of results to return
`product_types`|`string` *optional*|Filter results by AWS product/service (e.g., ["Amazon Simple Storage Service"])
`search_intent`|`string` *optional*|For the search_phrase parameter, describe the search intent of the user. CRITICAL: Do not include any PII or customer data, describe only the AWS-related intent for search.

---

## Screenshots

![AWS Documentation screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/aws-documentation-1.png)

![AWS Documentation screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/aws-documentation-2.png)

![AWS Documentation screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/aws-documentation-3.png)
