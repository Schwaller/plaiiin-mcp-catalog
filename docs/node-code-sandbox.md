A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/node-code-sandbox](https://hub.docker.com/repository/docker/mcp/node-code-sandbox)
**Author**|[alfonsograziano](https://github.com/alfonsograziano)
**Repository**|https://github.com/alfonsograziano/node-code-sandbox-mcp

## Available Tools (7)
Tools provided by this Server|Short Description
-|-
`get_dependency_types`|Given an array of npm package names (and optional versions), fetch whether each package ships its own TypeScript definitions or has a corresponding @types/… package, and return the raw .d.ts text.|
`run_js`|Install npm dependencies and run JavaScript code inside a running sandbox container.|
`run_js_ephemeral`|Run a JavaScript snippet in a temporary disposable container with optional npm dependencies, then automatically clean up.|
`sandbox_exec`|Execute one or more shell commands inside a running sandbox container.|
`sandbox_initialize`|Start a new isolated Docker container running Node.js.|
`sandbox_stop`|Terminate and remove a running sandbox container.|
`search_npm_packages`|Search for npm packages by a search term and get their name, description, and a README snippet.|

---
## Tools Details

#### Tool: **`get_dependency_types`**
Given an array of npm package names (and optional versions), 
  fetch whether each package ships its own TypeScript definitions 
  or has a corresponding @types/… package, and return the raw .d.ts text.

  Useful whenwhen you're about to run a Node.js script against an unfamiliar dependency 
  and want to inspect what APIs and types it exposes.
Parameters|Type|Description
-|-|-
`dependencies`|`array`|

---
#### Tool: **`run_js`**
Install npm dependencies and run JavaScript code inside a running sandbox container.
  After running, you must manually stop the sandbox to free resources.
  The code must be valid ESModules (import/export syntax). Best for complex workflows where you want to reuse the environment across multiple executions.
  When reading and writing from the Node.js processes, you always need to read from and write to the "./files" directory to ensure persistence on the mounted volume.
Parameters|Type|Description
-|-|-
`code`|`string`|JavaScript code to run inside the container.
`container_id`|`string`|Docker container identifier
`dependencies`|`array` *optional*|A list of npm dependencies to install before running the code. Each item must have a `name` (package) and `version` (range). If none, returns an empty array.
`listenOnPort`|`number` *optional*|If set, leaves the process running and exposes this port to the host.

---
#### Tool: **`run_js_ephemeral`**
Run a JavaScript snippet in a temporary disposable container with optional npm dependencies, then automatically clean up. 
  The code must be valid ESModules (import/export syntax). Ideal for simple one-shot executions without maintaining a sandbox or managing cleanup manually.
  When reading and writing from the Node.js processes, you always need to read from and write to the "./files" directory to ensure persistence on the mounted volume.
  This includes images (e.g., PNG, JPEG) and other files (e.g., text, JSON, binaries).

  Example:
  ```js
  import fs from "fs/promises";
  await fs.writeFile("./files/hello.txt", "Hello world!");
  console.log("Saved ./files/hello.txt");
  ```
Parameters|Type|Description
-|-|-
`code`|`string`|JavaScript code to run inside the ephemeral container.
`dependencies`|`array` *optional*|A list of npm dependencies to install before running the code. Each item must have a `name` (package) and `version` (range). If none, returns an empty array.
`image`|`string` *optional*|Docker image to use for ephemeral execution. e.g. - **node:lts-slim**: Node.js LTS version, slim variant. (Lightweight and fast for JavaScript execution tasks.)
- **mcr.microsoft.com/playwright:v1.55.0-noble**: Playwright image for browser automation. (Preconfigured for running Playwright scripts.)
- **alfonsograziano/node-chartjs-canvas:latest**: Chart.js image for chart generation and mermaid charts generation. ('Preconfigured for generating charts with chartjs-node-canvas and Mermaid. Minimal Mermaid example:
    import fs from "fs";
    import { run } from "@mermaid-js/mermaid-cli";
    fs.writeFileSync("./files/diagram.mmd", "graph LR; A-->B;", "utf8");
    await run("./files/diagram.mmd", "./files/diagram.svg");)

---
#### Tool: **`sandbox_exec`**
Execute one or more shell commands inside a running sandbox container. Requires a sandbox initialized beforehand.
Parameters|Type|Description
-|-|-
`commands`|`array`|
`container_id`|`string`|

---
#### Tool: **`sandbox_initialize`**
Start a new isolated Docker container running Node.js. Used to set up a sandbox session for multiple commands and scripts.
Parameters|Type|Description
-|-|-
`image`|`string` *optional*|
`port`|`number` *optional*|If set, maps this container port to the host

---
#### Tool: **`sandbox_stop`**
Terminate and remove a running sandbox container. Should be called after finishing work in a sandbox initialized with sandbox_initialize.
Parameters|Type|Description
-|-|-
`container_id`|`string`|

---
#### Tool: **`search_npm_packages`**
Search for npm packages by a search term and get their name, description, and a README snippet.
Parameters|Type|Description
-|-|-
`searchTerm`|`string`|The term to search for in npm packages. Should contain all relevant context. Should ideally be text that might appear in the package name, description, or keywords. Use plus signs (+) to combine related terms (e.g., "react+components" for React component libraries). For filtering by author, maintainer, or scope, use the qualifiers field instead of including them in the search term. Examples: "express" for Express.js, "ui+components" for UI component packages, "testing+jest" for Jest testing utilities.
`qualifiers`|`object` *optional*|Optional qualifiers to filter the search results. For example, { not: "insecure" } will exclude insecure packages, { author: "sindresorhus" } will only show packages by that author, { scope: "@vue" } will only show Vue.js scoped packages.

---

## Screenshots

![Node.js Sandbox screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/node-code-sandbox-1.png)
