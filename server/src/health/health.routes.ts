import { FastifyInstance, RouteShorthandOptions } from 'fastify'
import { HealthController } from './health.controller'
import { HealthResponse } from './health.model'

const healthController = new HealthController()
// TODO: move logic to HealthController
export const healthRoutes = async (app: FastifyInstance, options: RouteShorthandOptions) => {
	app.get('/', (_, res) => {
		healthController.getOverallHealth().then((result: HealthResponse) => res.send(result).status(200))
	})
}
