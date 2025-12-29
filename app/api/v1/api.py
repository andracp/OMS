from fastapi import APIRouter
from app.api.v1.routes import health, orders, executions

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(executions.router, prefix="/executions", tags=["executions"])
