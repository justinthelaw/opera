import { HealthCustomFetchObject, ServiceHealthResponse } from './HealthModel'
import healthCustomFetch from './health.fetch'
import dateBuilder from '../utils/date.builder'

jest.mock('../index', () => ({
	server: {
		log: {
			warn: jest.fn()
		}
	}
}))

describe('health.fetch', () => {
	afterEach(() => {
		jest.restoreAllMocks()
	})

	test('should fetch health data successfully and set status as healthy', async () => {
		const fetchParams: HealthCustomFetchObject = {
			name: 'Service1',
			endPoint: 'http://example.com/service1'
		}

		const mockFetchResponse = {
			status: 200
		}

		jest.spyOn(global, 'fetch').mockResolvedValueOnce(mockFetchResponse as Response)

		return healthCustomFetch(fetchParams).then((result) => {
			expect(global.fetch).toHaveBeenCalledWith(fetchParams.endPoint)
			expect(result).toEqual({
				name: 'Service1',
				description: 'Health and status of Service1',
				status: 'healthy',
				timeStamp: dateBuilder()
			})
		})
	})

	test('should handle fetch error and set status as down', async () => {
		const fetchParams: HealthCustomFetchObject = {
			name: 'Service2',
			endPoint: 'http://example.com/service2'
		}

		const mockFetchResponse = {
			status: 400
		}

		jest.spyOn(global, 'fetch').mockRejectedValueOnce(mockFetchResponse)

		return healthCustomFetch(fetchParams).then((result) => {
			expect(global.fetch).toHaveBeenCalledWith(fetchParams.endPoint)
			expect(result).toEqual({
				name: 'Service2',
				description: 'Health and status of Service2',
				status: 'down',
				degradedReason: 'Service2 at http://example.com/service2 is unreachable',
				timeStamp: dateBuilder()
			})
		})
	})

	test('should use custom fetch handler when provided', async () => {
		const fetchParams: HealthCustomFetchObject = {
			name: 'Service3',
			endPoint: 'http://example.com/service3',
			fetchHandler: (_, serviceHealthResponse: ServiceHealthResponse) => {
				serviceHealthResponse.status = 'degraded'
				serviceHealthResponse.degradedReason = 'Custom fetch handler'
			}
		}

		const mockFetchResponse = {
			status: 200
		}

		jest.spyOn(global, 'fetch').mockResolvedValueOnce(mockFetchResponse as Response)

		return healthCustomFetch(fetchParams).then((result) => {
			expect(global.fetch).toHaveBeenCalledWith(fetchParams.endPoint)
			expect(result).toEqual({
				name: 'Service3',
				description: 'Health and status of Service3',
				status: 'degraded',
				degradedReason: 'Custom fetch handler',
				timeStamp: dateBuilder()
			})
		})
	})
})
