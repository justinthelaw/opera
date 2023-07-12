from loguru import logger
from scripts.utils.file_utils import jsonl_read


# Reads in training data and performs tokenization and encoding
async def tokenize_and_encode(training_file, max_size, tokenizer):
    training_file_path = f"../data/training/{training_file}"
    data = await jsonl_read(training_file_path, max_size)
    if not data:
        logger.error(
            f"An error occurred during the reading of JSONL file: {training_file_path}"
        )
        raise ValueError("No training data available.")
    
    prepared_data = await encoder(data, tokenizer)

    # Ensure data has been processed
    # If yes, log some metadata and warnings for the user
    if not prepared_data:
        logger.error("An error occurred during tokenization and encoding process.")
        raise

    logger.info(f"Sample of the tokenized and encoded data: {prepared_data[0]}")
    logger.info(f"Total count of tokenized and encoded data: {len(prepared_data)}")
    logger.success("The data has been tokenized and encoded into memory!")
    logger.warning(
        "This tokenized and encoded data is only temporarily stored in the Jupyter Notebook instance."
    )
    logger.warning(
        "Failing to save the data to file will result in loss during restart or clearing of outputs."
    )

    return prepared_data


# Tokenization and encoding
async def encoder(training_data, tokenizer):
    prepared_data = []
    try:
        for line in training_data:
            input_text = line.get("summary", "")
            output_text = line.get("evaluation", "")

            input_ids = tokenizer.encode(
                input_text,
                padding="max_length",
                truncation=True,
                return_tensors="pt",
            ).squeeze()
            output_ids = tokenizer.encode(
                output_text,
                padding="max_length",
                truncation=True,
                return_tensors="pt",
            ).squeeze()

            input_ids_tensor = input_ids.clone().detach()
            labels_tensor = output_ids.clone().detach()

            prepared_data.append(
                {"input_ids": input_ids_tensor, "labels": labels_tensor}
            )

        return prepared_data

    except Exception as e:
        logger.exception(f"A runtime error occurred: {e}")
        raise
