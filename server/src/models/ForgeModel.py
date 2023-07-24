from pydantic import BaseModel, validator
from transformers import T5TokenizerFast

max_input_token_length = 512
min_input_token_length = 1
model = "google/flan-t5-small"


class Input(BaseModel):
    input: str

    @validator("input")
    def max_token_length(cls, v):
        """
        The `max_token_length` function is a validator in Python that checks if the tokenized length of the
        input exceeds a maximum length and raises a `ValueError` if it does.

        :param cls: The `cls` parameter refers to the class that the `max_token_length` method is defined
        in. In this case, it is a class that contains the `max_token_length` method
        :param v: The parameter `v` represents the input value that is being validated. In this case, it is
        the `input` value that is being passed to the `max_token_length` function
        :return: The variable `v` is being returned.
        """
        tokenizer = T5TokenizerFast.from_pretrained(model)
        tokenized_length = len(tokenizer.tokenize(v))

        if tokenized_length > max_input_token_length:
            max_length_error = f"The maximum token length is {max_input_token_length}"
            raise ValueError(max_length_error)

        if tokenized_length < min_input_token_length:
            min_length_error = f"The minimum token length is {min_input_token_length}"
            raise ValueError(min_length_error)

        return v


class Output(BaseModel):
    output: str


class Describe(BaseModel):
    MODEL: str
    MAX_SOURCE_TEXT_LENGTH: int
    MAX_TARGET_TEXT_LENGTH: int
    NUM_BEAMS: int
    TEMPERATURE: float
    TOP_K: int
    TOP_P: float
