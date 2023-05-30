# _smarter_-bullets

![example event parameter](https://github.com/justinthelaw/smarter-bullets/actions/workflows/node.js.yml/badge.svg?event=push)

This is a hard-fork of the original [pdf-bullets](https://github.com/AF-VCD/pdf-bullets) project, created and maintained by Christopher Kodama and the members of the Air Force Volunteer Cyber Depository (AF-VCD) group.

## Why the Hard Fork

The purpose of hard-forking this particular tool's repository is as follows:

1. Refactor the codebase to modern TypeScript, and eliminate Create-React-App (CRA) overhead
2. Provide more GitOps and open-source developer direction/instructions
3. Add OpenAI GPT4 prompt engineering to create new "bullet forge" feature
4. Revamp the user interface and experience using modern Material UI standards
5. Re-architect to a client-server application to provide persistence, security, and improvement insights

## What are "Bullets"

One of the most pointless and time-consuming things that Air and Space Force officer and enlisted personnel do all the time is bullet-writing.

Air and Space Force personnel typically are required to write bullets for performance reports and award packages, and these bullets could mean the difference between the stagnation or advancement of an Airman or Guardian's career.

These bullets follow a few formatting rules:

-   Each bullet must be exactly one line, with the width of the line depending on the form (performance reports, award packages, etc).
-   Acronyms and abbreviations can be force-wide, organization, and/or commander-specific, with major inconsistencies with their abbreviation/acronym policies.

## How are "Bullets" Formatted

Those bullet formatting rules lead to the following:

-   Information compression is prioritized over legibility
-   Time is wasted on acronym and/or abbreviation revisions
-   Bullet "appearance" becomes highly valued; some examples of arbitrary bullet appearance rules:
    -   Any sort of repetition = bad
    -   Bullets near flush with page boundaries = good

The purpose of _smarter_-bullets is to develop a set of tools to automate the pointless aspects of bullet-writing so that an officer and/or enlisted members can focus more on writing actual content rather than worry about irrelevant formatting.

## Application Usage

### Bullet Writing

The application provides instructions within the landing page for usage. The User Interface (UI) should be relatively easy to navigate. If the UI is not intuitive to you, then feedback can be submitted using the To-Be-Built feedback form or an Issue can be posted to this Github repository.

### Acronym List Imports

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

## Contributing

Below are some GitOps rules for contributing to this repository. As time moves forward, more formalized pull request and issue templates will be established.

### Local Development

The two options developers have for starting the application in development mode is as follows:

1. (RECOMMENDED) [Root Directory Run](#root-directory-run): running and installing using the NPM project at the root of the directory
2. [Individual Directory Run](#individual-directory-run): going into each sub-directory to run each individual sub-stack/service

#### General

1. Fork and/or clone this repository
2. Go to the root `config/` directory and create a `.env.local` using the `.env.example` as a reference
3. Execute the following at the root of the repository:

```bash
npm install
# next line may not be necessary depending on dev environment
npx install-peerdeps --dev eslint-config-react-app
```

#### Root Directory Run

When running with these instructions, run each sub-stack command in a new terminal.

```bash
# installs all dependencies in the sub-stacks
npm run install-all
# see database access instructions in Individual Directory Run
npm run database
# new terminal
npm run client
# new terminal
npm run server
```

#### Individual Directory Run

##### Database

1. Open a new terminal
2. Execute the following to start a PostgreSQL database:

```bash
# set execution permissions to file
chmod +x ./data/database.dev.sh
# run docker command for configured postgresql image and container
./data/database.dev.sh
```

3. To access the PostgreSQL container, execute the following:

```bash
# get the docker container ID for smarter-bullets postgresql
docker ps -a
# open mongo shell for container
docker exec -it <CONTAINER_ID> mongosh
```

4. For more PostgreSQL commands, you can reference this guide: [PostgreSQL Cheat Sheet](https://www.postgresqltutorial.com/postgresql-cheat-sheet/)

##### Server

1. Open a new terminal
2. Go to the `server/src/constants/` directory and ensure you are okay with defaults sans environment variable
3. In `server/`, execute the following to start the server:

```bash
# npm run start:dev wraps a build-step that includes tsc build and nodemon for hot-reload
npm install && npm run start:dev
```

##### Client

1. Open a new terminal
2. In `client/`, execute the following to start the client:

```bash
npm install && npm start
```

### Pull Requests

When describing a pull request, please provide the following:

1. A title or summary as outlined in the [Committing and Merging](#committing-and-merging) section
2. A description of what was changed and whether it was attached to an existing issue

### Issues

When describing an issue, please provide the following:

1. A title or summary of the issues
2. Did the issue occur in the Local Development Environment or Production Environment?
    - If Local, describe the operating system and any other relevant information
3. Describe the expected behavior vs. the observed behavior
4. Provide all available error logs and network activity
5. Provide a recommended fix or area of concern

### Branching

When creating a branch, we like to follow the naming template:

`<STATEMENT OF BRANCH PURPOSE>`

Use a dash, `-`, as the delimiter, e.g., `this-is-a-feature-branch`

### Code Conventions and Standards

Prior to attempting a push to a branch or submitting of a merge request to a branch and/or main, do the following:

1. Run a formatter on all files in accordance with the `.prettierrc` at the root of this repository
2. Run the eslint linter on all files in accordance with the `.eslint.yaml`, `security.eslintrc.yaml`, and the `package.json` at the root of this repository
    
```bash
npm run lint
npm run security-lint
```

3. Run all client (jest, testing-library), server (jest, testing-library), and integration (cypress) tests

### Committing and Merging

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

## Licensing

_smarter_-bullets is licensed under the [MIT license](./LICENSE).
