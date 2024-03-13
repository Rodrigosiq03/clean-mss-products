from src.shared.domain.repositories.product_repository_interface import IProductRepository


class GetAllProductsUsecase:
  def __init__(self, repo: IProductRepository):
    self.repo = repo

  def __call__(self):
    all_products_list = self.repo.get_all_products()
    return all_products_list