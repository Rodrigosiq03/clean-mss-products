from abc import ABC, abstractmethod
from typing import List
from src.shared.domain.entities.product import Product

class IProductRepository(ABC):
  @abstractmethod
  def get_all_products(self) -> List[Product]:
    pass