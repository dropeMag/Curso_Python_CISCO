# EXCEPTION DENTRO DE FUNÇÕES

def errou(x):
    try:
        return print(1/x)
    except ArithmeticError:
        print('Tá errando, bixo!')
    return


val = int(input('Insira um valor inteiro: '))

errou(val)
