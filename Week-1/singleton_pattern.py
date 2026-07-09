class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating database connection...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self):
        print("Connected to database")


db1 = DatabaseConnection()
db2 = DatabaseConnection()

print("Same instance:", db1 is db2)