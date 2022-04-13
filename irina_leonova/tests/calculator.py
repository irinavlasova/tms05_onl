class Calculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calc = Calculator()
print(calc.sum(5, 4))
print(calc.sub(5, 4))
print(calc.mul(5, 4))
print(calc.div(5, 4))
