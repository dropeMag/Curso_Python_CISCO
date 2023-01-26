from math import factorial


def fun_fatorar():
    print('='*35,
          'Escolha um número inteiro para fatorar',
          sep='\n')

    val = int(input('Valor Inteiro: ').strip())

    print('O resultado da fatoração é:', factorial(val))
