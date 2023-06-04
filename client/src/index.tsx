import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Favicon from './components/Favicon'
import { FAVICON_URL } from './constants/client.constants'

export const App: React.FC = () => {
	return (
		<React.Fragment>
			<Favicon faviconUrl={FAVICON_URL || ''} />
			<Router>
				<Routes>
					<Route path='/' element={<div>Hello World</div>} />
				</Routes>
			</Router>
		</React.Fragment>
	)
}

const container = document.getElementById('root') as HTMLElement
const root = createRoot(container)
root.render(<App />)
