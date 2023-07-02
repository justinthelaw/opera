import httpx
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from loguru import logger
import asyncio
import random

# Track visited URLs to avoid duplicates
visited_urls = set()

# Crawl and scrape a page based on the bullet regex pattern
async def crawl_level_1(base_url, url, file_path):
    try:
        if not url.startswith(('http://', 'https://')):
            # Resolve relative URLs
            url = urljoin(base_url, url)

        parsed_base_url = urlparse(base_url)
        parsed_url = urlparse(url)

        if parsed_url.netloc != parsed_base_url.netloc:
            return  # Skip URLs outside the base URL

        async with httpx.AsyncClient() as client:
            # Send an async GET request to fetch the web page content
            for i in range(10):  # retry up to 10 times
                try:
                    response = await client.get(url, headers={"User-Agent": "Mozilla/5.0"})
                    break  # if the request is successful, break the loop
                except Exception as e:
                    await asyncio.sleep(2 ** i)  # wait for an exponentially increasing amount of time
            response.raise_for_status()
            page_content = response.text
            await asyncio.sleep(random.uniform(1, 3))  # introduce random delay between requests
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

        # Find all links on the page and crawl them recursively
        for link in soup.find_all('a', href=True):
            absolute_link = urljoin(url, link['href'])
            if absolute_link not in visited_urls:
                visited_urls.add(absolute_link)
                await crawl_level_1(base_url, absolute_link, file_path)
                logger.success(f"\tPage #{len(visited_urls)}: {absolute_link}")

    # Error handling for the entire crawl process
    except httpx.RequestError as e:
        logger.error(f"An error occurred while sending the HTTP request: {e}")
    except httpx.HTTPStatusError as e:
        logger.error(f"Received HTTP status code {e.response.status_code} for URL: {url}")
    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")

