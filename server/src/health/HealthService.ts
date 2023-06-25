import {
	HealthFetch,
	HealthResponse,
	ServiceHealth,
	OpenAIHealth,
	OpenAIHealthComponentsArray,
	PossibleHealthServices
} from './HealthModels'
import { OPENAI_API_STATUS_URL, DATABASE_URL, CLIENT_URL } from '../server.constants'
import HealthCustomFetch from './health.fetch'
import dateBuilder from '../utils/date.builder'
import { baseServerHealth } from './health.constants'

export default class HealthService {
	async getOverallHealth() {
		const overallHealth: HealthResponse = {
			...this.getServerHealth(),
			serviceStatuses: await this.getThirdPartyServicesHealth()
		}
		return overallHealth
	}

	async getRequestedServiceHealth(requestedHealthService: PossibleHealthServices): Promise<ServiceHealth> {
		let response: ServiceHealth
		switch (requestedHealthService) {
			case 'client':
				response = await this.getClientHealth()
				break
			case 'database':
				response = await this.getDatabaseHealth()
				break
			case 'openai':
			case 'openaiapi':
			case 'open-ai-api':
				response = await this.getOpenAIHealth()
				break
			case 'server':
			case 'api':
				response = this.getServerHealth()
				break
			default:
				throw new Error(`${requestedHealthService} is not a Smarter Bullets service`)
		}
		return response
	}

	getServerHealth(): ServiceHealth {
		return baseServerHealth
	}

	async getThirdPartyServicesHealth(): Promise<ServiceHealth[]> {
		const openAIHealth = await this.getOpenAIHealth()
		const databaseHealth = await this.getDatabaseHealth()
		const clientHealth = await this.getClientHealth()
		return [clientHealth, databaseHealth, openAIHealth]
	}

	async getDatabaseHealth(): Promise<ServiceHealth> {
		const name = 'Smarter Bullets Database'

		const databaseHealthFetch: HealthFetch = {
			name: name,
			endPoint: DATABASE_URL
		}

		return HealthCustomFetch(databaseHealthFetch)
	}

	async getClientHealth(): Promise<ServiceHealth> {
		const name = 'Smarter Bullets Client'

		const clientHealthFetch: HealthFetch = {
			name: name,
			endPoint: CLIENT_URL
		}

		return HealthCustomFetch(clientHealthFetch)
	}

	async getOpenAIHealth(): Promise<ServiceHealth> {
		const name = 'OpenAI API'

		const openAIHealthFetchHandler = async (response: any, serviceHealthResponse: ServiceHealth) => {
			const json: OpenAIHealth = await response.json()
			const components: OpenAIHealthComponentsArray = json.components
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

		const openAIHealthFetch: HealthFetch = {
			name: name,
			endPoint: OPENAI_API_STATUS_URL as string,
			fetchHandler: openAIHealthFetchHandler
		}

		return HealthCustomFetch(openAIHealthFetch)
	}
}
