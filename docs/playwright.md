Playwright MCP server.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/playwright](https://hub.docker.com/repository/docker/mcp/playwright)
**Author**|[microsoft](https://github.com/microsoft)
**Repository**|https://github.com/microsoft/playwright-mcp

## Available Tools (23)
Tools provided by this Server|Short Description
-|-
`browser_click`|Click|
`browser_close`|Close browser|
`browser_console_messages`|Get console messages|
`browser_drag`|Drag mouse|
`browser_drop`|Drop files or data onto an element|
`browser_evaluate`|Evaluate JavaScript|
`browser_file_upload`|Upload files|
`browser_fill_form`|Fill form|
`browser_handle_dialog`|Handle a dialog|
`browser_hover`|Hover mouse|
`browser_navigate`|Navigate to a URL|
`browser_navigate_back`|Go back|
`browser_network_request`|Show network request details|
`browser_network_requests`|List network requests|
`browser_press_key`|Press a key|
`browser_resize`|Resize browser window|
`browser_run_code_unsafe`|Run Playwright code (unsafe)|
`browser_select_option`|Select option|
`browser_snapshot`|Page snapshot|
`browser_tabs`|Manage tabs|
`browser_take_screenshot`|Take a screenshot|
`browser_type`|Type text|
`browser_wait_for`|Wait for|

---
## Tools Details

#### Tool: **`browser_click`**
Perform click on a web page
Parameters|Type|Description
-|-|-
`target`|`string`|Exact target element reference from the page snapshot, or a unique element selector
`button`|`string` *optional*|Button to click, defaults to left
`doubleClick`|`boolean` *optional*|Whether to perform a double click instead of a single click
`element`|`string` *optional*|Human-readable element description used to obtain permission to interact with the element
`modifiers`|`array` *optional*|Modifier keys to press

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_close`**
Close the page
#### Tool: **`browser_console_messages`**
Returns all console messages
Parameters|Type|Description
-|-|-
`level`|`string`|Level of the console messages to return. Each level includes the messages of more severe levels. Defaults to "info".
`all`|`boolean` *optional*|Return all console messages since the beginning of the session, not just since the last navigation. Defaults to false.
`filename`|`string` *optional*|Filename to save the console messages to. If not provided, messages are returned as text.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_drag`**
Perform drag and drop between two elements
Parameters|Type|Description
-|-|-
`endTarget`|`string`|Exact target element reference from the page snapshot, or a unique element selector
`startTarget`|`string`|Exact target element reference from the page snapshot, or a unique element selector
`endElement`|`string` *optional*|Human-readable target element description used to obtain the permission to interact with the element
`startElement`|`string` *optional*|Human-readable source element description used to obtain the permission to interact with the element

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_drop`**
Drop files or MIME-typed data onto an element, as if dragged from outside the page. At least one of "paths" or "data" must be provided.
Parameters|Type|Description
-|-|-
`target`|`string`|Exact target element reference from the page snapshot, or a unique element selector
`data`|`object` *optional*|Data to drop, as a map of MIME type to string value (e.g. {"text/plain": "hello", "text/uri-list": "https://example.com"}).
`element`|`string` *optional*|Human-readable element description used to obtain permission to interact with the element
`paths`|`array` *optional*|Absolute paths to files to drop onto the element.

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_evaluate`**
Evaluate JavaScript expression on page or element
Parameters|Type|Description
-|-|-
`function`|`string`|() => { /* code */ } or (element) => { /* code */ } when element is provided
`element`|`string` *optional*|Human-readable element description used to obtain permission to interact with the element
`filename`|`string` *optional*|Filename to save the result to. If not provided, result is returned as text.
`target`|`string` *optional*|Exact target element reference from the page snapshot, or a unique element selector

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_file_upload`**
Upload one or multiple files
Parameters|Type|Description
-|-|-
`paths`|`array` *optional*|The absolute paths to the files to upload. Can be single file or multiple files. If omitted, file chooser is cancelled.

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_fill_form`**
Fill multiple form fields
Parameters|Type|Description
-|-|-
`fields`|`array`|Fields to fill in

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_handle_dialog`**
Handle a dialog
Parameters|Type|Description
-|-|-
`accept`|`boolean`|Whether to accept the dialog.
`promptText`|`string` *optional*|The text of the prompt in case of a prompt dialog.

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_hover`**
Hover over element on page
Parameters|Type|Description
-|-|-
`target`|`string`|Exact target element reference from the page snapshot, or a unique element selector
`element`|`string` *optional*|Human-readable element description used to obtain permission to interact with the element

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_navigate`**
Navigate to a URL
Parameters|Type|Description
-|-|-
`url`|`string`|The URL to navigate to

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_navigate_back`**
Go back to the previous page in the history
#### Tool: **`browser_network_request`**
Returns full details (headers and body) of a single network request, or a single part if `part` is set. Use the number from browser_network_requests.
Parameters|Type|Description
-|-|-
`index`|`integer`|1-based index of the request, as printed by browser_network_requests.
`filename`|`string` *optional*|Filename to save the result to. If not provided, output is returned as text.
`part`|`string` *optional*|Return only this part of the request. Omit to return full details.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_network_requests`**
Returns a numbered list of network requests since loading the page. Use browser_network_request with the number to get full details.
Parameters|Type|Description
-|-|-
`static`|`boolean`|Whether to include successful static resources like images, fonts, scripts, etc. Defaults to false.
`filename`|`string` *optional*|Filename to save the network requests to. If not provided, requests are returned as text.
`filter`|`string` *optional*|Only return requests whose URL matches this regexp (e.g. "/api/.*user").

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_press_key`**
Press a key on the keyboard
Parameters|Type|Description
-|-|-
`key`|`string`|Name of the key to press or a character to generate, such as `ArrowLeft` or `a`

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_resize`**
Resize the browser window
Parameters|Type|Description
-|-|-
`height`|`number`|Height of the browser window
`width`|`number`|Width of the browser window

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_run_code_unsafe`**
Run a Playwright code snippet. Unsafe: executes arbitrary JavaScript in the Playwright server process and is RCE-equivalent.
Parameters|Type|Description
-|-|-
`code`|`string` *optional*|A JavaScript function containing Playwright code to execute. It will be invoked with a single argument, page, which you can use for any page interaction. For example: `async (page) => { await page.getByRole('button', { name: 'Submit' }).click(); return await page.title(); }`
`filename`|`string` *optional*|Load code from the specified file. If both code and filename are provided, code will be ignored.

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_select_option`**
Select an option in a dropdown
Parameters|Type|Description
-|-|-
`target`|`string`|Exact target element reference from the page snapshot, or a unique element selector
`values`|`array`|Array of values to select in the dropdown. This can be a single value or multiple values.
`element`|`string` *optional*|Human-readable element description used to obtain permission to interact with the element

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_snapshot`**
Capture accessibility snapshot of the current page, this is better than screenshot
Parameters|Type|Description
-|-|-
`boxes`|`boolean` *optional*|Include each element's bounding box as [box=x,y,width,height] in the snapshot. Coordinates are viewport-relative, in CSS pixels (Element.getBoundingClientRect)
`depth`|`number` *optional*|Limit the depth of the snapshot tree
`filename`|`string` *optional*|Save snapshot to markdown file instead of returning it in the response.
`target`|`string` *optional*|Exact target element reference from the page snapshot, or a unique element selector

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_tabs`**
List, create, close, or select a browser tab.
Parameters|Type|Description
-|-|-
`action`|`string`|Operation to perform
`index`|`number` *optional*|Tab index, used for close/select. If omitted for close, current tab is closed.
`url`|`string` *optional*|URL to navigate to in the new tab, used for new.

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_take_screenshot`**
Take a screenshot of the current page. You can't perform actions based on the screenshot, use browser_snapshot for actions.
Parameters|Type|Description
-|-|-
`type`|`string`|Image format for the screenshot. Default is png.
`element`|`string` *optional*|Human-readable element description used to obtain permission to interact with the element
`filename`|`string` *optional*|File name to save the screenshot to. Defaults to `page-{timestamp}.{png|jpeg}` if not specified. Prefer relative file names to stay within the output directory.
`fullPage`|`boolean` *optional*|When true, takes a screenshot of the full scrollable page, instead of the currently visible viewport. Cannot be used with element screenshots.
`target`|`string` *optional*|Exact target element reference from the page snapshot, or a unique element selector

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_type`**
Type text into editable element
Parameters|Type|Description
-|-|-
`target`|`string`|Exact target element reference from the page snapshot, or a unique element selector
`text`|`string`|Text to type into the element
`element`|`string` *optional*|Human-readable element description used to obtain permission to interact with the element
`slowly`|`boolean` *optional*|Whether to type one character at a time. Useful for triggering key handlers in the page. By default entire text is filled in at once.
`submit`|`boolean` *optional*|Whether to submit entered text (press Enter after)

*This tool may perform destructive updates.*

*This tool interacts with external entities.*

---
#### Tool: **`browser_wait_for`**
Wait for text to appear or disappear or a specified time to pass
Parameters|Type|Description
-|-|-
`text`|`string` *optional*|The text to wait for
`textGone`|`string` *optional*|The text to wait for to disappear
`time`|`number` *optional*|The time to wait in seconds

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
