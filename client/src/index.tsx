import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

export const App: React.FC = () => {
	return (
		<Router>
			<Routes>
				<Route path='/' element={<div>Hello World</div>} />
			</Routes>
		</Router>
	)
}

const container = document.getElementById('root') as HTMLElement
const root = createRoot(container)
root.render(<App />)
