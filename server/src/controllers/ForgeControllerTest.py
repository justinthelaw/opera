import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from fastapi import FastAPI

from src.controllers.ForgeController import ForgeController
from src.models.ForgeModel import Input, Output


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
        request = self.client.post("/generate", json=request_object)

        mock_forge_service.generate.assert_called_once_with(Input(input=request_text))

        self.assertEqual(request.status_code, 400)

    @patch("src.controllers.ForgeController.forge_service")
    def test_generate_get(self, mock_forge_service):
        mock_forge_service.describe.return_value = {"description": "test description"}

        self.forge_controller = ForgeController()
        self.app.include_router(self.forge_controller.get_router())

        response = self.client.get("/generate")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"description": "test description"})

        mock_forge_service.describe.assert_called_once()


if __name__ == "__main__":
    unittest.main()
