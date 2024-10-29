# src/main.py

from src.animal import Dog, Cat, Hamster, Horse, Camel, Donkey
from src.registry import AnimalRegistry
from src.counteiner import Counter

def main():
    registry = AnimalRegistry()
    counter = Counter()

    while True:
        print("\nМеню:")
        print("1. Завести новое животное")
        print("2. Увидеть список команд, которое выполняет животное")
        print("3. Обучить животное новым командам")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            try:
                with counter:
                    name = input("Введите имя животного: ")
                    birth_date = input("Введите дату рождения животного (YYYY-MM-DD): ")
                    animal_type = input("Введите тип животного (Dog, Cat, Hamster, Horse, Camel, Donkey): ")
                    commands = input("Введите команды, которые выполняет животное (через запятую): ").split(',')

                    if not name or not birth_date or not animal_type or not commands:
                        raise ValueError("Все поля должны быть заполнены")

                    if animal_type == 'Dog':
                        animal = Dog(name, birth_date, commands)
                    elif animal_type == 'Cat':
                        animal = Cat(name, birth_date, commands)
                    elif animal_type == 'Hamster':
                        animal = Hamster(name, birth_date, commands)
                    elif animal_type == 'Horse':
                        animal = Horse(name, birth_date, commands)
                    elif animal_type == 'Camel':
                        animal = Camel(name, birth_date, commands)
                    elif animal_type == 'Donkey':
                        animal = Donkey(name, birth_date, commands)
                    else:
                        print("Неверный тип животного")
                        continue

                    registry.add_animal(animal)
                    counter.add()
                    print(f"Животное {name} добавлено в реестр.")

            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            name = input("Введите имя животного: ")
            animal = registry.get_animal_by_name(name)
            if animal:
                commands = registry.list_commands(animal)
                print(f"Команды, которые выполняет {name}: {', '.join(commands)}")
            else:
                print("Животное не найдено")

        elif choice == '3':
            name = input("Введите имя животного: ")
            animal = registry.get_animal_by_name(name)
            if animal:
                command = input("Введите новую команду: ")
                registry.teach_command(animal, command)
                print(f"Команда '{command}' добавлена для {name}")
            else:
                print("Животное не найдено")

        elif choice == '4':
            break

        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
