import { HealthResponse, PossibleHealthServices } from './HealthModel'

export const getOverallHealthSchema = {
  description: 'Get overall health of the server',
  tags: ['health'],
  summary: 'Returns overall health of the server',
  response: {
    200: {
      description: 'Successful response',
      type: 'object',
      properties: {
        ...HealthResponse
      }
    }
  }
}

export const getRequestedServiceHealthSchema = {
  description: 'Get health of a specific service',
  tags: ['health'],
  summary: 'Returns health of a specific service',
  params: {
    type: 'object',
    properties: {
      service: { type: 'string', enum: PossibleHealthServices }
    }
  },
  response: {
    200: {
      description: 'Successful response',
      type: 'object',
      properties: {
        ...HealthResponse
      }
    },
    400: {
      description: 'Invalid service requested',
      type: 'object'
    }
  }
}
```

