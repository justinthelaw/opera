import fastify, { FastifyInstance } from 'fastify'
import { Server, IncomingMessage, ServerResponse } from 'http'
import { loggerConfiguration } from './logging/logger.config'
import { loggerConfigurationInterface } from './logging/logger.interface'
import { ENV, HOST, PORT } from './constants/api.constants'
import { healthRoutes } from './health/health.routes'
import fastifyStatic from '@fastify/static'
import path from 'path'

// TODO: Reformat according to https://www.youtube.com/watch?v=Lk-uVEVGxOA

export const server: FastifyInstance<Server, IncomingMessage, ServerResponse> = fastify({
	logger: loggerConfiguration[ENV as keyof loggerConfigurationInterface]
})

server.register(fastifyStatic, {
	root: path.join(__dirname, 'dist'),
	prefix: '/'
})

server.register(healthRoutes, { prefix: '/api/health' })

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
