import os
from transformers import T5Tokenizer, T5ForConditionalGeneration


from src.models.ForgeModel import Input, Output, Describe
from src.constants.ForgeConstants import (
    MODEL,
    TOKENIZER,
    MAX_INPUT_TOKEN_LENGTH,
    MAX_OUTPUT_TOKEN_LENGTH,
    MIN_INPUT_TOKEN_LENGTH,
    TOP_K,
    TOP_P,
    TEMPERATURE,
    NUM_BEAMS,
)


class ForgeService:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained(
            TOKENIZER,
            model_max_length=MAX_INPUT_TOKEN_LENGTH,
            legacy=False,
        )
        self.model = T5ForConditionalGeneration.from_pretrained(MODEL)

    def generate(self, body: Input):
        """
        The `generate` function takes an input body, encodes it using a tokenizer, and then generates an
        output using a pre-trained model. The output is decoded and returned as a string.

        :param body: The `body` parameter is of type `Input` and represents the input text that you want to
        generate a response for. It contains the `input` attribute, which is the actual input text
        :type body: Input
        :return: The `generate` function returns an instance of the `Output` class. The `output` attribute
        of the `Output` instance contains the generated text, which is the decoded output of the model.
        """
        inputs = self.tokenizer.encode_plus(
            body.input,
            return_tensors="pt",
            truncation=True,
            max_length=MAX_INPUT_TOKEN_LENGTH,
        )

        outputs = self.model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=MAX_OUTPUT_TOKEN_LENGTH,
            num_beams=NUM_BEAMS,
            temperature=TEMPERATURE,
            top_k=TOP_K,
            top_p=TOP_P,
            early_stopping=True,
        )
        return Output(
            output=self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        )

    def describe(self) -> Describe:
        """
        The `describe` function returns the `params` attribute of the object.
        :return: The `describe` method is returning the `params` attribute.
        """
        return Describe(
            MODEL=os.path.basename(MODEL),
            TOKENIZER=TOKENIZER,
            MIN_INPUT_TOKEN_LENGTH=MIN_INPUT_TOKEN_LENGTH,
            MAX_INPUT_TOKEN_LENGTH=MAX_INPUT_TOKEN_LENGTH,
            MAX_OUTPUT_TOKEN_LENGTH=MAX_OUTPUT_TOKEN_LENGTH,
            NUM_BEAMS=NUM_BEAMS,
            TEMPERATURE=TEMPERATURE,
            TOP_K=TOP_K,
            TOP_P=TOP_P,
        )
