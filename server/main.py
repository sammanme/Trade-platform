from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import chart, arbitrage


app = FastAPI(title=settings.app_name)

app.include_router(chart.router, prefix="/api/v1/chart", tags=["chart"])
app.include_router(arbitrage.router, prefix="/api/v1/arbitrage", tags=["arbitrage"])

@app.get("/")
def read_root():
    return {"message": "Backend is live!"}