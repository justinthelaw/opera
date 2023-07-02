import sys
import signal
from loguru import logger
import asyncio
from utils.crawler import crawl
from utils.file_utils import delete_file, clean_file


# Define a signal handler for Ctrl+C
def signal_handler(signal, frame):
    logger.info("Gracefully shutting down Bullet Scraper.")
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)


async def bullet_scraper():
    logger.info("Bullet scraper starting up...")

    # Prompt the user to input a base URL and file path
    base_url = sys.argv[1]
    file_path = sys.argv[2]

    delete_file(file_path)
    await crawl(base_url, base_url, file_path)
    clean_file(file_path)

    logger.info(f"Output file now ready for viewing at: '{file_path}'")
    logger.info("Gracefully shutting down Bullet Scraper.")


asyncio.run(bullet_scraper())
