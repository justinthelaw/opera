import torch
import unittest
from unittest.mock import patch

from src.services.ForgeService import ForgeService
from src.models.ForgeModel import Input, Output, Describe


class ForgeServiceTest(unittest.TestCase):
    def setUp(self):
        self.forge_service = ForgeService()
        self.test_input = Input(input="This is a test input")

    @patch("src.services.ForgeService.T5ForConditionalGeneration.from_pretrained")
    @patch("src.services.ForgeService.T5Tokenizer.from_pretrained")
    def test_init(self, mock_tokenizer, mock_model):
        mock_tokenizer.return_value = None
        mock_model.return_value = None
        forge_service = ForgeService()
        self.assertIsNotNone(forge_service)

    @patch("src.services.ForgeService.T5ForConditionalGeneration.generate")
    @patch("src.services.ForgeService.T5Tokenizer.encode")
    def test_generate(self, mock_encode, mock_generate):
        mock_encode.return_value = {"input_ids": [], "attention_mask": []}
        mock_generate.return_value = torch.tensor([[101, 202, 303]])
        output = self.forge_service.generate(self.test_input)
        self.assertIsInstance(output, Output)

    def test_describe(self):
        describe = self.forge_service.describe()
        self.assertIsInstance(describe, Describe)


if __name__ == "__main__":
    unittest.main()
