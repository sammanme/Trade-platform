from fastapi import APIRouter, Query
import pandas as pd
import numpy as np


router = APIRouter()


def calculate_arbitrage(prices_a: list, prices_b: list):
    spread = np.array(prices_a) - np.array(prices_b)
    z_score = (spread - spread.mean()) / spread.std()
    return {
        "spread": spread.tolist(),
        "z_score": z_score.tolist(),
        "threshold": 2.0
    }