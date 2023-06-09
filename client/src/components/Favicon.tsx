import { useEffect } from 'react'

export interface FaviconProps {
	faviconUrl?: string
}

const Favicon: React.FC<FaviconProps> = (props) => {
	useEffect(() => {
		const faviconElement: Element | null = document.querySelector('link[rel="icon"]')
		if (faviconElement && props.faviconUrl) faviconElement.setAttribute('href', props.faviconUrl)
	}, [props.faviconUrl])

	return null
}

export default Favicon
