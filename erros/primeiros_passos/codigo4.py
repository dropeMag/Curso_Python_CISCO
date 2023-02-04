# ÁRVORE DA EXCEÇÃO (olhar página 49 do caderno)

try:
    x = 1 / 0
except BaseException:
    print('Base de toda exceção')

try:
    x = 1 / 0
except Exception:
    print('Tipo de exceção para erros não causados pelo sistema')

try:
    x = 1 / 0
except ArithmeticError:
    print('Exceção para erros matemáticos')

try:
    x = []
    y = x[1]
except LookupError:
    print('Exceção para keys/indexes inválidos')
