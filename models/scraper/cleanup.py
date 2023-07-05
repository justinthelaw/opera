import asyncio
import sys
from loguru import logger
from utils.file_utils import delete_file

output_filepath = "data/training/consolidated-bullets.jsonl"

async def process_line(line):
    try:
        line = line.replace('"', "'").strip()
        processed_line = (
            f'{{"prompt": "<ADD THE FULL-FORM PARAGRAPH>", "completion": "{line}"}}\n'
        )
        return processed_line
    except Exception as e:
        logger.error(f"Error processing line: {line} ({e})")

    return ""


async def process_file(file_path):
    try:
        # Read the input file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Process each line asynchronously
        processed_lines = await asyncio.gather(*[process_line(line) for line in lines])

        # Append to consolidated file
        with open(
            output_filepath, "a", newline="\n"
        ) as file:
            for processed_line in processed_lines:
                file.write(processed_line)

        logger.success(f"Cleanup completed on file: {file_path}")
    except Exception as e:
        logger.error(f"Error processing file: {file_path} ({e})")


async def process_files(file_paths):
    try:
        delete_file(output_filepath)
        # Process each file asynchronously
        await asyncio.gather(*[process_file(file_path) for file_path in file_paths])
    except Exception as e:
        logger.error(f"Error processing file list: {e}")


# Extract the file paths from command-line arguments
file_paths = sys.argv[1:]

# Create an asyncio event loop
loop = asyncio.get_event_loop()

# Run the file processing asynchronously
loop.run_until_complete(process_files(file_paths))

# Close the event loop
loop.close()
