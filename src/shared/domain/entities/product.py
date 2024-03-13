import abc
import uuid
from src.shared.helpers.errors.domain_errors import EntityError

class Product(abc.ABC):
  id: str
  name: str
  price: float
  storage: int
  description: str

  def __init__(self, name: str, price: float, storage: int, description: str):
    self.id = str(uuid.uuid4())
    if not Product.validate_name(name):
      raise EntityError("name")
    self.name = name
    if not Product.validate_price(price):
      raise EntityError("price")
    self.price = price
    if not Product.validate_storage(storage):
      raise EntityError("storage")
    self.storage = storage
    if not Product.validate_description(description):
      raise EntityError("description")
    self.description = description

  @staticmethod
  def validate_name(name: str) -> bool:
    if name is None:
      return False
    elif type(name) != str:
      return False
    elif len(name) < 2:
      return False

    return True
  
  @staticmethod
  def validate_price(price: float) -> bool:
    if price is None:
      return False
    elif type(price) != float:
      return False
    elif price < 0:
      return False

    return True
  
  @staticmethod
  def validate_storage(storage: int) -> bool:
    if storage is None:
      return False
    elif type(storage) != int:
      return False
    elif storage < 0:
      return False

    return True
  
  @staticmethod
  def validate_description(description: str) -> bool:
    if description is None:
      return False
    elif type(description) != str:
      return False
    elif len(description) < 2:
      return False

    return True
  
  def __repr__(self):
    return f"Product(id={self.id}, name={self.name}, price={self.price}, storage={self.storage}, description={self.description})"