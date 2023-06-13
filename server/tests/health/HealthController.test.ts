import HealthController from '../../src/health/HealthController'
import { HealthResponse, PossibleHealthServices, ServiceHealthResponse } from '../../src/health/HealthModel'
import dateBuilder from '../../src/utils/date.builder'

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
				name: 'Smarter Bullets Server (API)',
				status: 'healthy',
				description: 'Health and status of the Smarter Bullets Server (API) and third-party services',
				timeStamp: dateBuilder(),
				serviceStatuses: [undefined, undefined, undefined] as unknown as ServiceHealthResponse[]
			} as HealthResponse)
		})
	})

	describe('getRequestedServiceHealth', () => {
		it('should return the health of the requested service, server', async () => {
			const requestedServiceHealthResponse = await healthController.getRequestedServiceHealth('server')
			expect(requestedServiceHealthResponse).toEqual({
				name: 'Smarter Bullets Server (API)',
				status: 'healthy',
				description: 'Health and status of the Smarter Bullets Server (API) and third-party services',
				timeStamp: dateBuilder()
			} as ServiceHealthResponse)
		})

		it('should throw an error for an invalid requested service', async () => {
			const requestedService = 'invalid-service'

			await expect(
				healthController.getRequestedServiceHealth(requestedService as PossibleHealthServices)
			).rejects.toThrowError('invalid-service is not a Smarter Bullets service')
		})
	})
})
