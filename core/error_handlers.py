from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_400_BAD_REQUEST
from schemas.order import OrderError
from fastapi import FastAPI


def add_exception_handlers(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=HTTP_400_BAD_REQUEST,
            content={
                "error_code": "validation_error",
                "message": format_validation_errors(exc.errors())
            }
        )
    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        return JSONResponse(
            status_code=HTTP_400_BAD_REQUEST,
            content={
                "error_code": "value_error",
                "message": str(exc)
            }
        )

def format_validation_errors(errors):
    messages = []
    for error in errors:
        loc = ".".join(str(e) for e in error.get("loc", []))
        msg = error.get("msg", "")
        messages.append(f"{loc}: {msg}")
    return "; ".join(messages)
