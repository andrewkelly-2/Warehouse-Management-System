from User import User

class Customer(User):
    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)
    
    def use(self, org):
        pass
    
    def __str__(self):
        pass
