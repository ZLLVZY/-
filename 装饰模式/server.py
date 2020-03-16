class Person(object):
    def __init__(self,name):
        self.name=name
    def show(self):
        print('装扮的%s' % self.name)

class Finery(Person):
    def __init__(self):
        pass
    def Decorate(self,component):
        self.component=component
    def show(self):
        if (self.component!=None):
            self.component.show()

class Tshirts(Finery):
    def __init__(self):
        pass
    def show(self):
        print('大T恤')
        super().show()#调用父类的show()方法

class Shoes(Finery):
    def __init__(self):
        pass
    def show(self):
        print('大皮鞋')
        super().show()