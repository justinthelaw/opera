import os
import sys
import signal
import asyncio
from loguru import logger
from utils.crawl import crawl
from utils.file_utils import file_exists


# Define a signal handler for Ctrl+C
def signal_handler(signal, frame):
    logger.info("Gracefully shutting down...")
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)


# This is the regex for a standard bullet pattern "-<ACTION>;<IMPACT>--<OUTCOME>"
# The pattern is not all-encompassing, and this hardcoded value needs to be experimented with
# and changed manually for maximum bullet capture
pattern = r"^-?([\w\W\s]{0,255});?([\w\W\s]{0,255})--([\w\W\s]{0,255})$"


async def bullet_scraper(base_url, file_path):
    logger.info("Bullet scraper starting up...")

    if not file_exists(file_path):
        await crawl(base_url, base_url, file_path, pattern)

    logger.info(f"Output file now ready for viewing at: '{file_path}'")
    logger.info("Gracefully shutting down Bullet Scraper.")


# Run the scraping function with the event loop
if __name__ == "__main__":
    # Prompt the user to input a base URL and file path
    base_url = sys.argv[1]

    filename = base_url[base_url.index("www.") + 4:base_url.index(".com")]
    file_path = f"../data/raw/{filename}.txt"

    print(os.getcwd())

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(bullet_scraper(base_url, file_path))
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt. Gracefully shutting down...")
    finally:
        loop.close()
