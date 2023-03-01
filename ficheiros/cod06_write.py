stream = open('teste.txt', mode='wt', encoding='utf-8')

for x in range(10):
    stream.write(str(x) + "\n")

stream.close()
