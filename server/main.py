from fastapi import FastAPI
from controllers.ForgeController import ForgeController

# Instantiate Fast API
app = FastAPI()


@app.get("/")
def welcome():
    """
    The `welcome` function returns a welcome message for the Bullet Forge API.
    :return: a dictionary with a key "response" and a welcome message as the value
    """
    return {
        "response": "Welcome to the Bullet Forge API! This is the LLM server for the Smarter Bullets web application."
    }


# Instantiate each controller
forge_routes = ForgeController().get_router()

# Register routes
app.include_router(forge_routes)
