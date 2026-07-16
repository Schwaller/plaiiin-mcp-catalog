A MCP Server for browsing the official Minecraft Wiki!.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/minecraft-wiki](https://hub.docker.com/repository/docker/mcp/minecraft-wiki)
**Author**|[L3-N0X](https://github.com/L3-N0X)
**Repository**|https://github.com/L3-N0X/Minecraft-Wiki-MCP

## Available Tools (9)
Tools provided by this Server|Short Description
-|-
`MinecraftWiki_getCategoriesForPage`|Get categories associated with a specific page.|
`MinecraftWiki_getPageContent`|Get the raw wikitext content of a specific Minecraft Wiki page.|
`MinecraftWiki_getPageSection`|Get a specific section from a Minecraft Wiki page.|
`MinecraftWiki_getPageSummary`|Step 2 of the recommended workflow: After finding a page through search, use this to get both the page summary AND a list of all available sections.|
`MinecraftWiki_getSectionsInPage`|Retrieves an overview of all sections in the page.|
`MinecraftWiki_listAllCategories`|List all categories in the Minecraft Wiki.|
`MinecraftWiki_listCategoryMembers`|List all pages that are members of a specific category on the Minecraft Wiki.|
`MinecraftWiki_resolveRedirect`|Resolve a redirect and return the title of the target page.|
`MinecraftWiki_searchWiki`|Search the Minecraft Wiki for a specific structure, entity, item or block.|

---
## Tools Details

#### Tool: **`MinecraftWiki_getCategoriesForPage`**
Get categories associated with a specific page.
Parameters|Type|Description
-|-|-
`title`|`string`|Title of the Minecraft Wiki page

---
#### Tool: **`MinecraftWiki_getPageContent`**
Get the raw wikitext content of a specific Minecraft Wiki page.
Parameters|Type|Description
-|-|-
`title`|`string`|Title of the Minecraft Wiki page to retrieve the raw wikitext content for.

---
#### Tool: **`MinecraftWiki_getPageSection`**
Get a specific section from a Minecraft Wiki page. Should be used as step 3 after searching for the page and getting its summary. The section index corresponds to the order of sections on the page, starting with 0 for the main content, 1 for the first section, 2 for the second section, etc.
Parameters|Type|Description
-|-|-
`sectionIndex`|`number`|Index of the section to retrieve (0 = main, 1 = first section, 2 = second section, etc.)
`title`|`string`|Title of the Minecraft Wiki page

---
#### Tool: **`MinecraftWiki_getPageSummary`**
Step 2 of the recommended workflow: After finding a page through search, use this to get both the page summary AND a list of all available sections. This helps determine which specific section to retrieve next using getPageSection.
Parameters|Type|Description
-|-|-
`title`|`string`|Title of the Minecraft Wiki page

---
#### Tool: **`MinecraftWiki_getSectionsInPage`**
Retrieves an overview of all sections in the page.
Parameters|Type|Description
-|-|-
`title`|`string`|Title of the page to retrieve sections for.

---
#### Tool: **`MinecraftWiki_listAllCategories`**
List all categories in the Minecraft Wiki.
Parameters|Type|Description
-|-|-
`limit`|`number` *optional*|The maximum number of categories to return (default: 10, max: 500).
`prefix`|`string` *optional*|Filters categories by prefix.

---
#### Tool: **`MinecraftWiki_listCategoryMembers`**
List all pages that are members of a specific category on the Minecraft Wiki.
Parameters|Type|Description
-|-|-
`category`|`string`|The name of the category to list members from (e.g., 'Items', 'Blocks', 'Entities', 'Structure Blueprints').
`limit`|`number` *optional*|The maximum number of pages to return (default: 100, max: 500).

---
#### Tool: **`MinecraftWiki_resolveRedirect`**
Resolve a redirect and return the title of the target page.
Parameters|Type|Description
-|-|-
`title`|`string`|Title of the page to resolve the redirect for.

---
#### Tool: **`MinecraftWiki_searchWiki`**
Search the Minecraft Wiki for a specific structure, entity, item or block. NOTE: Only use for basic search terms like item/block/structure/entity names - complex queries (like 'loot table of X' or 'how to craft Y') will not work. For best results: 1. Search for the basic entity/structure/etc name first, 2. Then use getPageSummary to see available sections, 3. Finally use getPageSection to get specific section content.
Parameters|Type|Description
-|-|-
`query`|`string`|Search term to find on the Minecraft Wiki.

---
