import uvicorn
from fastapi import FastAPI
# from app.models import task, user
from routers import task
from routers import user
from backend.db import engine, Base

# создали сущность FastAPI
app = FastAPI()


@app.get("/")  # созд.1 маршрут "/"
async def welcome() -> dict:  # возвр.словарь
    return {"message": "Welcome to Taskmanager"}

# подкл. объектов APIRouter к созд.FastAPI
app.include_router(task.router)
app.include_router(user.router)

# if __name__ == 'main':
#     uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
