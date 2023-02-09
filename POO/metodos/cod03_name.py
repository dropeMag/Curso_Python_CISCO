class Classe:
    def __init__(self):
        self.__name__ = 'Paçoca'


print(Classe.__name__)
obj = Classe()
print(obj.__name__)
