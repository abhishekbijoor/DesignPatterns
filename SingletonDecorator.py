def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs): 
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def log(self, message):
        print(f"Log: {message}")

if __name__ == "__main__":
    # Singleton pattern using decorator
    print("Singleton pattern using decorator")
    logger1 = Logger()
    logger2 = Logger()
    logger1.log(f"This is a log message.+{id(logger1)}")
    logger2.log(f"This is another log message.+{id(logger2)}")
    print(logger1 is logger2)  # True, both variables point to the same instance
    print(logger1)  # <__main__.Logger object at 0x...>
    print(logger2)  # <__main__.Logger object at 0x...>
    print(id(logger1))  # Memory address of logger1
    print(id(logger2))  # Memory address of logger2
    print("Memory address of logger1 and logger2 are same")