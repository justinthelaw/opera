import sys
from loguru import logger
from utils.file_utils import extra_clean_file
from scrape import pattern

def main():
    # Extract the file path
    file_path = sys.argv[1]

    logger.info(f"Performing extra cleaning on file: {file_path}")

    # Perform extra cleaning
    extra_clean_file(file_path, pattern)

    logger.success(f"Extra cleaning on file complete!")


if __name__ == "__main__":
    main()