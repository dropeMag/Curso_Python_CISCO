class SuperA:
    var_a = 'Variable A'


class SuperB:
    var_b = 'Variable B'


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, '|', obj.var_b)
