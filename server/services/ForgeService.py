from transformers import T5TokenizerFast, T5ForConditionalGeneration

from models.ForgeModel import (
    Input,
    Output,
    model,
    max_input_token_length,
)


class ForgeService:
    def __init__(self):
        # Model generation parameter control object
        self.params = {
            # Name of the pre-trained model that will be fine-tuned
            "MODEL": model,
            # Maximum number of tokens from source text that model accepts
            "MAX_SOURCE_TEXT_LENGTH": max_input_token_length,
            # Maximum number of tokens from target text that model generates
            "MAX_TARGET_TEXT_LENGTH": 64,
            # Number of alternative sequences generated at each step
            # More beams improve results, but increase computation
            "NUM_BEAMS": 2,
            # Scales logits before soft-max to control randomness
            # Lower values (~0) make output more deterministic
            "TEMPERATURE": 0.90,
            # Limits generated tokens to top K probabilities
            # Reduces chances of rare word predictions
            "TOP_K": 50,
            # Applies nucleus sampling, limiting token selection to a cumulative probability
            # Creates a balance between randomness and determinism
            "TOP_P": 0.90,
        }
        self.tokenizer = T5TokenizerFast.from_pretrained(
            self.params["MODEL"], model_max_length=max_input_token_length
        )
        self.model = T5ForConditionalGeneration.from_pretrained(self.params["MODEL"])

    def generate(self, body: Input) -> Output:
        inputs = self.tokenizer.encode_plus(
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

    def describe(self):
        return self.params
