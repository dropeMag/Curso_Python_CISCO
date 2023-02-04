try:
    print('3')
    x = 1 / 0
    print('2')

except ZeroDivisionError:
    print('ERRO!')

print('1')
