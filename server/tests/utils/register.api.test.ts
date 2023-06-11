import { server } from '../../src/index'
import { API_VERSION } from '../../src/server.constants'
import registerAPIRoute from '../../src/utils/register.api'

jest.mock('../../src/index', () => ({
	server: {
		register: jest.fn()
	}
}))

describe('register.api', () => {
	const mockRouteName = 'route'

	test('should register route with prefix `/api`', async () => {
		const mockRoute = jest.fn()

		registerAPIRoute(mockRoute, `/${mockRouteName}`)

		expect(server.register).toHaveBeenCalledTimes(2)
		expect(server.register).toHaveBeenCalledWith(mockRoute, { prefix: '/api/route' })
	})

	test('should register route with prefix `/api/{API_VERSION}`', async () => {
		const mockRoute = jest.fn()

		registerAPIRoute(mockRoute, `/${mockRouteName}`)

		expect(server.register).toHaveBeenCalledTimes(4)
		expect(server.register).toHaveBeenCalledWith(mockRoute, { prefix: `/api/${API_VERSION}/${mockRouteName}` })
	})
})
