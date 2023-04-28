# Parent class/User class
class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        
    def register(self):
        print(f"Welcome {self.name}! You have successfully registered.")
        

# Child class/Buyer class
class Buyer(User):
    def __init__(self, name, username, password, contact, address):
        super().__init__(name, username, password)
        self.contact = contact
        self.address = address
        
    def register(self):
        super().register()
        print(f"Your contact number is {self.contact} and your address is {self.address}.")
        

# Child class/Seller class
class Seller(User):
    def __init__(self, name, username, password, company_name, business_type, location):
        super().__init__(name, username, password)
        self.company_name = company_name
        self.business_type = business_type
        self.location = location
        
    def register(self):
        super().register()
        print(f"You are registered as a seller with {self.company_name}.")
        print(f"Your business type is {self.business_type} and your location is {self.location}.")
        

# Driver code
users = []
buyer = Buyer("John Doe", "johndoe123", "password123", "+12345678901", "1234 Main Street")
seller = Seller("Jane Doe", "janedoe123", "password123", "ABC Inc.", "Retailer", "5678 Market Street")
users.append(buyer)
users.append(seller)

for user in users:
    user.register()
