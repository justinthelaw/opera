import os
from uvicorn import run
from dotenv import load_dotenv

load_dotenv("../config/.env.local")


host = os.getenv("SERVER_HOST")
port = int(os.getenv("SERVER_PORT") or 3000)

run("server:app", host=host or "localhost", port=port)
