import { TIMEZONE } from '../constants/api.constants'

export default function dateBuilder(dateString?: string): string {
	const time = dateString || new Date().toISOString()

	const timeString = new Date(time).toLocaleString('en-US', {
		timeZone: TIMEZONE,
		hour12: false
	})

	return `${timeString} (${TIMEZONE})`
}
