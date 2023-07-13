import sys
from loguru import logger
from consolidate import consolidate_files


def consolidate_one_file(file_path, output_file_path):
    # Run consolidate_files on 1 file and add output path
    consolidate_files(file_path, output_file_path)

    logger.success(f"Consolidated, clean data has been output to: {output_file_path}")


if __name__ == "__main__":
    # Extract the file paths from command-line arguments
    file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    consolidate_one_file(file_path, output_file_path)
