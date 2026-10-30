print('Введите числа')
a = int(input())
b = int(input())
print('Что сделать?')
c = input()
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print(a/b)
else:
    print('Такой команды нет')
