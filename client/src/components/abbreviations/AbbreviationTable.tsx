import { HotTable } from '@handsontable/react'
import { ChangeSource } from 'handsontable/common'
import React, { Dispatch, SetStateAction, useRef } from 'react'
import { Abbreviation } from '../../const/defaults'

const tableSettings = {
    columns: [
        {
            data: 'enabled',
            type: 'checkbox',
            disableVisualSelection: true,
            width: 20
        },
        {
            data: 'value',
            type: 'text'
        },
        {
            data: 'abbr',
            type: 'text'
        }
    ],
    width: 500,
    autoWrapRow: true,
    height: 500,
    maxRows: Infinity,
    manualRowResize: true,
    manualColumnResize: true,
    rowHeaders: true,
    colHeaders: ['Enabled', 'Word', 'Abbreviation'],
    trimWhitespace: false,
    enterBeginsEditing: false,
    manualRowMove: true,
    manualColumnMove: true,
    columnSorting: {
        indicator: true
    },
    autoColumnSize: false,
    minRows: 15,
    contextMenu: true,
    licenseKey: 'non-commercial-and-evaluation'
}

type Props = {
    data: Abbreviation[]
    setData: Dispatch<SetStateAction<Abbreviation[]>>
}

export const AbbreviationTable = ({ data, setData }: Props) => {
    const tableRef = useRef<HotTable>(null)

    const update = (source?: ChangeSource) => {
        // TODO remove these logs later, once we've got the app running similarly
        // console.log({source, payload, tableRef: tableRef.current , data})
        console.log('update source: ', source)
        const updateSources = ['ContextMenu.removeRow', 'edit', 'ContextMenu.rowAbove', 'ContextMenu.rowBelow']
        if (source && updateSources.includes(source) && tableRef.current !== null) {
            const rawData = tableRef.current.hotInstance?.getData()
            const newData = rawData?.map((row: [boolean, string, string]): Abbreviation => {
                return {
                    enabled: row[0],
                    value: row[1],
                    abbr: row[2]
                }
            })

            setData(newData || [])
        }
    }

    return (
        <HotTable
            {...tableSettings}
            stretchH='all'
            data={data}
            ref={tableRef}
            afterChange={(_changes, source) => update(source)}
            afterRemoveRow={(_i, _a, _r, source) => update(source)}
            afterCreateRow={(_i, _a, source) => update(source)}
        />
    )
}
