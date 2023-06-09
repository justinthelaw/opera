import LoggerConfigurationInterface from './LoggerConfigurationModel'

const loggerConfiguration: LoggerConfigurationInterface = {
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

export default loggerConfiguration
