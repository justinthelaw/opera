import dotenv from 'dotenv'

dotenv.config({ path: '../config/.env.local' })
export const {
	MONGO_HOST,
	MONGO_PORT,
	CLIENT_HOST,
	CLIENT_PORT,
	API_VERSION,
	API_HOST,
	API_PORT,
	NODE_ENV,
	OPENAI_API_STATUS_URL
} = process.env

export const ENV: string = NODE_ENV || 'development'
export const HOST: string = API_HOST || 'localhost'
export const PORT: number = parseInt(API_PORT || '8080')
export const TIMEZONE: string = 'UTC'
export const PROTOCOL: string = NODE_ENV === 'development' ? 'http://' : 'https://'
export const DATABASE_URL: string =
	NODE_ENV === 'development' ? `${PROTOCOL}${MONGO_HOST}:${MONGO_PORT}` : `${PROTOCOL}${MONGO_HOST}`
export const CLIENT_URL: string =
	NODE_ENV === 'development' ? `${PROTOCOL}${CLIENT_HOST}:${CLIENT_PORT}` : `${PROTOCOL}${MONGO_HOST}`
