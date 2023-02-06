# ELSE ´será executado quando não houver nenhuma exceção

try:
    num = int(input('Digite um denominador: '))
    x = 1/num
except BaseException:
    print('Ocorreu um erro!')
    print('Else não será executado!')
else:
    print('Não ocorreu um erro!')
    print('Então sou executado!')
