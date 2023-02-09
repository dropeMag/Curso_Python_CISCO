class Classe:
    def mtd1(self):
        print('Boa Tarde, Itália.')

    def mtd2(self):
        print('Bom Dia, Brasil.')
        self.mtd1()


obj = Classe()
obj.mtd2()
