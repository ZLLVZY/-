class Action(object):
    def __init__(self):
        pass
    def GetManConclusion(self,concreteElementA):
        pass
    def GetWomanConclusion(self,concreteElementB):
        pass

class Person(object):
    def __init__(self):
        pass
    def Accept(self,visitor):
        pass

class Success(Action):
    def GetManConclusion(self,concreteElementA):
        print("%s %s时，背后多半有一个伟大的女人。" % (type(concreteElementA).__name__,type(self).__name__))
    def GetWomanConclusion(self,concreteElementB):
        print("%s %s时，背后大多有一个不成功的男人。" % (type(concreteElementB).__name__,type(self).__name__))

class Failing(Action):
    def GetManConclusion(self,concreteElementA):
        print("%s %s时，闷头喝酒，谁也不用劝。" % (type(concreteElementA).__name__,type(self).__name__))
    def GetWomanConclusion(self,concreteElementB):
        print("%s %s时，眼泪汪汪，谁也劝不了。" % (type(concreteElementB).__name__,type(self).__name__))

class Amativeness(Action):
    def GetManConclusion(self,concreteElementA):
        print("%s %s时，凡是不懂也要装懂。" % (type(concreteElementA).__name__,type(self).__name__))
    def GetWomanConclusion(self,concreteElementB):
        print("%s %s时，遇事懂也装作不懂。" % (type(concreteElementB).__name__,type(self).__name__))

class Marriage(Action):
    def GetManConclusion(self,concreteElementA):
        print("%s %s时，感慨道：恋爱游戏终结时，‘有妻徒刑’遥无期。" % (type(concreteElementA).__name__,type(self).__name__))
    def GetWomanConclusion(self,concreteElementB):
        print("%s %s时，欣慰曰：爱情长跑路漫漫，婚姻保险保平安。" % (type(concreteElementB).__name__,type(self).__name__))

class Man(Person):
    def Accept(self,visitor):
        visitor.GetManConclusion(self)

class Woman(Person):
    def Accept(self,visitor):
        visitor.GetWomanConclusion(self)

class ObjectStructure(object):
    def __init__(self):
        self.elements=[]
    def Attach(self,element):
        self.elements.append(element)
    def Detach(self,element):
        self.elements.remove(element)
    def Display(self,visitor):
        for e in self.elements:
            e.Accept(visitor)