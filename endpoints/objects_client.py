import allure
from config import Settings
from httpx import Response
from endpoints.base_client import BaseClient, get_http_client
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
    
def get_object_client(settings: Settings) -> ObjectsClient:
    """
    Функция для создания экземпляра OperationsClient с нужными настройками.

    :param settings: Конфигурация с настройками для работы с API.
    :return: Экземпляр клиента для работы с операциями.
    """
    return ObjectsClient(client=get_http_client(settings.api_dev_http_client))