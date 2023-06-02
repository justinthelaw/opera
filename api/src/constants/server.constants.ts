import dotenv from 'dotenv'

dotenv.config({ path: '../../config/.env.local' })
export const { API_HOST, API_PORT, NODE_ENV, OPENAI_API_STATUS_URL } = process.env

export const ENV: string = NODE_ENV || 'development'
export const HOST: string = API_HOST || 'localhost'
export const PORT: number = parseInt(API_PORT || '8080')
export const TIMEZONE: string = 'UTC'
