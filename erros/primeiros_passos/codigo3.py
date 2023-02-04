# MULTIPLOS EXCEPTs

try:
    num = int(input('Entre com um valor válido: '))
    res = 1 / num
    print('Resultado:', res)
except ZeroDivisionError:
    print('Impossível dividir por zero!')
except ValueError:
    print('Valor introduzido é inválido!')
