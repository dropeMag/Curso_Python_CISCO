# RAISE (olhar página 49 do caderno)

try:
    print('E lá vamos nós!')
    raise KeyboardInterrupt
    # o restante aqui escrito não será levado em conta
except KeyboardInterrupt:
    print('O programa foi encerrado!')
