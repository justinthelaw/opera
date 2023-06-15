export type Status = 'healthy' | 'degraded' | 'down' | 'maintenance'
export type PossibleHealthServices = 'server' | 'api' | 'client' | 'database' | 'openai' | 'openaiapi' | 'open-ai-api'

export interface RequestedServiceParams {
	service: PossibleHealthServices
}

export interface HealthCustomFetchObject {
	name: string
	endPoint: string
	fetchHandler?: (res: any, serviceHealthResponse: ServiceHealthResponse) => void
	description?: string
	status?: Status
	degradedReason?: string
}

export interface HealthResponse extends ServiceHealthResponse {
	serviceStatuses?: Array<ServiceHealthResponse>
}

export interface ServiceHealthResponse {
	name: string
	status: Status
	description: string
	timeStamp: string
	degradedReason?: string
}

export interface OpenAIHealthResponseComponent {
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

export interface OpenAIHealthResponseComponentsArray {
	[index: number]: OpenAIHealthResponseComponent
}

export interface OpenAIResponse {
	page: {
		id: string
		name: string
		url: string
		time_zone: string
		updated_at: string
	}
	components: OpenAIHealthResponseComponentsArray
}

export interface RouteSchema {
	method: string
	url: string
	schema: {
		response: {
			200: {
				type: string
				properties: {
					name: { type: string }
					status: { type: string }
					description: { type: string }
					timeStamp: { type: string }
					degradedReason?: { type: string }
				}
			}
		}
		params?: {
			type: string
			properties: {
				service: { type: string }
			}
		}
	}
	handler: (request: any, reply: any) => void
}
