import dateBuilder from '../utils/date.builder'
import { HealthCustomFetchObject, HealthResponse, ServiceHealthResponse, Status } from './HealthModel'

export const baseServerHealth: ServiceHealthResponse = {
	name: 'Smarter Bullets Server (API)',
	status: 'healthy',
	description: 'Health and status of the Smarter Bullets Server (API) and third-party services',
	timeStamp: dateBuilder()
}

export const defaultStatus: Status = 'down'

export const defaultDegradedReason = (name: string, endPoint: string): string => `${name} at ${endPoint} is unreachable`

export const defaultDescription = (name: string): string => `Health and status of ${name}`

export const defaultFetchHandler = (
	response: any,
	serviceHealthResponse: ServiceHealthResponse,
	name: string,
	endPoint: string
) => {
	const status = response.status
	if (status >= 200 && status < 300) {
		serviceHealthResponse.status = 'healthy'
		delete serviceHealthResponse.degradedReason
	} else {
		serviceHealthResponse.status = 'degraded'
		serviceHealthResponse.degradedReason = `${name} at ${endPoint} 
			returned an HTTP status code ${response.status}, with message: ${response.message}`
	}
}

const mockName = 'Mock Service'
const mockURL = 'http://example.com/service'
export const mockDate = '1/1/1960, 00:00:00 (UTC)'

export const mockServiceResponseHealthy: ServiceHealthResponse = {
	name: mockName,
	status: 'healthy',
	description: defaultDescription(mockName),
	timeStamp: mockDate
}

export const mockServiceResponseDown: ServiceHealthResponse = {
	...mockServiceResponseHealthy,
	status: 'down',
	degradedReason: defaultDegradedReason(mockName, mockURL)
}

export const mockServiceResponseDegraded: ServiceHealthResponse = {
	...mockServiceResponseHealthy,
	status: 'degraded'
}

export const mockOverallHealthResponseHealthy: HealthResponse = {
	...mockServiceResponseHealthy,
	serviceStatuses: Array(3).fill(mockServiceResponseHealthy)
}

export const mockOverallHealthResponseDown: HealthResponse = {
	...mockOverallHealthResponseHealthy,
	status: 'down'
}

export const mockOverallHealthResponseDegraded: HealthResponse = {
	...mockOverallHealthResponseHealthy,
	status: 'degraded'
}

export const mockHealthCustomFetchObject: HealthCustomFetchObject = {
	name: mockName,
	endPoint: mockURL
}
