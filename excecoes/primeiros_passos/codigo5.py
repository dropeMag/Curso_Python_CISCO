# HIRERQUIA

try:
    x = 1/0
except ZeroDivisionError:
    print('zero')
except ArithmeticError:
    print('Arithmetic')

print('-' * 65)

try:
    x = 1/0
except ArithmeticError:
    print('Nesse caso gera Warning por Arithmetic vir antes de ZeroDivision')
    print('Arithmetic')
except ZeroDivisionError:
    print('zero')
