# Opera: Optimized Performance and Evaluation Rhetoric AI

<div align="center">
    
[![test-pipeline](https://github.com/justinthelaw/opera/actions/workflows/test-pipeline.yml/badge.svg)](https://github.com/justinthelaw/opera/actions)
[![snyk-security](https://github.com/justinthelaw/opera/actions/workflows/snyk-security.yml/badge.svg)](https://github.com/justinthelaw/opera/actions/workflows/snyk-security.yml)

</div>

**_Opera_**: Latin word (plural of opus) meaning "work," "effort," or "service." Usually referring to an individual or group's skillful or creative work.

Opera is a project focused on developing a set of tools to automate the pointless aspects of performance report and award writing so that officer and enlisted members can focus more on the individual and the achievements, rather than worry about irrelevant formatting. The ultimate objective is to allow the end-user to type or speak a stream of consciousness about a member's accomplishments and let Opera handle the rest.

The Forge is Opera's narrative generation tool that harnesses the power of Natural Language Processing (NLP) through the use of Large Language Models (LLM). The Forge is an API that is connected to a fine-tuned model that has been trained using 33,000+ unique EPR, OPR, and Award packages, across all of the Air and Space Force's positions and ranks.

# Table of Contents

1. [Background](#background)
2. [The Forge](#the-forge)
3. [Application Usage](#application-usage)
4. [Contributing](#contributing)
5. [Local Development](#local-development)
6. [Licensing](#licensing)

# Background

## What are "Bullets" and "Narratives"

One of the most pointless and time-consuming things that Air and Space Force officer and enlisted personnel do all the time is Bullet and Narrative writing.

Air and Space Force personnel are required to write Bullets for performance reports, and these Bullets could mean the difference between the stagnation or advancement of an Airman or Guardian's career. Bullets are action-impact-outcome statements that follow specific formatting and acronym usage rules which, more often than not, hinder effective communication and/or embellish the accomplishments of competing officers and enlisted personnel. Bullets also must stay within one line on a standardized PDF form's input.

In more recent times, the Air and Space Force have begun transitioning over to Narratives for award packages, and eventually for performance reports. Narratives still follow the action and impact/outcome format, and are still hard to write on the fly. They still enforce the same-but-different formatting and acronym-usage limitations. Narratives are meant to be written as multiple sentences across 1-5 lines on a standardized PDF form's input.

## How are "Bullets" Formatted

Bullets follow a few formatting rules:

- Each Bullet must be exactly one line, with the width of the line depending on the form (performance reports, award packages, etc).
- Bullets generally adhere to the following formula, with some situational exceptions: `[ACTION];[IMPACT]--[OUTCOME]`
- Acronyms and abbreviations can be force-wide, organization, and/or commander-specific, with major inconsistencies in their abbreviation/acronym policies.
- In Awards Packages, Enlisted Performance Reports (EPRs), and most other evaluation documents, the length of a Bullet must be ~202.321mm
- In Officer Performance Reports (OPRs), the length of a Bullet must be ~201.041mm
- In the failed rollout of the Air Force's myEval tool, Bullets were based on a maximum length of 115 characters

Those Bullet formatting rules lead to the following:

- Information compression is prioritized over legibility
- Time is wasted on acronym and/or abbreviation revisions
- Bullet "appearance" becomes highly valued; some examples of arbitrary Bullet appearance rules:
  - Any sort of repetition = bad
  - Bullets near flush with page boundaries = good
- Closing Bullets (push statements) are always generic but need to catch attention

## Example Bullets

Below are examples of unclassified Air and Space Force Bullets:

- Delivered enterprise network s/w cert; adv'd 3 docs thru 5 orgs--guaranteed vital rqmts s/w accessibility DAF-wide
- Streamlined 3-ktr proposal rvw; resolved 277 elements in <5 wks--trailblazed $900M resilient POTUS/CCMD comms
- Justin embraces challenges with vigor; #1 choice to tackle big problems--perfect fit for NRO--send to PDE 1st look!

One non-obvious similarity amongst all 3 of these bullets is that they fit into the form perfectly - right up against the edge of the field. This is because the input area within the PDF form renders characters differently depending on the encoding, such as the space character in UTF-8 versus UTF-16.

## How are "Narratives" Formatted

Narratives follow very vague guidance that is still evolving as this README was written. At the moment, stricter guidance on how they are to be written was delegated to lower level commands and units. The following are the only rules that are required of a narrative, where statements are synonymous with sentences:

- Each statement must be standalone and can be used as a evaluation point regardless of the rest of the sentences
- Each statement must be readable, using minimal acronyms and plain english
- If acronyms are used, they must be on a Headquarters Air Force (HAF) approved list
- The narrative and per-statement length will be announced by the awarding authority, but must fit in the AF1206
- Whitespace at the end of statements in encouraged - there is no need to fill an entire line

## Example Narratives

Below are HAF generated examples of unclassified Air and Space Force Narratives:

- Capt Snuffy led a survey team of 33 MCA to establish an XAB in support of a PACAF ACE exercise across 4 countries and including 7 allies, culminating in 153 sorties and 334 training events completed. She also championed a critical organizational merger of the squadron’s maintenance and operations; results saved 360 maintenance workhours per week and increased sortie generation by 10%.

- TSgt Snuffy led 4 instructors through Mission Ready Airmen course validation, generating 153 changes, eliminating 32 classroom hours, and enhancing course experience for 6 instructors and 70 students per year. Additionally, he facilitated a $15M facility renovation project, ensuring the CY22 schedule started on-time for 8 different courses spanning 11 AFSCs.

# The Forge

For more more details, to include contributing, on the The Forge machine learning strategy, please read the [The Forge README](./forge/README.md).

# Application Usage

## Bullet and Narrative Writing

The application provides instructions within the application for usage. The User Interface (UI) should be relatively easy to navigate. If the UI is not intuitive to you, then feedback can be submitted using the in-app feedback form or an Issue can be posted to this repository.

## Acronym List Imports

Note: When importing rules from a Excel (.xlsx) file containing acronym definition, the columns are:

| COLUMN NUMBER | COLUMN DESCRIPTION                                                         | EXAMPLE VALUES                                     |
| :------------ | :------------------------------------------------------------------------- | :------------------------------------------------- |
| 1             | Enabled: Boolean value, indicates whether to activate an acronym-word pair | TRUE, FALSE                                        |
| 2             | Word: String value that contains the full-form, un-abbreviated word        | "United States Space Force", "Command and Control" |
| 3             | Acronym: String value that contains the short-form, abbreviated word       | "USSF", "C2"                                       |

_CORRECT USAGE NOTE_: Sort the Excel sheet in DESCENDING ORDER. Due to the greedy nature of the replacement, the reverse sorted order is required to ensure proper compression of abbreviations.

_EXAMPLE OF INCORRECT USAGE_:

Ordering the following acronyms:

- United States Air Force: USAF
- United States Air Force Academy: USAFA

Will cause "United States Air Force Academy" to be abbreviated as "USAF Academy"

# Contributing

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
3. Go to the _config/_ directory and create a `.env.local` using the [.env.example](./config/.env.example) as a reference

## Installing

Execute the following at the root of the repository to install everything required to run any part of the project:

```bash
# create python3 venv in forge and server
npm run create:venv
# installs all dependencies in the sub-stacks
npm run install:all
```

When adding new packages using `pip3` or `npm`, be sure to commit an updated _package.json_ or _requirements.txt_ in the correct directory. For `pip3` in particular, please execute the following:

```bash
# activate the correct .venv
source $INSERT_DIRECTORY/.venv/bin/activate
# execute the following in the correct relative directory
pip3 freeze > $INSERT_DIRECTORY/requirements.txt
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

Prior to attempting a push to a branch, run the check all command to ensure all tests pass locally:

```bash
# runs all tests and linting
npm run check:all
```

## Pipelines

To get context on the GitHub actions that run during a push or pull to a branch, please read the [GitHub Workflows README](./.github/workflows/README.md).

# Licensing

_smarter_-bullets is licensed under the [MIT license](./LICENSE).

## Why the Hard Fork

This is a hard-fork of the original [pdf-bullets](https://github.com/AF-VCD/pdf-bullets) project, a web-application affectionately named the [**AIR FORCE BULL**et **SH**aping & **I**teration **T**ool](https://af-vcd.github.io/pdf-bullets/), created and maintained by Christopher Kodama and the members of the Air Force Volunteer Cyber Depository (AF-VCD) group.

The purpose of hard-forking this original pdf-bullets tool is as follows:

1. Refactor the frontend codebase to modern TypeScript, and eliminate React bootstrap (e.g., CRA) overhead
2. Provide more GitOps and open-source developer workflows and instructions
3. Add fine-tuned T5 pre-trained model(s) to create a new [The Forge](#The-Forge) feature
4. Revamp the UI/UX using modern components and design standards
5. Re-architect to a client-server application to provide persistence, security, and improvement insights
