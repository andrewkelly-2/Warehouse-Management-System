from Suppliers import Suppliers
from Users import Users
from InvalidUserError import InvalidUserError

class Organisation:
    def __init__(self, suppliers, users):
        self.suppliers = suppliers
        self.users = users
    
    def use(self):
        print("Welcome to the Organisation!")
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            user = self.users.validate_user(username, password)
            user.use(self)
        except InvalidUserError:
            print("Invalid username or password. Please try again.")
    
if __name__ == "__main__":
    seeded_suppliers = Suppliers().seed_data()
    seeded_users = Users().seed_data(seeded_suppliers)
    Organisation(seeded_suppliers, seeded_users).use()
