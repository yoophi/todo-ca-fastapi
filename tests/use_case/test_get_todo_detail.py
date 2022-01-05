from todo_ca.use_case.get_todo_detail import GetTodoDetailUseCase


def test_get_todo_list_execute(mocker):
    mock_repo = mocker.Mock()
    mock_repo.get = mocker.Mock()
    uc = GetTodoDetailUseCase(mock_repo)
    uc.execute()
    mock_repo.get.assert_called()
