# FINALLY sempre será executado

try:
    raise ArithmeticError('legenda personalizada para aparecer no prompt')
finally:
    print('Sou executado! Com ou sem erro.')
