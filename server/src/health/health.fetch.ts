<<<<<<< Updated upstream
import { HealthCustomFetchObject, ServiceHealthResponse } from './HealthModel'
=======
import { HealthFetch, ServiceHealth } from './HealthModels'
>>>>>>> Stashed changes
import { server } from '../index'
import dateBuilder from '../utils/date.builder'
import { defaultDegradedReason, defaultDescription, defaultFetchHandler, defaultStatus } from './health.constants'

const healthCustomFetch = async (fetchParams: HealthFetch): Promise<ServiceHealth> => {
	const serviceHealthResponse: ServiceHealth = {
		name: fetchParams.name,
		description: fetchParams.description || defaultDescription(fetchParams.name),
		status: fetchParams.status || defaultStatus,
		degradedReason: fetchParams.degradedReason || defaultDegradedReason(fetchParams.name, fetchParams.endPoint),
		timeStamp: dateBuilder()
	}

	await fetch(fetchParams.endPoint)
		.then(async (response) => {
			if (fetchParams.fetchHandler !== undefined) {
				return fetchParams.fetchHandler(response, serviceHealthResponse)
			} else {
				return defaultFetchHandler(response, serviceHealthResponse, fetchParams.name, fetchParams.endPoint)
			}
		})
		.catch((error) => {
			server.log.warn(serviceHealthResponse.degradedReason)
			server.log.warn(error)
		})

	return serviceHealthResponse
}

export default healthCustomFetch
