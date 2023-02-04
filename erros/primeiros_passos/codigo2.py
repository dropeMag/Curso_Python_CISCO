# DUAS OU MAIS EXCEÇÕES JUNTAS

try:
    num = int(input('Entre com um número: '))
    res = 1 / num
    print('Resultado:', res)
except (ZeroDivisionError, ValueError):
    print('Valor introduzido é inválido!')
