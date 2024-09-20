from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')

class Shop(Product):
    def __init__(self, name, weight, category, __file_name='product.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name
    def get_product(self):
        file = open(self.__file_name, 'r')
        st = file.read()
        file.close()
        print(f'{st}')
    def add(self, *product):
        for i in product:
            s = (str(i))
            file = open(self.__file_name, 'r')
            f = file.read()
            file.close()
            if s in f:
                print(f'Продукт {s} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{s}')
                file.close()

s1 = Shop('',0 , '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#
print(p1)  # __str__
print(p2)  # __str__
print(p3)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

s1.get_products()
