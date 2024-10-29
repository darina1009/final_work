# src/counter.py

class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            raise Exception("Resource not closed properly")

