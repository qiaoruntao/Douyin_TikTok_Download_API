from fastapi import Request, HTTPException

from app.api.endpoints.douyin_web import router
from app.api.models.APIResponseModel import ResponseModel, ErrorResponseModel
from server.douyin_tiktoki_download_router.crawler import CustomDouyinCrawler

custom_router = router
custom_douyin_crawler = CustomDouyinCrawler()


@custom_router.post('/fetch_follow_live', response_model=ResponseModel)
async def fetch_user_mix_videos(request: Request):
    try:
        data = await custom_douyin_crawler.fetch_follow_live()
        return ResponseModel(code=200,
                             router=request.url.path,
                             data=data)
    except Exception as e:
        status_code = 400
        detail = ErrorResponseModel(code=status_code,
                                    router=request.url.path,
                                    params=dict(request.query_params),
                                    )
        raise HTTPException(status_code=status_code, detail=detail.dict())
