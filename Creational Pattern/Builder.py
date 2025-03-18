#Creating a Pizza 🍕 (with different toppings and crust types)

class Pizza:
    def __init__(self):
        self.toppings = None
        self.crust = None
    
    def __str__(self):
        return f'Pizza has {self.crust} crust and {self.toppings} toppings'
    
from abc import ABC,abstractmethod

class PizzaBuilder(ABC):
    @abstractmethod
    def setToppings(self,toppings):
        pass
    @abstractmethod
    def setCrust(self, crust):
        pass

class NonVegPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    
    def setToppings(self, toppings):
        self.pizza.toppings = toppings
        return self

    def setCrust(self, crust):
        self.pizza.crust = crust
        return self
    
    def build(self):
        return self.pizza
    
if __name__ == '__main__':
    pizza = NonVegPizzaBuilder().setToppings("Chicken").setCrust("Thin").build()

    print(pizza)
