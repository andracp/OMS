from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class OrderStatus(str, Enum):
    NEW = "NEW"
    CANCELED = "CANCELED"
    FILLED = "FILLED"


class OrderCreate(BaseModel):
    symbol: str
    side: str              # BUY / SELL
    qty: int
    order_type: str        # MARKET / LIMIT
    limit_price: Optional[float] = None


class OrderOut(OrderCreate):
    id: str
    status: OrderStatus
    created_at: datetime
