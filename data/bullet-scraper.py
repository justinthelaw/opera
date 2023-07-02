import sys
import signal
from loguru import logger
import asyncio
from crawlers.crawler_level_1 import crawl_level_1
from utils.file_utils import delete_file, clean_file

# Define a signal handler for Ctrl+C
def signal_handler(signal, frame):
    print()
    logger.info("Gracefully shutting down Bullet Scraper Level 1 (Simple HTML)!")
    print()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

async def main():
    logger.info("Welcome to the Bullet Scraper Level 1 (Simple HTML)")

    # Prompt the user to input a base URL and file path
    base_url = input("\n\tEnter the base URL from which to scrape: ")
    file_name = input("\n\tEnter the output file name: ") + ".txt"
    file_path = f"~/raw/{file_name}"
    scraper_level = input("\n\tEnter the complexity of the scraper required (1 / 2 / 3): ")

    # TODO: setup more complex scrapers as necessary
    while scraper_level != "1":
        logger.error(f"Scraper of level {scraper_level} has not been implemented yet.")
        scraper_level = input("\n\tEnter the complexity of the scraper required (1 / 2 / 3): ")
    print()

    # Start crawling and scraping the page
    if scraper_level == "1":
        # Warning for overwriting an existing file
        delete_file(file_path)
        await crawl_level_1(base_url, base_url, file_path)
        

    logger.info("Cleaning up output file...")
    # Clean up potential empty lines
    clean_file(file_path)

    logger.info(f"Matching snippets have been saved to: {file_path}")

# Run the main function asynchronously
if __name__ == '__main__':
    asyncio.run(main())
