import { hashCode, optimize, renderBulletText, Results } from '../../../src/components/bullets/utils'
import { STATUS } from '../../../src/const/const'

describe('hashCode', () => {
    it('should return a hash code of 0 if the given string is empty', () => {
        const stringToHash = ''
        const expectedHashCode = 0

        const actualHashCode = hashCode(stringToHash)

        expect(actualHashCode).toEqual(expectedHashCode)
    })

    it('should return a hash code of the given string', () => {
        const stringToHash = 'hello world'
        const expectedHashCode = 1794106052

        const actualHashCode = hashCode(stringToHash)

        expect(actualHashCode).toEqual(expectedHashCode)
    })
})

describe('optimize', () => {
    const mockRawBulletText =
        'Assisted 11 stranded motorists/police during blizzard; protected from freezing weather--ensured safe travel condition'

    it('should return initial results as optimized if not over/underflowing', () => {
        const mockInitEvalResults: Results = {
            textLines: [mockRawBulletText],
            fullWidth: 100,
            lines: 1,
            overflow: 0
        }
        const mockEvalFcn = jest.fn(() => mockInitEvalResults)
        const expectedResults = { status: STATUS.OPTIMIZED, rendering: mockInitEvalResults }

        const actualResults = optimize(mockRawBulletText, mockEvalFcn)

        expect(mockEvalFcn).toHaveBeenCalledTimes(1)
        expect(actualResults).toEqual(expectedResults)
    })

    it('should fail if making a space smaller cannot resolve overflow', () => {
        const mockWorstCaseText =
            'Assisted 11 stranded motorists/police during blizzard; protected from freezing weather--ensured safe travel condition'
        const mockInitEvalResults: Results = {
            textLines: [mockRawBulletText],
            fullWidth: 100,
            lines: 1,
            overflow: 1
        }
        const mockWorstCaseResults: Results = { ...mockInitEvalResults, textLines: [mockWorstCaseText], overflow: 2 }
        const mockEvalFcn = jest.fn((str: string) =>
            str === mockRawBulletText ? mockInitEvalResults : mockWorstCaseResults
        )
        const expectedResults = { status: STATUS.FAILED_OPT, rendering: mockWorstCaseResults }

        const actualResults = optimize(mockRawBulletText, mockEvalFcn)

        expect(mockEvalFcn).toHaveBeenCalledTimes(2)
        expect(actualResults).toEqual(expectedResults)
    })

    it('should fail if making a space larger cannot resolve max underflow', () => {
        const mockWorstCaseText =
            'Assisted 11 stranded motorists/police during blizzard; protected from freezing weather--ensured safe travel condition'
        const mockInitEvalResults: Results = {
            textLines: [mockRawBulletText],
            fullWidth: 100,
            lines: 1,
            overflow: -6
        }
        const mockWorstCaseResults: Results = { ...mockInitEvalResults, textLines: [mockWorstCaseText], overflow: -5 }
        const mockEvalFcn = jest.fn((str: string) =>
            str === mockRawBulletText ? mockInitEvalResults : mockWorstCaseResults
        )
        const expectedResults = { status: STATUS.FAILED_OPT, rendering: mockWorstCaseResults }

        const actualResults = optimize(mockRawBulletText, mockEvalFcn)

        expect(mockEvalFcn).toHaveBeenCalledTimes(2)
        expect(actualResults).toEqual(expectedResults)
    })

    // TODO: is there any way to mock getRandomInt to be deterministic?
    //  Otherwise, the while loop in optimize() seems untestable
    it.skip('should succeed if it cannot add any more larger spaces without overflowing', () => {
        const mockWorstCaseText =
            'Assisted 11 stranded motorists/police during blizzard; protected from freezing weather--ensured safe travel condition'
        const mockNewResultsText =
            'Assisted 11 stranded motorists/police during blizzard; protected from freezing weather--ensured safe travel condition'
        const mockPrevResultsText =
            'Assisted 11 stranded motorists/police during blizzard; protected from freezing weather--ensured safe travel condition'

        console.log(mockRawBulletText.replaceAll(' ', ''))

        const mockInitEvalResults: Results = {
            textLines: [mockRawBulletText],
            fullWidth: 100,
            lines: 1,
            overflow: -1
        }
        const mockWorstCaseResults: Results = { ...mockInitEvalResults, textLines: [mockWorstCaseText], overflow: 0 }
        const mockNewResults: Results = { ...mockInitEvalResults, textLines: [mockNewResultsText], overflow: 1 }
        const mockPrevResults: Results = { ...mockInitEvalResults, textLines: [mockPrevResultsText], overflow: 0 }
        const mockEvalFcn = jest.fn((str: string) => {
            if (str === mockRawBulletText) {
                return mockInitEvalResults
            } else if (str === mockWorstCaseText) {
                return mockWorstCaseResults
            } else if (str === mockPrevResultsText) {
                return mockPrevResults
            } else {
                return mockNewResults
            }
        })
        const expectedResults = { status: STATUS.OPTIMIZED, rendering: mockPrevResults }

        const actualResults = optimize(mockRawBulletText, mockEvalFcn)

        expect(mockEvalFcn).toHaveBeenCalledTimes(3)
        expect(actualResults).toEqual(expectedResults)
    })
})

describe('renderBulletText', () => {
    it('returns empty results if the given text is empty', () => {
        const expectedResults: Results = { textLines: [], fullWidth: 0, lines: 0, overflow: -100 }

        const actualResults: Results = renderBulletText('', jest.fn(), 100)

        expect(actualResults).toEqual(expectedResults)
    })

    it('returns underflow results if width of the text is less than desired', () => {
        const mockText = 'hello world'
        const mockFullWidth = 50
        const mockGetWidth = jest.fn(() => mockFullWidth)
        const expectedResults: Results = { textLines: [mockText], fullWidth: mockFullWidth, lines: 1, overflow: -50 }

        const actualResults: Results = renderBulletText(mockText, mockGetWidth, 100)

        expect(actualResults).toEqual(expectedResults)
    })

    // TODO this test feels a bit contrived,
    //      can we find a real example that causes the scenario under test?
    //  although this might be caused by widths actually being pixel amounts
    //  rather than how this test uses them as char counts
    it('returns overflow results if text cannot be fit on a single line', () => {
        const mockText = 'eleven char'
        const mockFullWidth = 11
        const mockGetWidth = jest.fn((str: string) => str.length)
        const expectedResults: Results = { textLines: [mockText], fullWidth: mockFullWidth, lines: 1, overflow: 0 }

        const actualResults: Results = renderBulletText(mockText, mockGetWidth, 11)

        expect(actualResults).toEqual(expectedResults)
    })

    // TODO add more tests once we understand renderBulletText function better
})