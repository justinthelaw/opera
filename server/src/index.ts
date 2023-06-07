import fastify, { FastifyInstance } from 'fastify'
import { Server, IncomingMessage, ServerResponse } from 'http'
import { loggerConfiguration } from './logging/LoggerConfig'
import { loggerConfigurationInterface } from './logging/LoggerInterface'
import { ENV, HOST, PORT } from './utils/Constants'
import { healthRoutes } from './health/HealthRoutes'
import { RegisterApiRoute } from './utils/RegisterApiRoute'
import fastifyStatic from '@fastify/static'
import path from 'path'

export const server: FastifyInstance<Server, IncomingMessage, ServerResponse> = fastify({
	logger: loggerConfiguration[ENV as keyof loggerConfigurationInterface]
})

server.register(fastifyStatic, {
	root: path.join(__dirname, 'dist'),
	prefix: '/'
})

RegisterApiRoute(healthRoutes, '/health')

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
