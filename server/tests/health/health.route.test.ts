import { server } from '../../src/index'

describe('health route', () => {
	test('should return successful health check', async () => {
		const response = await server.inject({
			method: 'GET',
			url: '/api/health'
		})
		expect(response.statusCode).toBe(200)
	})

	test('should handle non-existent API paths', async () => {
		const response = await server.inject({
			method: 'GET',
			url: '/api/does-not-exist'
		})
		expect(response.statusCode).toBe(404)
	})
})
