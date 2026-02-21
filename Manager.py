from User import User
from Suppliers import Suppliers

class Manager(User):
    def __init__(self, first_name, last_name, username, password, suppliers):
        super().__init__(first_name, last_name, username, password)
        #Requires implementation
        self.suppliers = suppliers
        
    
    def use(self, org):
        pass
    
    def __str__(self):
        pass

