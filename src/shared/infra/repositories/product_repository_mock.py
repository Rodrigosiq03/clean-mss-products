from typing import List
from src.shared.domain.entities.product import Product
from src.shared.domain.repositories.product_repository_interface import IProductRepository


class ProductRepositoryMock(IProductRepository):
  products: List[Product]
  def __init__(self) -> None:
    self.products = [
      Product("Product 1", 10.0, 10, "Description 1"),
      Product("Product 2", 20.0, 20, "Description 2"),
      Product("Product 3", 30.0, 30, "Description 3"),
    ]
  
  def get_all_products(self) -> List[Product]:
    return self.products