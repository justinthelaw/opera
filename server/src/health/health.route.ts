import xss from 'xss'
import { FastifyInstance, FastifyRequest } from 'fastify'

import HealthController from './HealthController'
import { HealthResponse, PossibleHealthServices, RequestedServiceParams, RouteSchema } from './HealthModel'
import { server } from '..'

const healthController = new HealthController()

const healthRoutes = async (app: FastifyInstance) => {
	const getOverallHealth: RouteSchema = {
		method: 'GET',
		url: '/',
		schema: {
			response: {
				200: {
					type: 'object',
					properties: {
						name: { type: 'string' },
						status: { type: 'string' },
						description: { type: 'string' },
						timeStamp: { type: 'string' },
						degradedReason: { type: 'string' }
					}
				}
			}
		},
		handler: async (_, res) => {
			try {
				const result: HealthResponse = await healthController.getOverallHealth()
				res.send(result).status(200)
			} catch (error) {
				server.log.error(error)
				res.status(500)
			}
		}
	}

	const getRequestedServiceHealth: RouteSchema = {
		method: 'GET',
		url: '/:service',
		schema: {
			response: {
				200: {
					type: 'object',
					properties: {
						name: { type: 'string' },
						status: { type: 'string' },
						description: { type: 'string' },
						timeStamp: { type: 'string' },
						degradedReason: { type: 'string' }
					}
				}
			},
			params: {
				type: 'object',
				properties: {
					service: { type: 'string' }
				}
			}
		},
		handler: async (req: FastifyRequest<{ Params: RequestedServiceParams }>, res) => {
			try {
				const sanitizeInput = xss(req.params.service) as PossibleHealthServices
				const result: HealthResponse = await healthController.getRequestedServiceHealth(sanitizeInput)
				res.send(result).status(200)
			} catch (error) {
				server.log.warn(error)
				res.status(400).send(error)
			}
		}
	}

	app.route(getOverallHealth)
	app.route(getRequestedServiceHealth)
}

export default healthRoutes
