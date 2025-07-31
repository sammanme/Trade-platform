import requests
from app.core.config import settings
import ccxt
import pandas as pd


async def fetch_ohlcv(symbol: str, timeframe: str = '1d'):
    binance = ccxt.binance({'enableRateLimit': True})
    ohlcv = await binance.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df.to_dict(orient='records')