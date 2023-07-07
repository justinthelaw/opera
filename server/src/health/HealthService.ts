import { HealthFetch, HealthResponse, ServiceHealth, PossibleHealthServices } from './HealthModels'
import { DATABASE_URL, CLIENT_URL } from '../server.constants'
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
		const databaseHealth = await this.getDatabaseHealth()
		const clientHealth = await this.getClientHealth()
		return [clientHealth, databaseHealth]
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
}
