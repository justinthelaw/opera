import HealthService from '../../src/health/HealthService'
import healthCustomFetch from '../../src/health/health.fetch'
import { mockServiceResponseHealthy } from '../../src/health/health.constants'

jest.mock('../../src/health/health.fetch', () => ({
	__esModule: true,
	default: jest.fn()
}))

describe('HealthService', () => {
	let healthService: HealthService

	beforeEach(() => {
		healthService = new HealthService()
		;(healthCustomFetch as jest.Mock).mockResolvedValue(mockServiceResponseHealthy)
	})

	afterEach(() => {
		jest.restoreAllMocks()
	})

	describe('getOverallHealth', () => {
		it('should return the overall health of the server', async () => {
			const overallHealth = await healthService.getOverallHealth()
			expect(overallHealth).toBeDefined()
			expect(overallHealth).toHaveProperty('serviceStatuses')
			expect(overallHealth.serviceStatuses?.length).toBe(2)
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
	})
})
