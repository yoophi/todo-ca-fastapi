from typing import List


class InvalidRequestObject:
    errors = List[str]

    def __init__(self, errors=None):
        if errors is None:
            errors = []

        self.errors = errors

    def __bool__(self):
        return False


class ValidRequestObject:
    def __bool__(self):
        return True
