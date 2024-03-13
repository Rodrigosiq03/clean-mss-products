from src.shared.domain.entities.product import Product


class Test_GetAllProductsViewmodel:
  all_products_list = [
    Product("product1", 10.0, 100, "description1"),
    Product("product2", 20.0, 200, "description2"),
    Product("product3", 30.0, 300, "description3"),
  ]

  def test_get_all_products_viewmodel(self):
    from src.get_all_products.app.get_all_products_viewmodel import GetAllProductsViewmodel

    viewmodel = GetAllProductsViewmodel(self.all_products_list)

    viewmodel_dict = viewmodel.to_dict()

    assert viewmodel_dict["message"] == "all products has been retrieved"
    assert len(viewmodel_dict["products"]) == len(self.all_products_list)
    for i in range(len(self.all_products_list)):
      assert viewmodel_dict["products"][i]["name"] == self.all_products_list[i].name
      assert viewmodel_dict["products"][i]["price"] == self.all_products_list[i].price
      assert viewmodel_dict["products"][i]["storage"] == self.all_products_list[i].storage
      assert viewmodel_dict["products"][i]["description"] == self.all_products_list[i].description