from loguru import logger
from transformers import T5ForConditionalGeneration, T5Tokenizer

from scripts.constants import max_input_token_length


def select_model():
    """
    The function `select_model()` prompts the user to input the paths of a pre-trained model and
    tokenizer, and returns these paths as a tuple.
    :return: two values: `model_path` and `tokenizer_path`.
    """
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


def load_model(model_path, tokenizer_path, save_model=True):
    """
    The function `load_model` loads a pre-trained model and tokenizer, sends the model to the
    device, and optionally saves the model to the local environment.
    
    :param model_path: The `model_path` parameter is the path to the directory where the pre-trained
    model is saved. This directory should contain the model's configuration file, weights, and other
    necessary files
    :param tokenizer_path: The `tokenizer_path` parameter is the path to the directory where the
    tokenizer files are stored. These files are necessary for tokenizing the input text and preparing it
    for the model
    :param save_model: A boolean flag indicating whether or not to save the loaded model to the local
    environment, defaults to True (optional)
    :return: the `model` and `tokenizer` objects.
    """

    
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
    # Model is sent to device for use
    model = input_model.to(device)  # type: ignore
    logger.success("Instantiated target tokenizer and model")

    if save_model:
        save_model_decision = input(
            'Would you like to save an instance this model to your local environment? Type "yes" or "no".'
        )
        save_model_boolean = save_model_decision.lower() == "yes"

        if save_model_boolean:
            optionally_save_model(model_path, tokenizer_path, tokenizer, input_model)

    return model, tokenizer


def optionally_save_model(model_path, tokenizer_path, tokenizer, input_model):
    """
    The function `optionally_save_model` downloads a tokenizer and a model from specified paths and
    saves them in a local directory.
    
    :param model_path: The `model_path` parameter is the path where the model will be saved. It is a
    string that specifies the location and name of the model file
    :param tokenizer_path: The `tokenizer_path` parameter is the path where the tokenizer is located. It
    is used to download the tokenizer from this path and save it to a local directory
    :param tokenizer: The `tokenizer` parameter is an instance of a tokenizer class. It is used to
    tokenize text data, which is an important step in natural language processing tasks such as text
    classification or language generation. The tokenizer is responsible for breaking down the input text
    into individual tokens or sub-words
    :param input_model: The `input_model` parameter is the model that you want to save. It should be an
    instance of a model class
    """
    logger.info(
        f"Downloading tokenizer from {tokenizer_path}, and model from {model_path}"
    )
    tokenizer.save_pretrained(f"../models/{tokenizer_path.replace('/', '_')}")
    input_model.save_pretrained(f"../models/{model_path.replace('/', '_')}")  # type: ignore
    logger.success("Successfully downloaded target tokenizer and model")
