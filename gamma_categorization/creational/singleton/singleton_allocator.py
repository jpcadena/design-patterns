"""
Singleton Allocator script
"""
import random


class Database:
    """
    Database class
    """
    initialized: bool = False

    def __init__(self):
        self.db_id: int = random.randint(1, 101)
        print('Generated an id of', self.db_id)
        print('Loading database from file')

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls) \
                .__new__(cls, *args, **kwargs)

        return cls._instance


database: Database = Database()

if __name__ == '__main__':
    d1: Database = Database()
    d2: Database = Database()

    print(d1 == d2)
    print(database == d1)
    print(d1.db_id, d2.db_id)
