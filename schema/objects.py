from pydantic import BaseModel

class ObjectSchema(BaseModel):
    """
    Модель объекта, содержащий ID.
    """
    id: str