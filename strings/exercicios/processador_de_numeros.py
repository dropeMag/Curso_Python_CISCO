strng = input('Entre com uma sequencia de números separados por espaço: ')
lista = strng.split()
total, cont = 0, 0

for x in lista:
    if not x.isnumeric():
        print(x, 'não é um valor válido!')
        break

    total += float(x)
    cont += 1

    if cont == len(lista):
        print('O total da soma é:', total)
