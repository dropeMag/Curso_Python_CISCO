def read_int(prompt, min, max):
    try:
        x = int(input(prompt))
        assert x in range(min, max+1)
    except ValueError:
        return 'O valor inserido não é válido!'
    except AssertionError:
        return 'Número fora dos limites!'
    return f'O valor é: {x}'


v = read_int("Entre com um número de -10 a 10: ", -10, 10)

print(v)
