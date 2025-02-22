class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def connect(self):
        print("Connected to the database.")

# Client Code
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # True (Same instance)
db1.connect()
