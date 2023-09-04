from loguru import logger

from scripts.constants import *


def prompt(model, tokenizer, input_text):
    """
    The `prompt` function takes a model, tokenizer, and input text as input, encodes the input text
    using the tokenizer, and generates a summary using the model. The summary is returned as a decoded
    string.

    :param model: The "model" parameter refers to the pre-trained language model that you are using for
    text generation. It could be a model like GPT-2 or T5
    :param tokenizer: The tokenizer is responsible for converting text into tokens, which are the basic
    units of input for the model. It also handles tasks such as padding and truncation
    :param input_text: The input text is the text that you want to generate a summary for. It can be any
    piece of text, such as an article, a blog post, or a news story
    :return: the generated summary of the input text.
    """
    try:
        # Encode the input text
        encoded_input_text = tokenizer.encode_plus(
            input_text,
            return_tensors="pt",
            truncation=True,
            max_length=max_input_token_length,
        )

        # Generate summary
        summary_ids = model.generate(
            encoded_input_text["input_ids"],
            attention_mask=encoded_input_text["attention_mask"],
            max_length=max_output_token_length,
            num_beams=number_of_beams,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            early_stopping=True,
        )

        return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    except KeyboardInterrupt:
        logger.warning("Received interrupt, stopping script...")
    except Exception as e:
        logger.error(f"An error occurred during generation: {e}")
