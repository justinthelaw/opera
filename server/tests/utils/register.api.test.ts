import { server } from '../../src/index'
import { API_VERSION } from '../../src/server.constants'
import registerAPIRoute from '../../src/utils/register.api'

jest.mock('../../src/index', () => ({
	server: {
		register: jest.fn(),
		log: {
			error: jest.fn()
		}
	}
}))

describe('register.api', () => {
	const mockRouteName = 'route'

	afterEach(() => {
		jest.restoreAllMocks()
		jest.clearAllTimers()
	})

	test('should register route with prefix `/api`', async () => {
		const mockRoute = jest.fn()

		registerAPIRoute(mockRoute, `/${mockRouteName}`)

		expect(server.register).toHaveBeenCalledTimes(2)
		expect(server.register).toHaveBeenCalledWith(mockRoute, { prefix: '/api/route' })
	})

	test('should register route with prefix `/api/{API_VERSION}`', () => {
		const mockRoute = jest.fn()

		registerAPIRoute(mockRoute, `/${mockRouteName}`)

		expect(server.register).toHaveBeenCalledTimes(2)
		expect(server.register).toHaveBeenCalledWith(mockRoute, { prefix: `/api/${API_VERSION}/${mockRouteName}` })
	})

	test('should not register route if route name is not provided', () => {
		const mockRoute = jest.fn()

		registerAPIRoute(mockRoute, null as unknown as string)

		expect(server.register).not.toHaveBeenCalled()
	})

	test('should not register route if route function is not provided', () => {
		registerAPIRoute(null as unknown as jest.Mock<any, any, any>, `/${mockRouteName}`)

		expect(server.register).not.toHaveBeenCalled()
	})

	test('should not register route if both route name and route function are not provided', () => {
		registerAPIRoute(null as unknown as jest.Mock<any, any, any>, null as unknown as string)

		expect(server.register).not.toHaveBeenCalled()
	})
})
