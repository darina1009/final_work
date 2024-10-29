# src/registry.py

from src.animal import Dog, Cat, Hamster, Horse, Camel, Donkey

class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_commands(self, animal):
        return animal.get_commands()

    def teach_command(self, animal, command):
        animal.add_command(command)

    def get_animal_by_name(self, name):
        for animal in self.animals:
            if animal.get_name() == name:
                return animal
        return None

