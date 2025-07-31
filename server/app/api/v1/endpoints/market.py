# server/app/api/v1/endpoints/market.py
from fastapi import APIRouter
from app.services import data_fetcher, arbitrage

router = APIRouter()

@router.get("/ohlcv/{symbol}")
async def get_ohlcv(symbol: str, timeframe: str):
    return await data_fetcher.fetch_ohlcv(symbol, timeframe)

@router.get("/arbitrage")
async def get_arbitrage(symbol_a: str, symbol_b: str):
    data_a = await data_fetcher.fetch_ohlcv(symbol_a)
    data_b = await data_fetcher.fetch_ohlcv(symbol_b)
    closes_a = [item['close'] for item in data_a]
    closes_b = [item['close'] for item in data_b]
    return arbitrage.calculate_arbitrage(closes_a, closes_b)