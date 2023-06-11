import React from 'react'
import { render } from '@testing-library/react'
import App from '../../src/components/App'

describe('App', () => {
	test('should render "Hello World"', () => {
		const { getByText } = render(<App />)
		const helloWorldElement = getByText('Hello World')
		expect(helloWorldElement).toBeInTheDocument()
	})
})
