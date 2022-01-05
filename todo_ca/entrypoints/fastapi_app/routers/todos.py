from typing import List

from fastapi import APIRouter, HTTPException

from todo_ca.entrypoints.fastapi_app.schema.todos import TodoOut
from todo_ca.use_case.get_todo_list import GetTodoListUseCase
from todo_ca.use_case.get_todo_detail import GetTodoDetailUseCase

router = APIRouter()


@router.get("/", summary="Todo List", response_model=List[TodoOut])
def todo_list():
    uc = GetTodoListUseCase(todos=None)
    resp = uc.execute()
    if not resp:
        raise HTTPException(status_code=404, detail="Item not found")

    return resp.value


@router.get("/{id}", summary="Todo Detail", response_model=TodoOut)
def todo_detail(id):
    uc = GetTodoDetailUseCase(todos=None)
    resp = uc.execute()
    if not resp:
        raise HTTPException(status_code=404, detail="Item not found")

    return resp.value
