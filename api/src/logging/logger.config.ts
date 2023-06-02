import { loggerConfigurationInterface } from './logger.interface'

export const loggerConfiguration: loggerConfigurationInterface = {
	development: {
		transport: {
			target: 'pino-pretty',
			options: {
				translateTime: 'HH:MM:ss Z',
				ignore: 'pid,hostname'
			}
		}
	},
	production: true,
	test: false
}
