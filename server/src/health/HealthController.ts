import HealthService from './HealthService'
import { HealthResponse, PossibleHealthServices, ServiceHealthResponse } from './HealthModel'

const healthService = new HealthService()

export default class HealthController {
	async getOverallHealth(): Promise<HealthResponse> {
		const response: HealthResponse = await healthService.getOverallHealth()
		return response
	}
	async getRequestedServiceHealth(service: PossibleHealthServices): Promise<ServiceHealthResponse> {
		const response: ServiceHealthResponse = await healthService.getRequestedServiceHealth(
			service.toLowerCase() as PossibleHealthServices
		)
		return response
	}
}
