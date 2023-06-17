import fastifySwagger from 'fastify-swagger'
import { Server, IncomingMessage, ServerResponse } from 'http'
import fastify, { FastifyInstance } from 'fastify'
import fastifyStatic from '@fastify/static'
import path from 'path'

import LoggerConfigurationInterface from './logging/LoggerConfigurationModel'
import { ENV, HOST, PORT } from './server.constants'
import loggerConfiguration from './logging/logger.config'
import healthRoutes from './health/health.route'
import registerAPIRoute from './utils/register.api'

export const server: FastifyInstance<Server, IncomingMessage, ServerResponse> = fastify({
	logger: loggerConfiguration[ENV as keyof LoggerConfigurationInterface]
})

server.register(fastifySwagger, {
	routePrefix: '/documentation',
	swagger: {
		info: {
			title: 'Smarter Bullets API',
			description: 'API documentation for the Smarter Bullets application',
			version: '1.0.0'
		},
		externalDocs: {
			url: 'https://swagger.io',
			description: 'Find more info here'
		},
		host: 'localhost',
		schemes: ['http'],
		consumes: ['application/json'],
		produces: ['application/json']
	},
	exposeRoute: true
})
})

server.register(fastifyStatic, {
	root: path.join(__dirname, 'dist'),
	prefix: '/'
})

registerAPIRoute(healthRoutes, '/health')

export function start() {
	try {
		server.listen({ host: HOST, port: PORT }, function (err, address) {
			if (err) {
				server.log.error(err)
			}
			server.log.info(`Server is now listening on ${address}`)
		})
	} catch (error) {
		server.log.error(error)
		process.exit(1)
	}
}

start()
