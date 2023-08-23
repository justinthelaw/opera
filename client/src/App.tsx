import React from 'react'
import { HashRouter, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'

const App: React.FC = () => {
    return (
        <React.Fragment>
            <HashRouter>
                <Routes>
                    <Route path='/' element={<Home />} />
                </Routes>
            </HashRouter>
        </React.Fragment>
    )
}

export default App
