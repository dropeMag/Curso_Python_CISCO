"""
print('Hello, Wolrd!')
print('I like to be a module')
print(__name__)
"""
#!/usr/bin/env python3
# essa linha de cima define aonde o interpretador do python esta (mais utilizado em sistemas Unix)

__counter = 0

def sum1(the_list):  # soma os valores de uma lista
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prod1(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == '__main__':
    print('I prefer to be a module, but I can do some testes for you.')
    my_list = [i+1 for i in range(5)]
    print(sum1(my_list) == 15)
    print(prod1(my_list) == 120)