import os
from loguru import logger
import re


# Warns for overwriting an existing file that already exists
def file_exists(file_path):
    try:
        if os.path.exists(file_path):
            logger.warning(f"File '{file_path}' already existed and will be skipped")
            return True
        logger.info(f"Printing all lines to file path: {file_path}")
    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")

    logger.info(f"Printing all lines to file path: {file_path}")
    return False


# Cleans extra spacing in the file
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

        logger.success("Output file cleaned!")

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")


# Provides extra cleaning steps
def extra_clean_file(file_path, pattern):
    clean_lines = []
    try:
        logger.info("Cleaning up output file...")
        # Read the file and filter out empty lines
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                # remove all empty lines and newline characters
                line = line.strip()
                line = line.replace("\n", "")
                # add the dash to bullets missing it
                if not line.startswith("-"):
                    line = "- " + line
                # re-use the pattern with line length check
                # 115 chars is a myEval 1.0 standard, and it is highly unlikely
                # that a compliant / good bullet is less than <50 or >115 chars
                if re.match(pattern, line) and 50 < len(line) <= 115:
                    clean_lines.append(line)

        # Write the filtered lines back to the file
        with open(file_path, "w") as file:
            file.write("\n".join(clean_lines))

        logger.success("Output file cleaned!")

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")


# Removes duplicate bullets
def remove_duplicates(file_path):
    try:
        logger.info("Cleaning up duplicates...")
        with open(file_path, "r") as file:
            lines = file.readlines()
            lines = list(set(lines))

        # Write the filtered lines back to the file
        with open(file_path, "w") as file:
            file.write("".join(lines))

        logger.success("Output file's duplicate bullets removed!")

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")
