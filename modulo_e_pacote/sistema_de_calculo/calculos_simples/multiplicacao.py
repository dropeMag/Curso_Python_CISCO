def fun_multiplicar():
    print('='*35,
          'Escolha dois valores para multiplicar',
          sep='\n')

    val1 = float(input('Valor 1: ').strip())
    val2 = float(input('Valor 2: ').strip())

    print('O resultado da multiplicação é:', val1*val2)
