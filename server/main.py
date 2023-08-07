from fastapi import FastAPI
from transformers import logging
from dotenv import load_dotenv
from uvicorn import run
import os

from src.controllers.ForgeController import ForgeController

app = FastAPI()

logging.set_verbosity_error()

load_dotenv("../config/.env.local")

host = os.getenv("SERVER_HOST")
port = int(os.getenv("SERVER_PORT"))


@app.get("/")
def welcome():
    """
    The `welcome` function returns a welcome message for the The Forge API.
    :return: a dictionary with a key "response" and a welcome message as the value
    """
    return {
        "response": "Welcome to the The Forge API! This is the LLM server for the Opera web application."
    }


forge_routes = ForgeController().get_router()

app.include_router(forge_routes)

run("main:app", host=host, port=port)