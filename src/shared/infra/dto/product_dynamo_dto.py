from decimal import Decimal
from src.shared.domain.entities.product import Product



class ProductDynamoDTO:
    id: str
    name: str
    price: float
    storage: int
    description: str

    def __init__(self, name: str, price: float, storage: int, description: str):
        self.name = name
        self.price = price
        self.storage = storage
        self.description = description

    @staticmethod
    def from_entity(product: Product) -> "ProductDynamoDTO":
        """
        Parse data from Product to ProductDynamoDTO
        """
        return ProductDynamoDTO(
            name=product.name,
            price=product.price,
            storage=product.storage,
            description=product.description
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from ProductDTO to dict
        """
        return {
            "entity": "product",
            "name": self.name,
            "price": Decimal(self.price),
            "storage": self.storage,
            "description": self.description
        }

    @staticmethod
    def from_dynamo(product_data: dict) -> "ProductDynamoDTO":
        """
        Parse data from DynamoDB to UserDynamoDTO
        @param user_data: dict from DynamoDB
        """
        return ProductDynamoDTO(
            name=product_data["name"],
            price=Decimal(product_data["price"]),
            storage=int(product_data["storage"]),
            description=product_data["description"]
        )

    def to_entity(self) -> Product:
        """
        Parse data from ProductDynamoDTO to product
        """
        return Product(
            name=self.name,
            price=self.price,
            storage=self.storage,
            description=self.description
        )

    def __repr__(self):
        return f"ProductDynamoDTO(name={self.name}, price={self.price}, storage={self.storage}, description={self.description})"
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
