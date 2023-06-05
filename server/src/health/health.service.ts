import dateBuilder from '../utils/dateBuilder'
import {
	HealthCustomFetch,
	HealthResponse,
	ServiceHealthResponse,
	OpenAiApiResponse,
	OpenAiApiHealthResponseComponentsArray
} from './health.models'
import { OPENAI_API_STATUS_URL, DATABASE_URL, CLIENT_URL } from '../constants/server.constants'
import { healthCustomFetch } from './health.fetch'

export default class HealthService {
	async getOverallHealth() {
		const overallHealth: HealthResponse = {
			name: 'Smarter Bullets API',
			status: 'healthy',
			description: 'Health and status of the Smarter Bullets API and third-party services',
			timeStamp: dateBuilder(),
			serviceStatuses: await this.getAllServicesHealth()
		}
		return overallHealth
	}

	private async getAllServicesHealth(): Promise<ServiceHealthResponse[]> {
		const openAiApiHealth = await this.getOpenAiApiHealth()
		const databaseHealth = await this.getDatabaseHealth()
		const clientHealth = await this.getClientHealth()
		return [clientHealth, databaseHealth, openAiApiHealth]
	}

	private async getDatabaseHealth(): Promise<ServiceHealthResponse> {
		const name = 'Smarter Bullets Database'

		const databaseHealthFetchHandler = (response: any, serviceHealthResponse: ServiceHealthResponse) => {
			const status = response.status
			if (status >= 200 && status < 300) {
				serviceHealthResponse.status = 'healthy'
				delete serviceHealthResponse.degradedReason
			}
		}

		const databaseHealthFetch: HealthCustomFetch = {
			name: name,
			endPoint: DATABASE_URL,
			fetchHandler: databaseHealthFetchHandler
		}

		return healthCustomFetch(databaseHealthFetch)
	}

	private async getClientHealth(): Promise<ServiceHealthResponse> {
		const name = 'Smarter Bullets Client'

		const clientHealthFetchHandler = (response: any, serviceHealthResponse: ServiceHealthResponse) => {
			const status = response.status
			if (status >= 200 && status < 300) {
				serviceHealthResponse.status = 'healthy'
				delete serviceHealthResponse.degradedReason
			}
		}

		const clientHealthFetch: HealthCustomFetch = {
			name: name,
			endPoint: CLIENT_URL,
			fetchHandler: clientHealthFetchHandler
		}

		return healthCustomFetch(clientHealthFetch)
	}

	private async getOpenAiApiHealth(): Promise<ServiceHealthResponse> {
		const name = 'OpenAI API'

		const openAiApiHealthFetchHandler = async (response: any, serviceHealthResponse: ServiceHealthResponse) => {
			const json: OpenAiApiResponse = await response.json()
			const components: OpenAiApiHealthResponseComponentsArray = json.components
			const component = components[0]
			switch (component.status) {
				case 'operational':
					serviceHealthResponse.status = 'healthy'
					break
				case 'degraded_performance':
				case 'partial_outage':
					serviceHealthResponse.status = 'degraded'
					break
				default:
					serviceHealthResponse.status = 'down'
					break
			}
			serviceHealthResponse.timeStamp = dateBuilder(component.updated_at)
			delete serviceHealthResponse.degradedReason
		}

		const openAiApiHealthFetch: HealthCustomFetch = {
			name: name,
			endPoint: OPENAI_API_STATUS_URL || '[URL NOT AVAILABLE]',
			fetchHandler: openAiApiHealthFetchHandler
		}

		return healthCustomFetch(openAiApiHealthFetch)
	}
}
