import HealthService from './HealthService'
import { HealthResponse, PossibleHealthServices, ServiceHealth } from './HealthModels'

const healthService = new HealthService()

export default class HealthController {
	async getOverallHealth(): Promise<HealthResponse> {
		const response: HealthResponse = await healthService.getOverallHealth()
		return response
	}
	async getRequestedServiceHealth(service: PossibleHealthServices): Promise<ServiceHealth> {
		const response: ServiceHealth = await healthService.getRequestedServiceHealth(
			service.toLowerCase() as PossibleHealthServices
		)
		return response
	}
}
