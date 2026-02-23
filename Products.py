class Products:
    def __init__(self, products=[]):
        #Requires implementation
        self.products = products
        
    def get_all_products(self):
        return self.products
    
    def get_available_products(self):
        return [product for product in self.products if product.is_available()]
    