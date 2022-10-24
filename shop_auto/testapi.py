import aiohttp
import asyncio
import json
from pathlib import Path
from typing import Optional
import requests

BASE_DIR = Path(__file__).resolve().parent
def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),
):
    
    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")
    
    
    

URL = "https://openapi.naver.com/v1/search/shop"

headers = {"X-Naver-Client-Id": get_secret('NAVER_API_ID'), "X-Naver-Client-Secret": get_secret('NAVER_API_SECRET')}

keyword = "갤럭시z플립4"
tong = "KT"
productId = "34546886169"

allCount = 0
itemCount = 0
chk_loop = ""
while chk_loop == "":
    params = {'query': keyword,'start': allCount * 100 + 1, 'display': '100'}
    res = requests.get(URL, headers=headers, params=params).json()
    for item in res['items']:
        if item['category3'] == tong:
            print(item['title'])
            itemCount += 1
        if item['productId'] == productId:
            chk_loop = "ok"
            break
    allCount += 1
    
print(itemCount)


# params = {'query': keyword,'start': allCount * 10 + 1, 'display': '10'}
# res = requests.get(URL, headers=headers, params=params).json()
# for item in res['items']:
#     print(item['title'])




# import requests
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print(r.status_code)

# r.headers['content-type']
# r.encoding
# r.text
# r.json()



