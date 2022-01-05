class ResponseSuccess:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return True


class ResponseFailure:
    def __init__(self, message):
        self.message = message

    def __bool__(self):
        return False
