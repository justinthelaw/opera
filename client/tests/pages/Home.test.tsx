import React from 'react'
import { render } from '@testing-library/react'
import Home from '../../src/pages/Home'

describe('App', () => {
	test('should render application title, smarter bullets', () => {
		const { getByText } = render(<Home />)
		const appTitleElement = getByText(/smarter bullets/i)
		expect(appTitleElement).toBeInTheDocument()
	})
})
