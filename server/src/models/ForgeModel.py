from pydantic import BaseModel, validator
from transformers import T5Tokenizer

from src.constants.ForgeConstants import (
    MAX_INPUT_TOKEN_LENGTH,
    MIN_INPUT_TOKEN_LENGTH,
    TOKENIZER,
)


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
        tokenizer = T5Tokenizer.from_pretrained(
            TOKENIZER,
            legacy=False,
        )
        tokenized_length = len(tokenizer.tokenize(v))

        if tokenized_length > MAX_INPUT_TOKEN_LENGTH:
            max_length_error = f"The maximum token length is {MAX_INPUT_TOKEN_LENGTH}"
            raise ValueError(max_length_error)

        if tokenized_length < MIN_INPUT_TOKEN_LENGTH:
            min_length_error = f"The minimum token length is {MIN_INPUT_TOKEN_LENGTH}"
            raise ValueError(min_length_error)

        return v


class Output(BaseModel):
    output: str


class Describe(BaseModel):
    MODEL: str
    TOKENIZER: str
    MIN_INPUT_TOKEN_LENGTH: int
    MAX_INPUT_TOKEN_LENGTH: int
    MAX_OUTPUT_TOKEN_LENGTH: int
    NUM_BEAMS: int
    TEMPERATURE: float
    TOP_K: int
    TOP_P: float
