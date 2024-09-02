# 配置文件路径
import asyncio
import os
import platform

from motor.motor_asyncio import AsyncIOMotorClient

import crawlers.douyin.web.utils

custom_config = None

hostname = platform.node() or 'default'
print(hostname)


async def manage_config():
    while True:
        await handle_single_change_stream()
        await asyncio.sleep(10)


async def handle_single_change_stream():
    client = AsyncIOMotorClient(os.environ['MongoDbConfigStr'])
    print("client connected")
    change_stream = client.MConfig.DouYinWeb.watch([{
        '$match': {
            'operationType': {'$in': ['update']},
            'fullDocument.key': {'$eq': hostname},
        }
    }], full_document="updateLookup")
    print("start watching config")
    global custom_config
    document = await client.MConfig.DouYinWeb.find_one({'key': {'$eq': hostname}})
    if document is None:
        print("config document not found")
        exit(1)
    custom_config = document['data']
    override_douyin_download_api_config(custom_config)
    print("initial config fetched")
    async for change in change_stream:
        print(change)
        custom_config = change['fullDocument']['data']
        override_douyin_download_api_config(custom_config)
    print("change stream ends")


def override_douyin_download_api_config(config):
    crawlers.douyin.web.utils.config = config
    crawlers.douyin.web.web_crawler.config = config


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(manage_config())
    loop.run_forever()
