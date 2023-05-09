import fastify, { FastifyInstance } from "fastify";
import { Server, IncomingMessage, ServerResponse } from "http";

import { loggerConfiguration } from "./logging/logger.config";
import { loggerConfigurationInterface } from "./logging/logger.interface";

import { ENV, HOST, PORT } from "./constants/server.constants";

const server: FastifyInstance<Server, IncomingMessage, ServerResponse> =
  fastify({
    logger: loggerConfiguration[ENV as keyof loggerConfigurationInterface],
  });

server.listen({ host: HOST, port: PORT }, function (err, address) {
  if (err) {
    server.log.error(err);
    process.exit(1);
  }
  server.log.info(`Server is now listening on ${address}`);
});
