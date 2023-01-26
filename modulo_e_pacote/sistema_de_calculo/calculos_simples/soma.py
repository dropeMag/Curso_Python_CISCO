def fun_somar():
    print('='*35,
          'Escolha dois valores para somar',
          sep='\n')

    val1 = float(input('Valor 1: ').strip())
    val2 = float(input('Valor 2: ').strip())

    print('O resultado da soma é:', val1+val2)
