from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class Side(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderCreate(BaseModel):
    symbol: str = Field(..., examples=["AAPL"])
    side: Side
    qty: int = Field(..., gt=0)
    limit_price: Optional[float] = Field(None, gt=0)

class OrderOut(OrderCreate):
    id: UUID
    status: str
    created_at: datetime


class OrderStatus:
    pass