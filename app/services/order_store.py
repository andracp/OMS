from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional
from uuid import uuid4

from app.schemas.order import OrderCreate, OrderOut, OrderStatus


@dataclass
class OrderStore:
    _orders: Dict[str, OrderOut] = field(default_factory=dict)

    def create(self, payload: OrderCreate) -> OrderOut:
        oid = str(uuid4())
        order = OrderOut(
            id=oid,
            symbol=payload.symbol,
            side=payload.side,
            qty=payload.qty,
            order_type=payload.order_type,
            limit_price=payload.limit_price,
            status=OrderStatus.NEW,
            created_at=datetime.utcnow(),
        )
        self._orders[oid] = order
        return order

    def get(self, order_id: str) -> Optional[OrderOut]:
        return self._orders.get(order_id)

    def list(self) -> List[OrderOut]:
        return list(self._orders.values())

    def cancel(self, order_id: str) -> Optional[OrderOut]:
        order = self._orders.get(order_id)
        if not order:
            return None
        # basic rule: don’t cancel filled
        if order.status == OrderStatus.FILLED:
            return order
        updated = order.model_copy(update={"status": OrderStatus.CANCELED})
        self._orders[order_id] = updated
        return updated


store = OrderStore()
