# A model class for Product items
# See https://docs.pydantic.dev/latest/concepts/models/
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float
    rating: float
    stock: int
    brand: str
    sku: str
    thumbnail: str
