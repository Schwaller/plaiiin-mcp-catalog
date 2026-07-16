Enterprise search and RAG enhancement.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/amazon-kendra-index-mcp-server](https://hub.docker.com/repository/docker/mcp/amazon-kendra-index-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`KendraListIndexesTool`|List all Amazon Kendra indexes in the specified region.|
`KendraQueryTool`|Query Amazon Kendra and retrieve content from the response.|

---
## Tools Details

#### Tool: **`KendraListIndexesTool`**
List all Amazon Kendra indexes in the specified region.

This tool lists all the Kendra indexes available in the region specified in the mcp configuration.

Parameters:
    region (str, optional): The AWS region to list Kendra indexes from.

Returns:
    Dict containing the list of Kendra indexes.
Parameters|Type|Description
-|-|-
`region`|`string` *optional*|

---
#### Tool: **`KendraQueryTool`**
Query Amazon Kendra and retrieve content from the response.

This tool queries the specified Amazon Kendra index with the provided query
and returns the search results. The specified Kendra Index is either provided by the user in the chat, or the default index configured in the environemnt variables

Parameters:
    query (str): The search query to send to Amazon Kendra.
    region (str): The region of the Kendra Index to send the search query to.
    indexId (str): The indexId of the Kendra index to send the search query to.

Returns:
    Dict containing the query results from Amazon Kendra.
Parameters|Type|Description
-|-|-
`query`|`string`|
`indexId`|`string` *optional*|
`region`|`string` *optional*|

---

## Screenshots

![Amazon Kendra Index screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/amazon-kendra-index-1.png)

![Amazon Kendra Index screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/amazon-kendra-index-2.png)

![Amazon Kendra Index screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/amazon-kendra-index-3.png)
