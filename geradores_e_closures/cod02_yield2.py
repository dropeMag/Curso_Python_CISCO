def com_return():
    return "Só fica aqui"
    # return "Nunca vem pra cá"
    # return "Nem aqui"


def cria_gerador():
    yield "Começa aqui"
    yield "Continua aqui"
    yield "Termina aqui"


gerador = cria_gerador()
print(next(gerador))
print(next(gerador))
print(next(gerador))

# next() vai rodar todo o código da função até encontrar um yield

castigo = com_return()
print(castigo)
print(castigo)
print(castigo)
