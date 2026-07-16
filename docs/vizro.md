provides tools and templates to create a functioning Vizro chart or dashboard step by step.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/vizro](https://hub.docker.com/repository/docker/mcp/vizro)
**Author**|[mckinsey](https://github.com/mckinsey)
**Repository**|https://github.com/mckinsey/vizro

## Available Tools (6)
Tools provided by this Server|Short Description
-|-
`get_model_json_schema`|Get the JSON schema for the specified Vizro model.|
`get_sample_data_info`|If user provides no data, use this tool to get sample data information.|
`get_vizro_chart_or_dashboard_plan`|Get instructions for creating a Vizro chart or dashboard.|
`load_and_analyze_data`|Use to understand local or remote data files.|
`validate_chart_code`|Validate the chart code created by the user and optionally open the PyCafe link in a browser.|
`validate_dashboard_config`|Validate Vizro model configuration.|

---
## Tools Details

#### Tool: **`get_model_json_schema`**
Get the JSON schema for the specified Vizro model. Server Vizro version: 0.1.46
Parameters|Type|Description
-|-|-
`model_name`|`string`|Name of the Vizro model to get schema for (e.g., 'Card', 'Dashboard', 'Page')

---
#### Tool: **`get_sample_data_info`**
If user provides no data, use this tool to get sample data information.

    Use the following data for the below purposes:
        - iris: mostly numerical with one categorical column, good for scatter, histogram, boxplot, etc.
        - tips: contains mix of numerical and categorical columns, good for bar, pie, etc.
        - stocks: stock prices, good for line, scatter, generally things that change over time
        - gapminder: demographic data, good for line, scatter, generally things with maps or many categories

    Returns:
        Data info object containing information about the dataset.
Parameters|Type|Description
-|-|-
`data_name`|`string`|Name of the dataset to get sample data for

---
#### Tool: **`get_vizro_chart_or_dashboard_plan`**
Get instructions for creating a Vizro chart or dashboard. Call FIRST when asked to create Vizro things.

    Must be ALWAYS called FIRST with advanced_mode=False, then call again with advanced_mode=True
    if the JSON config does not suffice anymore.

    Returns:
        Instructions for creating a Vizro chart or dashboard
Parameters|Type|Description
-|-|-
`user_host`|`string`|The host the user is using, if 'ide' you can use the IDE/editor to run python code
`user_plan`|`string`|The type of Vizro thing the user wants to create
`advanced_mode`|`boolean` *optional*|Only call if you need to use custom CSS, custom components or custom actions.
No need to call this with advanced_mode=True if you need advanced charts,
use `custom_charts` in the `validate_dashboard_config` tool instead.

---
#### Tool: **`load_and_analyze_data`**
Use to understand local or remote data files. Must be called with absolute paths or URLs.

    Supported formats:
    - CSV (.csv)
    - JSON (.json)
    - HTML (.html, .htm)
    - Excel (.xls, .xlsx)
    - OpenDocument Spreadsheet (.ods)
    - Parquet (.parquet)

    Returns:
        DataAnalysisResults object containing DataFrame information and metadata
Parameters|Type|Description
-|-|-
`path_or_url`|`string`|Absolute (important!) local file path or URL to a data file

---
#### Tool: **`validate_chart_code`**
Validate the chart code created by the user and optionally open the PyCafe link in a browser.

    Returns:
        ValidationResults object with status and dashboard details
Parameters|Type|Description
-|-|-
`chart_config`|`string`|A ChartPlan object with the chart configuration
`data_info`|`string`|Metadata for the dataset to be used in the chart
`auto_open`|`boolean` *optional*|Whether to automatically open the PyCafe link in a browser

---
#### Tool: **`validate_dashboard_config`**
Validate Vizro model configuration. Run ALWAYS when you have a complete dashboard configuration.

    If successful, the tool will return the python code and, if it is a remote file, the py.cafe link to the chart.
    The PyCafe link will be automatically opened in your default browser if auto_open is True.

    Returns:
        ValidationResults object with status and dashboard details
Parameters|Type|Description
-|-|-
`custom_charts`|`array`|List of ChartPlan objects containing information about the custom charts in the dashboard
`dashboard_config`|`object`|Either a JSON string or a dictionary representing a Vizro dashboard model configuration
`data_infos`|`array`|List of DFMetaData objects containing information about the data files
`auto_open`|`boolean` *optional*|Whether to automatically open the PyCafe link in a browser

---

## Screenshots

![Vizro screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/vizro-1.png)

![Vizro screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/vizro-2.png)

![Vizro screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/vizro-3.png)
