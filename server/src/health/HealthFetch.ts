import { HealthCustomFetchObject, ServiceHealthResponse, Status } from './HealthModels'
import { server } from '../index'
import dateBuilder from '../utils/DateBuilder'

const defaultStatus: Status = 'down'

const defaultDegradedReason = (fetchParams: HealthCustomFetchObject): string =>
	`${fetchParams.name} at ${fetchParams.endPoint} is unreachable`

const defaultDescription = (fetchParams: HealthCustomFetchObject): string => `Health and status of ${fetchParams.name}`

const defaultFetchHandler = (
	response: any,
	serviceHealthResponse: ServiceHealthResponse,
	fetchParams: HealthCustomFetchObject
) => {
	const status = response.status
	if (status >= 200 && status < 300) {
		serviceHealthResponse.status = 'healthy'
		delete serviceHealthResponse.degradedReason
	} else {
		serviceHealthResponse.status = 'degraded'
		serviceHealthResponse.degradedReason = `${fetchParams.name} at ${fetchParams.endPoint} 
			returned an HTTP status code ${response.status}, with message: ${response.message}`
	}
}

export const HealthCustomFetch = async (fetchParams: HealthCustomFetchObject): Promise<ServiceHealthResponse> => {
	const serviceHealthResponse: ServiceHealthResponse = {
		name: fetchParams.name,
		description: fetchParams.description || defaultDescription(fetchParams),
		status: fetchParams.status || defaultStatus,
		degradedReason: fetchParams.degradedReason || defaultDegradedReason(fetchParams),
		timeStamp: dateBuilder()
	}

	await fetch(fetchParams.endPoint)
		.then((response) => {
			if (fetchParams.fetchHandler !== undefined) {
				fetchParams.fetchHandler(response, serviceHealthResponse)
			} else {
				defaultFetchHandler(response, serviceHealthResponse, fetchParams)
			}
		})
		.catch(() => {
			server.log.warn(serviceHealthResponse.degradedReason)
		})

	return serviceHealthResponse
}
