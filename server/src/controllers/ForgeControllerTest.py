import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from fastapi import FastAPI

from src.controllers.ForgeController import ForgeController
from src.utils.generators import generate_random_string
from src.models.ForgeModel import (
    Input,
    Output,
    min_input_token_length,
    max_input_token_length,
)


class ForgeControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = FastAPI()
        self.client = TestClient(self.app)

    @patch("src.controllers.ForgeController.forge_service")
    def test_generate_post(self, mock_forge_service):
        request_text = "hello"
        response_text = "world"
        mock_forge_service.generate.return_value = Output(output=response_text)

        self.forge_controller = ForgeController()
        self.app.include_router(self.forge_controller.get_router())

        request_object = {"input": request_text}
        request = self.client.post("/generate", json=request_object)

        mock_forge_service.generate.assert_called_once_with(Input(input=request_text))

        response_object = {"output": response_text}
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.json(), response_object)

    @patch("src.controllers.ForgeController.forge_service")
    def test_generate_post_min_input(self, mock_forge_service):
        request_text = ""

        self.forge_controller = ForgeController()
        self.app.include_router(self.forge_controller.get_router())

        request_object = {"input": request_text}
        response = self.client.post("/generate", json=request_object)

        expected_error_message = f"The minimum token length is {min_input_token_length}"
        self.assertEqual(response.status_code, 422)
        self.assertTrue(expected_error_message in response.json()["detail"][0]["msg"])

    @patch("src.controllers.ForgeController.forge_service")
    def test_generate_post_max_input(self, mock_forge_service):
        request_text = generate_random_string(1024)

        self.forge_controller = ForgeController()
        self.app.include_router(self.forge_controller.get_router())

        request_object = {"input": request_text}
        response = self.client.post("/generate", json=request_object)

        expected_error_message = f"The maximum token length is {max_input_token_length}"
        self.assertEqual(response.status_code, 422)
        self.assertTrue(expected_error_message in response.json()["detail"][0]["msg"])

    @patch("src.controllers.ForgeController.forge_service")
    def test_generate_get(self, mock_forge_service):
        response_object = {
            "MODEL": "some_model",
            "MAX_SOURCE_TEXT_LENGTH": max_input_token_length,
            "MAX_TARGET_TEXT_LENGTH": 0,
            "NUM_BEAMS": 0,
            "TEMPERATURE": 0.1,
            "TOP_K": 0,
            "TOP_P": 0.1,
        }
        mock_forge_service.describe.return_value = response_object

        self.forge_controller = ForgeController()
        self.app.include_router(self.forge_controller.get_router())

        response = self.client.get("/generate")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), response_object)

        mock_forge_service.describe.assert_called_once()


if __name__ == "__main__":
    unittest.main()
