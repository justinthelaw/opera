import HealthService from './HealthService'
import { HealthCustomFetch } from './HealthFetch'

jest.mock('./HealthFetch', () => ({
	HealthCustomFetch: jest.fn()
}))

describe('HealthService', () => {
	let healthService: HealthService

	beforeEach(() => {
		healthService = new HealthService()
		;(HealthCustomFetch as jest.Mock).mockResolvedValueOnce({
			name: 'Mock Service',
			status: 'healthy',
			description: 'Mock Service Health',
			timeStamp: '1/1/1960, 00:00:00 (UTC)'
		})
	})

	afterEach(() => {
		jest.clearAllMocks()
	})

	describe('getOverallHealth', () => {
		it('should return the overall health of the server', async () => {
			const overallHealth = await healthService.getOverallHealth()
			expect(overallHealth).toBeDefined()
			expect(overallHealth).toHaveProperty('status', 'healthy')
			expect(overallHealth).toHaveProperty('timeStamp')
			expect(overallHealth).toHaveProperty('serviceStatuses')
			expect(Array.isArray(overallHealth.serviceStatuses)).toBeTruthy()
			expect(overallHealth.serviceStatuses?.length).toBe(3)
		})
	})

	describe('getRequestedServiceHealth', () => {
		it('should call the getServerHealth method when given argument, "server"', async () => {
			const serverHealthSpy = jest.spyOn(healthService, 'getServerHealth')
			await healthService.getRequestedServiceHealth('server')
			expect(serverHealthSpy).toHaveBeenCalledTimes(1)
		})
		it('should call the getClientHealth method when given argument, "client"', async () => {
			const serverHealthSpy = jest.spyOn(healthService, 'getClientHealth')
			await healthService.getRequestedServiceHealth('client')
			expect(serverHealthSpy).toHaveBeenCalledTimes(1)
		})
		it('should call the getDatabaseHealth method when given argument, "database"', async () => {
			const serverHealthSpy = jest.spyOn(healthService, 'getDatabaseHealth')
			await healthService.getRequestedServiceHealth('database')
			expect(serverHealthSpy).toHaveBeenCalledTimes(1)
		})
		it('should call the getOpenAiApiHealth method when given argument, "openai"', async () => {
			const serverHealthSpy = jest.spyOn(healthService, 'getOpenAiApiHealth')
			await healthService.getRequestedServiceHealth('openai')
			await healthService.getRequestedServiceHealth('openaiapi')
			await healthService.getRequestedServiceHealth('open-ai-api')
			expect(serverHealthSpy).toHaveBeenCalledTimes(3)
		})
	})
})
