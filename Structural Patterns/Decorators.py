from abc import ABC, abstractmethod
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 5

class CoffeeDecorator(Coffee):
    def __init__(self, coffee:Coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()
    
class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost()+2

class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost()+2


coffee = SimpleCoffee()
print("Total Cost:"+ str(coffee.cost()))
coffee = Milk(coffee)
print("Total Cost:"+ str(coffee.cost()))
coffee = Sugar(coffee)

print("Total Cost:"+ str(coffee.cost()))