# Opera: Optimized Performance and Evaluation Rhetoric AI

<div align="center">
    
[![test-pipeline](https://github.com/justinthelaw/opera/actions/workflows/test-pipeline.yml/badge.svg)](https://github.com/justinthelaw/opera/actions)
[![snyk-security](https://github.com/justinthelaw/opera/actions/workflows/snyk-security.yml/badge.svg)](https://github.com/justinthelaw/opera/actions/workflows/snyk-security.yml)
[![CodeQL](https://github.com/justinthelaw/opera/actions/workflows/codeql.yml/badge.svg)](https://github.com/justinthelaw/opera/actions/workflows/codeql.yml)

</div>

**_Opera_**: Latin word (plural of opus) meaning "work," "effort," or "service." Usually referring to an individual or group's skillful or creative endeavors.

Opera is a project focused on developing a set of tools to automate the pointless aspects of performance report and award writing so that officer and enlisted members can focus more on the individual and the achievements, rather than worry about irrelevant formatting. The ultimate objective is to allow the end-user to type or speak a stream of consciousness about a member's accomplishments and let Opera handle the rest.

The Forge is Opera's narrative generation tool that harnesses the power of Natural Language Processing (NLP) through the use of Large Language Models (LLM). The Forge is an API that is connected to a fine-tuned model that has been trained using 33,000+ unique EPR, OPR, and Award packages, across all of the Air and Space Force's positions and ranks.

# Table of Contents

1. [Background](#background)
2. [The Forge](#the-forge)
3. [Application Usage](#application-usage)
4. [Contributing](#contributing)
5. [Local Development](#local-development)
6. [Licensing](#licensing)

# Opera: Optimized Performance and Evaluation Rhetoric AI

<div align="center">
    
[![test-pipeline](https://github.com/justinthelaw/opera/actions/workflows/test-pipeline.yml/badge.svg)](https://github.com/justinthelaw/opera/actions)
[![snyk-security](https://github.com/justinthelaw/opera/actions/workflows/snyk-security.yml/badge.svg)](https://github.com/justinthelaw/opera/actions/workflows/snyk-security.yml)
[![CodeQL](https://github.com/justinthelaw/opera/actions/workflows/codeql.yml/badge.svg)](https://github.com/justinthelaw/opera/actions/workflows/codeql.yml)

</div>

**_Opera_**: Latin word (plural of opus) meaning "work," "effort," or "service." Usually referring to an individual or group's skillful or creative endeavors.

Opera is a project focused on developing a set of tools to automate the pointless aspects of performance report and award writing so that officer and enlisted members can focus more on the individual and the achievements, rather than worry about irrelevant formatting. The ultimate objective is to allow the end-user to type or speak a stream of consciousness about a member's accomplishments and let Opera handle the rest.

The Forge is Opera's narrative generation tool that harnesses the power of Natural Language Processing (NLP) through the use of Large Language Models (LLM). The Forge is an API that is connected to a fine-tuned model that has been trained using 33,000+ unique EPR, OPR, and Award packages, across all of the Air and Space Force's positions and ranks.

# Table of Contents

1. [Background](#background)
2. [The Forge](#the-forge)
3. [Application Usage](#application-usage)
4. [Contributing](#contributing)
5. [Local Development](#local-development)
6. [Licensing](#licensing)
7. [Manual Deployment](#manual-deployment)

# Background

## What are "Bullets" and "Narratives"

...

## How are "Bullets" Formatted

...

## Example Bullets

...

## How are "Narratives" Formatted

...

## Example Narratives

...

# The Forge

...

# Application Usage

...

# Contributing

...

# Local Development

...

# Pushing

...

## Pipelines

...

# Licensing

...

# Manual Deployment

Please note that only authorized users with the necessary permissions can manually trigger the deployment workflow.

</old_file>

## Pull Requests

When describing a pull request, please provide the following:

1. Merge request title or summary as outlined in the [Committing and Merging](#committing-and-merging) section
2. High-level description of what was changed or been added/deleted
3. Attachment and/or linking to an existing issue or project task

## Issues

For bugs, follow the [bug report template](./.github/ISSUE_TEMPLATE/bug_report.md) as closely as possible so that developers can reproduce and debug the issue.

For feature requests, follow the [feature request template](./.github/ISSUE_TEMPLATE/feature_request.md) as closely as possible, providing detail (imagery, notes, etc.) as necessary to describe the desired end-state.

For everything else in-between, just go with the "no template" option.

## Branching

When creating a branch, we like to follow the naming template:

`<STATEMENT OF BRANCH PURPOSE>`

Use a dash, `-`, as the delimiter, e.g., `this-is-a-feature-branch`

## Coding Conventions and Standards

## Committing and Merging

When merging, we should squash all commits and follow the following commit message template:

`<TYPE>(<OPTIONAL SCOPE>): <DESCRIPTION OF STORY>`

Spaces are allowed within the description, e.g., `Feature(DSR): This revolves around the scope of DSRs`

| Type        | Description                                                                                            |
| :---------- | :----------------------------------------------------------------------------------------------------- |
| Feature     | Commits, that adds a new feature                                                                       |
| Fix         | Commits, that fixes a bug                                                                              |
| Refactor    | Commits, that rewrite/restructure your code, however does not change any behavior                      |
| Performance | Commits are special refactor commits, that improve performance                                         |
| Style       | Commits, that do not affect the meaning (white-space, formatting, missing semi-colons, etc)            |
| Test        | Commits, that add missing tests or correcting existing tests                                           |
| Docs        | Commits, that affect documentation only                                                                |
| Build       | Commits, that affect build components like build tool, ci pipeline, dependencies, project version, ... |
| Ops         | Commits, that affect operational components like infrastructure, deployment, backup, recovery, ...     |
| Chore       | Miscellaneous commits e.g. modifying .gitignore                                                        |

# Local Development

For best results, pleases read and follow the instructions under this header in order.

## General

Do the following prior to moving on to any further instructions below this section:

1. At a minimum, have an integrated development environment (e.g., VSCode), a browser (e.g., Google Chrome), `git`, `node`, `npm`, and `python3` installed
2. Fork or clone this repository to your local development environment

## Installing

Execute the following at the root of the repository to install, test, and build everything required to run any part of the stack:

```bash
# copies .env.example into a local version
npm run config:copy
# installs all dependencies in all stacks
npm run install:all
# runs through all linting, testing, and building
npm run check:all
```

When adding new packages using `pip3` or `npm`, be sure to commit an updated _package.json_ or _requirements.txt_ in the correct directory. For `pip3` in particular, please execute the following:

```bash
npm run freeze:all
```

## Running

To run each sub-stack in one terminal, with integrated logs, execute the following:

```bash
# starts all sub-stacks
npm run start:all
```

## Building

For building the client in development mode, use the automated process through the execution of the following commands at the root of this project:

```bash
npm run build:client
```

## Testing

When testing in development execute the following at the root of the repository:

```bash
# this runs all the unit and acceptance tests
npm run test:all
```

To run acceptance tests interactively in cypress, execute the following at the root of the repository:

```bash
# this opens cypress with the UI
npm run acceptance:open
```

# Pushing

Prior to attempting a push to a branch, run the check all command again to ensure that all tests pass locally:

```bash
npm run check:all
```

## Pipelines

To get context on the GitHub actions that run during a push or pull to a branch, please read the [GitHub Workflows README](./.github/workflows/README.md).

# Licensing

Opera and all its components are licensed under the [MIT license](./LICENSE).

## Why the Hard Fork

This is a hard-fork of the original [pdf-bullets](https://github.com/AF-VCD/pdf-bullets) project, a web-application affectionately named the [**AIR FORCE BULL**et **SH**aping & **I**teration **T**ool](https://af-vcd.github.io/pdf-bullets/), created and maintained by Christopher Kodama and the members of the Air Force Volunteer Cyber Depository (AF-VCD) group.

The purpose of hard-forking this original pdf-bullets tool is as follows:

1. Refactor the frontend codebase to modern TypeScript, and eliminate React bootstrap (e.g., CRA) overhead
2. Provide more GitOps and open-source developer workflows and instructions
3. Add fine-tuned T5x pre-trained model(s) to create a new [The Forge](#The-Forge) feature
4. Revamp the UI/UX using modern components and design standards
5. Re-architect to a client-server application to provide persistence, security, and improvement insights
