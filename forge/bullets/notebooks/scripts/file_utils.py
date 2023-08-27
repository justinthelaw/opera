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


def clean_special_chars(line):
    """
    The function `clean_special_chars` removes special characters from a given string.

    :param line: The `line` parameter is a string that represents a line of text that you want to clean
    by removing special characters
    :return: a modified version of the input line with special characters removed.
    """
    return re.sub(r'["\\/\b\f\n\r\t`]', "", line)


def contains_unprintable_characters(line):
    """
    The function checks if a given string contains any unprintable characters.

    :param line: The `line` parameter is a string that represents a line of text
    :return: a boolean value indicating whether the given line contains any unprintable characters.
    """
    return bool(re.search(r"[^\x20-\x7E]", line))


def clean_file(filepath, pattern):
    """
    The `clean_file` function takes a file path and a pattern as input, reads the file, cleans it by
    removing extraneous new lines, special characters, and leading/ending whitespace, ensures each line
    starts with a bullet character, and writes the cleaned lines back to the file.

    :param filepath: The `filepath` parameter is the path to the file that needs to be cleaned up. It
    should be a string representing the file's location on the file system.
    :param pattern: The `pattern` parameter is a regular expression pattern that is used to match and
    select specific lines in the file for cleaning.
    """
    try:
        logger.info("Cleaning up file...")
        clean_lines = []

        with open(filepath, "r") as file:
            for line in file:
                # Clean the line of special characters, new lines, and strip whitespace
                cleaned_line = clean_special_chars(line).strip()

                # Skip empty lines
                if not cleaned_line or contains_unprintable_characters(line):
                    continue

                # Ensure the line starts with a bullet and space
                if not cleaned_line.startswith("-"):
                    cleaned_line = "- " + cleaned_line
                elif not cleaned_line.startswith("- "):
                    cleaned_line = cleaned_line.replace("-", "- ", 1)

                # Perform stricter selection of bullets to keep
                # Where a character length of 115 is the old standard
                # A character length of 50 is an arbitrary, but reasonable minimum
                if re.match(pattern, cleaned_line) and 50 < len(cleaned_line) <= 115:
                    clean_lines.append(cleaned_line)

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


def load_jsonl_data(filepath):
    """
    The function `load_jsonl_data` loads data from a JSONL file and returns it as a list of JSON objects.

    :param filepath: The filepath parameter is the path to the JSONL file that you want to load the data
    from
    :return: The function `load_jsonl_data` returns a list of dictionaries
    """
    jsonl_array = []

    with open(filepath, "r") as file:
        file_contents = file.readlines()

    for line in file_contents:
        # Each json object is stored as an dict in an array
        data = json.loads(line)
        jsonl_array.append(data)

    return jsonl_array


def load_jsonl_as_dataframe(filepath, prefix):
    """
    The function `load_jsonl_as_dataframe` loads data from a JSONL file and returns it as a Pandas
    DataFrame.

    :param filepath: The filepath parameter is the path to the JSONL file that you want to load the data
    from
    :param prefix: The prefix is a string that will be added to the "input" field of each data item
    :return: The function `load_jsonl_as_dataframe` returns a pandas DataFrame
    """
    # Pandas jsonlines to dataframe method
    data = pandas.read_json(filepath, lines=True)
    data["input"] = prefix + data["input"]

    return data


def append_line_to_file(filepath, line_of_data):
    """
    The function `append_line_to_file` appends a line of data to a file specified by the `filepath`
    parameter.

    :param filepath: The filepath parameter is a string that represents the path to the file where you
    want to append the line of data
    :param line_of_data: The `line_of_data` parameter is a string that represents the line of data that
    you want to append to the file
    """
    try:
        with open(filepath, "a") as file:
            # Check if the data ends with a newline, if not add one
            if not line_of_data.endswith("\n"):
                line_of_data += "\n"
            file.write(line_of_data)
    except Exception as e:
        logger.error(f"Error processing file: {filepath}, on line: {line_of_data}: {e}")
        raise
