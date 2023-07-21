from fastapi import FastAPI
from controllers.ForgeController import forge_router

# from ServeModel import ServeModel

app = FastAPI()


@app.get("/")
def welcome():
    return {
        "response": "Welcome to the Bullet Forge API! This is the LLM server for the Smarter Bullets web application."
    }

app.include_router(forge_router)