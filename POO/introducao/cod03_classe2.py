class Pilha:
    def __init__(self):
        self.lista = []

    def push(self, val):
        self.lista.append(val)

    def pop(self):
        self.lista.pop()


stack1 = Pilha()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.lista)

stack1.pop()
print(stack1.lista)

print('=' * 20)

stack2 = Pilha()
stack2.push(stack1.lista)
print(stack2.lista)

print('=' * 20)

stack2.pop()
print(stack2.lista)
print(stack1.lista)
