def fun_subtrair():
    print('='*35,
          'Escolha dois valores para subtrair',
          sep='\n')

    val1 = float(input('Valor 1: ').strip())
    val2 = float(input('Valor 2: ').strip())

    print('O resultado da subtração é:', val1-val2)
