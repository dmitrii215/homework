immutable_war = (1, 'пять', 3.5, [1, 2, 3], True)
print(type(immutable_war))
print(immutable_war)


 #immutable_war[0] = 2
# TypeError: объект 'tuple' не поддерживает назначение элемента
# главное свойство кортежа: не возможность изменить его содержимое
# после его создания


'''список'''
mutable_list = [1, 2, 'a', 'b']

m = mutable_list

m[0] = 9
print(m)

m[0] = m[0] + 6
print(m)

m.append('modifed')
print(m)



