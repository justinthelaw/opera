export type Status = 'healthy' | 'degraded' | 'down' | 'maintenance'
export type PossibleHealthServices = 'server' | 'api' | 'client' | 'database'

export interface RequestedServiceParams {
	service: PossibleHealthServices
}

export interface HealthFetch {
	name: string
	endPoint: string
	fetchHandler?: (res: any, serviceHealthResponse: ServiceHealth) => void
	description?: string
	status?: Status
	degradedReason?: string
}

export interface HealthResponse extends ServiceHealth {
	serviceStatuses?: Array<ServiceHealth>
}

export interface ServiceHealth {
	name: string
	status: Status
	description: string
	timeStamp: string
	degradedReason?: string
}
