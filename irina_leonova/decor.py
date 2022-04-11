def decorator(func):
    def put_on():
        a = func()
        for i in range(a):
            if i % 2 == 0:
                print("!")
            elif i % 3 == 0:
                print("*")
    return put_on()


@decorator
def my_age():
    x = 26
    return x
