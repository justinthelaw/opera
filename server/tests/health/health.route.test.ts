import { server } from '../../src/index'

describe('health route', () => {
	afterEach(() => {
		jest.restoreAllMocks()
		jest.clearAllTimers()
	})

	afterAll(async () => {
		await server.close()
	})
	test('should return successful health check with Swagger documentation', async () => {
		const response = await server.inject({
			method: 'GET',
			url: '/api/health'
		})
		expect(response.statusCode).toBe(200)
		expect(response.payload).toContain('swagger')
	})

	test('should handle non-existent API paths', async () => {
		const response = await server.inject({
			method: 'GET',
			url: '/api/does-not-exist'
		})
		return expect(response.statusCode).toBe(404)
	})

	test('should return successful health check for a specific service with Swagger documentation', async () => {
		const response = await server.inject({
			method: 'GET',
			url: '/api/health/server'
		})
		expect(response.statusCode).toBe(200)
		expect(response.payload).toContain('swagger')
	})
})
