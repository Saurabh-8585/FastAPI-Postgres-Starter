from fastapi import FastAPI
from uvicorn import run
from src.routes.startup import init_all
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from src.routes.all_routes import router as all_routes


app = FastAPI(title="Test API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(all_routes)


@app.on_event("startup")
async def init_processes():
    try:
        init_all()
    except Exception as e:
        logger.critical(f"Init Process Error: {e}")


if __name__ == "__main__":
    logger.info("Started main")
    run("main:app", host="0.0.0.0", port=8099, reload=True)
