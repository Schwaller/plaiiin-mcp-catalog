Connect to Lara Translate API, enabling powerful translation capabilities with support for language detection and context-aware translations.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/lara](https://hub.docker.com/repository/docker/mcp/lara)
**Author**|[translated](https://github.com/translated)
**Repository**|https://github.com/translated/lara-mcp

## Available Tools (22)
Tools provided by this Server|Short Description
-|-
`add_glossary_entry`|Add or replace glossary entry|
`add_translation`|Add translation unit to memory|
`check_glossary_import_status`|Check glossary import status|
`check_import_status`|Check TMX import status|
`create_glossary`|Create glossary|
`create_memory`|Create translation memory|
`delete_glossary`|Delete glossary|
`delete_glossary_entry`|Delete glossary entry|
`delete_memory`|Delete translation memory|
`delete_translation`|Delete translation unit from memory|
`detect_language`|Detect language|
`export_glossary`|Export glossary as CSV|
`get_glossary`|Get glossary|
`get_glossary_counts`|Get glossary entry count|
`import_glossary_csv`|Import glossary CSV|
`import_tmx`|Import TMX file|
`list_glossaries`|List glossaries|
`list_languages`|List supported languages|
`list_memories`|List translation memories|
`translate`|Translate text|
`update_glossary`|Rename glossary|
`update_memory`|Rename translation memory|

---
## Tools Details

#### Tool: **`add_glossary_entry`**
Adds or replaces an entry in a glossary in your Lara Translate account. Supports both monodirectional and multidirectional glossaries.
Parameters|Type|Description
-|-|-
`id`|`string`|The glossary ID (format: gls_*, e.g., 'gls_xyz123')
`terms`|`array`|Array of terms with language and value. For monodirectional glossaries, the first term is the source and the rest are targets. For multidirectional glossaries, all terms are treated equally. Use the list_languages tool to get supported language codes.
`guid`|`string` *optional*|Optional entry identifier. Use this for multidirectional glossaries or to update a specific entry.

---
#### Tool: **`add_translation`**
Adds a translation to a translation memory in your Lara Translate account.
Parameters|Type|Description
-|-|-
`id`|`array`|The ID or list of IDs where to save the translation unit. Format: mem_xyz123
`sentence`|`string`|The source sentence
`source`|`string`|The source language code of the sentence, it MUST be a language supported by the system, use the list_languages tool to get a list of all the supported languages
`target`|`string`|The target language code of the translation, it MUST be a language supported by the system, use the list_languages tool to get a list of all the supported languages
`translation`|`string`|The translated sentence
`sentence_after`|`string` *optional*|The sentence after the source sentence to specify the context of the translation unit
`sentence_before`|`string` *optional*|The sentence before the source sentence to specify the context of the translation unit
`tuid`|`string` *optional*|Translation Unit unique identifier

---
#### Tool: **`check_glossary_import_status`**
Checks the status of a glossary CSV import job started by import_glossary_csv. Poll this tool with the import_id returned from import_glossary_csv until the import is complete.
Parameters|Type|Description
-|-|-
`id`|`string`|The ID of the glossary import job

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`check_import_status`**
Checks the status of a TMX import job started by import_tmx. Poll this tool with the import_id returned from import_tmx until the import is complete. The response includes a progress field to track completion.
Parameters|Type|Description
-|-|-
`id`|`string`|The ID of the import job

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`create_glossary`**
Create a glossary with a custom name in your Lara Translate account. Glossaries enforce specific terminology during translation.
Parameters|Type|Description
-|-|-
`name`|`string`|

---
#### Tool: **`create_memory`**
Create a translation memory with a custom name in your Lara Translate account. Translation memories store pairs of source and target text segments (translation units) for reuse in future translations.
Parameters|Type|Description
-|-|-
`name`|`string`|
`external_id`|`string` *optional*|The ID of the memory to be imported from MyMemory. Use this to initialize the memory with external content. Format: ext_my_[MyMemory ID]

---
#### Tool: **`delete_glossary`**
Deletes a glossary from your Lara Translate account.
Parameters|Type|Description
-|-|-
`id`|`string`|The glossary ID to delete (format: gls_*, e.g., 'gls_xyz123')

*This tool may perform destructive updates.*

---
#### Tool: **`delete_glossary_entry`**
Deletes an entry from a glossary in your Lara Translate account. Use term for monodirectional glossaries or guid for multidirectional glossaries.
Parameters|Type|Description
-|-|-
`id`|`string`|The glossary ID (format: gls_*, e.g., 'gls_xyz123')
`guid`|`string` *optional*|The entry GUID to delete. Use this for multidirectional glossaries.
`term`|`object` *optional*|The term to delete. Use this for monodirectional glossaries.

*This tool may perform destructive updates.*

---
#### Tool: **`delete_memory`**
Deletes a translation memory from your Lara Translate account.
Parameters|Type|Description
-|-|-
`id`|`string`|The unique identifier of the memory to update. Format: mem_xyz123

*This tool may perform destructive updates.*

---
#### Tool: **`delete_translation`**
Deletes a translation from a translation memory in your Lara Translate account.
Parameters|Type|Description
-|-|-
`id`|`array`|The ID or list of IDs where to delete the translation unit from. Format: mem_xyz123
`sentence`|`string`|The source sentence
`source`|`string`|The source language code of the sentence
`target`|`string`|The target language code of the translation
`translation`|`string`|The translated sentence
`sentence_after`|`string` *optional*|The sentence after the source sentence to specify the context of the translation unit
`sentence_before`|`string` *optional*|The sentence before the source sentence to specify the context of the translation unit
`tuid`|`string` *optional*|Translation Unit unique identifier

*This tool may perform destructive updates.*

---
#### Tool: **`detect_language`**
Detects the language of the provided text. Returns the detected language, content type, and a list of predictions with confidence scores. Accepts a single string or an array of strings (up to 128 elements).
Parameters|Type|Description
-|-|-
`text`|`string`|The text to detect the language of. Can be a single string or an array of strings (up to 128 elements).
`hint`|`string` *optional*|Optional language code hint to guide detection (e.g., 'en-EN').
`passlist`|`array` *optional*|Optional list of language codes to restrict detection results to.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`export_glossary`**
Exports a glossary as CSV from your Lara Translate account. Supports unidirectional and multidirectional formats.
Parameters|Type|Description
-|-|-
`content_type`|`string`|The export format. 'csv/table-uni' for unidirectional (requires source parameter), 'csv/table-multi' for multidirectional
`id`|`string`|The glossary ID (format: gls_*, e.g., 'gls_xyz123')
`source`|`string` *optional*|The source language code. Required when content_type is 'csv/table-uni'

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_glossary`**
Retrieves a specific glossary by ID from your Lara Translate account. Returns null if the glossary is not found.
Parameters|Type|Description
-|-|-
`id`|`string`|The glossary ID (format: gls_*, e.g., 'gls_xyz123')

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_glossary_counts`**
Retrieves the term and language counts for a glossary in your Lara Translate account.
Parameters|Type|Description
-|-|-
`id`|`string`|The glossary ID (format: gls_*, e.g., 'gls_xyz123')

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`import_glossary_csv`**
Imports a CSV file into a glossary. Supports unidirectional and multidirectional formats. This is an async operation that returns an import job object containing an import_id. Poll with check_glossary_import_status using the returned import_id until the import is complete.
Parameters|Type|Description
-|-|-
`content_type`|`string`|The format of the CSV file. 'csv/table-uni' for unidirectional, 'csv/table-multi' for multidirectional
`csv_content`|`string`|The content of the CSV file to upload
`id`|`string`|The glossary ID (format: gls_*, e.g., 'gls_xyz123')
`gzip`|`boolean` *optional*|Whether the CSV content is gzip compressed

---
#### Tool: **`import_tmx`**
Imports a TMX file into a translation memory. This is an async operation that returns an import job object containing an import_id. Poll with check_import_status using the returned import_id until the import is complete.
Parameters|Type|Description
-|-|-
`id`|`string`|The ID of the memory to update. Format: mem_xyz123.
`tmx_content`|`string`|The content of the tmx file to upload.

---
#### Tool: **`list_glossaries`**
Lists all glossaries in your Lara Translate account. Glossaries are collections of terms with their translations that enforce specific terminology during translation.
#### Tool: **`list_languages`**
Lists all supported languages in your Lara Translate account.
#### Tool: **`list_memories`**
Lists all translation memories in your Lara Translate account.
#### Tool: **`translate`**
Translate text between languages using Lara Translate. Supports language detection, context-aware translations, translation memories, and glossaries. The optional 'instructions' parameter accepts short localization directives (e.g., 'Translate formally') — only provide them when the content specifically requires tone, formality, or terminology adjustments.
Parameters|Type|Description
-|-|-
`target`|`string`|The target language code (e.g., 'it-IT' for Italian). This specifies the language you want the text translated into.
`text`|`array`|An array of text blocks to translate. Each block contains a text string and a boolean indicating whether it should be translated. This allows for selective translation where some text blocks can be preserved in their original form while others are translated.
`adapt_to`|`array` *optional*|A list of translation memory IDs for adapting the translation.
`content_type`|`string` *optional*|Specifies the content type of the text. Autodetected if omitted.
`context`|`string` *optional*|Additional context string to improve translation quality (e.g., 'This is a legal document' or 'Im talking with a doctor'). This helps the translation system better understand the domain.
`glossaries`|`array` *optional*|Array of glossary IDs to apply during translation (max 10). IDs must match format: gls_* (e.g., ['gls_xyz123', 'gls_abc456']). Glossaries enforce specific terminology and terms.
`instructions`|`array` *optional*|Optional list of short localization directives to adjust translation output. Each instruction MUST be no more than 20 words. These are NOT free-form LLM prompts — they are expert localization directives about formality, tone, or domain-specific terminology. Only provide instructions when the content specifically requires them; omitting instructions for general content preserves higher translation quality. Do NOT combine contradictory instructions (e.g., formal and informal tone together). Examples: 'Translate formally', 'Use a creative and concise tone', 'Make translation gender-neutral', 'Mask any price with the [price] placeholder', 'Use quotation marks (« ») for quotations'.
`no_trace`|`boolean` *optional*|Privacy flag. If set to true, the request content will not be stored or traced by Lara. Use for sensitive content.
`priority`|`string` *optional*|Translation priority. 'normal' for real-time translations, 'background' for batch processing with lower priority.
`reasoning`|`boolean` *optional*|Enables Lara Think multi-step linguistic analysis. Can increase processing time up to 10x but may improve translation quality for complex texts.
`source`|`string` *optional*|The source language code (e.g., 'en-EN' for English). If not specified, the system will attempt to detect it automatically. If you have a hint about the source language, you should specify it in the source_hint field.
`source_hint`|`string` *optional*|Used to guide language detection. Specify this when the source language is uncertain to improve detection accuracy.
`style`|`string` *optional*|Controls how the translation balances accuracy against natural readability. 'faithful' stays close to the source, 'fluid' prioritizes natural readability, 'creative' allows more freedom in the translation.
`timeout_in_millis`|`integer` *optional*|Custom timeout for the translation request in milliseconds. Max: 300000ms (5 minutes). Useful for very long texts.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`update_glossary`**
Updates the name of a glossary in your Lara Translate account.
Parameters|Type|Description
-|-|-
`id`|`string`|The glossary ID (format: gls_*, e.g., 'gls_xyz123')
`name`|`string`|

---
#### Tool: **`update_memory`**
Updates a translation memory in your Lara Translate account.
Parameters|Type|Description
-|-|-
`id`|`string`|The unique identifier of the memory to update. Format: mem_xyz123
`name`|`string`|

---
