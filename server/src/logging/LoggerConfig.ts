import LoggerConfigurationInterface from './LoggerInterface'

const LoggerConfiguration: LoggerConfigurationInterface = {
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

export default LoggerConfiguration
