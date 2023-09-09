import sys
from typing import NoReturn

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routers import v1_router
from src.settings import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True)
app.include_router(v1_router)


def serve() -> NoReturn:
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)
    sys.exit()


if __name__ == "__main__":
    serve()
