import HealthService from './HealthService'
import healthCustomFetch from './HealthFetch'

jest.mock('./HealthFetch', () => ({
	__esModule: true,
	default: jest.fn()
}))

describe('HealthService', () => {
	let healthService: HealthService

	beforeEach(() => {
		healthService = new HealthService()
		// Mock the implementation of healthCustomFetch
		;(healthCustomFetch as jest.Mock).mockResolvedValue({
			name: 'Mock Service',
			status: 'healthy',
			description: 'Mock Service Health',
			timeStamp: '1/1/1960, 00:00:00 (UTC)'
		})
	})

	afterEach(() => {
		jest.restoreAllMocks()
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
			const clientHealthSpy = jest.spyOn(healthService, 'getClientHealth')
			await healthService.getRequestedServiceHealth('client')
			expect(clientHealthSpy).toHaveBeenCalledTimes(1)
		})
		it('should call the getDatabaseHealth method when given argument, "database"', async () => {
			const databaseHealthSpy = jest.spyOn(healthService, 'getDatabaseHealth')
			await healthService.getRequestedServiceHealth('database')
			expect(databaseHealthSpy).toHaveBeenCalledTimes(1)
		})
		it('should call the getOpenAiApiHealth method when given argument, "openai"', async () => {
			const openAIAPIHealthSpy = jest.spyOn(healthService, 'getOpenAIHealth')
			await healthService.getRequestedServiceHealth('openai')
			await healthService.getRequestedServiceHealth('openaiapi')
			await healthService.getRequestedServiceHealth('open-ai-api')
			expect(openAIAPIHealthSpy).toHaveBeenCalledTimes(3)
		})
	})
})
