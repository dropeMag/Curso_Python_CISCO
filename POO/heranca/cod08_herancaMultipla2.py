class Alfa:
    var = "a"
    var_alfa = "AA"

    def fun(self):
        return "Alfa"


class Beta:
    var = "b"
    var_beta = "BB"

    def fun(self):
        return "Beta"


class Sub(Alfa, Beta):
    pass


obj = Sub()

print(obj.var, obj.var_alfa, obj.var_beta, obj.fun())
