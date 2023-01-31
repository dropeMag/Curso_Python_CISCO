from random import *

iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(random())                     # produz um float x do intervalo (0:1)
print('-='*15)
print(randrange(3))                 # escolhe no intervalo (:x)
print(randrange(1, 3))              # escolhe no intervalo (y:x)
print(randrange(1, 3, 2))           # escolhe no intervalo (y:x:z)
print('-='*15)
print(randint(1, 3))                # escolhe um valor entre x e y (incluindo x e y)
print('-='*15)
print(choice(iterable))             # escolhe um valor de iterable
print(list(sample(iterable, 4)))    # cria uma lista com x valores de iterable, sem repetição
