from typing import List
from src.shared.domain.entities.product import Product


class ProductViewmodel:
  def __init__(self, product: Product):
    self.name = product.name
    self.price = product.price
    self.storage = product.storage
    self.description = product.description

  def to_dict(self):
    return {
      "name": self.name,
      "price": self.price,
      "storage": self.storage,
      "description": self.description
    }


class GetAllProductsViewmodel:
  def __init__(self, products_list: List[Product]):
    self.products_viewmodel_list = [ProductViewmodel(product) for product in products_list]

  def to_dict(self):
    return {
      "products": [viewmodel.to_dict() for viewmodel in self.products_viewmodel_list],
      "message": "all products has been retrieved"
    }