from verificador_de_resposta import verificar_resposta as verif

from conversor_moedas.lista_taxas_cambio import *


def fun_real_estr(num=0):
    if num == 0:
        print(' ',
              'Escolha o Nº da moeda atual',
              sep='\n')
        verif.verificar_resposta(7, 'conv1')

    else:
        val = float(input('Valor em Real: ').strip().replace(',', '.'))
        print(f"R$ {val} em {lista_moedas[num-1]} é:", lista_cifroes[num-1], float(f"{val*float(lista_taxas[num-1]):.2f}"))
