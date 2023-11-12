import os

from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv


from app.routers import (
    chain,
    block,
)


def create_app() -> FastAPI:
    load_dotenv()
    app = FastAPI()

    app.include_router(chain.router)
    app.include_router(block.router)

    return app


app = create_app()


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=int(os.getenv("PORT")), reload=True)
