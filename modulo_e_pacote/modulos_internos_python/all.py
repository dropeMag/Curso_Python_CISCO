iterable1 = 'djtfgb 0 uj', 123, 223, 's', True, 0
iterable2 = ''

print(all(iterable1))
print(all(iterable2))

"""
Funciona como:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
"""
