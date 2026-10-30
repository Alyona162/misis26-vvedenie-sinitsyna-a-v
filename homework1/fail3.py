def f(x, y, z):
    if z == '+':
        return x+y
    if z == '-':
        return x-y
    if z == '*':
        return x*y
    if z == '/':
        return x/y
while True:
    a = int(input())
    b = int(input())
    c = input()
    print(f(a, b, c))
