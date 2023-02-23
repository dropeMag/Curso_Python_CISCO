def fun(args, func):
    for x in args:
        print(func(x), end=' ')


fun([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

print()

teste = list(map(lambda x: 2 * x**2 - 4 * x + 2, [x for x in range(-2, 3)]))
for x in teste:
    print(x, end=' ')
