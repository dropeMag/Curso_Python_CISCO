def powers_1(n):
    power = 1
    for i in range(n):
        return power
        # power *= 2


def powers_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


a = [powers_1(5)]
print(a)

b = [x for x in powers_2(5)]
print(b)
