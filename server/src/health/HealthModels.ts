export type Status = 'healthy' | 'degraded' | 'down' | 'maintenance'
export type PossibleHealthServices = 'server' | 'api' | 'client' | 'database' | 'openai' | 'openaiapi' | 'open-ai-api'

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

export interface OpenAIHealthComponent {
	id: string
	name: string
	status: string
	created_at: string
	updated_at: string
	position: number
	description: string
	showcase: boolean
	start_date: string
	group_id?: string
	page_id: string
	group: boolean
	only_show_if_degraded: boolean
}

export interface OpenAIHealthComponentsArray {
	[index: number]: OpenAIHealthComponent
}

export interface OpenAIHealth {
	page: {
		id: string
		name: string
		url: string
		time_zone: string
		updated_at: string
	}
	components: OpenAIHealthComponentsArray
}
