class Sla:
    def __init__(self, val):
        self.atr1 = True
        if val > 0:
            self.atr2 = True


obj1 = Sla(1)

if hasattr(obj1, 'atr2'):
    print('E assim verificamos se um obj tem x atributo.')
