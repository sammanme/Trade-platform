# server/app/models.py
from sqlalchemy import Column, Float, DateTime, String

class OHLCV(Base):
    __tablename__ = "ohlcv"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(12), index=True)
    timestamp = Column(DateTime, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    exchange = Column(String(24))