from User import User

class Customer(User):
    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)
    
    def use(self, org):
        print(f"Welcome, {self.get_first_name()} {self.get_last_name()}!")
        print("1. View Customer Details")
        print("2. Shop")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(self)
            self.use(org)
        elif choice == "2":
            print(org.suppliers)
            supplier_choice = input("Enter your choice of supplier (number): ")
            try:
                supplier_choice = int(supplier_choice)
                if 1 <= supplier_choice <= len(org.suppliers.suppliers):
                    supplier =org.suppliers.suppliers[supplier_choice - 1]
                    supplier.use(self)
            except ValueError:
                print("Invalid choice. Please try again.")
                self.use(org)
                
        elif choice == "3":
            print ("Thank you for visiting! Goodbye!")
            return
    
    def __str__(self):
        return f"{self.get_first_name()} {self.get_last_name()} {self.purchases}"
    