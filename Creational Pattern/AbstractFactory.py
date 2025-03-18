from abc import ABC,abstractmethod
class Laptop(ABC):
    @abstractmethod
    def specs(self):
        pass

class SmartPhone(ABC):
    @abstractmethod
    def specs(self):
        pass

class AppleLaptop(Laptop):
    def specs(self):
        print("Apple Laptop Rocks")
    
class SamsungLaptop(Laptop):
    def specs(self):
        print("Samsung Laptop Rocks")

class AppleSmartPhone(SmartPhone):
    def specs(self):
        print("Apple Iphone")

class SamsungSmartPhone(SmartPhone):
    def specs(self):
        print("Samsung Phone")


class GadgetFactory(ABC):
    @abstractmethod
    def createPhone(self)->SmartPhone:
        pass
    @abstractmethod
    def createLaptop(self)->Laptop:
        pass


class AppleFactory(GadgetFactory):
    def createLaptop(self):
        return AppleLaptop()

    def createPhone(self):
        return AppleSmartPhone()
    

class SamsungFactory(GadgetFactory):
    def createLaptop(self):
        return SamsungLaptop()
    
    def createPhone(self):
        return SamsungSmartPhone()


if __name__ =="__main__":
    appleFactory = AppleFactory()
    samsungFactory = SamsungFactory()

    iphone = appleFactory.createPhone()
    galaxy = samsungFactory.createPhone()

    macbook = appleFactory.createLaptop()
    galaxyLaptop = samsungFactory.createLaptop()


    iphone.specs()
    galaxy.specs()

    macbook.specs()
    galaxyLaptop.specs()

    
