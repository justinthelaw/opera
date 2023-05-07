# pull latest official node image
FROM node:latest

LABEL AUTHOR=AF-VCD
LABEL AUTHOR=justinthelaw
LABEL VERSION=${VERSION}

# point to container working directory
WORKDIR /client

# copy over the package.json for npm
COPY package.json /client

# copy all remaining source files
COPY . /client

# install npm packages
RUN npm install

# switch to root user
USER root

# expose port and start client
EXPOSE ${PORT}
ENTRYPOINT ["npm","start"]