MCP server that enables intelligent NPM package analysis powered by AI.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/npm-sentinel](https://hub.docker.com/repository/docker/mcp/npm-sentinel)
**Author**|[Nekzus](https://github.com/Nekzus)
**Repository**|https://github.com/Nekzus/npm-sentinel-mcp

## Available Tools (19)
Tools provided by this Server|Short Description
-|-
`npmAlternatives`|Find NPM Package Alternatives|
`npmChangelogAnalysis`|Analyze NPM Package Changelog (GitHub)|
`npmCompare`|Compare NPM Packages|
`npmDeprecated`|Check NPM Package Deprecation Status|
`npmDeps`|Get Package Dependencies|
`npmLatest`|Get Latest Package Information|
`npmLicenseCompatibility`|Check NPM License Compatibility|
`npmMaintainers`|Get NPM Package Maintainers|
`npmMaintenance`|Analyze NPM Package Maintenance (NPMS.io)|
`npmPackageReadme`|Get NPM Package README|
`npmQuality`|Analyze NPM Package Quality (NPMS.io)|
`npmRepoStats`|Get NPM Package Repository Stats (GitHub)|
`npmScore`|Get NPM Package Score (NPMS.io)|
`npmSearch`|Search NPM Packages|
`npmSize`|Get Package Size (Bundlephobia)|
`npmTrends`|Get NPM Package Download Trends|
`npmTypes`|Check TypeScript Type Availability|
`npmVersions`|Get All Package Versions|
`npmVulnerabilities`|Check Package Vulnerabilities (OSV.dev)|

---
## Tools Details

#### Tool: **`npmAlternatives`**
Find alternative packages with similar functionality
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to find alternatives for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmChangelogAnalysis`**
Analyze changelog and release history of packages
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to analyze changelogs for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmCompare`**
Compare multiple NPM packages based on various metrics
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to compare

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmDeprecated`**
Check if packages are deprecated
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to check for deprecation

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmDeps`**
Analyze dependencies and devDependencies of an NPM package
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to analyze dependencies for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmLatest`**
Get the latest version and changelog of an NPM package
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to get latest versions for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmLicenseCompatibility`**
Check license compatibility between multiple packages
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to check for license compatibility

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmMaintainers`**
Get maintainers information for NPM packages
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to get maintainers for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmMaintenance`**
Analyze package maintenance metrics
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to analyze

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmPackageReadme`**
Get the README content for NPM packages
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to get READMEs for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmQuality`**
Analyze package quality metrics
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to analyze

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmRepoStats`**
Get repository statistics for NPM packages
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to get repository stats for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmScore`**
Get consolidated package score based on quality, maintenance, and popularity metrics
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to get scores for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmSearch`**
Search for NPM packages with optional limit
Parameters|Type|Description
-|-|-
`query`|`string`|Search query for packages
`limit`|`number` *optional*|Maximum number of results to return (default: 10)

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmSize`**
Get package size information including dependencies and bundle size
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to get size information for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmTrends`**
Get download trends and popularity metrics for packages
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to get trends for
`period`|`string` *optional*|Time period for trends. Options: "last-week", "last-month", "last-year"

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmTypes`**
Check TypeScript types availability and version for a package
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to check types for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmVersions`**
Get all available versions of an NPM package
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to get versions for

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`npmVulnerabilities`**
Check for known vulnerabilities in packages
Parameters|Type|Description
-|-|-
`packages`|`array`|List of package names to check for vulnerabilities

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---

## Screenshots

![NPM Sentinel screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/npm-sentinel-1.png)
