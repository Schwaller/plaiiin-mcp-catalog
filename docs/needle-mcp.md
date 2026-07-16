Production-ready RAG service to search and retrieve data from your documents.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/needle-mcp](https://hub.docker.com/repository/docker/mcp/needle-mcp)
**Author**|[needle-ai](https://github.com/needle-ai)
**Repository**|https://github.com/needle-ai/needle-mcp

## Available Tools (7)
Tools provided by this Server|Short Description
-|-
`needle_add_file`|Add a new document to a Needle collection by providing a URL for download.|
`needle_create_collection`|Create a new document collection in Needle for organizing and searching documents.|
`needle_get_collection_details`|Fetch comprehensive metadata about a specific Needle collection.|
`needle_get_collection_stats`|Retrieve detailed statistical information about a Needle collection's contents and status.|
`needle_list_collections`|List Needle collections.|
`needle_list_files`|List all documents stored within a specific Needle collection with their current status.|
`needle_search`|Perform intelligent semantic search across documents in a Needle collection.|

---
## Tools Details

#### Tool: **`needle_add_file`**
Add a new document to a Needle collection by providing a URL for download.
            Supports multiple file formats including:
            - PDF documents
            - Microsoft Word files (DOC, DOCX)
            - Plain text files (TXT)
            - Web pages (HTML)

            The document will be:
            1. Downloaded from the provided URL
            2. Processed for text extraction
            3. Indexed for semantic search

            Use this tool when you need to:
            - Add new documents to a collection
            - Make documents searchable
            - Expand your knowledge base

            Important: Documents require processing time before they're searchable.
            Check processing status using needle_list_files before searching new content.
Parameters|Type|Description
-|-|-
`collection_id`|`string`|The unique collection identifier where the file will be added
`name`|`string`|A descriptive filename that will help identify this document in results
`url`|`string`|Public URL where the document can be downloaded from

---
#### Tool: **`needle_create_collection`**
Create a new document collection in Needle for organizing and searching documents. 
            A collection acts as a container for related documents and enables semantic search across its contents.
            Use this tool when you need to:
            - Start a new document organization
            - Group related documents together
            - Set up a searchable document repository
            Returns a collection ID that's required for subsequent operations. Choose a descriptive name that 
            reflects the collection's purpose for better organization.
Parameters|Type|Description
-|-|-
`name`|`string`|A clear, descriptive name for the collection that reflects its purpose and contents

---
#### Tool: **`needle_get_collection_details`**
Fetch comprehensive metadata about a specific Needle collection. 
            Provides detailed information about the collection's configuration, creation date, and current status.
            Use this tool when you need to:
            - Verify a collection's existence and configuration
            - Check collection metadata before operations
            - Get creation date and other attributes
            Requires a valid collection ID and returns detailed collection metadata. Will error if collection doesn't exist.
Parameters|Type|Description
-|-|-
`collection_id`|`string`|The unique collection identifier returned from needle_create_collection or needle_list_collections

---
#### Tool: **`needle_get_collection_stats`**
Retrieve detailed statistical information about a Needle collection's contents and status.
            Provides metrics including:
            - Total number of documents
            - Processing status of documents
            - Storage usage and limits
            - Index status and health
            Use this tool to:
            - Monitor collection size and growth
            - Verify processing completion
            - Check collection health before operations
            Essential for ensuring collection readiness before performing searches.
Parameters|Type|Description
-|-|-
`collection_id`|`string`|The unique collection identifier to get statistics for

---
#### Tool: **`needle_list_collections`**
List Needle collections. Returns maximum of 20 results. Get more results by increasing the offset.
            Returns detailed information including collection IDs, names, and creation dates. Use this tool when you need to:
            - Get an overview of available document collections
            - Find collection IDs for subsequent operations
            - Verify collection existence before performing operations
            The response includes metadata that's required for other Needle operations.
Parameters|Type|Description
-|-|-
`offset`|`number` *optional*|The offset to start listing from. Default is 0.

---
#### Tool: **`needle_list_files`**
List all documents stored within a specific Needle collection with their current status.
            Returns detailed information about each file including:
            - File ID and name
            - Processing status (pending, processing, complete, error)
            - Upload date and metadata
            Use this tool when you need to:
            - Inventory available documents
            - Check processing status of uploads
            - Get file IDs for reference
            - Verify document availability before searching
            Essential for monitoring document processing completion before performing searches.
Parameters|Type|Description
-|-|-
`collection_id`|`string`|The unique collection identifier to list files from

---
#### Tool: **`needle_search`**
Perform intelligent semantic search across documents in a Needle collection.
            This tool uses advanced embedding technology to find relevant content based on meaning,
            not just keywords. The search:
            - Understands natural language queries
            - Finds conceptually related content
            - Returns relevant text passages with source information
            - Ranks results by semantic relevance

            Use this tool when you need to:
            - Find specific information within documents
            - Answer questions from document content
            - Research topics across multiple documents
            - Locate relevant passages and their sources

            More effective than traditional keyword search for:
            - Natural language questions
            - Conceptual queries
            - Finding related content

            Returns matching text passages with their source file IDs.
Parameters|Type|Description
-|-|-
`collection_id`|`string`|The unique collection identifier to search within
`query`|`string`|Natural language query describing the information you're looking for

---
