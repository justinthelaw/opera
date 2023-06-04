import { useEffect } from 'react'

const Favicon = () => {
	useEffect(() => {
		const favicon: Element | null = document.querySelector('link[rel="icon"]')
		if (favicon) favicon.setAttribute('href', 'https://github.com/justinthelaw/smarter-bullets/tree/main/public/favicon.ico')
	}, [])

	return null
}

export default Favicon
