pilha1 = []
pilha2 = []


def push(pilha, val):
    pilha.append(val)


def pop(pilha):
    pilha.pop()


push(pilha1, 1)
push(pilha1, 2)
push(pilha1, 3)
print(pilha1)
pop(pilha1)
print(pilha1)

print('=' * 25)

push(pilha2, 'Olá')
push(pilha2, 'Mundo')
push(pilha2, 'Lindo')
print(pilha2)
pop(pilha2)
pop(pilha2)
print(pilha2)
