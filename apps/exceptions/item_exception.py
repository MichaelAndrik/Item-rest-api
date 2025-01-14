from ..common import StatusCode


class ItemException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ItemNotFoundException(ItemException):
    def __init__(self, message: str):
        super().__init__(message, StatusCode.NOT_FOUND)


class ItemAlreadyExistsException(ItemException):
    def __init__(self, message: str):
        super().__init__(message, StatusCode.BAD_REQUEST)


class ItemRepositoryException(ItemException):
    def __init__(self, message: str):
        super().__init__(message, StatusCode.INTERNAL_SERVER_ERROR)
