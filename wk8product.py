from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    def update_stock(self, new_stock):
        self.__stock = new_stock

    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    @property
    # to access the private attribute __product_id, we can create a property method that returns its value. This allows us to retrieve the product ID without directly accessing the private attribute. 
    # basically like a window to access the private attribute
    def product_id(self):   
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    @abstractmethod
    def get_fulfilment_info(self):
        pass