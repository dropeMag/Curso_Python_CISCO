x = 1


def y():
    return "ok"


class Z:
    pass


print(callable(x))
print(callable(y))
print(callable(Z))
