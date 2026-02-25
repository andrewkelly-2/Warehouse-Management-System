class Order:
    def __init__(self, product, quantity):
        #requires implementation
        self.product = product
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.product.get_name()} {self.quantity}"
