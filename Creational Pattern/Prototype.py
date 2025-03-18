import copy

class Vehicle:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def clone(self):
        return copy.deepcopy(self)
    
    def display(self):
        print(f'Vehicle with {self.name} and {self.type}')

if __name__=="__main__":
    suzuki =  Vehicle("Suzuki", "SUV")
    suzuki_copy = suzuki.clone()
    suzuki_copy.display()
    suzuki.display()

    print(id(suzuki))
    print(id(suzuki_copy))

