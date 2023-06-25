import HealthService from './HealthService'
<<<<<<< Updated upstream
import { HealthResponse, PossibleHealthServices, ServiceHealthResponse } from './HealthModel'
=======
import { HealthResponse, PossibleHealthServices, ServiceHealth } from './HealthModels'
>>>>>>> Stashed changes

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
