from dataclasses import dataclass

from todo_ca.request_objects import InvalidRequestObject, ValidRequestObject


@dataclass
class GetTodoRequestObject(ValidRequestObject):
    id: int

    @classmethod
    def from_dict(cls, params):
        id = params.get('id')
        if not id:
            return InvalidRequestObject(errors=['id is not valid'])

        return cls(id=id)
