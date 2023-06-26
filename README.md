<div align="center">
    <img src="./public/smarter-bullets-title-small.png" style="width: 70%" alt="smarter-bullets-title">
</div>
<br/>
<div align="center">
    
[![smarter-bullets-pipeline](https://github.com/justinthelaw/smarter-bullets/actions/workflows/node.js.yml/badge.svg)](https://github.com/justinthelaw/smarter-bullets/actions)
[![smarter-bullets-vulnerabilities](https://snyk.io/test/github/justinthelaw/smarter-bullets/badge.svg)](https://app.snyk.io/org/justinthelaw/project/c94ab3f5-ba0e-4408-8680-a46f4dd68d78)

</div>

---

This is a hard-fork of the original [pdf-bullets](https://github.com/AF-VCD/pdf-bullets) project, a web-application affectionately named the [**AIR FORCE BULL**et **SH**aping & **I**teration **T**ool](https://af-vcd.github.io/pdf-bullets/), created and maintained by Christopher Kodama and the members of the Air Force Volunteer Cyber Depository (AF-VCD) group.

# Table of Contents

1. [Background](#background)
    - [What are "Bullets"](#what-are-bullets)
    - [How are "Bullets" Formatted](#how-are-bullets-formatted)
    - [Why the Hard Fork](#why-the-hard-fork)
2. [Application Usage](#application-usage)
    - [Bullet Writing](#bullet-writing)
    - [Acronym List Imports](#acronym-list-imports)
3. [Bullet Forge](#bullet-forge)
    - [OpenAI GPT-3](#open-ai-gpt-3)
        - [Fine Tuning](#fine-tuning)
        - [API Key](#api-key)
4. [Contributing](#contributing)
    - [Feedback Form](#feedback-form)
    - [Pull Requests](#pull-requests)
    - [Issues](#issues)
    - [Branching](#branching)
    - [Coding Conventions and Standards](#coding-conventions-and-standards)
    - [Committing and Merging](#committing-and-merging)
    - [Local Development](#local-development)
        - [Client-Server](#client-server)
        - [General](#general)
        - [Root Directory Run](#root-directory-run)
        - [Individual Directory Run](#individual-directory-run)
5. [Licensing](#licensing)

# Background

## What are "Bullets"

One of the most pointless and time-consuming things that Air and Space Force officer and enlisted personnel do all the time is bullet-writing.

Air and Space Force personnel typically are required to write bullets for performance reports and award packages, and these bullets could mean the difference between the stagnation or advancement of an Airman or Guardian's career.

These bullets follow a few formatting rules:

-   Each bullet must be exactly one line, with the width of the line depending on the form (performance reports, award packages, etc).
-   Acronyms and abbreviations can be force-wide, organization, and/or commander-specific, with major inconsistencies in their abbreviation/acronym policies.

## How are "Bullets" Formatted

Those bullet formatting rules lead to the following:

-   Information compression is prioritized over legibility
-   Time is wasted on acronym and/or abbreviation revisions
-   Bullet "appearance" becomes highly valued; some examples of arbitrary bullet appearance rules:
    -   Any sort of repetition = bad
    -   Bullets near flush with page boundaries = good

The purpose of _smarter_-bullets is to develop a set of tools to automate the pointless aspects of bullet-writing so that an officer and/or enlisted members can focus more on writing actual content rather than worry about irrelevant formatting.

## Why the Hard Fork

The purpose of hard-forking this tool is as follows:

1. Refactor the frontend codebase to modern TypeScript, and eliminate Create-React-App (CRA) overhead
2. Provide more GitOps and open-source developer workflows and instructions
3. Add OpenAI GPT4 prompt engineering to create a new "Bullet Forge" feature
4. Revamp the UI/UX using modern Astro UXDS components and styling
5. Re-architect to a client-server application to provide persistence and security

# Application Usage

## Bullet Writing

The application provides instructions within the application for usage. The User Interface (UI) should be relatively easy to navigate. If the UI is not intuitive to you, then feedback can be submitted using the To-Be-Built feedback form or an Issue can be posted to this Github repository.

## Acronym List Imports

Note: When importing rules from a Excel (.xlsx) file containing acronym definition, the columns are:

| COLUMN NUMBER | COLUMN DESCRIPTION                                                         | EXAMPLE VALUES                                     |
| :------------ | :------------------------------------------------------------------------- | :------------------------------------------------- |
| 1             | Enabled: Boolean value, indicates whether to activate an acronym-word pair | TRUE, FALSE                                        |
| 2             | Word: String value that contains the full-form, un-abbreviated word        | "United States Space Force", "Command and Control" |
| 3             | Acronym: String value that contains the short-form, abbreviated word       | "USSF", "C2"                                       |

_CORRECT USAGE NOTE_: Sort the Excel sheet in DESCENDING ORDER. Due to the greedy nature of the replacement, the reverse sorted order is required to ensure proper compression of abbreviations.

_EXAMPLE OF INCORRECT USAGE_:
United States Air Force: USAF  
United States Air Force Academy: USAFA  
Will cause "United States Air Force Academy" to be abbreviated as "USAF Academy"

# Bullet Forge

Bullet Forge is a bullet generation tool that harnesses the power of Natural Language Processing (NLP) through OpenAI's GPT technologies, specifically Large Language Models (LLM).

The primary objective of this tool is to streamline the process of listing accomplishments and achievements by:

1. Offloading the cognitive and administrative burden of transforming factual information into effective bullets to the Smarter Bullets model.
2. Offering suggestions to rephrase verbs, impacts, and outcomes to enhance variety and avoid repetition throughout the document.
3. Intelligently incorporating acronyms to optimize spacing and enhance the readability of bullets, while maintaining consistency across the document.

## OpenAI GPT-3

The usage of the OpenAI API is documented on the [OpenAI API documentation website](https://platform.openai.com/docs) and within the Smarter Bullets server code.

### Fine Tuning

To run your own fine-tuning, you can use the Jupyter Notebook within the model directory. Please note that the following can only be executed if Jupyter Notebook and the `openai` CLI tool and its dependencies have been installed on your device:

#### Training Data

Example data that has been prepared for fine-tuning can be seen within this repository, but does not represent the full-set of data used to create Bullet Forge. This example data can be found within in the file: [model/example-data.jsonl](./model/example-data.jsonl). The [OpenAI API fine-tuning documentation](https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset) can provide more details on the data's setup.

#### Open AI Models

The specific model used depends on the specific prompt or task required for Bullet Forging within the Smarter Bullets server. You can read more about these in the [OpenAI API models documentation](https://platform.openai.com/docs/models/gpt-3).


### API Key

The OpenAI API key is a repository secret that is used by the application in the production environment. When developing on your own, you will not have access to the fine-tuned models nor the OpenAI API account that is being used to generate bullets.

As an individual contributor to this repository, you are not required to touch the OpenAI API fine-tuning and modelling portions of the application. If you have issues with the bullets being generated by Bullet Forge, please refer to the [Contributing](#contributing) section.

# Contributing

Below are some GitOps rules for contributing to this repository. As time moves forward, more formalized pull request and issue templates will be established.

## Feedback Form

A feedback form is built into the live web application, and all users can submit feature requests or defect reports via that form. Users and developers can also submit issues through this Github repository.

## Pull Requests

When describing a pull request, please provide the following:

1. Merge request title or summary as outlined in the [Committing and Merging](#committing-and-merging) section
2. High-level description of what was changed or been added/deleted
3. Attachment and/or linking to an existing issue or project task

## Issues

For bugs, follow the [bug report template](./.github/ISSUE_TEMPLATE/bug_report.md) as closely as possible so that developers can reproduce and debug the issue.

For feature requests, follow the [feature request template](./.github/ISSUE_TEMPLATE/feature_request.md) as closely as possible, providing detail (imagery, notes, etc.) as necessary to describe the desired end-state.

## Branching

When creating a branch, we like to follow the naming template:

`<STATEMENT OF BRANCH PURPOSE>`

Use a dash, `-`, as the delimiter, e.g., `this-is-a-feature-branch`

## Coding Conventions and Standards

Prior to attempting a push to a branch or submitting of a merge request to a branch and/or main, run the check all command to ensure all pipeline steps will run locally:

```bash
npm run check:all
```

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

The two options developers have for starting the application in development mode is as follows:

1. (RECOMMENDED) [Root Directory Run](#root-directory-run): running and installing using the NPM project at the root of the directory
2. [Individual Directory Run](#individual-directory-run): going into each sub-directory to run each individual sub-stack/service

### General

Do the following prior to moving on to any further instructions below this section.

1. Fork and/or clone this repository
2. Go to the root `config/` directory and create a `.env.local` using the `.env.example` as a reference
3. Execute the following at the root of the repository:

```bash
npm install
# next line is for linting dependencies
npx install-peerdeps --dev eslint-config-react-app
```

### Building

The two options developers have for building the full-stack application in development mode is as follows:

1. (RECOMMENDED) Use the automated process through the execution of the following commands at the root of this project:

```bash
npm run build:all
```

2. Build individual portions of the application and integrate through the execution of the following commands at the root of this project:

```bash
npm run build:client
npm run build:server
# moves client bundle and index over to server
npm run build:integrate
```

#### Client-Server

The Fastify Server within the Server is the main server of both the Smarter Bullets Server and Client. As it currently stands, the production build of the application and the development environment have the Server serving a static `bundle.js` and `index.html` to the user's browser.

In development, the Server watches and serves whatever client build resides within the `/server/build/dist` directory using nodemon. A new client can be built, integrated, and served by the Server using the instructions seen in the [Building](#building) section of this README.

### Root Directory Run

There are two options to run the full-stack application from the root directory:

1. (RECOMMENDED) To run each sub-stack in one terminal, execute the following:

```bash
npm run start:all
```

2. To run each sub-stack in a new terminal, execute the following:

```bash
# installs all dependencies in the sub-stacks
npm run install:all
# see database access instructions in individual directory run section
npm run start:database
# new terminal
npm run start:client
# new terminal
npm run start:server
```

### Individual Directory Run

#### _Database_

1. Open a new terminal
2. Execute the following to start a MongoDB database:

```bash
# set execution permissions to file
chmod +x ./server/data/start:database
# run docker command for configured mongodb image and container
./server/data/start:database
```

3. To access the MongoDB container, execute the following:

```bash
# get the docker container ID for smarter-bullets mongodb
docker ps -a
# open mongo shell for container
docker exec -it <CONTAINER_ID> mongosh
```

4. For more MongoDB commands, you can reference this guide: [MongoDB Cheat Sheet](https://www.mongodbtutorial.com/mongodb-cheat-sheet/)

#### _Server_

1. Open a new terminal
2. Go to the `server/src/constants/` directory and ensure you are okay with defaults sans environment variable
3. In `server/`, execute the following to start the server:

```bash
# npm run start:dev wraps a build-step that includes tsc build and nodemon for hot-reload
npm install && npm run start:dev
```

#### _Client_

1. Open a new terminal
2. In `client/`, execute the following to start the client:

```bash
npm install && npm start
```

#### _Testing_

When testing the client or server in development execute the following to get hot-reload testing:

```bash
npm run test:dev
```

```bash
# this opens cypress with the UI
npm run acceptance:open
```

```bash
# this opens cypress headless
npm run acceptance:run
```

# Licensing

_smarter_-bullets is licensed under the [MIT license](./LICENSE).
