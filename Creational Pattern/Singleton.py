class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
if __name__ =="__main__":
    # Singleton pattern
    print("Singleton pattern")
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(singleton1 is singleton2)  # True, both variables point to the same instance
    print(singleton1)  # <__main__.Singleton object at 0x...>   
    print(singleton2)  # <__main__.Singleton object at 0x...>
    print(id(singleton1))  # Memory address of singleton1
    print(id(singleton2))  # Memory address of singleton2
    print("Memory address of singleton1 and singleton2 are same")
    print("Memory address of singleton1 and singleton2 are same")