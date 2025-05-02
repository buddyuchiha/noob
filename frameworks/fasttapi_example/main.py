from fastapi import FastAPI

from contextlib import asynccontextmanager

from frameworks.fasttapi_example.database import create_tables, delete_tables
from frameworks.fasttapi_example.router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Base clear")
    await create_tables()
    print("Base create")
    yield
    print("Off")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router) 

