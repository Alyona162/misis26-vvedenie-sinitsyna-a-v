class calc:
    def __init__(self, pol, rost, ves):
        self.pol = pol
        self.rost = rost
        self.ves = ves
    def ras(self):
        if self.pol == 'м':
            return self.rost - 100
        elif self.pol == 'ж':
            return self.rost - 110
    def delta(self):
        if self.pol == 'м':
            return (self.rost - 100) - self.ves
        elif self.pol == 'ж':
            return (self.rost - 110) - self.ves
print('м/ж?')
a = input()
print('Какой у вас рост в см?')
b = int(input())
print('Какой у вас вес в кг?')
c = int(input())
rasi = calc(a, b, c)
print('Идеальный вес для вас:', rasi.ras(), 'кг')
if rasi.delta() > 0: 
    print('Вам нужно набрать', abs(rasi.delta()), 'кг')
elif rasi.delta() < 0:
    print('Вам нужно сбросить', abs(rasi.delta()), 'кг')
else:
    print('У вас идеальный вас, вы молодец!!')
        