import allure
from config import Settings
from httpx import Response
from endpoints.base_client import BaseClient, get_http_client
from tools.routes import APIRoutes
from schema.objects import CreateObjectsSchema

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
    
    @allure.step("Create object")
    def create_object(self, operation: CreateObjectsSchema) -> Response:
        """
        Создать операцию.

        :param operation: Данные для создания новой операции.
        :return: Ответ от сервера с информацией о созданной операции.
        """
        return self.post(
            APIRoutes.OBJECTS,
            json=operation.model_dump(mode='json', by_alias=True)  # Сериализуем объект в JSON перед отправкой
        )
    
    @allure.step("Delete object by id {object_id}")
    def delete_object(self, object_id: int) -> Response:
        """
        Удалить операцию по идентификатору.

        :param operation_id: Идентификатор операции, которую нужно удалить.
        :return: Ответ от сервера с результатом удаления операции.
        """
        return self.delete(f"{APIRoutes.OBJECTS}/{object_id}")
    
def get_object_client(settings: Settings) -> ObjectsClient:
    """
    Функция для создания экземпляра OperationsClient с нужными настройками.

    :param settings: Конфигурация с настройками для работы с API.
    :return: Экземпляр клиента для работы с операциями.
    """
    return ObjectsClient(client=get_http_client(settings.api_dev_http_client))