try:
    x = 1/0
except ZeroDivisionError as err:
    print('Erro:', err)
    print('Tipo:', type(err))
