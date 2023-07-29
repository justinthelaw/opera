from constants import BaseController, ForgeService, Input, Output, Describe

forge_service = ForgeService()


class ForgeController(BaseController):
    def __init__(self):
        super().__init__()
        self.forge_service = forge_service
        self.register_routes()

    def register_routes(self):
        """
        The `register_routes` function registers a POST route `/generate` that takes an `Input` object as
        the request body and returns an `Output` object.
        :return: The `generate` function is returning the result of the `self.forge_service.generate(body)`
        method call.
        """

        @self.router.post("/generate", response_model=Output)
        async def generate(body: Input) -> Output:
            """
            The function `generate` is a POST endpoint that takes an `Input` object as input and returns
            an `Output` object.

            :param body: The "body" parameter is of type "Input". It represents the input data that is
            sent to the "/generate" endpoint
            :type body: Input
            :return: The `generate` function is returning an instance of the `Output` model.
            """
            return self.forge_service.generate(body)

        @self.router.get("/generate")
        async def describe() -> Describe:
            """
            The function `describe()` returns the description of a service.
            :return: The `describe()` method of the `forge_service` object is being called and its return value
            is being returned.
            """
            return self.forge_service.describe()
