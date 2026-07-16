A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/circleci](https://hub.docker.com/repository/docker/mcp/circleci)
**Author**|[CircleCI-Public](https://github.com/CircleCI-Public)
**Repository**|https://github.com/CircleCI-Public/mcp-server-circleci

## Available Tools (12)
Tools provided by this Server|Short Description
-|-
`analyze_diff`|This tool is used to analyze a git diff (unstaged, staged, or all changes) against cursor rules to identify rule violations.|
`config_helper`|This tool helps analyze and validate and fix CircleCI configuration files.|
`create_prompt_template`|ABOUT THIS TOOL: - This tool is part of a toolchain that generates and provides test cases for a prompt template.|
`find_flaky_tests`|This tool retrieves information about flaky tests in a CircleCI project.|
`get_build_failure_logs`|This tool helps debug CircleCI build failures by retrieving failure logs.|
`get_job_test_results`|This tool retrieves test metadata for a CircleCI job.|
`get_latest_pipeline_status`|This tool retrieves the status of the latest pipeline for a CircleCI project.|
`list_followed_projects`|This tool lists all projects that the user is following on CircleCI.|
`recommend_prompt_template_tests`|About this tool: - This tool is part of a toolchain that generates and provides test cases for a prompt template.|
`rerun_workflow`|This tool is used to rerun a workflow from start or from the failed job.|
`run_evaluation_tests`|This tool allows the users to run evaluation tests on a circleci pipeline.|
`run_pipeline`|This tool triggers a new CircleCI pipeline and returns the URL to monitor its progress.|

---
## Tools Details

#### Tool: **`analyze_diff`**
This tool is used to analyze a git diff (unstaged, staged, or all changes) against cursor rules to identify rule violations.
  By default, the tool will use the staged changes, unless the user explicitly asks for unstaged or all changes.

  Parameters:
  - params: An object containing:
    - speedMode: boolean - A mode that can be enabled to speed up the analysis. Default value is false.
    - filterBy: enum - "Violations" | "Compliants" | "Human Review Required" | "None" - A filter that can be applied to set the focus of the analysis. Default is None.
    - diff: string - A git diff string.
    - rules: string - The rules to use for the analysis, found in .cursorrules or the .cursor/rules directory. Combine all rules from multiple files by separating them with ---

  Returns:
  - A list of rule violations found in the git diff.
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`config_helper`**
This tool helps analyze and validate and fix CircleCI configuration files.

  Parameters:
  - params: An object containing:
    - configFile: string - The full contents of the CircleCI config file as a string. This should be the raw YAML content, not a file path.

  Example usage:
  {
    "params": {
      "configFile": "version: 2.1
orbs:
  node: circleci/node@7
..."
    }
  }

  Note: The configFile content should be provided as a properly escaped string with newlines represented as 
.

  Tool output instructions:
    - If the config is invalid, the tool will return the errors and the original config. Use the errors to fix the config.
    - If the config is valid, do nothing.
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`create_prompt_template`**
ABOUT THIS TOOL:
  - This tool is part of a toolchain that generates and provides test cases for a prompt template.
  - This tool helps an AI assistant to generate a prompt template based on one of the following:
    1. feature requirements defined by a user - in which case the tool will generate a new prompt template based on the feature requirements.
    2. a pre-existing prompt or prompt template that a user wants to test, evaluate, or modify - in which case the tool will convert it into a more structured and testable prompt template while leaving the original prompt language relatively unchanged.
  - This tool will return a structured prompt template (e.g. `template`) along with a context schema (e.g. ``contextSchema``) that defines the expected input parameters for the prompt template.
  - In some cases, a user will want to add test coverage for ALL of the prompts in a given application. In these cases, the AI agent should use this tool to generate a prompt template for each prompt in the application, and should check the entire application for AI prompts that are not already covered by a prompt template in the `./prompts` directory.

  WHEN SHOULD THIS TOOL BE TRIGGERED?
  - This tool should be triggered whenever the user provides requirements for a new AI-enabled application or a new AI-enabled feature of an existing  application (i.e. one that requires a prompt request to an LLM or any AI model).
  - This tool should also be triggered if the user provides a pre-existing prompt or prompt template from their codebase that they want to test, evaluate, or modify.
  - This tool should be triggered even if there are pre-existing files in the `./prompts` directory with the `<relevant-name>.prompt.yml` convention (e.g. `bedtime-story-generator.prompt.yml`, `plant-care-assistant.prompt.yml`, `customer-support-chatbot.prompt.yml`, etc.). Similar files should NEVER be generated directly by the AI agent. Instead, the AI agent should use this tool to first generate a new prompt template.

  PARAMETERS:
  - params: object
    - prompt: string (the feature requirements or pre-existing prompt/prompt template that will be used to generate a prompt template. Can be a multi-line string.)
    - promptOrigin: "codebase" | "requirements" (indicates whether the prompt comes from an existing codebase or from new requirements)
    - model: string (the model that the prompt template will be tested against. Explicitly specify the model if it can be inferred from the codebase. Otherwise, defaults to `gpt-4.1-mini`.)
    - temperature: number (the temperature of the prompt template. Explicitly specify the temperature if it can be inferred from the codebase. Otherwise, defaults to 1.)

  EXAMPLE USAGE (from new requirements):
  {
    "params": {
      "prompt": "Create an app that takes any topic and an age (in years), then renders a 1-minute bedtime story for a person of that age.",
      "promptOrigin": "requirements"
      "model": "gpt-4.1-mini"
      "temperature": 1.0
    }
  }

  EXAMPLE USAGE (from pre-existing prompt/prompt template in codebase):
  {
    "params": {
      "prompt": "The user wants a bedtime story about {{topic}} for a person of age {{age}} years old. Please craft a captivating tale that captivates their imagination and provides a delightful bedtime experience.",
      "promptOrigin": "codebase"
      "model": "claude-3-5-sonnet-latest"
      "temperature": 0.7
    }
  }

  TOOL OUTPUT INSTRUCTIONS:
  - The tool will return...
    - a `template` that reformulates the user's prompt into a more structured format.
    - a ``contextSchema`` that defines the expected input parameters for the template.
    - a `promptOrigin` that indicates whether the prompt comes from an existing prompt or prompt template in the user's codebase or from new requirements.
  - The tool output -- the `template`, ``contextSchema``, and `promptOrigin` -- will also be used as input to the `recommend_prompt_template_tests` tool to generate a list of recommended tests that can be used to test the prompt template.
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`find_flaky_tests`**
This tool retrieves information about flaky tests in a CircleCI project. 

    The agent receiving this output MUST analyze the flaky test data and implement appropriate fixes based on the specific issues identified.

    CRITICAL REQUIREMENTS:
    1. Truncation Handling (HIGHEST PRIORITY):
       - ALWAYS check for <MCPTruncationWarning> in the output
       - When present, you MUST start your response with:
         "WARNING: The logs have been truncated. Only showing the most recent entries. Earlier build failures may not be visible."
       - Only proceed with log analysis after acknowledging the truncation

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug:
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI project in any of these formats:
      * Project URL: https://app.circleci.com/pipelines/gh/organization/project
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/xyz

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects
    - If using Option 2, the URLs MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, BOTH parameters (workspaceRoot, gitRemoteURL) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`get_build_failure_logs`**
This tool helps debug CircleCI build failures by retrieving failure logs.

    CRITICAL REQUIREMENTS:
    1. Truncation Handling (HIGHEST PRIORITY):
       - ALWAYS check for <MCPTruncationWarning> in the output
       - When present, you MUST start your response with:
         "WARNING: The logs have been truncated. Only showing the most recent entries. Earlier build failures may not be visible."
       - Only proceed with log analysis after acknowledging the truncation

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug and branch (BOTH required):
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")
    - branch: The name of the branch (required when using projectSlug)

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI project in any of these formats:
      * Project URL: https://app.circleci.com/pipelines/gh/organization/project
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123
      * Legacy Job URL: https://circleci.com/pipelines/gh/organization/project/123
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/xyz

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository
    - branch: The name of the current branch

    Recommended Workflow:
    1. Use listFollowedProjects tool to get a list of projects
    2. Extract the projectSlug from the chosen project (format: "gh/organization/project")
    3. Use that projectSlug with a branch name for this tool

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects
    - If using Option 2, the URLs MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, ALL THREE parameters (workspaceRoot, gitRemoteURL, branch) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`get_job_test_results`**
This tool retrieves test metadata for a CircleCI job.

    PRIORITY USE CASE:
    - When asked "are tests passing in CI?" or similar questions about test status
    - When asked to "fix failed tests in CI" or help with CI test failures
    - Use this tool to check if tests are passing in CircleCI and identify failed tests

    Common use cases:
    - Get test metadata for a specific job
    - Get test metadata for all jobs in a project
    - Get test metadata for a specific branch
    - Get test metadata for a specific pipeline
    - Get test metadata for a specific workflow
    - Get test metadata for a specific job

    CRITICAL REQUIREMENTS:
    1. Truncation Handling (HIGHEST PRIORITY):
       - ALWAYS check for <MCPTruncationWarning> in the output
       - When present, you MUST start your response with:
         "WARNING: The test results have been truncated. Only showing the most recent entries. Some test data may not be visible."
       - Only proceed with test result analysis after acknowledging the truncation

    2. Test Result Filtering:
       - Use filterByTestsResult parameter to filter test results:
         * filterByTestsResult: 'failure' - Show only failed tests
         * filterByTestsResult: 'success' - Show only successful tests
       - When looking for failed tests, ALWAYS set filterByTestsResult to 'failure'
       - When checking if tests are passing, set filterByTestsResult to 'success'

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug and branch (BOTH required):
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")
    - branch: The name of the branch (required when using projectSlug)

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI job in any of these formats:
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/789
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository
    - branch: The name of the current branch

    For simple test status checks (e.g., "are tests passing in CI?") or fixing failed tests, prefer Option 1 with a recent pipeline URL if available.

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects and include the branch parameter
    - If using Option 2, the URL MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, ALL THREE parameters (workspaceRoot, gitRemoteURL, branch) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`get_latest_pipeline_status`**
This tool retrieves the status of the latest pipeline for a CircleCI project. It can be used to check pipeline status, get latest build status, or view current pipeline state.

    Common use cases:
    - Check latest pipeline status
    - Get current build status
    - View pipeline state
    - Check build progress
    - Get pipeline information

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug and branch (BOTH required):
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")
    - branch: The name of the branch (required when using projectSlug)

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI project in any of these formats:
      * Project URL: https://app.circleci.com/pipelines/gh/organization/project
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/xyz
      * Legacy Job URL: https://circleci.com/gh/organization/project/123

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository
    - branch: The name of the current branch

    Recommended Workflow:
    1. Use listFollowedProjects tool to get a list of projects
    2. Extract the projectSlug from the chosen project (format: "gh/organization/project")
    3. Use that projectSlug with a branch name for this tool

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects
    - If using Option 2, the URLs MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, ALL THREE parameters (workspaceRoot, gitRemoteURL, branch) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`list_followed_projects`**
This tool lists all projects that the user is following on CircleCI.

    Common use cases:
    - Identify which CircleCI projects are available to the user
    - Select a project for subsequent operations
    - Obtain the projectSlug needed for other CircleCI tools

    Returns:
    - A list of projects that the user is following on CircleCI
    - Each entry includes the project name and its projectSlug

    Workflow:
    1. Run this tool to see available projects
    2. User selects a project from the list
    3. The LLM should extract and use the projectSlug (not the project name) from the selected project for subsequent tool calls
    4. The projectSlug is required for many other CircleCI tools, and will be used for those tool calls after a project is selected

    Note: If pagination limits are reached, the tool will indicate that not all projects could be displayed.

    IMPORTANT: Do not automatically run any additional tools after this tool is called. Wait for explicit user instruction before executing further tool calls. The LLM MUST NOT invoke any other CircleCI tools until receiving a clear instruction from the user about what to do next, even if the user selects a project. It is acceptable to list out tool call options for the user to choose from, but do not execute them until instructed.
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`recommend_prompt_template_tests`**
About this tool:
  - This tool is part of a toolchain that generates and provides test cases for a prompt template.
  - This tool generates an array of recommended tests for a given prompt template.

  Parameters:
  - params: object
    - promptTemplate: string (the prompt template to be tested)
    - contextSchema: object (the context schema that defines the expected input parameters for the prompt template)
    - promptOrigin: "codebase" | "requirements" (indicates whether the prompt comes from an existing codebase or from new requirements)
    - model: string (the model that the prompt template will be tested against)

  Example usage:
  {
    "params": {
      "promptTemplate": "The user wants a bedtime story about {{topic}} for a person of age {{age}} years old. Please craft a captivating tale that captivates their imagination and provides a delightful bedtime experience.",
      "contextSchema": {
        "topic": "string",
        "age": "number"
      },
      "promptOrigin": "codebase"
    }
  }

  The tool will return a structured array of test cases that can be used to test the prompt template.

  Tool output instructions:
    - The tool will return a `recommendedTests` array that can be used to test the prompt template.
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`rerun_workflow`**
This tool is used to rerun a workflow from start or from the failed job.

  Common use cases:
  - Rerun a workflow from a failed job
  - Rerun a workflow from start

Input options (EXACTLY ONE of these TWO options must be used):

Option 1 - Workflow ID:
- workflowId: The ID of the workflow to rerun
- fromFailed: true to rerun from failed, false to rerun from start. If omitted, behavior is based on workflow status. (optional)

Option 2 - Workflow URL:
- workflowURL: The URL of the workflow to rerun
  * Workflow URL: https://app.circleci.com/pipelines/:vcsType/:orgName/:projectName/:pipelineNumber/workflows/:workflowId
  * Workflow Job URL: https://app.circleci.com/pipelines/:vcsType/:orgName/:projectName/:pipelineNumber/workflows/:workflowId/jobs/:buildNumber
- fromFailed: true to rerun from failed, false to rerun from start. If omitted, behavior is based on workflow status. (optional)
Parameters|Type|Description
-|-|-
`params`|`object`|

---
#### Tool: **`run_evaluation_tests`**
This tool allows the users to run evaluation tests on a circleci pipeline.
    They can be referred to as "Prompt Tests" or "Evaluation Tests".

    This tool triggers a new CircleCI pipeline and returns the URL to monitor its progress.
    The tool will generate an appropriate circleci configuration file and trigger a pipeline using this temporary configuration.
    The tool will return the project slug.

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug and branch (BOTH required):
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")
    - branch: The name of the branch (required when using projectSlug)

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI project in any of these formats:
      * Project URL with branch: https://app.circleci.com/pipelines/gh/organization/project?branch=feature-branch
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/xyz

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository
    - branch: The name of the current branch

    Test Files:
    - promptFiles: Array of prompt template file objects from the ./prompts directory, each containing:
      * fileName: The name of the prompt template file
      * fileContent: The contents of the prompt template file

    Pipeline Selection:
    - If the project has multiple pipeline definitions, the tool will return a list of available pipelines
    - You must then make another call with the chosen pipeline name using the pipelineChoiceName parameter
    - The pipelineChoiceName must exactly match one of the pipeline names returned by the tool
    - If the project has only one pipeline definition, pipelineChoiceName is not needed

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects
    - If using Option 2, the URLs MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, ALL THREE parameters (workspaceRoot, gitRemoteURL, branch) must be provided
    - If none

[...]
