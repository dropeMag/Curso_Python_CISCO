from calculos_simples import menu_calculo_simples as menu_simples
from calculos_complexos import menu_calculo_complexo as menu_complexo
from conversor_moedas import menu_conversor_moedas as menu_conversor
from conversor_moedas import real_estrangeiro, estrangeiro_real


def verificar_resposta(opcoes, origem, atencao=False):
    if atencao:
        print(f'--> Opções válidas são de 1 a {opcoes}!')

    resposta_do_user = int(input('Escolha: ').strip())

    if resposta_do_user in range(1, opcoes+1):
        print('')
        if origem == 'menu':
            if resposta_do_user == 1:
                menu_simples.menu_calc1()
            elif resposta_do_user == 2:
                menu_complexo.menu_calc2()
            elif resposta_do_user == 3:
                menu_conversor.menu_calc3()

        elif origem == 'calc1':
            menu_simples.menu_calc1(resposta_do_user)

        elif origem == 'calc2':
            menu_complexo.menu_calc2(resposta_do_user)

        elif origem == 'calc3':
            menu_conversor.menu_calc3(resposta_do_user)

        elif origem == 'conv1':
            real_estrangeiro.fun_real_estr(resposta_do_user)

        elif origem == 'conv2':
            estrangeiro_real.fun_estr_real(resposta_do_user)

        elif origem == 'conv3':
            return resposta_do_user

    else:
        return verificar_resposta(opcoes, origem, atencao=True)
