class Subject(object):
    def __init__(self):
        pass
    def Notify(self):
        pass
    def SubjectState(self,action):
        pass

class Boss(Subject):
    def __init__(self):
        super(Boss,self).__init__()
        self.event=[]
    def Event(self,command):
        self.event.append(command)
    def Update(self):
        for i in self.event:
            i()
    def Notify(self):
        self.Update()
    def SubjectState(self,action):
        self.subjectstate=action

class Secretary(Subject):
    def __init__(self):
        super(Secretary,self).__init__()
    def Notify(self):
        self.Update()
    def SubjectState(self,action):
        self.subjectstate=action


class StockObserver(object):
    def __init__(self,name,sub):
        self.name=name
        self.sub=sub
    def CloseStockMarket(self):
        print(" %s,%s。关闭股票行情，继续工作！" % (self.sub.subjectstate,self.name))

class NBAObserver(object):
    def __init__(self,name,sub):
        self.name=name
        self.sub=sub
    def CloseNBADirectSeeding(self):
        print(" %s,%s。关闭NBA直播，继续工作！" % (self.sub.subjectstate,self.name))
