import httpx

httpx.Client.__init__.__kwdefaults__['verify'] = False
httpx.AsyncClient.__init__.__kwdefaults__['verify'] = False
import uvicorn
from fastapi import APIRouter, FastAPI

from server.douyin_tiktoki_download_router.douyin_web import custom_router

api_router = APIRouter()
api_router.include_router(custom_router, prefix="/douyin/web", tags=["Douyin-Web-API"])
app = FastAPI()

# API router
app.include_router(api_router, prefix="/api")
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3450)
