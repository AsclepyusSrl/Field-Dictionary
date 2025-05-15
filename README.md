# Automated PR Agent Workflow Template

This repository is a **GitHub Template** to quickly set up an automated pull request agent using Qodo’s PR-Agent and Google Gemini. Once instantiated, your repository will run the agent on every new, reopened, or ready-for-review PR (excluding Bot users), posting AI-generated comments and suggestions.

## Features

* Runs on PR events: `opened`, `reopened`, `ready_for_review`
* Skips bot-generated PRs
* Authenticates via a Personal Access Token stored as a secret
* Configurable Google Gemini model for AI summarization and review

## Prerequisites

1. **Organization or repository secrets:**

   * `Workflow_PAT`: A Personal Access Token (classic or fine-grained) with the following scopes:

     * **Repositories**: Contents (Read & Write)
     * **Issues**: Read & Write
     * **Pull requests**: Read & Write
   * `GEMINI_API_KEY`: Your Google AI Studio Gemini API key.
2. **Optional repository variable:**

   * `FEATURE_PRAGENT`: Set to `true` to enable the workflow. Default: `true`.

## Setup Instructions

1. **Create a repository from this template**

   * Click **Use this template** at the top of the repo page.
   * Choose your organization (or personal) account and provide a repository name.

2. **Configure secrets**

   * **Organization-level (Recommended):**

     1. Navigate to **Organization Settings > Secrets and variables > Actions**.
     2. Click **New organization secret**.
     3. Add and name the secrets `Workflow_PAT` and `GEMINI_API_KEY`, and grant access to this (and any) repository.

   * **Repository-level (Alternative):**

     1. Go to your new repo’s **Settings > Secrets and variables > Actions**.
     2. Click **New repository secret**.
     3. Add:

        * `Workflow_PAT`
        * `GEMINI_API_KEY`

3. **Add feature flag (if not using default)**

   1. Go to **Settings > Variables > Repository variables** in your new repo.
   2. Click **New variable**:

      * Name: `FEATURE_PRAGENT`
      * Value: `true`

4. **Review and customize (Optional)**

   * Edit `.github/workflows/pr_agent.yml` to adjust:

     * `CONFIG.MODEL`: change to a different Gemini model.
     * `CONFIG.FALLBACK_MODELS`: update the fallback model list.

## Usage

* Open, reopen, or mark a PR as “ready for review” to trigger the workflow.
* The PR-Agent will automatically post comments or review suggestions on the PR.

## Troubleshooting

* Ensure secrets are correctly named and scoped.
* Check **Actions > Workflows** for run logs and errors.
* Confirm `FEATURE_PRAGENT` variable is set to `true` if the workflow doesn’t run.
