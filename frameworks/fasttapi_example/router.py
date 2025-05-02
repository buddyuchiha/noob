from fastapi import APIRouter, Depends
from typing import Annotated 

from frameworks.fasttapi_example.schemas import STaskAdd 
from frameworks.fasttapi_example.repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()]

):
    task_id = await TaskRepository.add_one(task)
    return {"ok" :True, "task_id" : task_id}

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {"data" : tasks}