from crawlers.douyin.web.models import BaseLiveModel


class LiveLikeClick(BaseLiveModel):
    enter_from: str = "personal_homepage"
    room_id: str
    count: int
