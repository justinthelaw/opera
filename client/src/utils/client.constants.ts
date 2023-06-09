export const { CLIENT_HOST, CLIENT_PORT, NODE_ENV, FAVICON_URL } = process.env

export const ENV: string = NODE_ENV || 'development'
export const HOST: string = CLIENT_HOST || 'localhost'
export const PORT: number = parseInt(CLIENT_PORT || '8080')
