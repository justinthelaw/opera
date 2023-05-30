import dateBuilder from '../utils/dateBuilder'
import { HealthResponse, ServiceHealth } from './health.model'

export default class HealthService {
	getOverallHealth() {
		const overallHealth: HealthResponse = {
			name: 'smarter-bullets',
			status: true,
			timeStamp: dateBuilder(),
			serviceStatuses: this.getAllServicesHealth()
		}
		return overallHealth
	}

	private getAllServicesHealth(): Array<ServiceHealth> {
		// TODO: Check services as needed based on environment, e.g., database host is up
		return [{ name: 'thisIsAnExample', status: true, timeStamp: dateBuilder() }]
	}
}
