import { HotTableProps } from '@handsontable/react'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import React, { useEffect } from 'react'
import { AbbreviationTable } from '../../../src/components/abbreviations/AbbreviationTable'
import { Abbreviation } from '../../../src/const/defaults'

jest.mock('@handsontable/react', () => {
    const MockHotTable = (props: HotTableProps) => {
        useEffect(() => {
            if (props.afterChange) {
                props.afterChange(null, 'loadData')
            }
        }, [])
        useEffect(() => {
            if (props.afterChange) {
                props.afterChange(null, 'edit')
            }
        }, [props.data])
        return (
            <div data-testid='parent' onClick={() => props.afterChange}>
                HELLO WORLD
            </div>
        )
    }
    return {
        HotTable: MockHotTable
    }
})

describe('<AbbreviationTable />', () => {
    const defaultData: Abbreviation[] = [
        {
            enabled: true,
            value: 'abbreviations',
            abbr: 'abbrs'
        },
        {
            enabled: false,
            value: 'table',
            abbr: 'tbl'
        },
        {
            enabled: true,
            value: 'optimize',
            abbr: 'optim'
        },
        {
            enabled: false,
            value: 'with ',
            abbr: 'w/'
        },
        {
            enabled: true,
            value: 'parentheses',
            abbr: 'parens'
        }
    ]

    it('renders without crashing', () => {
        renderAbbreviationTable({})
    })

    // TODO: test is failing and setData mock is not being called, check the rerender method
    it.skip('changes table data correctly ', async () => {
        const changedData = [
            {
                enabled: false,
                value: 'abbreviations',
                abbr: 'abbrs'
            },
            {
                enabled: false,
                value: 'zebra',
                abbr: 'zbr'
            },
            {
                enabled: true,
                value: 'optimize',
                abbr: 'optam'
            },
            {
                enabled: false,
                value: 'with ',
                abbr: 'w/'
            },
            {
                enabled: true,
                value: 'parentheses',
                abbr: '()'
            }
        ]

        const setData = jest.fn((data: Abbreviation[]) =>
            data.filter((row) => row.enabled !== null && row.value !== null && row.abbr !== null)
        )

        const { rerender, user } = renderAbbreviationTable({ data: defaultData })

        rerender(<AbbreviationTable data={changedData} setData={() => setData} />)
        await user.dblClick(screen.getByTestId(/parent/))

        expect(setData).toReturnWith(changedData)
    })
})

const renderAbbreviationTable = ({
    data = [],
    setData = jest.fn()
}: {
    data?: Abbreviation[]
    setData?: (data: Abbreviation[]) => Abbreviation[]
}) => {
    // default values based on default examples in pdf-bullets
    const { rerender } = render(<AbbreviationTable data={data} setData={() => setData} />)

    return { rerender, user: userEvent.setup() }
}
