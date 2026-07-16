An MCP server to help make U.S. Government open datasets AI-friendly.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/pia](https://hub.docker.com/repository/docker/mcp/pia)
**Author**|[Program-Integrity-Alliance](https://github.com/Program-Integrity-Alliance)
**Repository**|https://github.com/Program-Integrity-Alliance/pia-mcp-local

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`pia_oversight_recommendations`|Search oversight recommendations (Open Recommendations dataset) with facets enabled by default.|
`pia_search`|Search the Program Integrity Alliance (PIA) database of government oversight reports, recommendations, executive orders, legislation, and integrity data (GAO, OIG/Oversight.gov, CRS, DOJ, Congress.gov, Federal Register).|

---
## Tools Details

#### Tool: **`pia_oversight_recommendations`**
Search oversight recommendations (Open Recommendations dataset) with facets enabled by default. Today's date is 2026-06-25. This dataset contains recommendations from GAO and Oversight.gov only — SourceDocumentDataSource filters for any other source will be ignored. Do NOT filter by SourceDocumentDataSet — this tool already targets the 'Open Recommendations' dataset automatically. IMPORTANT: When a text query is provided, do NOT add a referenced_agencies filter — the query handles relevance matching. Only use referenced_agencies when the query is empty (pure filter/facet lookups). `total_count` is the number of OPEN recommendations matching the query and all applied filters — report it as that count. The `results` are a representative sample to summarize, and `facets` break the set down by status, priority, agency, and theme. Counts from free-text queries are approximate (semantic matching); pure filter or agency lookups are exact. Recommendations have no per-document citations, so it is very important to always include the `govquery_url` for the full set in Rec Spotlight rather than citing individual rows.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query text
`facets_only`|`boolean` *optional*|Return ONLY the facet breakdown + total_count + Rec Spotlight govquery_url, omitting the individual recommendation rows — to see the open-rec population broken down by status/priority/agency/theme without pulling rows.
`filter`|`string` *optional*|Optional OData filter expression supporting complex boolean logic.

AVAILABLE FIELDS:
• SourceDocumentDataSource: Data source/agency that published the document. Major sources (>1k documents): 'Department of Justice', 'Congress.gov', 'Oversight.gov', 'CRS', 'GAO', 'Federal Register'
• SourceDocumentDataSet: Dataset or collection the document belongs to. Values include: 'reports', 'federal-reports', 'press-releases', 'executive orders', 'Open Recommendations'. Note: the value is 'Open Recommendations' (not 'recommendations'). Values: 'press-releases', 'bills-and-laws', 'reports', 'federal-reports', 'executive orders', 'state-and-local-reports', 'annual-financial-reports', 'congressional-justification-reports', 'performance-and-accountability-reports'
• SourceDocumentTitle: Document title - use contains, eq for text matching
• SourceDocumentPublishDate: Publication date - ISO 8601 format YYYY-MM-DD (e.g., '2023-01-01'). Use ge/le for ranges
• RecStatus: Recommendation status
• RecPriorityFlag: Priority flag for recommendations
• SourceDocumentIsRecDoc: Whether the document contains recommendations. Values: 'No', 'Yes'
• RecFraudRiskManagementThemePIA: Fraud risk management theme classification
• RecMatterForCongressPIA: Whether the matter is for Congressional attention
• RecRecommendation: Recommendation text - use contains, eq for text matching
• RecAgencyComments: Agency comments on recommendations - use contains, eq for text matching
• referenced_agencies: Agencies referenced by documents (collection field). IMPORTANT: Only use this filter when the query is empty (pure filter/facet lookups). Do NOT combine with a text query — the query already handles relevance matching. Example: (referenced_agencies/any(a: a eq 'Department of Defense (DOD)') or referenced_agencies/any(a: a eq 'Department of Justice (DOJ)')) - for single agency omit outer parentheses and 'or'. Get all values via pia_search with facets_only=true.

OPERATORS:
• Text: contains, eq, ne, startswith, endswith
• Exact: eq (equals), ne (not equals), in (in list)
• Date: ge (greater/equal), le (less/equal), eq (equals)
• Logic: and, or, not, parentheses for grouping

EXAMPLES:
• "SourceDocumentDataSource eq 'GAO'"
• "SourceDocumentDataSource eq 'GAO' and RecStatus ne 'Closed'"
• "(SourceDocumentDataSource eq 'GAO' or SourceDocumentDataSource eq 'OIG') and RecStatus eq 'Open'"
• "SourceDocumentPublishDate ge '2020-01-01' and SourceDocumentPublishDate le '2024-12-31'"

TIP: Use pia_search with facets_only=true to get the most current available values.

COMMON AGENCY NAMES (use EXACT spelling for referenced_agencies):
Department of Defense (DOD), Department of Health and Human Services (HHS),
Department of Homeland Security (DHS), Department of Justice (DOJ),
Department of Education (ED), Department of Veterans Affairs (VA),
Department of the Treasury, Department of Agriculture (USDA),
Department of the Interior (DOI), Department of Transportation (DOT),
Department of Energy (DOE), Department of State, Department of Labor (DOL),
Department of Commerce (DOC), Department of Housing and Urban Development (HUD),
Environmental Protection Agency (EPA),
National Aeronautics and Space Administration (NASA),
Social Security Administration (SSA), Small Business Administration (SBA),
Office of Personnel Management (OPM), General Services Administration (GSA)
`include_facets`|`boolean` *optional*|Include facets in results (default: true)
`limit`|`integer` *optional*|Maximum results limit
`page`|`integer` *optional*|Page number (default: 1)
`page_size`|`integer` *optional*|Results per page (default: 100)
`search_mode`|`string` *optional*|Search mode (default: content)

---
#### Tool: **`pia_search`**
Search the Program Integrity Alliance (PIA) database of government oversight reports, recommendations, executive orders, legislation, and integrity data (GAO, OIG/Oversight.gov, CRS, DOJ, Congress.gov, Federal Register). One tool for all document search: scope by source/dataset/agency/date via filter, choose content vs titles via search_mode, sweep every source with wide, or discover filter values with facets_only. WHAT THE COUNTS MEAN: in 'content' mode (default) total_count and facet counts are TEXT CHUNKS / EXCERPTS — a single document is split into many chunks, so these counts are much larger than the number of documents and must NOT be reported as a document/report/article count. In 'titles' mode the counts are whole DOCUMENTS / ARTICLES. Use search_mode='titles' whenever the user asks how many documents, reports, or articles there are. Citations are very important to PIA users, so it is strongly expected that your answer: (1) gives every factual claim at least one clickable inline citation in the form [[1]](url), numbered sequentially from 1; (2) ends with a References section listing every source you cited, each reference on its own line (never multiple references on one line) — omit this section only for a pure count or summary with nothing specific to cite; and (3) includes a Find Out More section with the `govquery_url` so the user can open the full result set. Please do not present findings from these results without their inline citations and References section. Counts from free-text queries are approximate, because semantic search matches variations of the search terms.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query — natural language or keywords. Use "" or "*" to match all documents (for pure filter/facet lookups).
`facets_only`|`boolean` *optional*|Return ONLY facet counts (available filter values), no document results — to discover filters before drilling in. Implies include_facets.
`filter`|`string` *optional*|OData filter to scope results (boolean logic + grouping). Source: SourceDocumentDataSource eq 'GAO' (valid: GAO, Oversight.gov, CRS, Department of Justice, Congress.gov, Federal Register). Agency: referenced_agencies/any(a: a eq 'Department of Defense (DOD)'). Dataset: SourceDocumentDataSet eq 'executive orders'. To restrict to one source, pass its SourceDocumentDataSource filter.
`include_facets`|`boolean` *optional*|Include per-dimension facet counts (source, status, priority, agency, theme, …) alongside results.
`limit`|`integer` *optional*|Optional hard cap on results (alias for page_size).
`page`|`integer` *optional*|Page number (1-based). Ignored when wide=true.
`page_size`|`integer` *optional*|Results per page (max 50). Per-source before merge when wide=true.
`search_mode`|`string` *optional*|'content' searches the full-text (chunked) index — total_count and facet counts are TEXT CHUNKS / EXCERPTS, NOT documents: one document is split into many chunks, so the counts EXCEED the number of documents. 'titles' searches the document-level index — total_count and facet counts are whole DOCUMENTS / ARTICLES, and it's faster for locating a specific document. Use 'titles' whenever the user asks how many documents / reports / articles there are.
`wide`|`boolean` *optional*|When true, sweep ALL sources/datasets in parallel and merge into one de-duplicated, score-ranked list. Use for the most comprehensive cross-source view.

---

## Screenshots

![Program Integrity Alliance screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/pia-1.png)
