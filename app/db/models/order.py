from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.sql import func

from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)
    symbol = Column(String, index=True)
    side = Column(String)
    qty = Column(Integer)
    order_type = Column(String)
    limit_price = Column(Float, nullable=True)
    status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
