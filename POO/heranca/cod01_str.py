class Star:
    def __init__(self, nome, galaxia):
        self.nome = nome
        self.galaxia = galaxia

    def __str__(self):
        return self.nome + ' está em ' + self.galaxia


sol = Star('sol', 'Via Láctea')
print(sol)
