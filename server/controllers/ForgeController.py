from fastapi import APIRouter
from services.ForgeService import ForgeService
from models.ForgeModel import Input, Output

forge_router = APIRouter()
forge_service = ForgeService()


@forge_router.post("/generate", response_model=Output)
async def generate(body: Input):
    return forge_service.generate(body)

@forge_router.get("/generate")
async def describe():
    return forge_service.describe()