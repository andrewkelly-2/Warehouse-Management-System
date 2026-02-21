class Product:
    def __init__(self, name, price, initialStock):
        #Requires implementation
        self.name = name
        self.price = price
        self.stock = initialStock
        self.available = True
        
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def is_available(self):
        pass
    
    def has(self, stock):
        return self.stock > stock
    
    def sell(self, amount):
        self.stock -= amount
        return self.stock * amount
    
    def restock(self, amount):
        self.stock += amount
    
    def prune(self):
        self.stock = 0

    def delist(self):
        pass
    
    def __str__(self):
        return f"{self.name} at ${self.price:.2f} ({self.stock})"
