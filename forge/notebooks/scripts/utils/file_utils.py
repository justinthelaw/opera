import jsonlines
from loguru import logger
import re
import os


async def jsonl_read(file_path, maximum_lines=0):
    try:
        data = []
        with jsonlines.open(file_path, mode="r") as lines:
            if maximum_lines > 0:
                for line_number, line in enumerate(lines):
                    if line_number >= maximum_lines:
                        break
                    data.append(line)
            else:
                for line in lines:
                    data.append(line)
        return data

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")
        raise


def file_exists(file_path):
    if os.path.exists(file_path):
        logger.warning(f"File '{file_path}' already exists and will be skipped")
        return True
    logger.info(f"Printing all lines to file path: {file_path}")
    return False


def clean_file(file_path, pattern):
    try:
        logger.info("Cleaning up file...")
        with open(file_path, "r") as file:
            lines = file.readlines()
            lines = [re.sub(r"\n", "", line.strip()) for line in lines if line.strip()]
            clean_lines = [
                "- " + line if not line.startswith("-") else line
                for line in lines
                if re.match(pattern, line) and 50 < len(line) <= 115
            ]

        with open(file_path, "w") as file:
            file.write("\n".join(clean_lines))

        logger.success("File cleaned!")

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")
        raise


def remove_duplicates(file_path):
    try:
        logger.info("Cleaning up duplicates...")
        with open(file_path, "r") as file:
            lines = list(set(file.readlines()))

        with open(file_path, "w") as file:
            file.write("".join(lines))

        logger.success("Output file's duplicate bullets removed!")

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")
        raise
