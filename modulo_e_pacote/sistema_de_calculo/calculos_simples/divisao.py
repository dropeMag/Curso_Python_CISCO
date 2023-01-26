def fun_dividir():
    print('='*35,
          'Escolha dois valores para dividir',
          sep='\n')

    val1 = float(input('Valor 1: ').strip())
    val2 = float(input('Valor 2: ').strip())

    print('O resultado da divisão é:', val1/val2)
