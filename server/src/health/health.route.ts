import { FastifyInstance, FastifyRequest } from 'fastify'

import HealthController from './HealthController'
import { HealthResponse, RequestedServiceParams } from './HealthModel'

const healthController = new HealthController()

const healthRoutes = async (app: FastifyInstance) => {
	app.get('/', (_, res) => {
		healthController.getOverallHealth().then((result: HealthResponse) => res.send(result).status(200))
	})

	app.get('/:service', (req: FastifyRequest<{ Params: RequestedServiceParams }>, res) => {
		healthController
			.getRequestedServiceHealth(req.params.service)
			.then((result: HealthResponse) => res.send(result).status(200))
	})
}

export default healthRoutes