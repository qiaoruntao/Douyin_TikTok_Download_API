# 关注用户的直播列表
from crawlers.base_crawler import BaseCrawler
from crawlers.douyin.web.endpoints import DouyinAPIEndpoints
from crawlers.douyin.web.models import FollowUserLive
from crawlers.douyin.web.utils import BogusManager
from crawlers.douyin.web.web_crawler import DouyinWebCrawler


class CustomDouyinCrawler(DouyinWebCrawler):
    def __init__(self):
        pass

    async def fetch_follow_live(self):
        kwargs = await self.get_douyin_headers()
        base_crawler = BaseCrawler(proxies=kwargs["proxies"], crawler_headers=kwargs["headers"])
        async with base_crawler as crawler:
            params = FollowUserLive()
            endpoint = BogusManager.xb_model_2_endpoint(
                DouyinAPIEndpoints.FOLLOW_USER_LIVE, params.dict(), kwargs["headers"]["User-Agent"]
            )
            response = await crawler.fetch_get_json(endpoint)
        return response
