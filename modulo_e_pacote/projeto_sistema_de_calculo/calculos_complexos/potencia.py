from math import pow


def fun_potenciar():
    print('='*35,
          'Escolha os valores da potenciação',
          sep='\n')

    base = int(input('Base: ').strip())
    expo = int(input('Espoente: ').strip())

    print('O resultado da potenciação é:', pow(base, expo))
