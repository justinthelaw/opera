import dateBuilder from '../utils/dateBuilder'
import { ServiceHealthResponse } from './health.models'
import { HealthCustomFetch } from './health.models'
import { server } from '../index'

export const healthCustomFetch = async (fetchParams: HealthCustomFetch): Promise<ServiceHealthResponse> => {
	let serviceHealthResponse: ServiceHealthResponse = {
		name: fetchParams.name,
		description: fetchParams.description || `Health and status of ${fetchParams.name}`,
		status: fetchParams.defaultStatus || 'down',
		degradedReason:
			fetchParams.defaultDegradedReason || `${fetchParams.name} at ${fetchParams.endPoint} is unreachable`,
		timeStamp: dateBuilder()
	}

	await fetch(fetchParams.endPoint)
		.then((response) => {
			fetchParams.fetchHandler(response, serviceHealthResponse)
		})
		.catch(() => {
			server.log.error(serviceHealthResponse.degradedReason)
		})

	return serviceHealthResponse
}
