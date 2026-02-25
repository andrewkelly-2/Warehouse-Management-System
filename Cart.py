from Order import Order

class Cart:
    def __init__(self, supplier, user):
        self.supplier = supplier
        self.user = user
        self.orders = []

    def use(self):
        pass
    
    def __str__(self):
        in_my_cart = ""
        for order in self.orders:
            in_my_cart += f"{order}\n"
        if in_my_cart == "":
            in_my_cart = "Your cart is empty."
        return in_my_cart
    
    def add_order(self, product, quantity):
        order = Order(product, quantity)
        self.orders.append(order)

    
