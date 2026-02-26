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
    
    def use(self, user, cart):
        print(self)
        print("available products:")

        #Print available products with options to return to previous menu or view cart
        available_products = self.products.get_available_products()
        return_option = len(available_products)+1
        view_cart_option = len(available_products)+2

        for i, product in enumerate(available_products):
            print(f"{i+1}. {product}")

        print(f"{return_option}. Return to previous menu")
        print(f"{view_cart_option}. View Cart")

        #Get user input
        pick_a_product = input("Enter the number of the product you wish to purchase: ")
        try:
            pick_a_product = int(pick_a_product)
            if pick_a_product == return_option:
                return
            elif pick_a_product == view_cart_option:
                print("Currently in your cart:")
                print(cart)
                print("What would you like to do next?\n"
                        "1. Continue shopping\n" 
                        "2. Check out\n"
                        "3. Cancel Cart")
                checkout_choice = input("Enter your choice: ")
                if int(checkout_choice) == 1:
                    self.use(user, cart)
                elif int(checkout_choice) == 2:
                    user.add_purchase(cart)
                    print("Thank you for your purchase!")
                    return
                elif int(checkout_choice) == 3:
                    print("Cart cancelled.")
                    for order in cart.orders:
                        order.product.restock(order.quantity)
                    return
            elif 1 <= pick_a_product <= len(available_products):
                how_many_units = input("How many units would you like to purchase? ")
                try:
                    how_many_units = int(how_many_units)
                    if available_products[pick_a_product-1].has(how_many_units):
                        cart.add_order(available_products[pick_a_product-1], how_many_units)
                        available_products[pick_a_product-1].sell(how_many_units)
                        self.use(user, cart)
                    else:
                        print("Not enough stock available. Please try again.")
                        self.use(user, cart)
                except ValueError:
                    print("Please enter a positive integer for the number of units.")
                    self.use(user, cart)
        except ValueError:
            print("Invalid choice. Please try again.")
            self.use(user, cart)

    def manage(self, user):
        pass
    
    def get_region(self):
        return self.region
    
    def get_name(self):
        return self.name    
    
    def __str__(self):
        return f"{self.name} ({self.region}), {self.address}"
