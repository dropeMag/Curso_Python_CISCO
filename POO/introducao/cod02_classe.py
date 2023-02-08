class Pilhas:
    def __init__(self):
        print('Criando nova pilha!')
        self.pilha_lista = []
        self.__segredo = 'Não revele!'


pilha_1 = Pilhas()
print(len(pilha_1.pilha_lista))
print(pilha_1.__segredo)
