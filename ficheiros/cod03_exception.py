try:
    open('naoExiste', mode='r', encoding=None)
except BaseException as exc:
    print(exc)
