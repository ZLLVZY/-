class Company(object):
    def __init__(self,name):
        self.name=name
    def Add(self,c):#增加
        pass
    def Remove(self,c):#移除
        pass
    def Display(self,depth):
        pass
    def LineOfDuty(self):
        pass

class ConcreteCompany(Company):
    def __init__(self,name):
        super(ConcreteCompany,self).__init__(name)
        self.children=[]
    def Add(self,c):
        self.children.append(c)
    def Remove(self,c):
        self.children.remove(c)
    def Display(self,depth):
        for i in range(depth):
            print("-",end='')
        print(self.name)
        for component in self.children:
            component.Display(depth+2)
    def LineOfDuty(self):
        for component in self.children:
            component.LineOfDuty()

class HRDepartment(Company):
    def Display(self,depth):
        for i in range(depth):
            print("-",end='')
        print(self.name)
    def LineOfDuty(self):
        print("%s 员工招聘培训管理" % self.name)

class FinaceDepartment(Company):
    def Display(self,depth):
        for i in range(depth):
            print("-",end='')
        print(self.name)
    def LineOfDuty(self):
        print("%s 公司财务收支管理" % self.name)