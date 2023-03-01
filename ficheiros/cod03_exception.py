try:
    open('naoExiste', mode='r', encoding=None)
except IOError as exc:
    print(exc)
    print(exc.errno)
