import time

comeco = time.time()

input('Pressione qualquer tecla para finalizar: ')

fim = time.time()

tempo = fim - comeco

print(f"Você levou {tempo:.0f} segundos para finalizar o programa")
