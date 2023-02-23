import random

valores = [random.randint(0, 100) for x in range(10)]
pares = list(filter(lambda x: x % 2 == 0, valores))

print(valores)
print(pares)

print('=' * 70)

lista = [random.choice([True, False]) for y in range(10)]
verdadeiros = list(filter(lambda y: y, lista))

print(lista)
print(verdadeiros)
