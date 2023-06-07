<div align="center">

![smarter-bullets-title](./public/smarter-bullets-title.png)

</div>

<div align="center">

[![smarter-bullets-pipeline](https://github.com/justinthelaw/smarter-bullets/actions/workflows/node.js.yml/badge.svg)](https://github.com/justinthelaw/smarter-bullets/actions)

</div>

This is a hard-fork of the original [pdf-bullets](https://github.com/AF-VCD/pdf-bullets) project, a web-application affectionately named the [**AIR FORCE BULL**et **SH**aping & **I**teration **T**ool](https://ea-pods-team.github.io/pdf-bullets/), created and maintained by Christopher Kodama and the members of the Air Force Volunteer Cyber Depository (AF-VCD) group.

# Table of Contents

1. [Background](#background)
    - [What are "Bullets"](#what-are-bullets)
    - [How are "Bullets" Formatted](#how-are-bullets-formatted)
    - [Why the Hard Fork](#why-the-hard-fork)
2. [Application Usage](#application-usage)
    - [Bullet Writing](#bullet-writing)
    - [Acronym List Imports](#acronym-list-imports)
3. [Contributing](#contributing)
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
4. [Licensing](#licensing)

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

# Contributing

Below are some GitOps rules for contributing to this repository. As time moves forward, more formalized pull request and issue templates will be established.

## Feedback Form

A feedback form is built into the live web application, and all users can submit feature requests or defect reports via that form.

## Pull Requests

When describing a pull request, please provide the following:

1. A title or summary as outlined in the [Committing and Merging](#committing-and-merging) section
2. A description of what was changed and whether it was attached to an existing issue

## Issues

When describing an issue, please provide the following:

1. A title or summary of the issues
2. Did the issue occur in the Local Development Environment or Production Environment?
    - If Local, describe the operating system and any other relevant information
3. Describe the expected behavior vs. the observed behavior
4. Provide all available error logs and network activity
5. Provide a recommended fix or area of concern

## Branching

When creating a branch, we like to follow the naming template:

`<STATEMENT OF BRANCH PURPOSE>`

Use a dash, `-`, as the delimiter, e.g., `this-is-a-feature-branch`

## Coding Conventions and Standards

Prior to attempting a push to a branch or submitting of a merge request to a branch and/or main, do the following:

1. Run a formatter on all files in accordance with the `.prettierrc` at the root of this repository
2. Run the eslint linter on all files in accordance with the `.eslint.yaml`, `security.eslintrc.yaml`, and the `package.json` at the root of this repository by executing the following:

```bash
npm run lint:general
npm run lint:security
```

3. Run all tests on all sub-stacks by executing the following at the root of the repository:

```bash
npm run test:all
```

4. Run the check all command to ensure all pipeline steps will run locally:

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

### Client-Server

The Fastify Server within the Server is the main server of both the Smarter Bullets Server and Client. As it currently stands, the production build of the application and the development environment have the Server serving a static `bundle.js` and `index.html` to the user's browser.

In development, the Server watches and serves whatever client build resides within the `/server/build/dist` directory using nodemon. A new client can be built, integrated, and served by the Server using the instructions seen in the [Building](#building) section of this README.

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

### Root Directory Run

To run each sub-stack in one terminal, execute the following:

```bash
npm run start:all
```

To run each sub-stack in a new terminal, execute the following:

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

# Licensing

_smarter_-bullets is licensed under the [MIT license](./LICENSE).
