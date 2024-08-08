import asyncio

import httpx
from uvicorn import Config, Server

from server.config import manage_config

httpx.Client.__init__.__kwdefaults__['verify'] = False
httpx.AsyncClient.__init__.__kwdefaults__['verify'] = False
from fastapi import APIRouter, FastAPI

from server.douyin_tiktoki_download_router.douyin_web import custom_router

api_router = APIRouter()
api_router.include_router(custom_router, prefix="/douyin/web", tags=["Douyin-Web-API"])
app = FastAPI()

# API router
app.include_router(api_router, prefix="/api")
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    config = Config(app=app, loop=loop, host="0.0.0.0", port=3450)
    server = Server(config)
    loop.create_task(server.serve())
    loop.create_task(manage_config())
    loop.run_forever()
