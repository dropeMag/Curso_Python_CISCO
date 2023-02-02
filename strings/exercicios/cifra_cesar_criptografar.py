frase = input('Entre com uma frase para criptografar: ').upper()
crip = list()

for x in frase:
    if x.isspace():
        continue

    y = ord(x) + 1

    if y > ord('Z'):
        y = ord('A')

    crip.append(chr(y))

print('A frase criptografada fica:', ''.join(crip))
