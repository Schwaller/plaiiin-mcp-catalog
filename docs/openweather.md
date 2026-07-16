A simple MCP service that provides current weather and 5-day forecast using the free OpenWeatherMap API.
.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/openweather](https://hub.docker.com/repository/docker/mcp/openweather)
**Author**|[mschneider82](https://github.com/mschneider82)
**Repository**|https://github.com/mschneider82/mcp-openweather

## Available Tools (1)
Tools provided by this Server|Short Description
-|-
`weather`|Retrieves current and forecast weather information for a given location.|

---
## Tools Details

#### Tool: **`weather`**
Retrieves current and forecast weather information for a given location.
Parameters|Type|Description
-|-|-
`city`|`string`|The name of the city to get weather for.
Must be in English.
Example: For Saint Petersburg, use "Saint Petersburg", not "Санкт-Петербург".
`lang`|`string` *optional*|The language for the weather description text. Use standard two-letter language codes (e.g., "en", "es", "zh_CN"). Default: "en".
`units`|`string` *optional*|The unit for temperature. Use "c" for Celsius, "f" for Fahrenheit, or "k" for Kelvin. Default: "c".

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
