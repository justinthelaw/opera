from loguru import logger
import re
import os
import pandas
import json


def file_already_exists(filepath):
    if os.path.exists(filepath):
        logger.warning(f"File '{filepath}' already exists and will be skipped")
        return True
    logger.info(f"Printing all lines to file path: {filepath}")
    return False


def clean_file_content(filepath, pattern):
    try:
        logger.info("Cleaning up file...")
        with open(filepath, "r") as file:
            lines = file.readlines()
            lines = [re.sub(r"\n", "", line.strip()) for line in lines if line.strip()]
            clean_lines = [
                line if line.startswith("-") else "- " + line
                for line in lines
                if re.match(pattern, line) and 50 < len(line) <= 115
            ]

        with open(filepath, "w") as file:
            file.write("\n".join(clean_lines))

        logger.success("File cleaned!")

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")
        raise


def remove_file_contents_duplicates(filepath):
    try:
        logger.info("Cleaning up duplicates...")
        with open(filepath, "r") as file:
            lines = list(set(file.readlines()))

        with open(filepath, "w") as file:
            file.write("".join(lines))

        logger.success("Output file's duplicate bullets removed!")

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")
        raise


def load_jsonl_data(filepath, prefix, isDataFrame):
    if isDataFrame:
        # Read in the JSONL training and validation data set
        data = pandas.read_json(filepath, lines=True)

        # Prepend T5's summarize task keyword to inputs
        data["input"] = prefix + data["input"]

        return data

    else:
        jsonl_array = []

        with open(filepath, "r") as file:
            # Read the contents of the file
            file_contents = file.readlines()

        for line in file_contents:
            # Load json objects
            data = json.loads(line)
            jsonl_array.append(data)

        return jsonl_array
