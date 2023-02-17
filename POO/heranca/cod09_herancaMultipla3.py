class Super:
    def acao(self):
        print("Ação do Super")

    def fun(self):
        self.acao()


class Sub(Super):
    def acao(self):
        print("Ação do Sub")


obj_super = Super()
obj_sub = Sub()

obj_super.fun()
obj_sub.fun()
