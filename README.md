![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

# Albiruni API Server

>**Warning** This project is EXPERIMENTAL

REST API Server for IIUM Course Browser: https://albiruni.iium.edu.my/myapps/StudentOnline/schedule1.php

## Database

All subjects are fetched and saved in https://github.com/iqfareez/albiruni_fetcher/tree/master/db

## Installation

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
