import HealthController from '../../src/health/HealthController'

jest.mock('../../src/health/health.fetch', () => ({
	__esModule: true,
	default: jest.fn()
}))

describe('HealthController', () => {
	// TODO: finish HealthController tests
	// eslint-disable-next-line @typescript-eslint/no-unused-vars
	let healthController: HealthController

	beforeEach(() => {
		healthController = new HealthController()
	})

	afterEach(() => {
		jest.restoreAllMocks()
	})

	describe('getOverallHealth', () => {
		it('should call the getOverallHealth service', async () => {})
	})

	describe('getRequestedServiceHealth', () => {
		it('should call the getRequestedServiceHealth service with the requested service string', async () => {})
	})
})
