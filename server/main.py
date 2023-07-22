from fastapi import FastAPI
from src.controllers.ForgeController import ForgeController

# Instantiate Fast API
app = FastAPI()


@app.get("/")
def welcome():
    """
    The `welcome` function returns a welcome message for the The Forge API.
    :return: a dictionary with a key "response" and a welcome message as the value
    """
    return {
        "response": "Welcome to the The Forge API! This is the LLM server for the Opera web application."
    }


# Instantiate each controller
forge_routes = ForgeController().get_router()

# Register routes
app.include_router(forge_routes)
