# При шифровании каждый символ заменяется другим, отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.

alfavit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
cod = input('Напишите ваше сообщение: ')
key = int(input("please enter a key(number from 1-25): "))
c = ""
for letter in cod:
    position = alfavit.find(letter)
    new_position = position + key
    if letter in alfavit:
        c = c + alfavit[new_position]
    else:
        c = c + letter
print('your message: ', c)
