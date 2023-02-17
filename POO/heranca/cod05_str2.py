class Super:
    def __init__(self):
        pass

    def __str__(self):
        return 'Class Super'


class Sub(Super):
    def __init__(self):
        Super.__init__(self)

    # def __str__(self):
    #     return 'Class Sub'


obj = Sub()
print(obj)
