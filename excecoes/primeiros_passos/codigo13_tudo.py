def divide(x, y):
    try:
        res = int(x) / int(y)
    except (ZeroDivisionError, ValueError) as err:
        print('Erro:', err)
    else:
        print("Resultado:", res)
    finally:
        print("Finalizando!")


n1 = input('Numerador: ')
n2 = input('Denominador: ')

divide(n1, n2)
