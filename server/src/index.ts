import fastify, { FastifyInstance } from "fastify";
import { Server, IncomingMessage, ServerResponse } from "http";

const dotenv = require("dotenv");
dotenv.config({ path: "../../config/.env.local" });

const { SERVER_HOST, SERVER_PORT } = process.env;

const server: FastifyInstance<Server, IncomingMessage, ServerResponse> =
  fastify({
    logger: true,
  });

server.listen(
  { host: SERVER_HOST || "localhost", port: parseInt(SERVER_PORT || "8080") },
  function (err, address) {
    if (err) {
      server.log.error(err);
      process.exit(1);
    }
    server.log.info(`Server is now listening on ${address}`);
  }
);
