import os
from dotenv import load_dotenv
from uvicorn import run

load_dotenv("../config/.env.local")


host = os.getenv("SERVER_HOST")
port = int(os.getenv("SERVER_PORT"))

run("main:app", host=host, port=port)
