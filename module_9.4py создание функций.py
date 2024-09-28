'''лямбда функция'''
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))
def get_advaced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding = 'utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

write = get_advaced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


'''метод __call__:'''
from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        return random.choice(self.words)  #Функция choice() из модуля random возвращает случайный элемент\
                                          # из переданной ей последовательности
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())









