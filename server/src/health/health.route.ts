import xss from 'xss'
import { FastifyInstance, FastifyRequest } from 'fastify'

import HealthController from './HealthController'
import { HealthResponse, PossibleHealthServices, RequestedServiceParams } from './HealthModel'
import { server } from '..'

const healthController = new HealthController()

const healthRoutes = async (app: FastifyInstance) => {
	app.get('/', {
		schema: {
			description: 'Get overall health of the application',
			summary: 'Get overall health',
			response: {
				200: {
					description: 'Successful response',
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
	})
	app.get('/:service', {
		schema: {
			description: 'Get health of a specific service',
			summary: 'Get service health',
			params: {
				type: 'object',
				properties: {
					service: { type: 'string' }
				}
			},
			response: {
				200: {
					description: 'Successful response',
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
	})
}

export default healthRoutes
