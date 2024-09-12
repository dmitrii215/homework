'''условная конструкция'''
first = int(input("введите первое число:  "))
sekond = int(input("введите первое число:  "))
third = int(input("введите первое число:  "))

a = first
b = sekond
c = third

if a == b == c:
    print(3)

elif a != b == c or a == b != c or b == a != c:
    print (2)

else:
    print(1)