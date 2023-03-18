import os
from fastapi import FastAPI, HTTPException, Path, Query
import requests

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

import kulliyyah_example

app = FastAPI(docs_url='/',
              title='Albiruni API',
              description='Albiruni API',
              version='0.0.1',
              )


@cache()
async def get_cache():
    return 1


@app.get("/kulliyyah/{kulliyyah}", description="Get all subjects in Kulliyyah", tags=["Kulliyyah"],
         response_description="All subjects in Kulliyyah", summary="Get all subjects in Kulliyyah")
@cache(expire=10800) # 3 hours
async def say_hello(kulliyyah: str = Path(None,
                                          description="Kulliyah code. Refer https://iiumschedule.vercel.app/docs/devs/albiruni#list-of-available-kulliyyah",
                                          examples=kulliyyah_example.kulliyyah
                                          ),
                    session: str = Query('2022/2023', description="Academic session"),
                    semester: int = 1,
                    ):

    # session convert slash become underscore
    session = session.replace('/', '_')

    # sanitize kulliyyah input
    kulliyyah = kulliyyah.strip().upper()

    json_url = f'https://raw.githubusercontent.com/iqfareez/albiruni_fetcher/master/db/{session}/{semester}/{kulliyyah}.json';

    response = requests.get(json_url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Kulliyyah/session/semester not found")
    data = response.json()
    return data


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(os.getenv('REDIS_URL'), encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
