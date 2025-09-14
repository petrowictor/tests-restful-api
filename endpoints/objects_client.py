import allure
from httpx import Response
from endpoints.base_client import BaseClient
from tools.routes import APIRoutes

class ObjectsClient(BaseClient):
    """
    Клиент для взаимодействия с обЪктами.
    """
    @allure.step("Get operation by id {operation_id}")
    def get_object(self, id) -> Response:
        """
        Получить операцию по идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера с информацией об операции.
        """
        return self.get(f"{APIRoutes.OPERATIONS}/{id}")