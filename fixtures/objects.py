import pytest

from endpoints.objects_client import ObjectsClient, get_object_client
from config import Settings
from schema.objects import ObjectSchema

@pytest.fixture
def object_client(settings: Settings) -> ObjectsClient:
    """
    Фикстура создаёт экземпляр API-клиента для работы с операциями.
    
    :param settings: Объект с настройками тестовой сессии.
    :return: Экземпляр OperationsClient.
    """
    return get_object_client(settings)


@pytest.fixture
def function_operation(object_client: ObjectsClient) -> ObjectSchema:
    """
    Фикстура создаёт тестовый объект и удаляет его после выполнения теста.
    
    :param objects_client: API-клиент для работы с объектами.
    :return: Создан тестовый объект.
    """
    operation = object_client.create_operation()
    yield operation

    object_client.delete_operation_api(operation.id)