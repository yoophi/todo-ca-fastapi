from fastapi import FastAPI
from todo_ca.entrypoints.fastapi_app.routers.todos import router as todo_router


def create_app():
    app = FastAPI()
    app.include_router(todo_router, prefix="/api/todos", tags=["Todo"])

    return app
