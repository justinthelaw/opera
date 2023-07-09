import sys
from loguru import logger
from .utils.file_utils import clean_file
from scrape import pattern

if __name__ == "__main__":
    # Extract the file path
    file_path = sys.argv[1]

    logger.info(f"Performing extra cleaning on file: {file_path}")

    # Perform extra cleaning
    clean_file(file_path, pattern)

    logger.success(f"Extra cleaning on file complete!")