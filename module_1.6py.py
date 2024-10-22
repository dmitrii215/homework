'''словарь'''

my_dict = {'Дмитрий': 1973, 'Маша': 1975}
print(my_dict)

print(my_dict['Дмитрий'])

print(my_dict.get('Маша'),': None')

my_dict.update({'Паша': 1988, 'Катя': 2002})
print(my_dict)

print(my_dict.pop('Маша'))

print(my_dict)

'''множества'''

my_set = {1, 2, 3, 2, 3,  'str', 'str', True}
print(my_set)

my_set.add('4')
my_set.add(5)
my_set.add(False)
print(my_set)

my_set.remove(2)
print(my_set)
