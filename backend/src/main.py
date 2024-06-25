from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routes import news
import uvicorn

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

api.include_router(news.router, prefix="/news", tags=["news"])

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=5000, reload=True)
