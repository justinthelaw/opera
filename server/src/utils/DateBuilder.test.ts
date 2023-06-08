import dateBuilder from './DateBuilder'
import { TIMEZONE } from './Constants'

describe('dateBuilder', () => {
	beforeEach(() => {
		const mockCurrentTime = new Date(Date.UTC(2023, 5, 1, 12, 0, 0)).toISOString()
		jest.spyOn(global.Date.prototype, 'toISOString').mockReturnValue(mockCurrentTime)
		jest.spyOn(global.Date.prototype, 'toLocaleString').mockReturnValue('6/1/2023, 12:00:00 PM')
	})

	afterEach(() => {
		jest.restoreAllMocks()
		jest.clearAllTimers()
	})

	it('returns the current date and time in the specified timezone if no dateString is provided', () => {
		expect(dateBuilder()).toBe(`6/1/2023, 12:00:00 PM (${TIMEZONE})`)
		expect(global.Date.prototype.toISOString).toHaveBeenCalled()
		expect(global.Date.prototype.toLocaleString).toHaveBeenCalledWith('en-US', {
			timeZone: TIMEZONE,
			hour12: false
		})
	})

	it('returns the formatted date and time in the specified timezone if a valid dateString is provided', () => {
		const customDateString = '2023-05-31T10:20:30Z'
		expect(dateBuilder(customDateString)).toBe(`6/1/2023, 12:00:00 PM (${TIMEZONE})`)
		expect(global.Date.prototype.toISOString).not.toHaveBeenCalled()
		expect(global.Date.prototype.toLocaleString).toHaveBeenCalledWith('en-US', {
			timeZone: TIMEZONE,
			hour12: false
		})
	})

	it('handles undefined dateString gracefully and uses the current date and time', () => {
		const undefinedDateString: any = undefined
		expect(dateBuilder(undefinedDateString)).toBe(`6/1/2023, 12:00:00 PM (${TIMEZONE})`)
		expect(global.Date.prototype.toISOString).toHaveBeenCalled()
		expect(global.Date.prototype.toLocaleString).toHaveBeenCalledWith('en-US', {
			timeZone: TIMEZONE,
			hour12: false
		})
	})
})
