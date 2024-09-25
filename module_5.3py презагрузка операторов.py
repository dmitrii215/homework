
class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.nFloors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor > self.nFloors:
            print('Такого этажа не существует!')
        else:
            if new_floor < 1:
                for f in range(1, new_floor-1, -1):
                    print('Спускаемся:', f)
            for f in range(1, new_floor+1):
                print('Поднимаемся:', f)

    def __len__(self):
        return self.nFloors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.nFloors}.'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.nFloors == other.nFloors
        elif isinstance(other, int):
            return self.nFloors == other

    def __add__(self, value):
        if isinstance(value, int):
            self.nFloors += value
        elif isinstance(value, House):
            self.nFloors += value.nFloors
        return self
    def __iadd__(self, other: int):
        return self.__add__(other)
    def __radd__(self, other):
        return self.__add__(other)
    def __lt__(self, other):
        if isinstance(other, House):
            return self.nFloors < other
        elif isinstance((other, int)):
            return self.nFloors < other
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    def __gt__(self, other):
        return not self.__le__(other)
    def __ge__(self, other):
        return not self.__lt__(other)
    def __ne__(self, other):
        return not self.__eq__(other)

def main():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne_

if __name__ == '__main__':
    main()

