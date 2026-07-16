Bridges multiple AI models and CLIs, enabling orchestrated workflows across Claude Code, Gemini CLI, Codex CLI, and other AI development tools.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/zen](https://hub.docker.com/repository/docker/mcp/zen)
**Author**|[BeehiveInnovations](https://github.com/BeehiveInnovations)
**Repository**|https://github.com/beehiveinnovations/zen-mcp-server

## Available Tools (18)
Tools provided by this Server|Short Description
-|-
`analyze`|Performs comprehensive code analysis with systematic investigation and expert validation.|
`apilookup`|Use this tool automatically when you need current API/SDK documentation, latest version info, breaking changes, deprecations, migration guides, or official release notes.|
`challenge`|Prevents reflexive agreement by forcing critical thinking and reasoned analysis when a statement is challenged.|
`chat`|General chat and collaborative thinking partner for brainstorming, development discussion, getting second opinions, and exploring ideas.|
`clink`|Link a request to an external AI CLI (Gemini CLI, Qwen CLI, etc.) through PAL MCP to reuse their capabilities inside existing workflows.|
`codereview`|Performs systematic, step-by-step code review with expert validation.|
`consensus`|Builds multi-model consensus through systematic analysis and structured debate.|
`debug`|Performs systematic debugging and root cause analysis for any type of issue.|
`docgen`|Generates comprehensive code documentation with systematic analysis of functions, classes, and complexity.|
`listmodels`|Shows which AI model providers are configured, available model names, their aliases and capabilities.|
`planner`|Breaks down complex tasks through interactive, sequential planning with revision and branching capabilities.|
`precommit`|Validates git changes and repository state before committing with systematic analysis.|
`refactor`|Analyzes code for refactoring opportunities with systematic investigation.|
`secaudit`|Performs comprehensive security audit with systematic vulnerability assessment.|
`testgen`|Creates comprehensive test suites with edge case coverage for specific functions, classes, or modules.|
`thinkdeep`|Performs multi-stage investigation and reasoning for complex problem analysis.|
`tracer`|Performs systematic code tracing with modes for execution flow or dependency mapping.|
`version`|Get server version, configuration details, and list of available tools.|

---
## Tools Details

#### Tool: **`analyze`**
Performs comprehensive code analysis with systematic investigation and expert validation. Use for architecture, performance, maintainability, and pattern analysis. Guides through structured code review and strategic planning.
Parameters|Type|Description
-|-|-
`findings`|`string`|Summary of discoveries from this step, including architectural patterns, tech stack assessment, scalability characteristics, performance implications, maintainability factors, and strategic improvement opportunities. IMPORTANT: Document both strengths (good patterns, solid architecture) and concerns (tech debt, overengineering, unnecessary complexity). In later steps, confirm or update past findings with additional evidence.
`model`|`string`|Currently in auto model selection mode. CRITICAL: When the user names a model, you MUST use that exact name unless the server rejects it. If no model is provided, you may use the `listmodels` tool to review options and select an appropriate match. Top models: gpt-5.2 (score 100, 400K ctx, thinking, code-gen); gpt-5.1-codex (score 100, 400K ctx, thinking, code-gen); gemini-2.5-pro (score 100, 1.0M ctx, thinking, code-gen); gemini-3-pro-preview (score 100, 1.0M ctx, thinking, code-gen); gpt-5.2-pro (score 100, 400K ctx, thinking, code-gen); +26 more via `listmodels`.
`next_step_required`|`boolean`|Set to true if you plan to continue the investigation with another step. False means you believe the analysis is complete and ready for expert validation.
`step`|`string`|The analysis plan. Step 1: State your strategy, including how you will map the codebase structure, understand business logic, and assess code quality, performance implications, and architectural patterns. Later steps: Report findings and adapt the approach as new insights emerge.
`step_number`|`integer`|The index of the current step in the analysis sequence, beginning at 1. Each step should build upon or revise the previous one.
`total_steps`|`integer`|Your current estimate for how many steps will be needed to complete the analysis. Adjust as new findings emerge.
`analysis_type`|`string` *optional*|Type of analysis to perform (architecture, performance, security, quality, general)
`confidence`|`string` *optional*|Your confidence in the analysis: exploring, low, medium, high, very_high, almost_certain, or certain. 'certain' indicates the analysis is complete and ready for validation.
`continuation_id`|`string` *optional*|Unique thread continuation ID for multi-turn conversations. Works across different tools. ALWAYS reuse the last continuation_id you were given—this preserves full conversation context, files, and findings so the agent can resume seamlessly.
`files_checked`|`array` *optional*|List all files examined (absolute paths). Include even ruled-out files to track exploration path.
`images`|`array` *optional*|Optional absolute paths to architecture diagrams or visual references that help with analysis context.
`issues_found`|`array` *optional*|Issues or concerns identified during analysis, each with severity level (critical, high, medium, low)
`output_format`|`string` *optional*|How to format the output (summary, detailed, actionable)
`relevant_context`|`array` *optional*|Methods/functions identified as involved in the issue
`relevant_files`|`array` *optional*|Subset of files_checked directly relevant to analysis findings (absolute paths). Include files with significant patterns, architectural decisions, or strategic improvement opportunities.
`temperature`|`number` *optional*|0 = deterministic · 1 = creative.
`thinking_mode`|`string` *optional*|Reasoning depth: minimal, low, medium, high, or max.
`use_assistant_model`|`boolean` *optional*|Use assistant model for expert analysis after workflow steps. False skips expert analysis, relies solely on your personal investigation. Defaults to True for comprehensive validation.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`apilookup`**
Use this tool automatically when you need current API/SDK documentation, latest version info, breaking changes, deprecations, migration guides, or official release notes. This tool searches authoritative sources (official docs, GitHub, package registries) to ensure up-to-date accuracy.
Parameters|Type|Description
-|-|-
`prompt`|`string`|The API, SDK, library, framework, or technology you need current documentation, version info, breaking changes, or migration guidance for.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`challenge`**
Prevents reflexive agreement by forcing critical thinking and reasoned analysis when a statement is challenged. Trigger automatically when a user critically questions, disagrees or appears to push back on earlier answers, and use it manually to sanity-check contentious claims.
Parameters|Type|Description
-|-|-
`prompt`|`string`|Statement to scrutinize. If you invoke `challenge` manually, strip the word 'challenge' and pass just the statement. Automatic invocations send the full user message as-is; do not modify it.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`chat`**
General chat and collaborative thinking partner for brainstorming, development discussion, getting second opinions, and exploring ideas. Use for ideas, validations, questions, and thoughtful explanations.
Parameters|Type|Description
-|-|-
`model`|`string`|Currently in auto model selection mode. CRITICAL: When the user names a model, you MUST use that exact name unless the server rejects it. If no model is provided, you may use the `listmodels` tool to review options and select an appropriate match. Top models: gpt-5.2 (score 100, 400K ctx, thinking, code-gen); gpt-5.1-codex (score 100, 400K ctx, thinking, code-gen); gemini-2.5-pro (score 100, 1.0M ctx, thinking, code-gen); gemini-3-pro-preview (score 100, 1.0M ctx, thinking, code-gen); gpt-5.2-pro (score 100, 400K ctx, thinking, code-gen); +26 more via `listmodels`.
`prompt`|`string`|Your question or idea for collaborative thinking to be sent to the external model. Provide detailed context, including your goal, what you've tried, and any specific challenges. WARNING: Large inline code must NOT be shared in prompt. Provide full-path to files on disk as separate parameter.
`working_directory_absolute_path`|`string`|Absolute path to an existing directory where generated code artifacts can be saved.
`absolute_file_paths`|`array` *optional*|Full, absolute file paths to relevant code in order to share with external model
`continuation_id`|`string` *optional*|Unique thread continuation ID for multi-turn conversations. Works across different tools. ALWAYS reuse the last continuation_id you were given—this preserves full conversation context, files, and findings so the agent can resume seamlessly.
`images`|`array` *optional*|Image paths (absolute) or base64 strings for optional visual context.
`temperature`|`number` *optional*|0 = deterministic · 1 = creative.
`thinking_mode`|`string` *optional*|Reasoning depth: minimal, low, medium, high, or max.

---
#### Tool: **`clink`**
Link a request to an external AI CLI (Gemini CLI, Qwen CLI, etc.) through PAL MCP to reuse their capabilities inside existing workflows.
Parameters|Type|Description
-|-|-
`cli_name`|`string`|Configured CLI client name (from conf/cli_clients). Available: claude, codex, gemini
`prompt`|`string`|User request forwarded to the CLI (conversation context is pre-applied).
`absolute_file_paths`|`array` *optional*|Full paths to relevant code
`continuation_id`|`string` *optional*|Unique thread continuation ID for multi-turn conversations. Works across different tools. ALWAYS reuse the last continuation_id you were given—this preserves full conversation context, files, and findings so the agent can resume seamlessly.
`images`|`array` *optional*|Optional absolute image paths or base64 blobs for visual context.
`role`|`string` *optional*|Optional role preset defined for the selected CLI (defaults to 'default'). Roles per CLI: claude: codereviewer, default, planner; codex: codereviewer, default, planner; gemini: codereviewer, default, planner

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`codereview`**
Performs systematic, step-by-step code review with expert validation. Use for comprehensive analysis covering quality, security, performance, and architecture. Guides through structured investigation to ensure thoroughness.
Parameters|Type|Description
-|-|-
`findings`|`string`|Capture findings (positive and negative) across quality, security, performance, and architecture; update each step.
`model`|`string`|Currently in auto model selection mode. CRITICAL: When the user names a model, you MUST use that exact name unless the server rejects it. If no model is provided, you may use the `listmodels` tool to review options and select an appropriate match. Top models: gpt-5.2 (score 100, 400K ctx, thinking, code-gen); gpt-5.1-codex (score 100, 400K ctx, thinking, code-gen); gemini-2.5-pro (score 100, 1.0M ctx, thinking, code-gen); gemini-3-pro-preview (score 100, 1.0M ctx, thinking, code-gen); gpt-5.2-pro (score 100, 400K ctx, thinking, code-gen); +26 more via `listmodels`.
`next_step_required`|`boolean`|True when another review step follows. External validation: step 1 → True, step 2 → False. Internal validation: set False immediately. Apply the same rule on continuation flows.
`step`|`string`|Review narrative. Step 1: outline the review strategy. Later steps: report findings. MUST cover quality, security, performance, and architecture. Reference code via `relevant_files`; avoid dumping large snippets.
`step_number`|`integer`|Current review step (starts at 1) – each step should build on the last.
`total_steps`|`integer`|Number of review steps planned. External validation: two steps (analysis + summary). Internal validation: one step. Use the same limits when continuing an existing review via continuation_id.
`confidence`|`string` *optional*|Confidence level: exploring (just starting), low (early investigation), medium (some evidence), high (strong evidence), very_high (comprehensive understanding), almost_certain (near complete confidence), certain (100% confidence locally - no external validation needed)
`continuation_id`|`string` *optional*|Unique thread continuation ID for multi-turn conversations. Works across different tools. ALWAYS reuse the last continuation_id you were given—this preserves full conversation context, files, and findings so the agent can resume seamlessly.
`files_checked`|`array` *optional*|Absolute paths of every file reviewed, including those ruled out.
`focus_on`|`string` *optional*|Optional note on areas to emphasise (e.g. 'threading', 'auth flow').
`hypothesis`|`string` *optional*|Current theory about issue/goal based on work
`images`|`array` *optional*|Optional diagram or screenshot paths that clarify review context.
`issues_found`|`array` *optional*|Issues with severity (critical/high/medium/low) and descriptions.
`relevant_context`|`array` *optional*|Methods/functions identified as involved in the issue
`relevant_files`|`array` *optional*|Step 1: list all files/dirs under review. Must be absolute full non-abbreviated paths. Final step: narrow to files tied to key findings.
`review_type`|`string` *optional*|Review focus: full, security, performance, or quick.
`review_validation_type`|`string` *optional*|Set 'external' (default) for expert follow-up or 'internal' for local-only review.
`severity_filter`|`string` *optional*|Lowest severity to include when reporting issues (critical/high/medium/low/all).
`standards`|`string` *optional*|Coding standards or style guides to enforce.
`temperature`|`number` *optional*|0 = deterministic · 1 = creative.
`thinking_mode`|`string` *optional*|Reasoning depth: minimal, low, medium, high, or max.
`use_assistant_model`|`boolean` *optional*|Use assistant model for expert analysis after workflow steps. False skips expert analysis, relies solely on your personal investigation. Defaults to True for comprehensive validation.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`consensus`**
Builds multi-model consensus through systematic analysis and structured debate. Use for complex decisions, architectural choices, feature proposals, and technology evaluations. Consults multiple models with different stances to synthesize comprehensive recommendations.
Parameters|Type|Description
-|-|-
`findings`|`string`|Step 1: your independent analysis for later synthesis (not shared with other models). Steps 2+: summarize the newest model response.
`next_step_required`|`boolean`|True if more model consultations remain; set false when ready to synthesize.
`step`|`string`|Consensus prompt. Step 1: write the exact proposal/question every model will see (use 'Evaluate…', not meta commentary). Steps 2+: capture internal notes about the latest model response—these notes are NOT sent to other models.
`step_number`|`integer`|Current step index (starts at 1). Step 1 is your analysis; steps 2+ handle each model response.
`total_steps`|`integer`|Total steps = number of models consulted plus the final synthesis step.
`continuation_id`|`string` *optional*|Unique thread continuation ID for multi-turn conversations. Works across different tools. ALWAYS reuse the last continuation_id you were given—this preserves full conversation context, files, and findings so the agent can resume seamlessly.
`current_model_index`|`integer` *optional*|0-based index of the next model to consult (managed internally).
`images`|`array` *optional*|Optional absolute image paths or base64 references that add helpful visual context.
`model_responses`|`array` *optional*|Internal log of responses gathered so far.
`models`|`array` *optional*|User-specified roster of models to consult (provide at least two entries). User-specified list of models to consult (provide at least two entries). Each entry may include model, stance (for/against/neutral), and stance_prompt. Each (model, stance) pair must be unique, e.g. [{'model':'gpt5','stance':'for'}, {'model':'pro','stance':'against'}]. When the user names a model, you MUST use that exact value or report the provider error—never swap in another option. Use the `listmodels` tool for the full roster. Top models: gpt-5.2 (score 100, 400K ctx, thinking, code-gen); gpt-5.1-codex (score 100, 400K ctx, thinking, code-gen); gemini-2.5-pro (score 100, 1.0M ctx, thinking, code-gen); gemini-3-pro-preview (score 100, 1.0M ctx, thinking, code-gen); gpt-5.2-pro (score 100, 400K ctx, thinking, code-gen); +26 more via `listmodels`.
`relevant_files`|`array` *optional*|Optional supporting files that help the consensus analysis. Must be absolute full, non-abbreviated paths.
`use_assistant_model`|`boolean` *optional*|Use assistant model for expert analysis after workflow steps. False skips expert analysis, relies solely on your personal investigation. Defaults to True for comprehensive validation.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`debug`**
Performs systematic debugging and root cause analysis for any type of issue. Use for complex bugs, mysterious errors, performance issues, race conditions, memory leaks, and integration problems. Guides through structured investigation with hypothesis testing and expert analysis.
Parameters|Type|Description
-|-|-
`findings`|`string`|Discoveries: clues, code/log evidence, disproven theories. Be specific. If no bug found, document clearly as valid.
`model`|`string`|Currently in auto model selection mode. CRITICAL: When the user names a model, you MUST use that exact name unless the server rejects it. If no model is provided, you may use the `listmodels` tool to review options and select an appropriate match. Top models: gpt-5.2 (score 100, 400K ctx, thinking, code-gen); gpt-5.1-codex (score 100, 400K ctx, thinking, code-gen); gemini-2.5-pro (score 100, 1.0M ctx, thinking, code-gen); gemini-3-pro-preview (score 100, 1.0M ctx, thinking, code-gen); gpt-5.2-pro (score 100, 400K ctx, thinking, code-gen); +26 more via `listmodels`.
`next_step_required`|`boolean`|True if you plan to continue the investigation with another step. False means root cause is known or investigation is complete. IMPORTANT: When continuation_id is provided (continuing a previous conversation), set this to False to immediately proceed with expert analysis.
`step`|`string`|Investigation step. Step 1: State issue+direction. Symptoms misleading; 'no bug' valid. Trace dependencies, verify hypotheses. Use relevant_files for code; this for text only.
`step_number`|`integer`|Current step index (starts at 1). Build upon previous steps.
`total_steps`|`integer`|Estimated total steps needed to complete the investigation. Adjust as new findings emerge. IMPORTANT: When continuation_id is provided (continuing a previous conversation), set this to 1 as we're not starting a new multi-step investigation.
`confidence`|`string` *optional*|Your confidence in the hypothesis: exploring (starting out), low (early idea), medium (some evidence), high (strong evidence), very_high (very strong evidence), almost_certain (nearly confirmed), certain (100% confidence - root cause and fix are both confirmed locally with no need for external validation). WARNING: Do NOT use 'certain' unless the issue can be fully resolved with a fix, use 'very_high' or 'almost_certain' instead when not 100% sure. Using 'certain' means you have ABSOLUTE confidence locally and PREVENTS external model validation.
`continuation_id`|`string` *optional*|Unique thread continuation ID for multi-turn conversations. Works across different tools. ALWAYS reuse the last continuation_id you were given—this preserves full conversation context, files, and findings so the agent can resume seamlessly.
`files_checked`|`array` *optional*|All examined files (absolute paths), including ruled-out ones.
`hypothesis`|`string` *optional*|Concrete root cause theory from evidence. Can revise. Valid: 'No bug found - user misunderstanding' or 'Symptoms unrelated to code' if supported.
`images`|`array` *optional*|Optional screenshots/visuals clarifying issue (absolute paths).
`issues_found`|`array` *optional*|Issues identified with severity levels during work
`relevant_context`|`array` *optional*|Methods/functions identified as involved in the issue
`relevant_files`|`array` *optional*|Files directly relevant to issue (absolute paths). Cause, trigger, or manifestation locations.
`temperature`|`number` *optional*|0 = deterministic · 1 = creative.
`thinking_mode`|`string` *optional*|Reasoning depth: minimal, low, medium, high, or max.
`use_assistant_model`|`boolean` *optional*|Use assistant model for expert analysis after workflow steps. False skips expert analysis, relies solely on your personal investigation. Defaults to True for comprehensive validation.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`docgen`**
Generates comprehensive code documentation with systematic analysis of functions, classes, and complexity. Use for documentation generation, code analysis, complexity assessment, and API documentation. Analyzes code structure and patterns to create thorough documentation.
Parameters|Type|Description
-|-|-
`comments_on_complex_logic`|`boolean`|True (default) to add inline comments around non-obvious logic.
`document_complexity`|`boolean`|Include algorithmic complexity (Big O) analysis when True (default).
`document_flow`|`boolean`|Include call flow/dependency notes when True (default).
`findings`|`string`|Important findings, evidence and insights discovered in this step
`next_step_required`|`boolean`|Whether another work step is needed. When false, aim to reduce total_steps to match step_number to avoid mismatch.
`num_files_documented`|`integer`|Count of files finished so far. Increment only when a file is fully documented.
`step`|`string`|Current work step content and findings from your overall work
`step_number`|`integer`|Current step number in work sequence (starts at 1)
`total_files_to_document`|`integer`|Total files identified in discovery; completion requires matching this count.
`total_steps`|`integer`|Estimated total steps needed to complete work
`update_existing`|`boolean`|True (default) to polish inaccurate or outdated docs instead of leaving them untouched.
`continuation_id`|`string` *optional*|Unique thread continuation ID for multi-turn conversations. Works across different tools. ALWAYS reuse the last continuation_id you were given—this preserves full conversation context, files, and findings so the agent can resume seamlessly.
`issues_found`|`array` *optional*|Issues identified with severity levels during work
`relevant_context`|`array` *optional*|Methods/functions identified as involved in the issue
`relevant_files`|`array` *optional*|Files identified as relevant to issue/goal (FULL absolute paths to real files/folders - DO NOT SHORTEN)
`use_assistant_model`|`boolean` *optional*|Use assistant model for expert analysis after workflow steps. False skips expert analysis, relies solely on your personal investigation. Defaults to True for comprehensive validation.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`listmodels`**
Shows which AI model providers are configured, available model names, their aliases and capabilities.
#### Tool: **`planner`**
Breaks down complex tasks through interactive, sequential planning with revision and branching capabilities. Use for complex project planning, system design, migration strategies, and architectural decisions. Builds plans incrementally with deep reflection for complex scenarios.
Parameters|Type|Description
-|-|-
`model`|

[...]
