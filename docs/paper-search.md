MCP, CLI, Skills for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/paper-search](https://hub.docker.com/repository/docker/mcp/paper-search)
**Author**|[openags](https://github.com/openags)
**Repository**|https://github.com/openags/paper-search-mcp

## Available Tools (57)
Tools provided by this Server|Short Description
-|-
`download_arxiv`|Download PDF of an arXiv paper.|
`download_base`|Download PDF for a paper from BASE.|
`download_biorxiv`|Download PDF of a bioRxiv paper.|
`download_citeseerx`|Download PDF for a paper from CiteSeerX.|
`download_crossref`|Attempt to download PDF of a CrossRef paper.|
`download_dblp`|Download PDF for a paper from dblp.|
`download_doaj`|Download PDF for a paper from DOAJ.|
`download_hal`|Download PDF for a paper from HAL.|
`download_iacr`|Download PDF of an IACR ePrint paper.|
`download_medrxiv`|Download PDF of a medRxiv paper.|
`download_openaire`|Download PDF for a paper from OpenAIRE.|
`download_openalex`|Download PDF for a paper from OpenAlex.|
`download_pubmed`|Attempt to download PDF of a PubMed paper.|
`download_scihub`|Download paper PDF via Sci-Hub (optional fallback connector).|
`download_semantic`|Download PDF of a Semantic Scholar paper.|
`download_ssrn`|Download PDF for a paper from SSRN.|
`download_with_fallback`|Try source-native download, OA repositories, Unpaywall, then optional Sci-Hub.|
`download_zenodo`|Download PDF for a paper from Zenodo.|
`get_crossref_paper_by_doi`|Get a specific paper from CrossRef by its DOI.|
`read_arxiv_paper`|Read and extract text content from an arXiv paper PDF.|
`read_base_paper`|Read and extract text content from a BASE paper.|
`read_biorxiv_paper`|Read and extract text content from a bioRxiv paper PDF.|
`read_citeseerx_paper`|Read and extract text content from a CiteSeerX paper.|
`read_crossref_paper`|Attempt to read and extract text content from a CrossRef paper.|
`read_dblp_paper`|Attempt to read and extract text content from a dblp paper.|
`read_doaj_paper`|Read and extract text content from a DOAJ paper.|
`read_hal_paper`|Read and extract text content from a HAL paper.|
`read_iacr_paper`|Read and extract text content from an IACR ePrint paper PDF.|
`read_medrxiv_paper`|Read and extract text content from a medRxiv paper PDF.|
`read_openaire_paper`|Attempt to read and extract text content from an OpenAIRE paper.|
`read_openalex_paper`|Attempt to read and extract text content from an OpenAlex paper.|
`read_pubmed_paper`|Read and extract text content from a PubMed paper.|
`read_semantic_paper`|Read and extract text content from a Semantic Scholar paper.|
`read_ssrn_paper`|Read paper content from SSRN.|
`read_zenodo_paper`|Read and extract text content from a Zenodo paper.|
`search_arxiv`|Search academic papers from arXiv.|
`search_base`|Search academic papers from BASE (Bielefeld Academic Search Engine).|
`search_biorxiv`|Search academic papers from bioRxiv.|
`search_citeseerx`|Search academic papers from CiteSeerX digital library.|
`search_core`|Search academic papers from CORE.|
`search_crossref`|Search academic papers from CrossRef database.|
`search_dblp`|Search academic papers from dblp computer science bibliography.|
`search_doaj`|Search academic papers from DOAJ (Directory of Open Access Journals).|
`search_europepmc`|Search academic papers from Europe PMC.|
`search_google_scholar`|Search academic papers from Google Scholar.|
`search_hal`|Search academic papers from HAL open archive.|
`search_iacr`|Search academic papers from IACR ePrint Archive.|
`search_medrxiv`|Search academic papers from medRxiv.|
`search_openaire`|Search academic papers from OpenAIRE European Open Access infrastructure.|
`search_openalex`|Search academic papers from OpenAlex.|
`search_papers`|Unified top-level search across all configured academic platforms.|
`search_pmc`|Search academic papers from PubMed Central (PMC).|
`search_pubmed`|Search academic papers from PubMed.|
`search_semantic`|Search academic papers from Semantic Scholar.|
`search_ssrn`|Search metadata records from SSRN.|
`search_unpaywall`|Lookup a DOI via Unpaywall and return OA metadata.|
`search_zenodo`|Search academic papers from Zenodo open repository.|

---
## Tools Details

#### Tool: **`download_arxiv`**
Download PDF of an arXiv paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|arXiv paper ID (e.g., '2106.12345').
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_base`**
Download PDF for a paper from BASE.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|BASE paper identifier.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_biorxiv`**
Download PDF of a bioRxiv paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|bioRxiv DOI.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_citeseerx`**
Download PDF for a paper from CiteSeerX.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|CiteSeerX paper identifier.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_crossref`**
Attempt to download PDF of a CrossRef paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|CrossRef DOI (e.g., '10.1038/nature12373').
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_dblp`**
Download PDF for a paper from dblp.

    Note: dblp doesn't provide direct PDF access.
    This function returns an informative message.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|dblp paper identifier.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_doaj`**
Download PDF for a paper from DOAJ.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|DOAJ paper identifier.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_hal`**
Download PDF for a paper from HAL.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|HAL paper identifier.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_iacr`**
Download PDF of an IACR ePrint paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|IACR paper ID (e.g., '2009/101').
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_medrxiv`**
Download PDF of a medRxiv paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|medRxiv DOI.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_openaire`**
Download PDF for a paper from OpenAIRE.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|OpenAIRE paper identifier.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_openalex`**
Download PDF for a paper from OpenAlex.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|OpenAlex paper ID.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_pubmed`**
Attempt to download PDF of a PubMed paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|PubMed ID (PMID).
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_scihub`**
Download paper PDF via Sci-Hub (optional fallback connector).
Parameters|Type|Description
-|-|-
`identifier`|`string`|DOI, title, PMID, or paper URL.
`base_url`|`string` *optional*|Sci-Hub mirror URL.
`save_path`|`string` *optional*|Directory to save the PDF.

---
#### Tool: **`download_semantic`**
Download PDF of a Semantic Scholar paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|Semantic Scholar paper ID, Paper identifier in one of the following formats:
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`download_ssrn`**
Download PDF for a paper from SSRN.

    Note: SSRN connector is metadata-only and download is not supported.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|SSRN paper identifier.
`save_path`|`string` *optional*|Directory to save the PDF (unused).

---
#### Tool: **`download_with_fallback`**
Try source-native download, OA repositories, Unpaywall, then optional Sci-Hub.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|Source-native paper identifier.
`source`|`string`|Source name (arxiv, biorxiv, medrxiv, iacr, semantic, crossref, pubmed, pmc, core, europepmc, citeseerx, doaj, base, zenodo, hal, ssrn).
`doi`|`string` *optional*|Optional DOI used for repository/unpaywall/Sci-Hub fallback.
`save_path`|`string` *optional*|Directory to save downloaded files.
`scihub_base_url`|`string` *optional*|Sci-Hub mirror URL for fallback.
`title`|`string` *optional*|Optional title used for repository/Sci-Hub fallback when DOI is unavailable.
`use_scihub`|`boolean` *optional*|Whether to fallback to Sci-Hub after OA attempts fail.

---
#### Tool: **`download_zenodo`**
Download PDF for a paper from Zenodo.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|Zenodo paper identifier.
`save_path`|`string` *optional*|Directory to save the PDF (default: './downloads').

---
#### Tool: **`get_crossref_paper_by_doi`**
Get a specific paper from CrossRef by its DOI.
Parameters|Type|Description
-|-|-
`doi`|`string`|Digital Object Identifier (e.g., '10.1038/nature12373').

---
#### Tool: **`read_arxiv_paper`**
Read and extract text content from an arXiv paper PDF.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|arXiv paper ID (e.g., '2106.12345').
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_base_paper`**
Read and extract text content from a BASE paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|BASE paper identifier.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_biorxiv_paper`**
Read and extract text content from a bioRxiv paper PDF.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|bioRxiv DOI.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_citeseerx_paper`**
Read and extract text content from a CiteSeerX paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|CiteSeerX paper identifier.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_crossref_paper`**
Attempt to read and extract text content from a CrossRef paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|CrossRef DOI (e.g., '10.1038/nature12373').
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_dblp_paper`**
Attempt to read and extract text content from a dblp paper.

    Note: dblp doesn't provide direct paper content access.
    This function returns an informative message.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|dblp paper identifier.
`save_path`|`string` *optional*|Directory where the PDF would be saved (unused).

---
#### Tool: **`read_doaj_paper`**
Read and extract text content from a DOAJ paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|DOAJ paper identifier.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_hal_paper`**
Read and extract text content from a HAL paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|HAL paper identifier.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_iacr_paper`**
Read and extract text content from an IACR ePrint paper PDF.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|IACR paper ID (e.g., '2009/101').
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_medrxiv_paper`**
Read and extract text content from a medRxiv paper PDF.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|medRxiv DOI.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_openaire_paper`**
Attempt to read and extract text content from an OpenAIRE paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|OpenAIRE paper identifier.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_openalex_paper`**
Attempt to read and extract text content from an OpenAlex paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|OpenAlex paper ID.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_pubmed_paper`**
Read and extract text content from a PubMed paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|PubMed ID (PMID).
`save_path`|`string` *optional*|Directory where the PDF would be saved (unused).

---
#### Tool: **`read_semantic_paper`**
Read and extract text content from a Semantic Scholar paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|Semantic Scholar paper ID, Paper identifier in one of the following formats:
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`read_ssrn_paper`**
Read paper content from SSRN.

    Note: SSRN connector is metadata-only and read is not supported.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|SSRN paper identifier.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (unused).

---
#### Tool: **`read_zenodo_paper`**
Read and extract text content from a Zenodo paper.
Parameters|Type|Description
-|-|-
`paper_id`|`string`|Zenodo paper identifier.
`save_path`|`string` *optional*|Directory where the PDF is/will be saved (default: './downloads').

---
#### Tool: **`search_arxiv`**
Search academic papers from arXiv.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).
`sort_by`|`string` *optional*|Sort criterion — 'relevance', 'submittedDate', or 'lastUpdatedDate' (default: 'relevance').
`sort_order`|`string` *optional*|Sort direction — 'descending' or 'ascending' (default: 'descending').

---
#### Tool: **`search_base`**
Search academic papers from BASE (Bielefeld Academic Search Engine).
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_biorxiv`**
Search academic papers from bioRxiv.

    Note: bioRxiv API filters by category name within the last 30 days, not full-text
    keyword search. Use a category keyword such as 'bioinformatics', 'neuroscience',
    'cell biology', etc.
Parameters|Type|Description
-|-|-
`query`|`string`|Category name to filter by (e.g., 'bioinformatics', 'neuroscience').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_citeseerx`**
Search academic papers from CiteSeerX digital library.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_core`**
Search academic papers from CORE.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_crossref`**
Search academic papers from CrossRef database.

    CrossRef is a scholarly infrastructure organization that provides 
    persistent identifiers (DOIs) for scholarly content and metadata.
    It's one of the largest citation databases covering millions of 
    academic papers, journals, books, and other scholarly content.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning', 'climate change').
`filter`|`string` *optional*|CrossRef filter string (e.g., 'has-full-text:true,from-pub-date:2020').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10, max: 1000).
`order`|`string` *optional*|Sort order ('asc' or 'desc').
`sort`|`string` *optional*|Sort field ('relevance', 'published', 'updated', 'deposited', etc.).

---
#### Tool: **`search_dblp`**
Search academic papers from dblp computer science bibliography.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_doaj`**
Search academic papers from DOAJ (Directory of Open Access Journals).
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_europepmc`**
Search academic papers from Europe PMC.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_google_scholar`**
Search academic papers from Google Scholar.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_hal`**
Search academic papers from HAL open archive.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_iacr`**
Search academic papers from IACR ePrint Archive.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'cryptography', 'secret sharing').
`fetch_details`|`boolean` *optional*|Whether to fetch detailed information for each paper (default: True).
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_medrxiv`**
Search academic papers from medRxiv.

    Note: medRxiv API filters by category name within the last 30 days, not full-text
    keyword search. Use a category keyword such as 'infectious_diseases',
    'cardiovascular_medicine', 'oncology', etc.
Parameters|Type|Description
-|-|-
`query`|`string`|Category name to filter by (e.g., 'infectious_diseases', 'oncology').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_openaire`**
Search academic papers from OpenAIRE European Open Access infrastructure.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_openalex`**
Search academic papers from OpenAlex.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_papers`**
Unified top-level search across all configured academic platforms.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string.
`max_results_per_source`|`integer` *optional*|Max results to fetch from each selected source.
`sources`|`string` *optional*|Comma-separated source names or 'all'.
`year`|`string` *optional*|Optional year filter for Semantic Scholar only.

---
#### Tool: **`search_pmc`**
Search academic papers from PubMed Central (PMC).
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_pubmed`**
Search academic papers from PubMed.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).
`sort`|`string` *optional*|Sort order — 'relevance' or 'pub_date' (default: 'relevance').

---
#### Tool: **`search_semantic`**
Search academic papers from Semantic Scholar.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).
`year`|`string` *optional*|Optional year filter (e.g., '2019', '2016-2020', '2010-', '-2015').

---
#### Tool: **`search_ssrn`**
Search metadata records from SSRN.

    Note: SSRN connector is metadata-only and does not support direct PDF download.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
#### Tool: **`search_unpaywall`**
Lookup a DOI via Unpaywall and return OA metadata.

    Unpaywall is DOI-centric and does not support generic keyword search.
    This tool extracts the first DOI from `query` and returns at most one record.
Parameters|Type|Description
-|-|-
`query`|`string`|DOI string or text containing a DOI.
`max_results`|`integer` *optional*|Kept for API consistency; Unpaywall returns max 1 record.

---
#### Tool: **`search_zenodo`**
Search academic papers from Zenodo open repository.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query string (e.g., 'machine learning').
`max_results`|`integer` *optional*|Maximum number of papers to return (default: 10).

---
