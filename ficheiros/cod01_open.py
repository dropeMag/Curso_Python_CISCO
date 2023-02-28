stream = open('teste.txt', mode='r+', encoding='UTF-8')

print(stream)
for linha in stream:
    print(linha)

stream.close()
