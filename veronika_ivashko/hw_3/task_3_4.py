"""
4. Напишите программу которая удаляет пробел в начале, в конце строки
"""

some_string = 'test some more case '
first_symbol = some_string[0].replace(' ', '')
last_symbol = some_string[-1].replace(' ', '')
result = first_symbol + some_string[1:-1] + last_symbol

print(f'Length of initial row "{some_string}" is {len(some_string)} symbols.')
print(f'Length of cleansed row "{result}" is {len(result)} symbols.')
