import { FastifyInstance } from 'fastify'

import { server } from '../index'
import { API_VERSION } from '../server.constants'

export default function registerAPIRoute(route: (app: FastifyInstance) => Promise<void>, routeName: string): void {
	server.register(route, { prefix: `/api${routeName}` })
	server.register(route, { prefix: `/api/${API_VERSION}${routeName}` })
}
