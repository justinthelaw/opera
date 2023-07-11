import sys
from transformers import T5ForConditionalGeneration, T5Tokenizer
from loguru import logger


def save_t5_model(model_name, output_path, max_length):
    try:
        logger.info("Starting T5 model saving...")

        # Load the T5 model and tokenizer
        model = T5ForConditionalGeneration.from_pretrained(model_name)
        tokenizer = T5Tokenizer.from_pretrained(model_name, model_max_length=max_length)

        # Save the model and tokenizer to the output directory
        model.save_pretrained(output_path)
        tokenizer.save_pretrained(output_path)

        logger.success(f"Successfully saved T5 model to: {output_path}/{model_name}")
    except Exception as e:
        logger.exception(f"An error occurred during saving the T5 model: {e}")
        raise


if __name__ == "__main__":
    if len(sys.argv) != 3:
        logger.exception(f"Missing model name or max model length arguments.")
        raise

    model_name = sys.argv[1]
    max_length = int(sys.argv[2])

    output_path = "../models/t5/base"

    save_t5_model(model_name, output_path, max_length)
