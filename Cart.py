from Order import Order

class Cart:
    def __init__(self, supplier, user):
        self.supplier = supplier
        self.user = user
        self.orders = []

    def use(self):
        pass
    
    def __str__(self):
        return f"{self.orders}"
    
