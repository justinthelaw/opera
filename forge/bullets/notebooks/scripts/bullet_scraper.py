import asyncio
import httpx
import re
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from loguru import logger

from scripts.file_utils import file_exists
from scripts.constants import bullet_pattern

# Track visited URLs to avoid duplicates
visited_urls = set()


def has_base_url(base_url, url):
    """
    The function `has_base_url` checks if a given URL has the same base URL as another given base URL.

    :param base_url: The `base_url` parameter is a string that represents the base URL that you want to
    compare against
    :param url: The `url` parameter is a string representing a URL. It can be any valid URL, such as
    "https://www.example.com/page1" or "http://localhost:8000/page2"
    :return: a boolean value indicating whether the netloc (domain) of the given URL matches the netloc
    of the given base URL.
    """
    parsed_base_url = urlparse(base_url)
    parsed_url = urlparse(url)

    return parsed_url.netloc == parsed_base_url.netloc


async def crawl(base_url, url, filepath, pattern):
    """
    The `crawl` function is an asynchronous web crawler that fetches web page content, extracts relevant
    portions based on a given pattern, and recursively crawls all links on the page.

    :param base_url: The `base_url` parameter is the base URL of the website you want to crawl. It is
    used to check if a URL is within the scope of the website or not. URLs that are not within the scope
    will be skipped
    :param url: The `url` parameter represents the URL of the web page that you want to crawl and scrape
    for relevant content
    :param filepath: The `filepath` parameter is the path to the file where the matching snippets will
    be written. It should be a string representing the file path, including the file name and extension.
    For example, `"output.txt"` or `"data/output.txt"`
    :param pattern: The `pattern` parameter is a regular expression pattern used to match and extract
    relevant content from the HTML page. It is used in the line `relevant_content =
    soup.find_all(string=re.compile(pattern))` to find all strings in the parsed HTML that match the
    given pattern
    :return: The function `crawl` returns `None`.
    """
    if not has_base_url(base_url, url):
        logger.warning(f"Skipping out-of-scope URL: {url}")
        return

    try:
        async with httpx.AsyncClient() as client:
            # Send an async GET request to fetch the web page content
            response = await client.get(
                url, headers={"User-Agent": "Mozilla/5.0"}, timeout=60
            )
            response.raise_for_status()
            page_content = response.text

        # Create BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(page_content, "html5lib")

        # Extract the relevant portions from the parsed HTML
        relevant_content = soup.find_all(string=re.compile(pattern))

        # Write the matching snippets to a text file
        with open(filepath, "a", encoding="utf-8") as file:
            for content in relevant_content:
                file.write(content + "\n")

        logger.success(f"Scraped Page: {url}")

        # Find all links on the page and crawl them recursively
        tasks = []
        for link in soup.find_all("a", href=True):
            absolute_link = urljoin(url, link["href"])
            if absolute_link not in visited_urls:
                visited_urls.add(absolute_link)
                tasks.append(crawl(base_url, absolute_link, filepath, pattern))

        # Run the crawl tasks concurrently
        await asyncio.gather(*tasks)

    except httpx.RequestError as e:
        logger.error("An error occurred while sending the HTTP request.")
    except httpx.HTTPStatusError as e:
        logger.error(
            f"Received HTTP status code {e.response.status_code} for URL: {url}"
        )
    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")


async def bullet_scraper(base_url):
    """
    The `bullet_scraper` function is an asynchronous function that scrapes bullet points from a website
    and saves them to a file.

    :param base_url: The base URL is the starting point for the web scraping process. It is the URL from
    which the scraper will begin crawling and extracting information
    :param filepath: The `filepath` parameter is the path where the output file will be saved. It
    specifies the location and name of the file
    """
    logger.info("Bullet scraper starting up...")

    filename = base_url[base_url.index("www.") + 4 : base_url.index(".com")]
    filepath = f"../data/raw/{filename}.txt"

    if not file_exists(filepath):
        await crawl(base_url, base_url, filepath, bullet_pattern)

    logger.info(f"Output file now ready for viewing at: '{filepath}'")
    logger.info("Gracefully shutting down Bullet Scraper.")
