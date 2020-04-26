class UnitedNations(object):
    def __init__(self):
        pass
    def Declare(self,message,colleague):
        pass

class Country(object):
    def __init__(self,mediator):
        self.mediator=mediator

class USA(Country):
    def __init__(self,mediator):
        super(USA,self).__init__(mediator)
    def Declare(self,message):
        self.mediator.Declare(message,self)
    def GetMessage(self,message):
        print("美国获得对方信息: "+message)

class Iraq(Country):
    def __init__(self,mediator):
        super(Iraq,self).__init__(mediator)
    def Declare(self,message):
        self.mediator.Declare(message,self)
    def GetMessage(self,message):
        print("伊拉克获得对方信息: "+message)

class UnitedNationsSecurityCouncil(UnitedNations):
    def __init__(self):
        super(UnitedNationsSecurityCouncil,self).__init__()
        self.colleague1=None
        self.colleague2=None
    def Declare(self,message,colleague):
        if (colleague==self.colleague1):
            self.colleague2.GetMessage(message)
        else:
            self.colleague1.GetMessage(message)