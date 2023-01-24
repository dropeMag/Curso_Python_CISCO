from sys import path

path.append('..\\modules_and_packages\\primeiro_modulo')

from modulos.mod_teste import *

# print(__counter)

zeroes = [i+1 for i in range(5)]
ones = [i+1 for i in range(5)]
print(sum1(zeroes))
print(prod1(ones))



