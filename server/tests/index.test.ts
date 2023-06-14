import { server } from '../../src/index'
import fastify from 'fastify'
import fastifyStatic from '@fastify/static'

jest.mock('fastify')
jest.mock('@fastify/static')

describe('server', () => {
  test('should start successfully', () => {
    const logSpy = jest.spyOn(server.log, 'info')
    server.listen({ host: 'localhost', port: 3000 }, () => {})
    expect(logSpy).toHaveBeenCalledWith('Server is now listening on http://localhost:3000')
  })

  test('should handle start errors', () => {
    const logSpy = jest.spyOn(server.log, 'error')
    const exitSpy = jest.spyOn(process, 'exit').mockImplementation(() => {})
    server.listen({ host: 'localhost', port: 3000 }, (err) => {
      if (err) throw err
    })
    expect(logSpy).toHaveBeenCalled()
    expect(exitSpy).toHaveBeenCalledWith(1)
  })

  test('should serve static files', () => {
    expect(fastifyStatic).toHaveBeenCalledWith({
      root: expect.any(String),
      prefix: '/'
    })
  })
})
```

