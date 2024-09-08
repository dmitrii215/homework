'''словари и множества'''

my_dikt = {"Дмитрий":1973}
print(my_dikt)

print(my_dikt.values())

my_dikt = {"Дмитрий":1973}
my_dikt["Валера"]=2000
my_dikt["Олег"]=2002
print(my_dikt)

del my_dikt["Олег"]
print(my_dikt.items())



'''задача множества'''
my_set = {1, 2, 2, 3, 44, 5, 5, 'str', False, (1, 2, 3)}
print(my_set)

print(my_set.add((99, 'кирпич')))
print(my_set.remove('str'))
print(my_set)














