import dateBuilder from '../utils/dateBuilder'
import {
	HealthResponse,
	ServiceHealthResponse,
	OpenAiApiResponse,
	OpenAiApiHealthResponseComponentsArray
} from './health.response'
import { server } from '../index'
import { OPENAI_API_STATUS_URL } from '../constants/server.constants'

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
		return [openAiApiHealth]
	}

	private async getOpenAiApiHealth(): Promise<ServiceHealthResponse> {
		let openAiApiHealth: ServiceHealthResponse = {
			name: 'OpenAI API',
			description: "Health and status of OpenAI's API services",
			status: 'down',
			degradedReason: `${OPENAI_API_STATUS_URL} is unreachable`,
			timeStamp: dateBuilder()
		}

		await fetch('https://status.openai.com/api/v2/components.json')
			.then((json) => json.json())
			.then((res: OpenAiApiResponse) => res.components)
			.then((components: OpenAiApiHealthResponseComponentsArray) => components[0])
			.then((openAiApiHealthResponse) => {
				switch (openAiApiHealthResponse.status) {
					case 'operational':
						openAiApiHealth.status = 'healthy'
						break
					case 'degraded_performance':
					case 'partial_outage':
						openAiApiHealth.status = 'degraded'
						break
					default:
						openAiApiHealth.status = 'down'
						break
				}
				openAiApiHealth.timeStamp = dateBuilder(openAiApiHealthResponse.updated_at)
				delete openAiApiHealth.degradedReason
			})
			.catch((err) => {
				server.log.error(err)
				server.log.error(`${OPENAI_API_STATUS_URL} is unreachable`)
			})

		return openAiApiHealth
	}
}
