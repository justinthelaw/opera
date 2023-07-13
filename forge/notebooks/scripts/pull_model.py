import sys
from loguru import logger


def save_model(model_name, output_path):
    try:
        logger.info("Starting model saving...")

        logger.success(f"Successfully saved model to: {output_path}/{model_name}")

        logger.success(f"Successfully saved model to: {output_path}/{model_name}")
    except Exception as e:
        logger.exception(f"An error occurred during saving the model: {e}")
        logger.exception(f"An error occurred during saving the model: {e}")
        raise


if __name__ == "__main__":
    if len(sys.argv) != 3:
        logger.exception(f"Missing model name or max model length arguments.")
        raise

    model_name = sys.argv[1]
    max_length = int(sys.argv[2])

    output_path = f"../models/{model_name}"

    save_model(model_name, output_path, max_length)
