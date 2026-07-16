MCP server to interact with the data feeds provided by the Nasdaq Data Link. Developed by the community and maintained by Stefano Amorelli.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/nasdaq-data-link](https://hub.docker.com/repository/docker/mcp/nasdaq-data-link)
**Author**|[stefanoamorelli](https://github.com/stefanoamorelli)
**Repository**|https://github.com/stefanoamorelli/nasdaq-data-link-mcp

## Available Tools (5)
Tools provided by this Server|Short Description
-|-
`export_dataset`|Export dataset in different formats.|
`get_dataset`|Get data from a specific dataset.|
`get_dataset_metadata`|Get metadata about a dataset without downloading data.|
`list_databases`|List available databases.|
`search_datasets`|Search for datasets by keyword.|

---
## Tools Details

#### Tool: **`export_dataset`**
Export dataset in different formats.

Parameters:
  - dataset_code: Dataset code in format 'DATABASE/DATASET'
  - output_format: Export format: 'csv', 'json', or 'xml' (default: csv)
  - start_date: Optional start date in YYYY-MM-DD format
  - end_date: Optional end date in YYYY-MM-DD format

Example: export_dataset(dataset_code='WIKI/AAPL', output_format='json')
Parameters|Type|Description
-|-|-
`dataset_code`|`string`|
`end_date`|`string` *optional*|
`output_format`|`string` *optional*|
`start_date`|`string` *optional*|

---
#### Tool: **`get_dataset`**
Get data from a specific dataset.

Parameters:
  - dataset_code: Dataset code in format 'DATABASE/DATASET' (e.g., 'WIKI/AAPL')
  - start_date: Optional start date in YYYY-MM-DD format
  - end_date: Optional end date in YYYY-MM-DD format

Example: get_dataset(dataset_code='WIKI/AAPL', start_date='2020-01-01')
Parameters|Type|Description
-|-|-
`dataset_code`|`string`|
`end_date`|`string` *optional*|
`start_date`|`string` *optional*|

---
#### Tool: **`get_dataset_metadata`**
Get metadata about a dataset without downloading data.

Parameters:
  - dataset_code: Dataset code in format 'DATABASE/DATASET' (e.g., 'WIKI/AAPL')

Example: get_dataset_metadata(dataset_code='WIKI/AAPL')
Parameters|Type|Description
-|-|-
`dataset_code`|`string`|

---
#### Tool: **`list_databases`**
List available databases.

Example: list_databases()
#### Tool: **`search_datasets`**
Search for datasets by keyword.

Parameters:
  - query: Search term (e.g., 'GDP', 'stock prices', 'bitcoin')

Example: search_datasets(query='oil prices')
Parameters|Type|Description
-|-|-
`query`|`string`|

---

## Screenshots

![Nasdaq Data Link screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/nasdaq-data-link-1.gif)

![Nasdaq Data Link screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/nasdaq-data-link-2.gif)

![Nasdaq Data Link screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/nasdaq-data-link-3.gif)
