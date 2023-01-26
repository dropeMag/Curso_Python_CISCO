from verificador_de_resposta import verificar_resposta as verif

from conversor_moedas import real_estrangeiro, estrangeiro_real, estrangeiro_estrangeiro


def menu_calc3(resposta=0):
    if resposta != 0:
        print('=' * 35,
              f"{'Lista de Moedas':^35}",
              '=' * 35,
              f"{'Nº':^4}|{'Moeda':^7}|{'Nome da Moeda':^22}",
              '-' * 35,
              f"{'01':^4}|{'USD':^7}|{' Dólar Americano':22}",
              f"{'02':^4}|{'EUR':^7}|{' Euro':22}",
              f"{'03':^4}|{'GBP':^7}|{' Libra Esterlina':22}",
              f"{'04':^4}|{'JPY':^7}|{' Iene Japonês':22}",
              f"{'05':^4}|{'CHF':^7}|{' Franco Suíço':22}",
              f"{'06':^4}|{'CAD':^7}|{' Dólar Canadense':22}",
              f"{'07':^4}|{'AUD':^7}|{' Dólar Australiano':22}", sep='\n')

        if resposta == 1:
            return real_estrangeiro.fun_real_estr()
        elif resposta == 2:
            return estrangeiro_real.fun_estr_real()
        elif resposta == 3:
            return estrangeiro_estrangeiro.fun_estr_estr()

    print('='*35,
          f"{'Escolha um método de conversão':^35}",
          '='*35,
          '[01] Real para Estrangeiro',
          '[02] Estrangeiro para Real',
          '[03] Moedas Distintas',
          '='*35, sep='\n')

    resposta = verif.verificar_resposta(3, 'calc3')
