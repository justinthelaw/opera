import { server } from '../../src/index'
import fastify from 'fastify'

jest.mock('fastify')

describe('health route', () => {
  test('should return successful health check', async () => {
    const response = await server.inject({
      method: 'GET',
      url: '/health'
    })
    expect(response.statusCode).toBe(200)
    expect(response.json()).toEqual({ status: 'ok' })
  })

  test('should handle errors', async () => {
    const response = await server.inject({
      method: 'GET',
      url: '/health'
    })
    expect(response.statusCode).toBe(500)
    expect(response.json()).toEqual({ status: 'error' })
  })
})
```

