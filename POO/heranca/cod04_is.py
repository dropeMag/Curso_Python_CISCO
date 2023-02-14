class Teste:
    def __init__(self, val):
        self.val = val


obj1 = Teste(0)
obj2 = Teste(0)
obj3 = obj1
obj3.val += 1

print(obj1 is obj2)
print(obj2 is obj3)
print(obj1 is obj3)

print('-' * 30)

print(obj1.val, obj2.val, obj3.val)

print('-' * 30)

str1 = 'Olá, '
str2 = 'Olá, Mundo'
str1 += 'Mundo'

print(str1 == str2)
print(str1 is str2)
