from loguru import logger
from transformers import T5Tokenizer


# Reads in training data and performs tokenization and encoding
async def tokenize_and_encode(data):
    # Preprocess the training data using the T5 tokenizer
    tokenizer = T5Tokenizer.from_pretrained("t5-base", model_max_length=1024)
    prepared_data = await encoder(data, tokenizer)

    if prepared_data == []:
        logger.error(
            f"An error occurred during tokenization and encoding process."
        )
        raise

    return prepared_data


# Tokenization and encoding
async def encoder(training_data, tokenizer):
    prepared_data = []
    try:
        # Define the tokenization parameters
        for line in training_data:
            input_text = line["summary"]
            output_text = line["evaluation"]

            input_ids = tokenizer.encode(
                input_text,
                padding="max_length",
                truncation=True,
                return_tensors="pt",
            )
            output_ids = tokenizer.encode(
                output_text,
                padding="max_length",
                truncation=True,
                return_tensors="pt",
            )

            prepared_data.append({"input_ids": input_ids, "labels": output_ids})

        return prepared_data

    except Exception as e:
        logger.exception(f"A runtime error occurred: {e}")
        raise
