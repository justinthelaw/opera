import os
from loguru import logger

# Warns for overwriting an existing file, then deletes file
def delete_file(file_path):
    if os.path.exists(file_path):
        logger.warning(f"File '{file_path}' will be overwritten!")
        response = input(f"\n\tOverwrite an existing file at {file_path} (y / n)?  ")
        print()
        if response.upper() == "Y":
            os.remove(file_path)
            logger.warning(f"File '{file_path}' has been deleted!")

    logger.info(f"Printing all matches to file path: {file_path}")

def clean_file(file_path):
    # Read the file and filter out empty lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    # Write the filtered lines back to the file
    with open(file_path, 'w') as file:
        file.write('\n'.join(lines))
