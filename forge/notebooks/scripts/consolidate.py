import asyncio
import sys
from loguru import logger
from utils.file_utils import file_exists, remove_duplicates

output_filepath = "../data/training/bullet_evaluations.jsonl"


async def process_line(line):
    try:
        # Remove double quotes for JSONL
        line = line.replace('"', "'").strip()
        # Format into JSONL, fine-tuning format
        processed_line = f'{{"summary": "<ADD PROMPT>", "evaluation": "{line}"}}\n'
        return processed_line
    except Exception as e:
        logger.error(f"Error processing line: {line} ({e})")
        raise


async def process_file(file_path):
    try:
        # Read the input file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Process each line asynchronously
        processed_lines = await asyncio.gather(*[process_line(line) for line in lines])

        # Append to consolidated file
        with open(output_filepath, "a", newline="\n") as file:
            file.writelines(processed_lines)

        logger.success(f"File added to consolidation: {file_path}")
    except Exception as e:
        logger.error(f"Error processing file: {file_path} ({e})")
        raise


async def process_files(file_paths):
    try:
        file_exists(output_filepath)
        # Process each file asynchronously
        await asyncio.gather(*[process_file(file_path) for file_path in file_paths])
    except Exception as e:
        logger.error(f"Error processing file list: {e}")
        raise


def consolidate_files(file_paths):
    # Create an asyncio event loop
    loop = asyncio.get_event_loop()

    # Run the file processing asynchronously
    loop.run_until_complete(process_files(file_paths))

    # Close the event loop
    loop.close()

    # Remove duplicate bullets
    remove_duplicates(output_filepath)

    logger.success(f"Consolidated, clean data has been output to: {output_filepath}")


if __name__ == "__main__":
    # Extract the file paths from command-line arguments
    file_paths = sys.argv[1:]

    consolidate_files(file_paths)
