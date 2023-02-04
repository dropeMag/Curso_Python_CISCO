# ASSERT (olhar página 49 do caderno)

from math import sqrt

x = float(input('Insira um valor positivo: '))
# assert x >= 0.0

try:
    assert x >= 0.0
    print(sqrt(x))
except AssertionError:
    print('Errou, bixo!')
