import sqlite3
from abc import ABC, abstractmethod
from typing import List

# Define the database connection
class DBUtil:
    @staticmethod
    def getDBConn():
        return sqlite3.connect('order_management.db')

# Define the Product class
class Product:
    def __init__(self, productId, productName, description, price, quantityInStock, type):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

# Define the Electronics subclass
class Electronics(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod

# Define the Clothing subclass
class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.size = size
        self.color = color

# Define the User class
class User:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

# Define the interface for Order Management Repository
class IOrderManagementRepository(ABC):
    @abstractmethod
    def createOrder(self, user: User, products: List[Product]):
        pass

    @abstractmethod
    def cancelOrder(self, userId: int, orderId: int):
        pass

    @abstractmethod
    def createProduct(self, user: User, product: Product):
        pass

    @abstractmethod
    def createUser(self, user: User):
        pass

    @abstractmethod
    def getAllProducts(self) -> List[Product]:
        pass

    @abstractmethod
    def getOrderByUser(self, user: User) -> List[Product]:
        pass

# Implement the Order Processor class
class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        self.conn = DBUtil.getDBConn()

    def createOrder(self, user: User, products: List[Product]):
        # Implement logic to create an order
        pass

    def cancelOrder(self, userId: int, orderId: int):
        # Implement logic to cancel an order
        pass

    def createProduct(self, user: User, product: Product):
        # Implement logic to create a product
        pass

    def createUser(self, user: User):
        # Implement logic to create a user
        pass

    def getAllProducts(self) -> List[Product]:
        # Implement logic to fetch all products
        pass

    def getOrderByUser(self, user: User) -> List[Product]:
        # Implement logic to fetch orders by user
        pass

# Main class for Order Management
class OrderManagement:
    def __init__(self):
        self.orderProcessor = OrderProcessor()

    def run(self):
        while True:
            choice = input("Enter your choice (createUser, createProduct, cancelOrder, getAllProducts, getOrderbyUser, exit): ")
            if choice == "createUser":
                # Implement createUser logic
                pass
            elif choice == "createProduct":
                # Implement createProduct logic
                pass
            elif choice == "cancelOrder":
                # Implement cancelOrder logic
                pass
            elif choice == "getAllProducts":
                # Implement getAllProducts logic
                pass
            elif choice == "getOrderbyUser":
                # Implement getOrderbyUser logic
                pass
            elif choice == "exit":
                break
            else:
                print("Invalid choice")

# Run the main class
if __name__ == "__main__":
    orderManagement = OrderManagement()
    orderManagement.run()
