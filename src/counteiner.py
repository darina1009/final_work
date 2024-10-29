# src/counter.py

class Counter:
    def __init__(self):
        self.count = 0
        self.open = False

    def add(self):
        self.count += 1

    def __enter__(self):
        self.open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.open:
            raise Exception("Resource not closed properly")
        self.open = False

