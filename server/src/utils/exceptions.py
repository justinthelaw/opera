from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import (
    ResponseValidationError,
    ValidationException as FastAPIValidationException,
)
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from main import app


@app.exception_handler(ValidationError)
async def request_validation_exception_handler(_: Request, e: ValidationError):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": e.errors(include_context=True)}),
    )
