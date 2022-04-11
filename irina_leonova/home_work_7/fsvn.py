#    Для классов "торговый центр" и "школа" придумайте 1 дополнительное свойство и 1 дополнительный метод.
#   Создайте объекты всех 3-х классов. Посмотрите их свойства, повызывайте их методы.
class Building:
    def __init__(self):
        self.building = 'Это здание - '

    def building_method(self):
        print(f'Посторойка{self.building}')

    building_1 = 0


class ShopMall(Building):
    def __add__(self):
        self.building = "Это здание - тц"


class School(Building):
    def __add__(self):
        self.building = "Это здание - школа"


a = Building
a.building()
b = ShopMall
b.building()
c = School
c.building()
print(ShopMall)
print(School)
