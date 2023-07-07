import HealthController from '../../src/health/HealthController'
import { HealthResponse, PossibleHealthServices, ServiceHealth } from '../../src/health/HealthModels'
import { baseServerHealth } from '../../src/health/health.constants'

jest.mock('../../src/health/health.fetch', () => ({
	__esModule: true,
	default: jest.fn()
}))

describe('HealthController', () => {
	let healthController: HealthController

	beforeEach(() => {
		healthController = new HealthController()
	})

	afterEach(() => {
		jest.restoreAllMocks()
	})

	describe('getOverallHealth', () => {
		it('should return the overall health', async () => {
			const overallHealthResponse = await healthController.getOverallHealth()
			expect(overallHealthResponse).toEqual({
				...baseServerHealth,
				serviceStatuses: Array(2).fill(undefined) as ServiceHealth[]
			} as HealthResponse)
		})
	})

	describe('getRequestedServiceHealth', () => {
		it('should return the health of the requested service, server', async () => {
			const requestedServiceHealthResponse = await healthController.getRequestedServiceHealth('server')
			expect(requestedServiceHealthResponse).toEqual(baseServerHealth)
		})

		it('should throw an error for an invalid requested service', async () => {
			const requestedService = 'invalid-service'

			await expect(
				healthController.getRequestedServiceHealth(requestedService as PossibleHealthServices)
			).rejects.toThrowError('invalid-service is not a Smarter Bullets service')
		})
	})
})
