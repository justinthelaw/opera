import torch
from loguru import logger
from transformers import T5ForConditionalGeneration, T5Tokenizer

from scripts.constants import max_input_token_length


def select_model():
    # Path of the pre-trained model that will be used
    model_path = input(
        "Input a checkpoint model's Hugging Face repository or a relative path"
    )
    # Path of the pre-trained model tokenizer that will be used
    # Must match the model checkpoint's signature
    tokenizer_path = input(
        "Input a tokenizer's Hugging Face repository or a relative path"
    )

    return model_path, tokenizer_path


def load_model(model_path, tokenizer_path):
    # Load the pre-trained model and tokenizer
    logger.info(
        f"Instantiating tokenizer from {tokenizer_path}, and model from {model_path}"
    )
    tokenizer = T5Tokenizer.from_pretrained(
        f"{tokenizer_path}",
        model_max_length=max_input_token_length,
        add_special_tokens=False,
    )
    input_model = T5ForConditionalGeneration.from_pretrained(f"{model_path}")
    logger.info(f"Loading {model_path}...")
    # Set device to be used based on GPU availability
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # Model is sent to device for use
    model = input_model.to(device)  # type: ignore
    logger.success("Instantiated target tokenizer and model")

    save_model_decision = input(
        'Would you like to save an instance this model to your local environment? Type "yes" or "no".'
    )
    save_model_boolean = save_model_decision.lower() == "yes"

    if save_model_boolean:
        optionally_save_model(model_path, tokenizer_path, tokenizer, input_model)

    return model, tokenizer


def optionally_save_model(model_path, tokenizer_path, tokenizer, input_model):
    logger.info(
        f"Downloading tokenizer from {tokenizer_path}, and model from {model_path}"
    )
    tokenizer.save_pretrained(f"../models/{tokenizer_path.replace('/', '_')}")
    input_model.save_pretrained(f"../models/{model_path.replace('/', '_')}")  # type: ignore
    logger.success("Successfully downloaded target tokenizer and model")
