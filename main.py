import os
from fastapi import FastAPI, HTTPException, Path, Query
import requests

from helpers.find_exam import find_exam
from schemas.exam_date_time import ExamDateTime
from enum import Enum

app = FastAPI(docs_url='/',
              title='Albiruni API',
              description='Albiruni API',
              version='0.0.1',
              )

class Kulliyyah(str, Enum):
    CFL = "CFL"
    LAWS = "LAWS"
    AED = "AED"
    ECONS = "ECONS"
    EDUC = "EDUC"
    ENGIN = "ENGIN"
    KICT = "KICT"
    IRKHS = "IRKHS"
    KAHS = "KAHS"
    DENT = "DENT"
    MEDIC = "MEDIC"
    NURS = "NURS"
    PHARM = "PHARM"
    KOS = "KOS"
    KLM = "KLM"
    SC4SH = "SC4SH"

@app.get("/kulliyyah/{kulliyyah}", description="Get all subjects in Kulliyyah", tags=["Kulliyyah"],
         response_description="All subjects in Kulliyyah", summary="Get all subjects in Kulliyyah")
async def all_subjects(kulliyyah: Kulliyyah = Path(...,
                                             description="Kulliyah code. Refer https://iiumschedule.vercel.app/docs/devs/albiruni#list-of-available-kulliyyah",
                                             ),
                       session: str = Query('2025/2026', description="Academic session"),
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


@app.get("/exams/{subject}", description="Find exams", tags=["Exams"],
         response_description="Date and time of the exam", summary="Find exam subject date & time")
async def search_exam(subject:str = Path(..., description="Course Code", example="PSCI 3150"),
                       session: str = Query('2025/2026', description="Academic session"),
                       semester: int = 1,) -> ExamDateTime:
    # sanitize session input
    session = session.replace('/', '_')

    subject = subject.strip().upper()

    try:
        exam_date, exam_time = find_exam(subject, session, semester)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.args[0])

    return ExamDateTime(date=exam_date, time=exam_time)

