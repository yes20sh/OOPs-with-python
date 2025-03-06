class Customer:  
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self. address = address

    def update_profile(self, new_name, new_city, new_pincode,new_state):
        self.name = new_name
        self.address.change_address(new_city,new_pincode,new_state)


class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pincode,new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state

address = Address('Dewas',455001,'MP')
customer = Customer('Yash','Male',address)


print(customer.name)
print(customer.address.city)

customer.update_profile("Tushar","Narmadapuram", 461001,'MP')

print(customer.name)
print(customer.address.city)