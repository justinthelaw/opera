from abc import ABC, abstractmethod
from fastapi import APIRouter


class BaseController(ABC):
    def __init__(self):
        self.router = APIRouter()

    @abstractmethod
    def register_routes(self):
        pass

    def get_router(self):
        return self.router
