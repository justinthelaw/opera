import { FastifyInstance } from 'fastify'

import { server } from '../index'
import { API_VERSION } from '../server.constants'

export default function registerAPIRoute(route: (app: FastifyInstance) => Promise<void>, routeName: string): void {
	if (route !== null && routeName !== null) {
		server.register(route, { prefix: `/api${routeName}` })
		server.register(route, { prefix: `/api/${API_VERSION}${routeName}` })
	} else {
		server.log.error(`Could not register an API route with name of, ${routeName}, and end point of, ${route}`)
	}
}
