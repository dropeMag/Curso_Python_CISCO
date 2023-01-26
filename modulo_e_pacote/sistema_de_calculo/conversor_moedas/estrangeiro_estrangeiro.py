from verificador_de_resposta import verificar_resposta as verif

from conversor_moedas.lista_taxas_cambio import *


def fun_estr_estr():
    print(' ',
          'Escolha o Nº da moeda atual',
          sep='\n')
    num1 = verif.verificar_resposta(7, 'conv3')

    print(' ',
          'Escolha o Nº da moeda a ser convertida',
          sep='\n')
    num2 = verif.verificar_resposta(7, 'conv3')

    val = float(input(f"Valor em {lista_moedas[num1-1]}: ").strip().replace(',', '.'))
    print(f"{lista_cifroes[num1-1]} {val} em {lista_moedas[num2-1]} é:", lista_cifroes[num2-1], float(f"{(val/float(lista_taxas[num1 - 1])) * float(lista_taxas[num2 - 1]):.2f}"))
