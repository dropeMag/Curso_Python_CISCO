frase = input('Entre com a frase para descriptografar: ').upper()
desc = list()

for x in frase:
    y = ord(x) - 1

    if y < ord('A'):
        y = ord('Z')

    desc.append(chr(y))

print('A tradução da frase fica:', ''.join(desc))
