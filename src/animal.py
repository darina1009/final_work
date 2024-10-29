# src/animal.py

class Animal:
    def __init__(self, name, birth_date):
        self._name = name
        self._birth_date = birth_date

    def get_name(self):
        return self._name

    def get_birth_date(self):
        return self._birth_date

class Pet(Animal):
    def __init__(self, name, birth_date, commands):
        super().__init__(name, birth_date)
        self._commands = commands

    def get_commands(self):
        return self._commands

    def add_command(self, command):
        self._commands.append(command)

class PackAnimal(Animal):
    def __init__(self, name, birth_date, commands):
        super().__init__(name, birth_date)
        self._commands = commands

    def get_commands(self):
        return self._commands

    def add_command(self, command):
        self._commands.append(command)

class Dog(Pet):
    pass

class Cat(Pet):
    pass

class Hamster(Pet):
    pass

class Horse(PackAnimal):
    pass

class Camel(PackAnimal):
    pass

class Donkey(PackAnimal):
    pass

