import uvicorn
from fastapi import FastAPI

from src.routes.historical_facts import router as historical_facts_router

app = FastAPI()

app.include_router(historical_facts_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)