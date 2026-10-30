class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def min(self):
        return self.a - self.b
    def ymn(self):
        return self.a * self.b
    def deli(self):
        return self.a / self.b

print('Введите числа')
a = int(input())
b = int(input())
calcy = calc(a, b)
print('Что сделать?')
op = input()
if op == "+":
    print(calcy.add())
elif op == "-":
    print(calcy.min())
elif op == '*':
    print(calcy.ymn())
elif op == "/":
    print(calcy.deli())
else:
    print('Не знаю такой операции')
