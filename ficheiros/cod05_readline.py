import time

stream = open('teste.txt', mode='rt', encoding='utf-8')

for x in range(10):
    print(stream.readline(), end='')
    time.sleep(.3)

stream.close()
