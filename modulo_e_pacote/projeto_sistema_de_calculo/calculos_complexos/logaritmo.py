from math import log


def fun_logaritmo():
    print('='*35,
          'Escolha os valores do logaritmo',
          sep='\n')

    val = int(input('Valor Inteiro: ').strip())
    base = int(input('Base do Log: ').strip())

    print('O resultado do logaritmo é:', log(val, base))
