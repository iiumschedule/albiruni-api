from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(docs_url='/',
              title='Albiruni API',
                description='Albiruni API',
                version='0.0.1',
              )

@app.get("/kulliyyah/{name}", description="Get all subjects in Kulliyyah", tags=["Kulliyyah"], response_description="All subjects in Kulliyyah", summary="Get all subjects in Kulliyyah")
async def say_hello(name: str, session: str = '2022/2023', semester: int = 1):

    # session convert slash become underscore
    session = session.replace('/', '_')

    json_url = f'https://raw.githubusercontent.com/iqfareez/albiruni_fetcher/master/db/{session}/{semester}/{name.upper()}.json';

    response = requests.get(json_url)

    if response.status_code != 200:
       raise HTTPException(status_code=404, detail="Kulliyyah/session/semester not found")
    data = response.json()
    return data
