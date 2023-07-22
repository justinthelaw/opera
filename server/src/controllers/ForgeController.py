from src.controllers.BaseController import BaseController
from src.services.ForgeService import ForgeService
from src.models.ForgeModel import Input, Output

forge_service = ForgeService()


class ForgeController(BaseController):
    def __init__(self):
        super().__init__()
        self.forge_service = forge_service
        self.register_routes()

    def register_routes(self):
        @self.router.post("/generate", response_model=Output)
        async def generate(body: Input) -> Output:
            return self.forge_service.generate(body)

        @self.router.get("/generate")
        async def describe():
            return self.forge_service.describe()
