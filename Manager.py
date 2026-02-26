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
            self.use(org)
        elif menu_option_choice == "2":
            for i, supplier in enumerate(self.suppliers):
                print(f"{i+1}. {supplier}")
            manager_choice_of_supplier = input("Enter the number of the supplier you want to view: ")
            try:
                manager_choice_of_supplier = int(manager_choice_of_supplier)
                if 1 <= manager_choice_of_supplier <= len(self.suppliers):
                    self.suppliers[manager_choice_of_supplier - 1].view_products()
                    self.use(org)
                else:
                    print("Invalid choice. Please try again.")
                    self.use(org)
            except ValueError:
                print("Please enter a valid number.")
                self.use(org)

        elif menu_option_choice == "3":
            print (f"Logging out {self.first_name} {self.last_name}...")
            return
        

    
    def __str__(self):
        result = "Suppliers:\n"
        for one_supplier in self.suppliers:
            result += f"{one_supplier}\n"
        return f"{self.get_first_name()} {self.get_last_name()}\n{result}"

