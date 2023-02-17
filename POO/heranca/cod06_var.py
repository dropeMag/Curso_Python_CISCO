class Super:
    varSup = 'Super'


class Sub(Super):
    varSub = 'Sub'


obj = Sub()
print(obj.varSup)
print(obj.varSub)
