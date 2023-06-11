import React, { useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { FAVICON_URL } from '../client.constants'

const App: React.FC = () => {
	useEffect(() => {
		const faviconElement: Element | null = document.querySelector('link[rel="icon"]')
		if (faviconElement && FAVICON_URL) faviconElement.setAttribute('href', FAVICON_URL)
	}, [])

	return (
		<React.Fragment>
			<Router>
				<Routes>
					<Route path='/' element={<div>Hello World</div>} />
				</Routes>
			</Router>
		</React.Fragment>
	)
}

export default App
