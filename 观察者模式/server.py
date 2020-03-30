class Subject(object):
    def __init__(self):
        self.observers=[]
    def Attach(self,observer):
        pass
    def Detach(self,observer):
        pass
    def Notify(self):
        pass
    def SubjectState(self,action):
        pass

class Boss(Subject):
    def __init__(self):
        super(Boss,self).__init__()
    def Attach(self,observer):
        self.observers.append(observer)
    def Detach(self,observer):
        self.observers.remove(observer)
    def Notify(self):
        for observer in self.observers:
            observer.Update()
    def SubjectState(self,action):
        self.subjectstate=action

class Secretary(Subject):
    def __init__(self):
        super(Secretary,self).__init__()
    def Attach(self,observer):
        self.observers.append(observer)
    def Detach(self,observer):
        self.observers.remove(observer)
    def Notify(self):
        for observer in self.observers:
            observer.Update()
    def SubjectState(self,action):
        self.subjectstate=action

class Observer(object):
    def __init__(self,name,sub):
        self.name=name
        self.sub=sub
    def Update():
        pass

class StockObserver(Observer):
    def __init__(self,name,sub):
        super(StockObserver,self).__init__(name,sub)
    def Update(self):
        print(" %s,%s。关闭股票行情，继续工作！" % (self.sub.subjectstate,self.name))

class NBAObserver(Observer):
    def __init__(self,name,sub):
        super(NBAObserver,self).__init__(name,sub)
    def Update(self):
        print(" %s,%s。关闭NBA直播，继续工作！" % (self.sub.subjectstate,self.name))