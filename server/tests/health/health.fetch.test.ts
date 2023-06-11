import dateBuilder from '../../src/utils/date.builder'
import { HealthCustomFetchObject, HealthResponse, ServiceHealthResponse } from '../../src/health/HealthModel'
import healthCustomFetch from '../../src/health/health.fetch'
import {
	mockHealthCustomFetchObject,
	mockServiceResponseDegraded,
	mockServiceResponseDown,
	mockServiceResponseHealthy,
	mockDate
} from '../../src/health/health.constants'

jest.mock('../../src/index', () => ({
	server: {
		log: {
			warn: jest.fn()
		}
	}
}))

jest.mock('../../src/utils/date.builder', () => ({
	__esModule: true,
	default: jest.fn()
}))

describe('health.fetch', () => {
	const fetchParams: HealthCustomFetchObject = mockHealthCustomFetchObject

	beforeEach(() => {
		;(dateBuilder as jest.Mock).mockReturnValue(mockDate)
	})

	afterEach(() => {
		jest.restoreAllMocks()
	})

	test('should fetch health data successfully and set status as healthy', async () => {
		jest.mock('../../src/health/HealthController', () => Promise.resolve(mockServiceResponseHealthy))
		const mockFetchResponse = {
			status: 200
		}

		jest.spyOn(global, 'fetch').mockResolvedValueOnce(mockFetchResponse as Response)

		return healthCustomFetch(fetchParams).then((result) => {
			expect(global.fetch).toHaveBeenCalledWith(fetchParams.endPoint)
			expect(result).toEqual(mockServiceResponseHealthy)
		})
	})

	test('should handle fetch error and set status as down', async () => {
		jest.mock('../../src/health/HealthController', () => Promise.resolve(mockServiceResponseDown))
		const mockFetchResponse = {
			status: 400
		}

		jest.spyOn(global, 'fetch').mockRejectedValueOnce(mockFetchResponse)

		return healthCustomFetch(fetchParams).then((result) => {
			expect(global.fetch).toHaveBeenCalledWith(fetchParams.endPoint)
			expect(result).toEqual(mockServiceResponseDown)
		})
	})

	test('should use custom fetch handler when provided', async () => {
		const fetchParams: HealthCustomFetchObject = {
			name: 'Mock Service',
			endPoint: 'http://example.com/service',
			fetchHandler: (_, serviceHealthResponse: ServiceHealthResponse) => {
				serviceHealthResponse.status = 'degraded'
				serviceHealthResponse.degradedReason = 'Custom fetch handler'
			}
		}

		const customFetchResponse: HealthResponse = {
			...mockServiceResponseDegraded,
			degradedReason: 'Custom fetch handler'
		}
		jest.mock('../../src/health/HealthController', () => Promise.resolve(customFetchResponse))
		const mockFetchResponse = {
			status: 200
		}

		jest.spyOn(global, 'fetch').mockResolvedValueOnce(mockFetchResponse as Response)

		return healthCustomFetch(fetchParams).then((result) => {
			expect(global.fetch).toHaveBeenCalledWith(fetchParams.endPoint)
			expect(result).toEqual(customFetchResponse)
		})
	})
})
