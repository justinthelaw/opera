import { Server, IncomingMessage, ServerResponse } from 'http'
import fastify, { FastifyInstance } from 'fastify'
import fastifyStatic from '@fastify/static'
import path from 'path'

import LoggerConfigurationInterface from './logging/LoggerInterface'
import { ENV, HOST, PORT } from './utils/Constants'
import LoggerConfiguration from './logging/LoggerConfig'
import HealthRoutes from './health/HealthRoutes'
import registerAPIRoute from './utils/RegisterAPIRoute'

export const server: FastifyInstance<Server, IncomingMessage, ServerResponse> = fastify({
	logger: LoggerConfiguration[ENV as keyof LoggerConfigurationInterface]
})

server.register(fastifyStatic, {
	root: path.join(__dirname, 'dist'),
	prefix: '/'
})

registerAPIRoute(HealthRoutes, '/health')

const start = () => {
	try {
		server.listen({ host: HOST, port: PORT }, function (err, address) {
			if (err) {
				server.log.error(err)
				process.exit(1)
			}
			server.log.info(`Server is now listening on ${address}`)
		})
	} catch (error) {
		server.log.error(error)
		process.exit(1)
	}
}

start()
