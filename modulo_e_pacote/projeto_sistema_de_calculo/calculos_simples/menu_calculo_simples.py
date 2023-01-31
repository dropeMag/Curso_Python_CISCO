from verificador_de_resposta import verificar_resposta as verif

from calculos_simples import soma, subtracao, multiplicacao, divisao


def menu_calc1(resposta=0):
    if resposta == 1:
        return soma.fun_somar()
    elif resposta == 2:
        return subtracao.fun_subtrair()
    elif resposta == 3:
        return multiplicacao.fun_multiplicar()
    elif resposta == 4:
        return divisao.fun_dividir()

    print('='*35,
          f"{'Escolha um cálculo simples':^35}",
          '='*35,
          '[01] Soma',
          '[02] Subtração',
          '[03] Multiplicação',
          '[04] Divisão',
          '='*35, sep='\n')

    resposta = verif.verificar_resposta(4, 'calc1')
