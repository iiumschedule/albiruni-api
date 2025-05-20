![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

# Albiruni API Server

>**Warning** This project is EXPERIMENTAL

REST API Server for IIUM Course Browser: https://albiruni.iium.edu.my/myapps/StudentOnline/schedule1.php

## Features

- [x] REST API access to IIUM Course Browser
- [x] Redis for caching and faster responses
- [x] Search for exam date
- [ ] Search subject

## Database

### For subjects 

All subjects are fetched and saved in https://github.com/iqfareez/albiruni_fetcher/tree/master/db

### For exams 

Exams are downloaded from https://www.iium.edu.my/division/amad/academic-calendarimportant-dates. Then, parsed manually and saved
to Excel file. See the files in the `db` folder.

## Installation

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Docker

You can run the API and Redis using Docker Compose:

```bash
docker-compose up --build
```

The API will be available at [http://localhost:8000](http://localhost:8000).

Environment variable `REDIS_URL` is set automatically for the API service.
