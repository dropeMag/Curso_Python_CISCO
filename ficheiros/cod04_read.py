stream = open('teste.txt', mode='rt', encoding='utf-8')

print(stream.read())
# não usar read() em ficheiros com comprimentos muito grandes

stream.close()
