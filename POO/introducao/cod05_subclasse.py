class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, val):
        self.pilha.append(val)


class Somador(Pilha):
    def __init__(self):
        Pilha.__init__(self)  # Sempre chame o __init__ da superclasse
        self.soma = 0

    def somar(self):
        self.soma = sum(self.pilha)


mostarda = Somador()
mostarda.push(1)
mostarda.push(2)
mostarda.push(3)
mostarda.push(4)
mostarda.push(5)

print(mostarda.pilha)
print(mostarda.soma)

mostarda.somar()

print(mostarda.soma)
print(mostarda.__dict__)
