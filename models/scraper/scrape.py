import sys
import signal
from loguru import logger
import asyncio
from utils.crawl import crawl
from utils.file_utils import file_exists, clean_file


# Define a signal handler for Ctrl+C
def signal_handler(signal, frame):
    logger.info("Gracefully shutting down...")
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)


# This is the regex for a standard bullet pattern "-<ACTION>;<IMPACT>--<OUTCOME>"
# The pattern is not all-encompassing, and this hardcoded value needs to be experimented with
# and changed manually for maximum bullet
pattern = r"^-?([\w\W\s]{0,255});?([\w\W\s]{0,255})--([\w\W\s]{0,255})$"


async def bullet_scraper():
    logger.info("Bullet scraper starting up...")

    # Prompt the user to input a base URL and file path
    base_url = sys.argv[1]
    file_path = sys.argv[2]

    if not file_exists(file_path):
        await crawl(base_url, base_url, file_path, pattern)
        clean_file(file_path)

    logger.info(f"Output file now ready for viewing at: '{file_path}'")
    logger.info("Gracefully shutting down Bullet Scraper.")


# Create the event loop and run the bullet scraper
async def main():
    await bullet_scraper()


# Run the main function with the event loop

if __name__ == "__main__":
    asyncio.run(main())
