from todo_ca.request_objects.get_todo import GetTodoRequestObject


def test_get_todo_invalid():
    ro = GetTodoRequestObject.from_dict({'id': 0})
    assert bool(ro) is False

    ro = GetTodoRequestObject.from_dict({})
    assert bool(ro) is False


def test_get_todo():
    ro = GetTodoRequestObject.from_dict({'id': 1})
    assert bool(ro) is True
