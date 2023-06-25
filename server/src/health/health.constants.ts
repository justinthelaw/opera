import dateBuilder from '../utils/date.builder'
import { HealthFetch, ServiceHealth, Status } from './HealthModels'

export const baseServerHealth: ServiceHealth = {
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
	serviceHealthResponse: ServiceHealth,
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

export const mockServiceResponseHealthy: ServiceHealth = {
	name: mockName,
	status: 'healthy',
	description: defaultDescription(mockName),
	timeStamp: mockDate
}

export const mockServiceResponseDown: ServiceHealth = {
	...mockServiceResponseHealthy,
	status: 'down',
	degradedReason: defaultDegradedReason(mockName, mockURL)
}

export const mockServiceResponseDegraded: ServiceHealth = {
	...mockServiceResponseHealthy,
	status: 'degraded'
}

export const mockHealthCustomFetchObject: HealthFetch = {
	name: mockName,
	endPoint: mockURL
}
