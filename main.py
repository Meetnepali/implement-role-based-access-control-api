from fastapi import FastAPI
from core.error_handlers import add_exception_handlers
from routers import orders

app = FastAPI()

app.include_router(orders.router, prefix="/orders", tags=["orders"])
add_exception_handlers(app)
