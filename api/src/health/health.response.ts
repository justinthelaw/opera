type Status = 'healthy' | 'degraded' | 'down' | 'maintenance'

export interface HealthResponse {
	name: string
	status: Status
	description: string
	degradedReason?: string
	serviceStatuses?: Array<ServiceHealthResponse>
	timeStamp: string
}

export interface ServiceHealthResponse {
	name: string
	status: Status
	description: string
	degradedReason?: string
	timeStamp: string
}

export interface OpenAiApiHealthResponseComponent {
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

export interface OpenAiApiHealthResponseComponentsArray {
	[index: number]: OpenAiApiHealthResponseComponent
}

export interface OpenAiApiResponse {
	page: {
		id: string
		name: string
		url: string
		time_zone: string
		updated_at: string
	}
	components: OpenAiApiHealthResponseComponentsArray
}
