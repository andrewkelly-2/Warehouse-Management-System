from Products import Products
from Product import Product
from Cart import Cart

class Supplier:
    def __init__(self, name, region, address, products):
        self.name = name
        self.region = region
        self.address = address
        self.products = Products(products)
        self.profit = 0
    
    def use(self, user):
        pass
    
    def manage(self, user):
        pass
    
    def get_region(self):
        return self.region
    
    def get_name(self):
        return self.name    
    
    def __str__(self):
        return f"{self.name} ({self.region}), {self.address}"
