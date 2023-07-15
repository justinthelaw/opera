import sys
from loguru import logger

from files import clean_file_content
from bullet_patterns import BULLET_PATTERN

if __name__ == "__main__":
    # Extract the file path
    file_path = sys.argv[1]

    dirty_file_path = f"../data/raw/{file_path}"

    logger.info(f"Performing extra cleaning on file: {dirty_file_path}")

    # Perform extra cleaning
    clean_file_content(dirty_file_path, BULLET_PATTERN)

    logger.success(f"Extra cleaning on file complete!")