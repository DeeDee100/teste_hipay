from fastapi import FastAPI
from starlette.background import BackgroundTasks
from .database.database import engine
from .database import models
from .routes import users
from .utils import create_data

app = FastAPI(
    title="Shipay",
    description="API Rest para teste técnico da Shipay.\nPor favor acesse a home para criar dados iniciais no banco.",
    version=0.1,
)

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def home():
    background_tasks = BackgroundTasks()
    background_tasks.add_task(create_data)
    teste = await background_tasks()
    if teste:
        print("Deu bão")
    return {
        "message": "This is the root path of the api, please refeer to the docs on how to use on /docs"
    }


app.include_router(users.router, prefix="/users")
# app.include_router(bank.router, prefix="/bank")