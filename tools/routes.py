from enum import Enum


class APIRoutes(str, Enum):
    """
    Перечисление всех URI-адресов API для проекта.

    Это перечисление позволяет централизованно управлять всеми маршрутами API, 
    что помогает избежать ошибок при их использовании и упрощает масштабирование.
    """
    OBJECTS = "/objects"

    def __str__(self):
        return self.value