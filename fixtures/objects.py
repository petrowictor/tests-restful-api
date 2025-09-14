import pytest

from endpoints.objects_client import ObjectsClient, get_object_client
from config import Settings
from schema.objects import ObjectSchema
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

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
    Фикстура создаёт тестовую операцию перед тестом и удаляет её после выполнения теста.
    
    :param operations_client: API-клиент для работы с операциями.
    :return: Созданная тестовая операция.
    """
    create_object = CreateObject()
    payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": 2019,
         "price": 1849.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }

    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(create_object.response_json['id'])