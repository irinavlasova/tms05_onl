a = input("Загаданное число: ")
print(a)
while True:
    b = input("Ваше число: ")
    c = 0
    k = 0
    for i in range(0, 4):
        if b[i] == a[i]:
            c += 1
        if b[i] != a[i]:
            for j in a:
                if b[i] == j:
                    k += 1
    print("быков: ", c)
    print("коров: ", k)
    if c == 4:
        print("Победа!")
        break