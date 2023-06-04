import { FastifyInstance } from 'fastify'
import { HealthController } from './health.controller'
import { HealthResponse } from './health.models'

const healthController = new HealthController()
export const healthRoutes = async (app: FastifyInstance) => {
	app.get('/', (_, res) => {
		healthController.getOverallHealth().then((result: HealthResponse) => res.send(result).status(200))
	})
}
