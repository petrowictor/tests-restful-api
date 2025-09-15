from pydantic import BaseModel, ConfigDict, Field

class DataObjectSchema(BaseModel):
    year: int = Field(default=2024)
    price: float = Field(default=1600.50)
    CPU_model: str = Field(default="Intel Core i9", alias="CPU model")
    Hard_disk_size: str = Field(default="1 TB", alias="Hard disk size")

class CreateObjectsSchema(BaseModel):
    """
    Модель для создания нового объекта.

    """
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(default="Apple MacBook Pro 16")
    data: DataObjectSchema = Field(
        default=DataObjectSchema(),  # ← ✅ КЛЮЧЕВОЙ ШАГ: создаем экземпляр здесь!
        description="Технические характеристики объекта"
    )


class ObjectSchema(CreateObjectsSchema):
    """
    Модель объекта, содержащий ID.

    """
    id: str