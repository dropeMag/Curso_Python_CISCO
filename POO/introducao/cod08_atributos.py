class Exemplo:
    def __init__(self, var):
        if var % 2 == 0:
            self.atr1 = 'Atributo nº1'
        else:
            self.atr2 = 'Atributo nº2'


obj1 = Exemplo(2)
obj2 = Exemplo(1)

print(obj1.__dict__)
print(obj2.__dict__)
