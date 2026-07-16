Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/mcp-playwright](https://hub.docker.com/repository/docker/mcp/mcp-playwright)
**Author**|[executeautomation](https://github.com/executeautomation)
**Repository**|https://github.com/executeautomation/mcp-playwright

## Available Tools (32)
Tools provided by this Server|Short Description
-|-
`clear_codegen_session`|Clear a code generation session without generating a test|
`end_codegen_session`|End a code generation session and generate the test file|
`get_codegen_session`|Get information about a code generation session|
`playwright_assert_response`|Wait for and validate a previously initiated HTTP response wait operation.|
`playwright_click`|Click an element on the page|
`playwright_click_and_switch_tab`|Click a link and switch to the newly opened tab|
`playwright_close`|Close the browser and release all resources|
`playwright_console_logs`|Retrieve console logs from the browser with filtering options|
`playwright_custom_user_agent`|Set a custom User Agent for the browser|
`playwright_delete`|Perform an HTTP DELETE request|
`playwright_drag`|Drag an element to a target location|
`playwright_evaluate`|Execute JavaScript in the browser console|
`playwright_expect_response`|Ask Playwright to start waiting for a HTTP response.|
`playwright_fill`|fill out an input field|
`playwright_get`|Perform an HTTP GET request|
`playwright_get_visible_html`|Get the HTML content of the current page.|
`playwright_get_visible_text`|Get the visible text content of the current page|
`playwright_go_back`|Navigate back in browser history|
`playwright_go_forward`|Navigate forward in browser history|
`playwright_hover`|Hover an element on the page|
`playwright_iframe_click`|Click an element in an iframe on the page|
`playwright_iframe_fill`|Fill an element in an iframe on the page|
`playwright_navigate`|Navigate to a URL|
`playwright_patch`|Perform an HTTP PATCH request|
`playwright_post`|Perform an HTTP POST request|
`playwright_press_key`|Press a keyboard key|
`playwright_put`|Perform an HTTP PUT request|
`playwright_save_as_pdf`|Save the current page as a PDF file|
`playwright_screenshot`|Take a screenshot of the current page or a specific element|
`playwright_select`|Select an element on the page with Select tag|
`playwright_upload_file`|Upload a file to an input[type='file'] element on the page|
`start_codegen_session`|Start a new code generation session to record Playwright actions|

---
## Tools Details

#### Tool: **`clear_codegen_session`**
Clear a code generation session without generating a test
Parameters|Type|Description
-|-|-
`sessionId`|`string`|ID of the session to clear

---
#### Tool: **`end_codegen_session`**
End a code generation session and generate the test file
Parameters|Type|Description
-|-|-
`sessionId`|`string`|ID of the session to end

---
#### Tool: **`get_codegen_session`**
Get information about a code generation session
Parameters|Type|Description
-|-|-
`sessionId`|`string`|ID of the session to retrieve

---
#### Tool: **`playwright_assert_response`**
Wait for and validate a previously initiated HTTP response wait operation.
Parameters|Type|Description
-|-|-
`id`|`string`|Identifier of the HTTP response initially expected using `Playwright_expect_response`.
`value`|`string` *optional*|Data to expect in the body of the HTTP response. If provided, the assertion will fail if this value is not found in the response body.

---
#### Tool: **`playwright_click`**
Click an element on the page
Parameters|Type|Description
-|-|-
`selector`|`string`|CSS selector for the element to click

---
#### Tool: **`playwright_click_and_switch_tab`**
Click a link and switch to the newly opened tab
Parameters|Type|Description
-|-|-
`selector`|`string`|CSS selector for the link to click

---
#### Tool: **`playwright_close`**
Close the browser and release all resources
#### Tool: **`playwright_console_logs`**
Retrieve console logs from the browser with filtering options
Parameters|Type|Description
-|-|-
`clear`|`boolean` *optional*|Whether to clear logs after retrieval (default: false)
`limit`|`number` *optional*|Maximum number of logs to return
`search`|`string` *optional*|Text to search for in logs (handles text with square brackets)
`type`|`string` *optional*|Type of logs to retrieve (all, error, warning, log, info, debug, exception)

---
#### Tool: **`playwright_custom_user_agent`**
Set a custom User Agent for the browser
Parameters|Type|Description
-|-|-
`userAgent`|`string`|Custom User Agent for the Playwright browser instance

---
#### Tool: **`playwright_delete`**
Perform an HTTP DELETE request
Parameters|Type|Description
-|-|-
`url`|`string`|URL to perform DELETE operation

---
#### Tool: **`playwright_drag`**
Drag an element to a target location
Parameters|Type|Description
-|-|-
`sourceSelector`|`string`|CSS selector for the element to drag
`targetSelector`|`string`|CSS selector for the target location

---
#### Tool: **`playwright_evaluate`**
Execute JavaScript in the browser console
Parameters|Type|Description
-|-|-
`script`|`string`|JavaScript code to execute

---
#### Tool: **`playwright_expect_response`**
Ask Playwright to start waiting for a HTTP response. This tool initiates the wait operation but does not wait for its completion.
Parameters|Type|Description
-|-|-
`id`|`string`|Unique & arbitrary identifier to be used for retrieving this response later with `Playwright_assert_response`.
`url`|`string`|URL pattern to match in the response.

---
#### Tool: **`playwright_fill`**
fill out an input field
Parameters|Type|Description
-|-|-
`selector`|`string`|CSS selector for input field
`value`|`string`|Value to fill

---
#### Tool: **`playwright_get`**
Perform an HTTP GET request
Parameters|Type|Description
-|-|-
`url`|`string`|URL to perform GET operation

---
#### Tool: **`playwright_get_visible_html`**
Get the HTML content of the current page. By default, all <script> tags are removed from the output unless removeScripts is explicitly set to false.
Parameters|Type|Description
-|-|-
`cleanHtml`|`boolean` *optional*|Perform comprehensive HTML cleaning (default: false)
`maxLength`|`number` *optional*|Maximum number of characters to return (default: 20000)
`minify`|`boolean` *optional*|Minify the HTML output (default: false)
`removeComments`|`boolean` *optional*|Remove all HTML comments (default: false)
`removeMeta`|`boolean` *optional*|Remove all meta tags from the HTML (default: false)
`removeScripts`|`boolean` *optional*|Remove all script tags from the HTML (default: true)
`removeStyles`|`boolean` *optional*|Remove all style tags from the HTML (default: false)
`selector`|`string` *optional*|CSS selector to limit the HTML to a specific container

---
#### Tool: **`playwright_get_visible_text`**
Get the visible text content of the current page
#### Tool: **`playwright_go_back`**
Navigate back in browser history
#### Tool: **`playwright_go_forward`**
Navigate forward in browser history
#### Tool: **`playwright_hover`**
Hover an element on the page
Parameters|Type|Description
-|-|-
`selector`|`string`|CSS selector for element to hover

---
#### Tool: **`playwright_iframe_click`**
Click an element in an iframe on the page
Parameters|Type|Description
-|-|-
`iframeSelector`|`string`|CSS selector for the iframe containing the element to click
`selector`|`string`|CSS selector for the element to click

---
#### Tool: **`playwright_iframe_fill`**
Fill an element in an iframe on the page
Parameters|Type|Description
-|-|-
`iframeSelector`|`string`|CSS selector for the iframe containing the element to fill
`selector`|`string`|CSS selector for the element to fill
`value`|`string`|Value to fill

---
#### Tool: **`playwright_navigate`**
Navigate to a URL
Parameters|Type|Description
-|-|-
`url`|`string`|URL to navigate to the website specified
`browserType`|`string` *optional*|Browser type to use (chromium, firefox, webkit). Defaults to chromium
`headless`|`boolean` *optional*|Run browser in headless mode (default: false)
`height`|`number` *optional*|Viewport height in pixels (default: 720)
`timeout`|`number` *optional*|Navigation timeout in milliseconds
`waitUntil`|`string` *optional*|Navigation wait condition
`width`|`number` *optional*|Viewport width in pixels (default: 1280)

---
#### Tool: **`playwright_patch`**
Perform an HTTP PATCH request
Parameters|Type|Description
-|-|-
`url`|`string`|URL to perform PUT operation
`value`|`string`|Data to PATCH in the body

---
#### Tool: **`playwright_post`**
Perform an HTTP POST request
Parameters|Type|Description
-|-|-
`url`|`string`|URL to perform POST operation
`value`|`string`|Data to post in the body
`headers`|`object` *optional*|Additional headers to include in the request
`token`|`string` *optional*|Bearer token for authorization

---
#### Tool: **`playwright_press_key`**
Press a keyboard key
Parameters|Type|Description
-|-|-
`key`|`string`|Key to press (e.g. 'Enter', 'ArrowDown', 'a')
`selector`|`string` *optional*|Optional CSS selector to focus before pressing key

---
#### Tool: **`playwright_put`**
Perform an HTTP PUT request
Parameters|Type|Description
-|-|-
`url`|`string`|URL to perform PUT operation
`value`|`string`|Data to PUT in the body

---
#### Tool: **`playwright_save_as_pdf`**
Save the current page as a PDF file
Parameters|Type|Description
-|-|-
`outputPath`|`string`|Directory path where PDF will be saved
`filename`|`string` *optional*|Name of the PDF file (default: page.pdf)
`format`|`string` *optional*|Page format (e.g. 'A4', 'Letter')
`margin`|`object` *optional*|Page margins
`printBackground`|`boolean` *optional*|Whether to print background graphics

---
#### Tool: **`playwright_screenshot`**
Take a screenshot of the current page or a specific element
Parameters|Type|Description
-|-|-
`name`|`string`|Name for the screenshot
`downloadsDir`|`string` *optional*|Custom downloads directory path (default: user's Downloads folder)
`fullPage`|`boolean` *optional*|Store screenshot of the entire page (default: false)
`height`|`number` *optional*|Height in pixels (default: 600)
`savePng`|`boolean` *optional*|Save screenshot as PNG file (default: false)
`selector`|`string` *optional*|CSS selector for element to screenshot
`storeBase64`|`boolean` *optional*|Store screenshot in base64 format (default: true)
`width`|`number` *optional*|Width in pixels (default: 800)

---
#### Tool: **`playwright_select`**
Select an element on the page with Select tag
Parameters|Type|Description
-|-|-
`selector`|`string`|CSS selector for element to select
`value`|`string`|Value to select

---
#### Tool: **`playwright_upload_file`**
Upload a file to an input[type='file'] element on the page
Parameters|Type|Description
-|-|-
`filePath`|`string`|Absolute path to the file to upload
`selector`|`string`|CSS selector for the file input element

---
#### Tool: **`start_codegen_session`**
Start a new code generation session to record Playwright actions
Parameters|Type|Description
-|-|-
`options`|`object`|Code generation options

---

## Screenshots

![ExecuteAutomation Playwright screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/playwright-mcp-server-1.png)
