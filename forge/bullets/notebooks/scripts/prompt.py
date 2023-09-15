from loguru import logger

from scripts.constants import *
from scripts.file_utils import append_line_to_file, load_jsonl_data
from scripts.model_instantiation import load_model, select_model


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


def data_modification_prompt(
    device, output_filepath, input_filepath, prompt_prefix, stop_at=1500
):
    """
    The function `data_modification_prompt` takes in various parameters such as device, output and input
    file paths, prompt prefix, and stop_at value, and performs data modification by loading a model,
    preprocessing input data, generating output text using the model, and appending the modified data to
    an output file.

    :param device: The `device` parameter specifies the device (e.g., "cpu" or "cuda") on which the
    model will be loaded and run
    :param output_filepath: The `output_filepath` parameter is the file path where the generated data
    will be saved
    :param input_filepath: The `input_filepath` parameter is the file path to the input data file. This
    file contains the data that will be used to generate modified data
    :param prompt_prefix: The `prompt_prefix` parameter is a string that is added as a prefix to each
    input text before generating the output text. It is used to provide context or instructions to the
    model
    :param stop_at: The `stop_at` parameter is an optional parameter that specifies the maximum number
    of lines of data to generate. If this parameter is not provided, the default value is set to 1500,
    defaults to 1500 (optional)
    """

    try:
        model_path, tokenizer_path = select_model()
        model, tokenizer = load_model(
            model_path, tokenizer_path, device, save_model=False
        )

        # Preprocess input
        inputs_array = load_jsonl_data(input_filepath)

        maximum_lines_of_data = stop_at

        for count, input_line in enumerate(inputs_array):
            if count == (maximum_lines_of_data - 1):
                raise InterruptedError()

            input_text = prompt_prefix + input_line["output"]

            output_text = prompt(model, tokenizer, input_text)

            # input_text and output_text insert into data sets
            line_of_data = (
                f'{{"input": "{output_text}", "output": "{input_line["output"]}"}}'
            )
            append_line_to_file(output_filepath, line_of_data)
            logger.success(
                f"Appended {count + 1}/{maximum_lines_of_data}: {line_of_data}"
            )

    except KeyboardInterrupt:
        logger.warning("Received interrupt, stopping script...")
    except InterruptedError:
        logger.success("Data generation complete! Stopping script...")
    except Exception as e:
        logger.error(f"An error occurred during generation: {e.with_traceback}")
