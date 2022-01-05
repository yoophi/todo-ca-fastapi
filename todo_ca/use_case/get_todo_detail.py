class GetTodoDetailUseCase:
    def __init__(self, todos):
        self.todos = todos

    def execute(self):
        self.todos.get()
        return []
