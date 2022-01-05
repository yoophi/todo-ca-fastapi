import pytest
from fastapi.testclient import TestClient

from todo_ca.entrypoints.fastapi_app import create_app
from todo_ca.entrypoints.fastapi_app.schema.todos import TodoOut
from todo_ca.shared import ResponseSuccess, ResponseFailure
from todo_ca.use_case.get_todo_detail import GetTodoDetailUseCase
from todo_ca.use_case.get_todo_list import GetTodoListUseCase


@pytest.fixture
def client():
    app = create_app()
    client = TestClient(app)
    return client


def test_get_main(client):
    response = client.get("/")
    assert response.status_code == 404


def test_get_todo_list(mocker, client):
    return_value = [
        TodoOut(id=1, title="sample", completed=False),
    ]
    mocker.patch.object(
        GetTodoListUseCase, "execute", return_value=ResponseSuccess(value=return_value)
    )
    response = client.get("/api/todos/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "sample", "completed": False}]


def test_get_todo_list_fails(mocker, client):
    mocker.patch.object(
        GetTodoListUseCase, "execute", return_value=ResponseFailure("some-error")
    )
    response = client.get("/api/todos/")
    assert response.status_code == 404


def test_get_todo_detail(mocker, client):
    return_value = TodoOut(id=1, title="sample", completed=False)
    mocker.patch.object(
        GetTodoDetailUseCase,
        "execute",
        return_value=ResponseSuccess(value=return_value),
    )
    response = client.get("/api/todos/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "sample", "completed": False}


def test_get_todo_detail_fails(mocker, client):
    mocker.patch.object(
        GetTodoDetailUseCase, "execute", return_value=ResponseFailure("not-found")
    )
    response = client.get("/api/todos/1")
    assert response.status_code == 404
