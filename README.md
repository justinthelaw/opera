npm run check:all

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
### Building
The two options developers have for building the full-stack application in development mode is as follows:
1. (RECOMMENDED) Use the automated process through the execution of the following commands at the root of this project:
npm run build:all
2. Build individual portions of the application and integrate through the execution of the following commands at the root of this project:
npm run build:client
npm run build:server
# moves client bundle and index over to server
npm run build:integrate
**_NOTE_**: Client-Server Architecture
The Fastify Server within the Server is the main server of both the Smarter Bullets Server and Client. As it currently stands, the production build of the application and the development environment have the Server serving a static `bundle.js` and `index.html` to the user's browser.
In development, the Server watches and serves whatever client build resides within the `/server/build/dist` directory using nodemon. A new client can be built, integrated, and served by the Server using the instructions seen in the [Building](#building) section of this README.
### Root Directory Run
There are two options to run the full-stack application from the root directory:
1. (RECOMMENDED) To run each sub-stack in one terminal, execute the following:
npm run start:all
2. To run each sub-stack in a new terminal, execute the following:
# installs all dependencies in the sub-stacks
npm run install:all
# see database access instructions in individual directory run section
npm run start:database
# new terminal
npm run start:client
# new terminal
npm run start:server
### Individual Directory Run
#### _Database_
1. Open a new terminal
2. Execute the following to start a MongoDB database:
# set execution permissions to file
chmod +x ./server/data/start:database
# run docker command for configured mongodb image and container
./server/data/start:database
3. To access the MongoDB container, execute the following:
# get the docker container ID for smarter-bullets mongodb
docker ps -a
# open mongo shell for container
docker exec -it <CONTAINER_ID> mongosh
4. For more MongoDB commands, you can reference this guide: [MongoDB Cheat Sheet](https://www.mongodbtutorial.com/mongodb-cheat-sheet/)
#### _Server_
1. Open a new terminal
2. Go to the `server/src/constants/` directory and ensure you are okay with defaults sans environment variable
3. In `server/`, execute the following to start the server:
# npm run start:dev wraps a build-step that includes tsc build and nodemon for hot-reload
npm install && npm run start:dev
#### _Client_
1. Open a new terminal
2. In `client/`, execute the following to start the client:
npm install && npm start
#### _Testing_
When testing the client or server in development execute the following to get hot-reload testing:
npm run test:dev
# this opens cypress with the UI
npm run acceptance:open
# this opens cypress headless
npm run acceptance:run
