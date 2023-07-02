import httpx
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from loguru import logger

# Track visited URLs to avoid duplicates
visited_urls = set()

def has_base_url(base_url, url):
    parsed_base_url = urlparse(base_url)
    parsed_url = urlparse(url)

    if parsed_url.netloc != parsed_base_url.netloc:
        # Skip URLs outside the base URL
        return False
    
    return True

# Crawl and scrape a page based on the bullet regex pattern
async def crawl(base_url, url, file_path):
    confirmed_base_url = has_base_url(base_url, url)
    if not confirmed_base_url:
        logger.warning(f"Skipping out-of-scope URL: {url}")
        visited_urls.remove(url)
        return
    try:
        async with httpx.AsyncClient() as client:
            # Send an async GET request to fetch the web page content
            response = await client.get(url, headers={"User-Agent": "Mozilla/5.0"})
            # Raise exception related to response
            response.raise_for_status()
            page_content = response.text

        # Create BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(page_content, 'html.parser')

        # This is the regex for a standard bullet pattern "-<ACTION>;<IMPACT>--<OUTCOME>""
        pattern = r'-\s*([\w\W\s]*?);\s*([\w\W\s]*?)--\s*([\w\W\s]*)'

        # Extract the relevant portions from the parsed HTML
        relevant_content = soup.find_all(string=re.compile(pattern))

        # Write the matching snippets to a text file
        with open(file_path, "a") as file:
            for content in relevant_content:
                file.write(content + "\n")

        logger.success(f"Page #{len(visited_urls)}: {url}")

        # Find all links on the page and crawl them recursively
        for link in soup.find_all('a', href=True):
            absolute_link = urljoin(url, link['href'])
            if absolute_link not in visited_urls:
                visited_urls.add(absolute_link)
                await crawl(base_url, absolute_link, file_path)

    # Error handling for the entire crawl process
    except httpx.RequestError as e:
        logger.error(f"An error occurred while sending the HTTP request: {e}")
    except httpx.HTTPStatusError as e:
        logger.error(f"Received HTTP status code {e.response.status_code} for URL: {url}")
    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")
