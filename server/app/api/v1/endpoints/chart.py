# We'll start with a mock data endpoint.
from fastapi import APIRouter, Query
import pandas as pd
import numpy as np
import time
from fastapi import WebSocket

router = APIRouter()


@router.get("/historical")
async def get_historical_data(
    symbol: str = Query(..., description="Ticker symbol"),
    resolution: str = Query("1D", description="Chart resolution (e.g., 1, 5, 15, 30, 60, D, W, M)"),
    _from: int = Query(..., description="Start timestamp"),
    to: int = Query(..., description="End timestamp")
):
    # Mock data for now
    # We'll generate a dataframe of dates from _from to to
    date_range = pd.date_range(start=pd.Timestamp(_from, unit='s'), end=pd.Timestamp(to, unit='s'), freq='D')
    data = {
        "t": date_range.astype(np.int64) // 10**9,  # convert to seconds
        "o": np.random.rand(len(date_range)) * 100,
        "h": np.random.rand(len(date_range)) * 100 + 10,
        "l": np.random.rand(len(date_range)) * 100 - 10,
        "c": np.random.rand(len(date_range)) * 100,
        "v": np.random.randint(1000, 10000, size=len(date_range))
    }
    return data


@router.websocket("/realtime")
async def websocket_realtime(websocket: WebSocket, symbol: str):
    await websocket.accept()
    # Here we would subscribe to a real-time data source for the symbol
    # and forward messages to the client.
    # For mock, we can send random data every second.
    while True:
        import time
        import json
        time.sleep(1)
        data = {
            "t": int(time.time()),
            "p": float(np.random.rand() * 100)
        }
        await websocket.send_json(data)