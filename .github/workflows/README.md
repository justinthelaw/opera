# GitHub Actions, Configurations and Workflows

## [Test Pipeline](./test-pipeline.yml)

Lints, tests, builds, and deploys the Opera full-stack application.

## [CodeQL Quality](./codeql.yml)

Scans source code for quality and security issues.

## [Deploy Application](./deploy-application.yml)

Pushes the built application source code to the production environment.

## [Cleanup Repository](./cleanup-repository.yml)

Cleans out all of the cached artifacts the pipelines use once a pull request has closed on a branch. Also deletes workflow runs older than 5 days old.

## [Dependabot](../dependabot.yml)

This workflow sets up the automatic pull request generation for dependency bumps, running checks to ensure the dependency doesn't break the application build.

# Available Issues Templates

## [Bug Report](../ISSUE_TEMPLATE/bug_report.md)

For reporting application or developer environment defects.

## [Feature Request](../ISSUE_TEMPLATE/feature_request.md)

For requesting new capabilities in any part of Opera.
