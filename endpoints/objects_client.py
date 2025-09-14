import allure
from httpx import Response
from endpoints.base_client import BaseClient
from tools.routes import APIRoutes

class ObjectsClient(BaseClient):
    """
    Клиент для взаимодействия с обЪктами.
    """
    @allure.step("Get operation by id {id}")
    def get_object(self, id) -> Response:
        """
        Получить обЪект по идентификатору.

        :param id: Идентификатор объекта.
        :return: Ответ от сервера с информацией об объекте.
        """
        return self.get(f"{APIRoutes.OBJECTS}/{id}")