from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
from schemas.order import OrderCreate, OrderOut, OrderError
from typing import List

router = APIRouter()

_orders_db = []  # In-memory order storage
_reference_ids = set()

@router.post("/", response_model=OrderOut, responses={400: {"model": OrderError}}, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate):
    if order.reference_id in _reference_ids:
        return JSONResponse(status_code=400, content={
            "error_code": "reference_id_exists",
            "message": "Order with this reference_id already exists."
        })
    # Save order
    _orders_db.append(order)
    _reference_ids.add(order.reference_id)
    return order

@router.get("/", response_model=List[OrderOut])
def list_orders():
    return _orders_db
