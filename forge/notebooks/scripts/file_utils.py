from loguru import logger
import re
import os
import pandas
import json


def file_exists(filepath):
    """
    The function checks if a file exists and logs a warning message if it does, otherwise it logs an
    info message.
    
    :param filepath: The parameter `filepath` is a string that represents the path to a file
    :return: The function `file_exists` returns a boolean value. If the file specified by the `filepath`
    parameter already exists, the function returns `True`. Otherwise, it returns `False`.
    """
    if os.path.exists(filepath):
        logger.warning(f"File '{filepath}' already exists and will be skipped")
        return True
    logger.info(f"Printing all lines to file path: {filepath}")
    return False


def batch_clean_files(base_directory_path, bullet_pattern):
    """
    The function `batch_clean_files` performs extra cleaning on raw text files in a given directory
    using a specified bullet pattern.
    
    :param base_directory_path: The base_directory_path is the path to the directory where the raw
    data files are located
    :param bullet_pattern: The `bullet_pattern` parameter is a regular expression pattern that is used
    to identify and remove bullet points from the text files. It is used in the `clean_file` function to
    perform the cleaning operation
    """
    file_paths = [
        os.path.join(root, file)
        for root, _, files in os.walk(base_directory_path)
        for file in files
    ]

    for dirty_file_path in file_paths:
        logger.info(f"Performing extra cleaning on file: {dirty_file_path}")
        clean_file(dirty_file_path, bullet_pattern)
        logger.success("Extra cleaning on file complete!")


def clean_file(filepath, pattern):
    """
    The `clean_file` function takes a file path and a pattern as input, reads the file, cleans it by
    removing extraneous new lines and leading/ending whitespace, ensures each line starts with a bullet
    character, and writes the cleaned lines back to the file.
    
    :param filepath: The `filepath` parameter is the path to the file that needs to be cleaned up. It
    should be a string representing the file's location on the file system
    :param pattern: The `pattern` parameter is a regular expression pattern that is used to match and
    select specific lines in the file for cleaning
    """
    try:
        logger.info("Cleaning up file...")
        with open(filepath, "r") as file:
            lines = file.readlines()
            # Clean file of all extraneous new lines and leading/ending whitespace
            lines = [re.sub(r"\n", "", line.strip()) for line in lines if line.strip()]
            clean_lines = [
                # Ensure for bullet beginning character is in each line
                line if line.startswith("-") else "- " + line
                for line in lines
                # Perform stricter selection of bullets to keep
                # Where a character length of 115 is the old myEval standard
                # A character length of 50 is an arbitrary, but reasonable minimum
                if re.match(pattern, line) and 50 < len(line) <= 115
            ]

        with open(filepath, "w") as file:
            file.write("\n".join(clean_lines))

        logger.success("File cleaned!")

    except Exception as e:
        logger.error(f"A runtime error occurred: {e}")
        raise


def remove_duplicates(filepath):
    """
    The function removes duplicate data from a file.
    
    :param filepath: The `filepath` parameter is a string that represents the path to the file that you
    want to remove duplicate bullets from
    """
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
    """
    The function `load_jsonl_data` loads data from a JSONL file and either returns it as a Pandas
    DataFrame with a modified "input" column or as a list of JSON objects.
    
    :param filepath: The filepath parameter is the path to the JSONL file that you want to load the data
    from
    :param prefix: The prefix is a string that will be added to the "input" field of each data item
    :param isDataFrame: The `isDataFrame` parameter is a boolean value that determines whether the data
    should be loaded into a pandas DataFrame or as a list of JSON objects. If `isDataFrame` is set to
    `True`, the data will be loaded into a DataFrame. If `isDataFrame` is set to `False
    :return: The function `load_jsonl_data` returns either a pandas DataFrame or a list of dictionaries
    (json objects) depending on the value of the `isDataFrame` parameter.
    """
    # Decision point for data frame or json array storage
    if isDataFrame:
        # Pandas jsonlines to dataframe method
        data = pandas.read_json(filepath, lines=True)
        data["input"] = prefix + data["input"]

        return data

    else:
        jsonl_array = []

        with open(filepath, "r") as file:
            file_contents = file.readlines()

        for line in file_contents:
            # Each json object is stored as an dict in an array
            data = json.loads(line)
            jsonl_array.append(data)

        return jsonl_array
