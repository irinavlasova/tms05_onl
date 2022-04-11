numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers = [n for n in numbers if n >= 0]
print(positive_numbers)
sentence = " the quick brown fox jumps over the lazy dog"
list_1 = sentence.split()
list_2 = []
for x in list_1:
    if x != 'the':
        x = len(x)
        list_2.append(x)
print(list_2)