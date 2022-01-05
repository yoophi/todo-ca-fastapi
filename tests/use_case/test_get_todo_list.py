from todo_ca.use_case.get_todo_list import GetTodoListUseCase


def test_get_todo_list_execute(mocker):
    mock_repo = mocker.Mock()
    mock_repo.list = mocker.Mock()
    uc = GetTodoListUseCase(mock_repo)
    uc.execute()
    mock_repo.list.assert_called()
