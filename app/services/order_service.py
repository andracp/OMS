from uuid import uuid4, UUID
from datetime import datetime
from typing import Dict, List

from app.schemas.order import OrderCreate, OrderOut

class OrderService:
    def __init__(self):
        self._orders: Dict[UUID, OrderOut] = {}

    def create(self, payload: OrderCreate) -> OrderOut:
        order = OrderOut(
            id=uuid4(),
            symbol=payload.symbol.upper(),
            side=payload.side,
            qty=payload.qty,
            limit_price=payload.limit_price,
            status="NEW",
            created_at=datetime.utcnow(),
        )
        self._orders[order.id] = order
        return order

    def list(self) -> List[OrderOut]:
        return list(self._orders.values())

    def get(self, order_id: UUID) -> OrderOut:
        return self._orders[order_id]

order_service = OrderService()
