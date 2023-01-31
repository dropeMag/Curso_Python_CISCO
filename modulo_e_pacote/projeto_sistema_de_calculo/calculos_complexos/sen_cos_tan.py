from math import sin, cos, tan


def fun_sen_cos_tan():
    print('='*35,
          'Escolha o número para calcular',
          sep='\n')

    val = int(input('Valor Inteiro: ').strip())

    print('Os resultados do cálculo são:',
          f'    Seno = {sin(val):.2f}',
          f'    Cosseno = {cos(val):.2f}',
          f'    Tangente = {tan(val):.2f}',
          sep='\n')
