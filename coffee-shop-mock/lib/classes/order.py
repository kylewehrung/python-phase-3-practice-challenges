from classes.customer import Customer
from classes.coffee import Coffee

class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price #_price? idk
        Order.add_to_order(self)

    @classmethod
    def add_to_order(cls, order):
        cls.all.append(order)
    


    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if (type(price) == int) and (1 <= price <= 10):
            self._price = price
        else:
            raise Exception ("Price must be an integer between 1-10")
        
    price = property(get_price, set_price)



    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        if (type(customer, Customer)): #might need to = str? or someting else
            self._customer = customer


    def get_coffee(self):
        return self._coffee

    def set_coffee(self, coffee):
        if (type(coffee, Coffee)):
            self._coffee = coffee


    customer = property(get_customer, set_customer)
    coffee = property(get_coffee, set_coffee)


