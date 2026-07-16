Educational Python refactoring assistant that provides guided suggestions for AI assistants.
.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/mcp-python-refactoring](https://hub.docker.com/repository/docker/mcp/mcp-python-refactoring)
**Author**|[slamer59](https://github.com/slamer59)
**Repository**|https://github.com/slamer59/mcp-python-refactoring

## Available Tools (9)
Tools provided by this Server|Short Description
-|-
`analyze_python_file`|Analyze Python file for refactoring opportunities with precise guidance|
`analyze_python_package`|Comprehensive package/folder analysis for refactoring opportunities|
`analyze_security_and_patterns`|Comprehensive security scanning and modern Python patterns analysis|
`analyze_test_coverage`|Analyze Python test coverage and suggest improvements|
`find_long_functions`|Find functions that are candidates for extraction|
`find_package_issues`|Identify package-level refactoring opportunities and structural issues|
`get_extraction_guidance`|Get detailed step-by-step guidance for extracting functions|
`get_package_metrics`|Get aggregated metrics for a Python package|
`tdd_refactoring_guidance`|Generate TDD-based refactoring guidance: test first, refactor, test again|

---
## Tools Details

#### Tool: **`analyze_python_file`**
Analyze Python file for refactoring opportunities with precise guidance
Parameters|Type|Description
-|-|-
`content`|`string`|Python file content to analyze
`file_path`|`string` *optional*|Path to Python file to analyze

---
#### Tool: **`analyze_python_package`**
Comprehensive package/folder analysis for refactoring opportunities
Parameters|Type|Description
-|-|-
`package_path`|`string`|Path to Python package/folder to analyze
`package_name`|`string` *optional*|Name of the package (optional, will be inferred from path)

---
#### Tool: **`analyze_security_and_patterns`**
Comprehensive security scanning and modern Python patterns analysis
Parameters|Type|Description
-|-|-
`content`|`string`|Python file content to analyze
`file_path`|`string` *optional*|Path to Python file to analyze
`include_dependency_scan`|`boolean` *optional*|Include dependency vulnerability scanning (default: true)
`include_modernization`|`boolean` *optional*|Include modern Python pattern suggestions (default: true)
`include_security_scan`|`boolean` *optional*|Include code security vulnerability scanning (default: true)

---
#### Tool: **`analyze_test_coverage`**
Analyze Python test coverage and suggest improvements
Parameters|Type|Description
-|-|-
`source_path`|`string`|Path to source code directory or file
`target_coverage`|`integer` *optional*|Target coverage percentage (default: 80)
`test_path`|`string` *optional*|Path to test directory (optional)

---
#### Tool: **`find_long_functions`**
Find functions that are candidates for extraction
Parameters|Type|Description
-|-|-
`content`|`string`|Python file content to analyze
`line_threshold`|`integer` *optional*|Minimum lines to consider a function long (default: 20)

---
#### Tool: **`find_package_issues`**
Identify package-level refactoring opportunities and structural issues
Parameters|Type|Description
-|-|-
`package_path`|`string`|Path to Python package/folder
`issue_types`|`array` *optional*|Specific types of issues to look for (optional): scattered_functionality, god_package, circular_dependency, etc.

---
#### Tool: **`get_extraction_guidance`**
Get detailed step-by-step guidance for extracting functions
Parameters|Type|Description
-|-|-
`content`|`string`|Python file content
`file_path`|`string` *optional*|Path to Python file
`function_name`|`string` *optional*|Name of function to analyze for extraction

---
#### Tool: **`get_package_metrics`**
Get aggregated metrics for a Python package
Parameters|Type|Description
-|-|-
`package_path`|`string`|Path to Python package/folder
`package_name`|`string` *optional*|Name of the package (optional)

---
#### Tool: **`tdd_refactoring_guidance`**
Generate TDD-based refactoring guidance: test first, refactor, test again
Parameters|Type|Description
-|-|-
`content`|`string`|Python code content to refactor
`function_name`|`string` *optional*|Specific function/class to refactor (optional)
`test_path`|`string` *optional*|Path to test directory (optional)

---
