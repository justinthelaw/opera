import {
	HealthCustomFetchObject,
	HealthResponse,
	ServiceHealthResponse,
	OpenAIResponse,
	OpenAIHealthResponseComponentsArray,
	PossibleHealthServices
} from './HealthModels'
import { OPENAI_API_STATUS_URL, DATABASE_URL, CLIENT_URL } from '../utils/Constants'
import HealthCustomFetch from './HealthFetch'
import dateBuilder from '../utils/DateBuilder'

export default class HealthService {
	async getOverallHealth() {
		const overallHealth: HealthResponse = {
			...this.getServerHealth(),
			serviceStatuses: await this.getThirdPartyServicesHealth()
		}
		return overallHealth
	}

	async getRequestedServiceHealth(requestedHealthService: PossibleHealthServices): Promise<ServiceHealthResponse> {
		let response: ServiceHealthResponse
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
			default:
				response = this.getServerHealth()
				break
		}
		return response
	}

	getServerHealth(): ServiceHealthResponse {
		const serverHealth: ServiceHealthResponse = {
			name: 'Smarter Bullets Server (API)',
			status: 'healthy',
			description: 'Health and status of the Smarter Bullets Server (API) and third-party services',
			timeStamp: dateBuilder()
		}

		return serverHealth
	}

	async getThirdPartyServicesHealth(): Promise<ServiceHealthResponse[]> {
		const openAIHealth = await this.getOpenAIHealth()
		const databaseHealth = await this.getDatabaseHealth()
		const clientHealth = await this.getClientHealth()
		return [clientHealth, databaseHealth, openAIHealth]
	}

	async getDatabaseHealth(): Promise<ServiceHealthResponse> {
		const name = 'Smarter Bullets Database'

		const databaseHealthFetch: HealthCustomFetchObject = {
			name: name,
			endPoint: DATABASE_URL
		}

		return HealthCustomFetch(databaseHealthFetch)
	}

	async getClientHealth(): Promise<ServiceHealthResponse> {
		const name = 'Smarter Bullets Client'

		const clientHealthFetch: HealthCustomFetchObject = {
			name: name,
			endPoint: CLIENT_URL
		}

		return HealthCustomFetch(clientHealthFetch)
	}

	async getOpenAIHealth(): Promise<ServiceHealthResponse> {
		const name = 'OpenAI API'

		const openAIHealthFetchHandler = async (response: any, serviceHealthResponse: ServiceHealthResponse) => {
			const json: OpenAIResponse = await response.json()
			const components: OpenAIHealthResponseComponentsArray = json.components
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

		const openAIHealthFetch: HealthCustomFetchObject = {
			name: name,
			endPoint: OPENAI_API_STATUS_URL || '[URL NOT AVAILABLE]',
			fetchHandler: openAIHealthFetchHandler
		}

		return HealthCustomFetch(openAIHealthFetch)
	}
}
