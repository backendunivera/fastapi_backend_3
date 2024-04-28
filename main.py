from fastapi import FastAPI

from db import create_tables
from public.films import films_router
from public.producers import producers_router

app = FastAPI()

app.include_router(producers_router)
app.include_router(films_router)


@app.on_event("startup")
# Создание таблиц в БД
async def startup_event():
    await create_tables()