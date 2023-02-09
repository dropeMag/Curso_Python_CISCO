class Exemplo:
    var = 0

    def __init__(self, val):
        Exemplo.var += val


print(Exemplo.__dict__)
calc1 = Exemplo(1)

print(Exemplo.__dict__)
calc2 = Exemplo(2)

print(Exemplo.__dict__)
calc3 = Exemplo(3)

print(Exemplo.__dict__)
