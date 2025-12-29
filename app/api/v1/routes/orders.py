from fastapi import APIRouter, HTTPException, status
from typing import List

from app.schemas.order import OrderCreate, OrderOut
from app.services.order_store import store

router = APIRouter()

@router.post("/", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
async def create_order(payload: OrderCreate):
    if payload.order_type == "LIMIT" and payload.limit_price is None:
        raise HTTPException(
            status_code=400,
            detail="limit_price is required for LIMIT orders"
        )

    return store.create(payload)


@router.get("/", response_model=List[OrderOut])
def list_orders():
    return store.list()

@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: str):
    order = store.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.post("/{order_id}/cancel", response_model=OrderOut)
def cancel_order(order_id: str):
    order = store.cancel(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
