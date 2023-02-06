# TRY/EXCEPT em um loop

while True:
    try:
        x = int(input("Digite um inteiro: "))
        break
    except ValueError:
        print("Valor inválido! Tente novamente...")

print('Agora foi.')
