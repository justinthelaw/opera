import os
from loguru import logger

# Warns for overwriting an existing file, then deletes file
def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.warning(f"File '{file_path}' already existed and has been deleted")
        logger.info(f"Printing all lines to file path: {file_path}")
    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")

# Cleans extra new lines in file
def clean_file(file_path):
    try:
        logger.info("Cleaning up output file...")
        # Read the file and filter out empty lines
        with open(file_path, "r") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines if line.strip()]

        # Write the filtered lines back to the file
        with open(file_path, "w") as file:
            file.write("\n".join(lines))

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")
