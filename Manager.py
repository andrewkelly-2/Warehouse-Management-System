from User import User
from Suppliers import Suppliers

class Manager(User):
    def __init__(self, first_name, last_name, username, password, suppliers):
        super().__init__(first_name, last_name, username, password)
        #Requires implementation
        self.suppliers = suppliers
        
    
    def use(self, org):
        print(f"Welcome, {self.first_name} {self.last_name}!")
        print("1. View manager details")
        print("2. view suppliers")
        print("3. Exit")
        menu_option_choice = input ("Enter choice: ")
        if menu_option_choice == "1":
            print(self)
        elif menu_option_choice == "2":
            print(self.suppliers)
        elif menu_option_choice == "3":
            print (f"Logging out {self.first_name} {self.last_name}...")
            return
        

    
    def __str__(self):
        suppliers = " "
        for one_supplier in self.suppliers:
            suppliers += f"{one_supplier}\n"
        return f"{self.get_first_name()} {self.get_last_name()} {suppliers}"

