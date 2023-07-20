from pydantic import BaseModel, validator
from transformers import T5TokenizerFast

max_input_token_length = 1024
model = "google/flan-t5-small"


class Input(BaseModel):
    input: str

    @validator("input")
    def max_token_length(cls, v):
        max_length = max_input_token_length
        tokenizer = T5TokenizerFast.from_pretrained(
            model, model_max_length=max_input_token_length
        )
        tokenized_length = len(tokenizer.tokenize(v))

        if tokenized_length > max_length:
            raise ValueError(f"The maximum token length is {max_length}")

        return v


class Output(BaseModel):
    output: str
