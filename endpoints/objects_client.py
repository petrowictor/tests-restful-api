import allure
from config import Settings
from httpx import Response
from endpoints.base_client import BaseClient, get_http_client
from tools.routes import APIRoutes
from schema.objects import CreateObjectsSchema, ObjectSchema

class ObjectsClient(BaseClient):
    """
    Клиент для взаимодействия с обЪктами.
    """
    @allure.step("Get operation by id {id}")
    def get_object_api(self, id) -> Response:
        """
        Получить обЪект по идентификатору.

        :param id: Идентификатор объекта.
        :return: Ответ от сервера с информацией об объекте.
        """
        return self.get(f"{APIRoutes.OBJECTS}/{id}")
    
    @allure.step("Create object")
    def create_object_api(self, object: CreateObjectsSchema) -> Response:
        """
        Создать операцию.

        :param operation: Данные для создания новой операции.
        :return: Ответ от сервера с информацией о созданной операции.
        """
        return self.post(
            APIRoutes.OBJECTS,
            json=object.model_dump(mode='json', by_alias=True)  # Сериализуем объект в JSON перед отправкой
        )
    
    @allure.step("Delete object by id {object_id}")
    def delete_object_api(self, object_id: int) -> Response:
        """
        Удалить операцию по идентификатору.

        :param operation_id: Идентификатор операции, которую нужно удалить.
        :return: Ответ от сервера с результатом удаления операции.
        """
        return self.delete(f"{APIRoutes.OBJECTS}/{object_id}")
    
    def create_object(self) -> ObjectSchema:
        """
        Упрощенный метод для создания новой операции.

        Этот метод создает операцию с помощью схемы `CreateOperationSchema`, отправляет запрос
        на создание, а затем преобразует ответ в объект `OperationSchema`.

        :return: Объект `OperationSchema`, представляющий созданную операцию.
        """
        # Создаем запрос с фейковыми данными (по умолчанию для теста)
        request = CreateObjectsSchema()
        # Отправляем запрос на создание
        response = self.create_object_api(request)
        # Возвращаем созданную операцию как объект схемы
        return ObjectSchema.model_validate_json(response.text)
    
def get_object_client(settings: Settings) -> ObjectsClient:
    """
    Функция для создания экземпляра OperationsClient с нужными настройками.

    :param settings: Конфигурация с настройками для работы с API.
    :return: Экземпляр клиента для работы с операциями.
    """
    return ObjectsClient(client=get_http_client(settings.api_dev_http_client))