class Super1:
    pass


class Super2:
    pass


class Sub(Super1, Super2):
    pass


def printa_bases(cls):
    print('(', end=' ')

    for x in cls.__bases__:
        print(x.__name__, end=' ')

    print(')')


printa_bases(Super1)
printa_bases(Super2)
printa_bases(Sub)
