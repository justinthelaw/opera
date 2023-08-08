export const defaultText: string =
    '- This is a custom built bullet writing tool; abbreviations will be replaced according to table in the abbreviations tab--you will see output on the right\n' +
    '- This tool can optimize spacing; output will be red if the optimizer could not fix spacing with 2004 or 2006 Unicode spaces\n' +
    '- Click the thesaurus button to show one; select a word in this or the output box to view synonyms--words in parentheses are abbreviations that are configured'

export const defaultWidth: number = 202.321

type Abbreviation = {
    enabled: boolean
    value: string
    abbr: string
}

export const defaultAbbrData: Abbreviation[] = [
    {
        enabled: true,
        value: 'abbreviations',
        abbr: 'abbrs'
    },
    {
        enabled: true,
        value: 'table',
        abbr: 'tbl'
    },
    {
        enabled: true,
        value: 'optimize',
        abbr: 'optim'
    },
    {
        enabled: true,
        value: 'with ',
        abbr: 'w/'
    },
    {
        enabled: true,
        value: 'parentheses',
        abbr: 'parens'
    }
]
