# A model class for Product items
# See https://docs.pydantic.dev/latest/concepts/models/

from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = 0 # default for new product
    title: str
    description: str
    category: Optional[str] = ""
    price: float
    rating: Optional[int] = 0
    stock: int
    brand: Optional[str] = ""
    sku: Optional[str] = ""
    thumbnail: Optional[str] = ""
