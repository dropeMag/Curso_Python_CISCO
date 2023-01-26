from verificador_de_resposta import verificar_resposta as verif

from calculos_complexos import fatorial, logaritmo, potencia, sen_cos_tan


def menu_calc2(resposta=0):
    if resposta == 1:
        return fatorial.fun_fatorar()
    elif resposta == 2:
        return logaritmo.fun_logaritmo()
    elif resposta == 3:
        return potencia.fun_potenciar()
    elif resposta == 4:
        return sen_cos_tan.fun_sen_cos_tan()

    print('='*35,
          f"{'Escolha um cálculo complexo':^35}",
          '='*35,
          '[01] Fatorial',
          '[02] Logaritmo',
          '[03] Potenciação',
          '[04] Seno, Cosseno e Tangente',
          '='*35, sep='\n')

    resposta = verif.verificar_resposta(4, 'calc2')
