import os
list_path = [ ]
for adress, papka, file in os.walk('c:\\'):
    for i in file:
        full_path = os.path.join(adress, i)
        list_path.append(full_path)
r = open('text.txt', 'w')
for x in list_path:
    r.write(x + '\n')
r.close()

