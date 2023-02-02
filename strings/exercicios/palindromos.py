palavra = input('Entre com uma palavra: ').replace(' ', '').lower()
sub = 0
resp = ' '

for x in palavra:
    tam = len(palavra) - sub
    if x == palavra[tam-1]:
        sub += 1
    else:
        resp = ' não '
        break

print('A palavra' + resp + 'é um Palíndromo')
