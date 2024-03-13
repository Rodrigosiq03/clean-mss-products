from src.get_all_products.app.get_all_products_controller import GetAllProductsController
from src.get_all_products.app.get_all_products_usecase import GetAllProductsUsecase
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo: IProductRepository = Environments.get_product_repo()()
usecase = GetAllProductsUsecase(repo)
controller = GetAllProductsController(usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()