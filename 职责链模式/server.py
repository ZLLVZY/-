class Request(object):
    def __init__(self):
        pass
    def RequestType(self,requestType):
        self.requestType=requestType
    def RequestContent(self,requestContent):
        self.requestContent=requestContent
    def Number(self,number):
        self.number=number

class Manager(object):
    def __init__(self,name):
        self.name=name
    def SetSuperior(self,superior):
        self.superior=superior
    def RequestApplication(self,request):
        pass

class CommonManager(Manager):
    def __init__(self,name):
        super(CommonManager,self).__init__(name)
    def RequestApplication(self,request):
        if request.requestType=='请假' and request.number<=2:
            print('%s:%s 数量%s 被批准' % (self.name,request.requestType,request.number))
        elif (self.superior != None):
            self.superior.RequestApplication(request)

class Majordomo(Manager):
    def __init__(self,name):
        super(Majordomo,self).__init__(name)
    def RequestApplication(self,request):
        if request.requestType=='请假' and request.number<=5:
            print('%s:%s 数量%s 被批准' % (self.name,request.requestType,request.number))
        elif (self.superior != None):
            self.superior.RequestApplication(request)

class GeneralManager(Manager):
    def __init__(self,name):
        super(GeneralManager,self).__init__(name)
    def RequestApplication(self,request):
        if request.requestType=='请假':
            print('%s:%s 数量%s 被批准' % (self.name,request.requestType,request.number))
        if request.requestType=='加薪' and request.number<=500:
            print('%s:%s 数量%s 被批准' % (self.name,request.requestType,request.number))
        if request.requestType=='加薪' and request.number>500:
            print('%s:%s 数量%s 再说吧' % (self.name,request.requestType,request.number))
        
        
         
