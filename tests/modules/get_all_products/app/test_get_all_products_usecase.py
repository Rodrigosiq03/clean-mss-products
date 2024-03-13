from src.get_all_products.app.get_all_products_usecase import GetAllProductsUsecase
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_GetAllProductsUsecase:
  def test_get_all_products_usecase(self):
    repo_mock = ProductRepositoryMock()
    usecase = GetAllProductsUsecase(repo_mock)

    all_products_list_returned = usecase()

    assert all_products_list_returned == repo_mock.products
    assert len(all_products_list_returned) == len(repo_mock.products)