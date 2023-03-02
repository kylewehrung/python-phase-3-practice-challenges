from classes.order import Order

class Coffee:
    def __init__(self, name):
        if (type(name) == str):
            self._name = name

    def get_name(self):
        return self._name
    
    def set_name(self):
        raise Exception ("Name cannot be changed")
    
    name = property(get_name, set_name)




    def orders(self):
        from classes.order import Order
        return [order for order in Order.all if order.coffee == self]
            

   
    def customers(self, customer):
        customers_who_ordered = []
        for customer in self.orders():
            if not customer.order in self.customer: # if not self.order in customer?
                customers_who_ordered.append(customer)
            else:
                raise customers_who_ordered

    












