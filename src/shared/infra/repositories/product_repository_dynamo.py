from typing import List
from src.shared.domain.entities.product import Product
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.environments import Environments
from src.shared.infra.dto.product_dynamo_dto import ProductDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class ProductRepositoryDynamo(IProductRepository):
    

  @staticmethod
  def partition_key_format(product_id) -> str:
    return f"product#{product_id}"

  @staticmethod
  def sort_key_format(product_id: int) -> str:
    return f"#{product_id}"

  def __init__(self):
    self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)
    
  def get_all_products(self) -> List[Product]:
    return self.dynamo.get_all_items()
  
  def add_product(self, product: Product) -> Product:
    product_dto = ProductDynamoDTO.from_entity(product=product)
    resp = self.dynamo.put_item(partition_key=self.partition_key_format(product.id),
                                sort_key=self.sort_key_format(product.id), item=product_dto.to_dynamo(),
                                is_decimal=True)
    return product