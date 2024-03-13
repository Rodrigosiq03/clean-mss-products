from src.get_all_products.app.get_all_products_controller import GetAllProductsController 
from src.get_all_products.app.get_all_products_usecase import GetAllProductsUsecase
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_GetAllProductsController:

    def test_get_all_products_controller(self):
        repo_mock = ProductRepositoryMock()
        get_all_users_usecase = GetAllProductsUsecase(repo_mock)
        controller = GetAllProductsController(get_all_users_usecase)

        response = controller(None)

        assert response.status_code == 200