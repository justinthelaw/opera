from loguru import logger
import torch

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


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def data_modification_prompt(
    output_filepath,
    input_filepath,
    prompt_prefix,
    modify_input=False,
    stop_at=1500,
):
    """
    The `data_modification_prompt` function takes an input file, modifies the input or output of each
    JSON line based on a prompt prefix, and appends the modified data to an output file.

    :param output_filepath: The `output_filepath` parameter is the file path where the modified data
    will be saved. It should be a string representing the file path, including the file name and
    extension
    :param input_filepath: The `input_filepath` parameter is the file path to the input data file. This
    file contains the data that will be used as input for the data modification process
    :param prompt_prefix: The `prompt_prefix` parameter is a list of strings that will be prepended to
    the input text before generating the output. It is used to provide context or instructions to the
    model
    :param modify_input: The `modify_input` parameter is a boolean flag that determines whether the
    input or output of each JSON line should be modified. If `modify_input` is set to `True`, the input
    text will be modified. If `modify_input` is set to `False`, the output text will be modified,
    defaults to False (optional)
    :param stop_at: The `stop_at` parameter is used to specify the maximum number of lines of data to
    process. Once this limit is reached, the script will stop generating data and exit, defaults to 1500
    (optional)
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

            # Decision point to modify the input or output of the JSON line
            input_text = prompt_prefix + (
                input_line["input"] if modify_input else input_line["output"]
            )

            output_text = prompt(model, tokenizer, input_text).replace('"', "'").strip()

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
        logger.error(f"An error occurred during generation: {e}")
