from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name #underscore _name?

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (type(name) ==  str) and (1 <= len(name) <= 25):
            self._name = name
        else:
            raise Exception ("Name must be string and between 1-25 charachters")
        
    name = property(get_name, set_name)



    def orders(self):
        from classes.order import Order
        return [order for order in Order.all if order.customer == self]
    

    def coffees(self, coffee):
        coffee_orders = []
        for coffee in self.orders():
            if not coffee.order in self.order: #may be wrong
                coffee_orders.append(coffee)
            else:
                return coffee_orders








