import HealthService from './health.service'
import { HealthResponse } from './health.models'

const healthService = new HealthService()

export class HealthController {
	async getOverallHealth(): Promise<HealthResponse> {
		const response: HealthResponse = await healthService.getOverallHealth()
		return response
	}
}
