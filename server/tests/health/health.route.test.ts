import { server } from '../../src/index'

describe('health route', () => {
	afterEach(() => {
		jest.restoreAllMocks()
		jest.clearAllTimers()
	})

	afterAll(async () => {
		await server.close()
	})

	test('should return successful health check', async () => {
		const response = await server.inject({
			method: 'GET',
			url: '/api/health'
		})
		return expect(response.statusCode).toBe(200)
	})

	test('should handle non-existent API paths', async () => {
		const response = await server.inject({
			method: 'GET',
			url: '/api/does-not-exist'
		})
		return expect(response.statusCode).toBe(404)
	})
})
