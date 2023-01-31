from verificador_de_resposta import verificar_resposta as verif


def menu_principal():
    print('='*35,
          f"{'Escolha uma opção':^35}",
          '='*35,
          '[01] Cálculo Simples',
          '[02] Cálculo Complexo',
          '[03] Conversão de Moedas',
          '='*35, sep='\n')

    verif.verificar_resposta(3, origem='menu')


menu_principal()
