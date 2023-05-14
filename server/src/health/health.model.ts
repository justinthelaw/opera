export interface HealthResponse {
    name: string;
    status: boolean;
    degradedReason?: string;
    serviceStatuses?: Array<ServiceHealth>;
    timeStamp: string;
}

export interface ServiceHealth {
    name: string;
    status: boolean;
    degradedReason?: string;
    timeStamp: string;
}