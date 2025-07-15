from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class OrderCreate(BaseModel):
    reference_id: str = Field(..., min_length=1, description="Unique reference for the order.")
    email: EmailStr
    quantity: int = Field(..., gt=0, description="Quantity must be positive.")
    order_date: str = Field(..., description="Order date in ISO8601 format.")

    @classmethod
    def __get_validators__(cls):
        yield from super().__get_validators__()
        yield cls.validate_date

    @classmethod
    def validate_date(cls, values):
        d = values.get('order_date')
        try:
            datetime.fromisoformat(d)
        except Exception:
            raise ValueError('order_date must be a valid ISO8601 string')
        return values

class OrderOut(OrderCreate):
    pass

class OrderError(BaseModel):
    error_code: str
    message: str
