import os
from transformers import T5Tokenizer, T5ForConditionalGeneration


from src.models.ForgeModel import (
    Input,
    Output,
    Describe,
    model,
    tokenizer,
    max_input_token_length,
)


class ForgeService:
    def __init__(self):
        # Model generation parameter control object
        self.params = {
            # Name of the pre-trained model that will be fine-tuned
            "MODEL": model,
            # Name of the base model's tokenizer
            "TOKENIZER": tokenizer,
            # Maximum number of tokens from source text that model accepts
            "MAX_SOURCE_TEXT_LENGTH": max_input_token_length,
            # Maximum number of tokens from target text that model generates
            "MAX_TARGET_TEXT_LENGTH": 64,
            # Number of alternative sequences generated at each step
            # More beams improve results, but increase computation
            "NUM_BEAMS": 2,
            # Scales logits before soft-max to control randomness
            # Lower values (~0) make output more deterministic
            "TEMPERATURE": 0.9,
            # Limits generated tokens to top K probabilities
            # Reduces chances of rare word predictions
            "TOP_K": 20,
            # Applies nucleus sampling, limiting token selection to a cumulative probability
            # Creates a balance between randomness and determinism
            "TOP_P": 0.10,
        }
        self.tokenizer = T5Tokenizer.from_pretrained(
            self.params["TOKENIZER"],
            model_max_length=max_input_token_length,
            legacy=False,
        )
        self.model = T5ForConditionalGeneration.from_pretrained(self.params["MODEL"])

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
        inputs = self.tokenizer.encode(
            body.input,
            return_tensors="pt",
            truncation=True,
            max_length=self.params["MAX_SOURCE_TEXT_LENGTH"],
        )

        outputs = self.model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=self.params["MAX_TARGET_TEXT_LENGTH"],
            num_beams=self.params["NUM_BEAMS"],
            temperature=self.params["TEMPERATURE"],
            top_k=self.params["TOP_K"],
            top_p=self.params["TOP_P"],
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
            MODEL=os.path.basename(self.params["MODEL"]),
            TOKENIZER=self.params["TOKENIZER"],
            MAX_SOURCE_TEXT_LENGTH=self.params["MAX_SOURCE_TEXT_LENGTH"],
            MAX_TARGET_TEXT_LENGTH=self.params["MAX_TARGET_TEXT_LENGTH"],
            NUM_BEAMS=self.params["NUM_BEAMS"],
            TEMPERATURE=self.params["TEMPERATURE"],
            TOP_K=self.params["TOP_K"],
            TOP_P=self.params["TOP_P"],
        )
