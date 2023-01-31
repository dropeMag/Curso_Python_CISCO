from verificador_de_resposta import verificar_resposta as verif

from conversor_moedas.lista_taxas_cambio import *


def fun_estr_real(num=0):
    if num == 0:
        print(' ',
              'Escolha o Nº da moeda a ser convertido',
              sep='\n')
        verif.verificar_resposta(7, 'conv2')

    else:
        val = float(input(f"Valor em {lista_moedas[num-1]}: ").strip().replace(',', '.'))
        print(f"{lista_cifroes[num-1]} {val} em Real é:", 'R$', float(f"{val/float(lista_taxas[num-1]):.2f}"))
