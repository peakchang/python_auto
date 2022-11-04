
import asyncio
import os

import aiofiles
import aiohttp
from bs4 import BeautifulSoup
from config import get_secret


async def img_downloader(session, img):
    img_name = img.split("/")[-1].split("?")[0]
    try:
        os.mkdir('./images')
    except FileExistsError:
        pass

    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f'./images/{img_name}', mode='wb') as file:
                img_data = await response.read()
                await file.write(img_data)

async def fetch(session, url, i):
    print(i + 1)
    # API 헤더에서 인증을 받을 때에는 session.get headers 에서 인증을 해준다.
    headers = {"X-Naver-Client-Id": get_secret('NAVER_API_ID'), "X-Naver-Client-Secret": get_secret('NAVER_API_SECRET')}
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result['items']
        images = [item['link'] for item in items]
        print(images)
        await asyncio.gather(*[img_downloader(session, img) for img in images])



async def naverImageDownloader():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "아이폰13"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1 + i * 20}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])
        
        
async def kakaoImageDownloader():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "아이폰13"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1 + i * 20}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
