import asyncio
from loguru import logger

from scripts.file_utils import file_exists, remove_duplicates

default_output_file_path = "../data/raw/consolidated_set.jsonl"


async def process_line(line):
    """
    The `process_line` function takes a line of text, removes double quotes, and returns a formatted
    JSONL string with the <ADD DETAIL> input line.

    :param line: The `line` parameter represents a single line of text that needs to be processed
    :return: a formatted string that represents a JSON object. The "input" field is set to "<ADD
    DETAIL>", and the "output" field is set to the processed line, which is the input line with double
    quotes replaced by single quotes and stripped of leading and trailing whitespace. The string is then
    appended with a newline character.
    """
    try:
        # Remove double quotes for JSONL
        line = line.replace('"', "'").strip()
        return f'{{"input": "<ADD DETAIL>", "output": "{line}"}}\n'
    except Exception as e:
        logger.error(f"Error processing line: {line} ({e})")
        raise


async def process_file(file_path, output_file_path):
    """
    The `process_file` function reads a file, processes each line asynchronously, and appends the
    processed lines to an output file.

    :param file_path: The `file_path` parameter is the path to the input file that you want to process.
    It should be a string representing the file's location on your computer
    :param output_file_path: The `output_file_path` parameter is the path to the file where the
    processed lines will be appended. It is the file that will contain the consolidated output after
    processing all the lines from the input file
    """
    try:
        # Read the input file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Process each line asynchronously
        processed_lines = await asyncio.gather(*[process_line(line) for line in lines])

        # Append to consolidated file
        with open(output_file_path, "a", newline="\n") as file:
            file.writelines(processed_lines)
            file.writelines(processed_lines)

        logger.success(f"File added to consolidation: {file_path}")
    except Exception as e:
        logger.error(f"Error processing file: {file_path} ({e})")
        raise


async def process_files(file_paths, output_file_path):
    """
    The function `process_files` processes a list of file paths asynchronously and writes the output to
    a specified output file path.

    :param file_paths: A list of file paths to be processed. Each file will be processed asynchronously
    :param output_file_path: The output_file_path parameter is a string that represents the path where
    the processed files will be saved
    """
    try:
        file_exists(output_file_path)
        # Process each file asynchronously
        if isinstance(file_paths, list):
            await asyncio.gather(
                *[process_file(file_path, output_file_path) for file_path in file_paths]
            )
        else:
            await asyncio.gather(process_file(file_paths, output_file_path))
    except Exception as e:
        logger.error(f"Error processing file list: {e}")
        raise


async def consolidate_files(file_paths, output_file_path=default_output_file_path):
    """
    The `consolidate_files` function takes a list of file paths and an optional output file path,
    processes the files asynchronously, removes duplicate bullets, and logs the success message with the
    output file path.

    :param file_paths: A list of file paths to the files that need to be consolidated
    :param output_file_path: The `output_file_path` parameter is the path where the consolidated and
    cleaned data will be saved. It is an optional parameter with a default value of
    `default_output_file_path`. If no value is provided for `output_file_path`, the default value will
    be used
    """
    # Consolidate all provided files
    await process_files(file_paths, output_file_path)

    # Remove duplicate bullets
    remove_duplicates(output_file_path)

    logger.success(f"Consolidated, clean data has been output to: {output_file_path}")