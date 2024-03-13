from src.get_all_products.app.get_all_products_usecase import GetAllProductsUsecase
from src.get_all_products.app.get_all_products_viewmodel import GetAllProductsViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound


class GetAllProductsController:
  def __init__(self, usecase: GetAllProductsUsecase):
    self.usecase = usecase

  def __call__(self, request: IRequest):
    try:
      products_list = self.usecase()
      viewmodel = GetAllProductsViewmodel(products_list)
      return OK(viewmodel.to_dict())
    except NoItemsFound as err:

            return NotFound(body=err.message)

    except MissingParameters as err:

            return BadRequest(body=err.message)

    except WrongTypeParameter as err:

            return BadRequest(body=err.message)

    except EntityError as err:

            return BadRequest(body=err.message)

    except Exception as err:
            return InternalServerError(body=err.args[0])