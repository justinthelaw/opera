import { render, screen } from '@testing-library/react'
import React from 'react'
import { Bullet } from '../../../src/components/bullets/Bullet'

describe('<Bullet />', () => {
    // This test is too close to implementation rather than user behavior
    it('renders text in red if the bullet cannot be optimized', () => {
        // text based on default examples in pdf-bullets
        const text =
            '- This is a custom built bullet writing tool; abbrs will be replaced according to tbl in the abbrs tab--you will see output on the right'

        renderBullet({ text })

        const renderedTextDiv = screen.getByText(text.substring(0, text.indexOf(';')), { exact: false }).parentElement!

        expect(renderedTextDiv).toHaveStyle('color: red')
    })

    it('renders text in black if the bullet is optimized', () => {
        // text based on default examples in pdf-bullets
        const text =
            '- This tool can optim spacing; output will be red if the optimizer could not fix spacing w/2004 or 2006 Unicode spaces'

        renderBullet({ text })

        const renderedTextDiv = screen.getByText(text).parentElement!

        expect(renderedTextDiv).toHaveStyle('color: black')
    })

    it('renders text in red if the bullet is unoptimized and optimization is disabled', () => {
        // text based on default examples in pdf-bullets
        const text =
            '- This tool can optim spacing; output will be red if the optimizer could not fix spacing w/2004 or 2006 Unicode spaces'
        const enableOptim: boolean = false

        renderBullet({ text, enableOptim })

        const renderedTextDiv = screen.getByText(text).parentElement!

        expect(renderedTextDiv).toHaveStyle('color: red')
    })

    it('renders text in black if the bullet is optimized and optimization is disabled', () => {
        // text based on default examples in pdf-bullets
        const text =
            '- This tool can optim spacing; output will be red if the optimizer could not fix spacing w/2004 or 2006 Unicode spacesf'
        const enableOptim: boolean = false

        renderBullet({ text, enableOptim })

        const renderedTextDiv = screen.getByText(text).parentElement!

        expect(renderedTextDiv).toHaveStyle('color: black')
    })
})

const renderBullet = ({ text = '', enableOptim = true }: { text: string; enableOptim?: boolean }) => {
    // default values based on default examples in pdf-bullets
    render(
        <Bullet text={text} widthPx={764.6777952755906} enableOptim={enableOptim} height={48} onHighlight={() => {}} />
    )
}
