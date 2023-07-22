import { render } from '@testing-library/react'
import React from 'react'
import Home from '../../src/pages/Home'

describe('App', () => {
    test('should render application title, opera', () => {
        const { getByText } = render(<Home />)
        const appTitleElement = getByText(/opera/i)
        expect(appTitleElement).toBeInTheDocument()
    })
})
