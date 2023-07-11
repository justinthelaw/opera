from transformers import T5ForConditionalGeneration, T5Tokenizer
from loguru import logger


def pull_t5_base(model_name, output_path):
    try:
        # Load the T5 model and tokenizer
        model = T5ForConditionalGeneration.from_pretrained(model_name)
        tokenizer = T5Tokenizer.from_pretrained(model_name)

        # Save the model and tokenizer to the output directory
        model.save_pretrained(output_path)
        tokenizer.save_pretrained(output_path)
        
    except Exception as e:
        logger.exception(f"An error occurred during saving the T5 model: {str(e)}")
        raise


if __name__ == "__main__":
    try:
        logger.info("Starting T5 model saving...")

        model_name = "t5-base"
        output_path = "forge/models/t5/base"
        pull_t5_base(model_name, output_path)

        logger.success(f"Successfully saved T5 model to: {output_path}/{model_name}")
    except Exception as e:
        logger.exception(f"A runtime error occurred: {e}")
        raise
