# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name = "Ivanou Ivan"
new_name = ' '.join(name.split(' ')[::-1])
print(new_name)
