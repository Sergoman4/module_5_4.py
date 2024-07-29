class House:
    houses_history = []  # Список для хранения истории зданий

    def __new__(cls, name, number_of_floors):
        instance = super().__new__(cls)  # Создаем экземпляр класса
        cls.houses_history.append(name)  # Добавляем название в историю
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Вывод: ['ЖК Эльбрус']
h2 = House('ЖК Акация', 20)
print(House.houses_history)  # Вывод: ['ЖК Эльбрус', 'ЖК Акация']
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # Вывод: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

del h2
del h3

print(House.houses_history)  # Вывод: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

del h1

