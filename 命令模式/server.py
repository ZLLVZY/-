import time
class Barbecuer(object):
    def __init__(self):
        pass
    def BakeMutton(self):
        print("烤羊肉串！")
    def BakeChickenWing(self):
        print("烤鸡翅！")

class Command(object):
    def __init__(self,receiver):
        self.receiver=receiver
    def ExcuteCommand(self):
        pass

class BakeMuttonCommand(Command):
    def __init__(self,receiver):
        super(BakeMuttonCommand,self).__init__(receiver)
    def ExcuteCommand(self):
        self.receiver.BakeMutton()

class BakeChickenWingCommand(Command):
    def __init__(self,receiver):
        super(BakeChickenWingCommand,self).__init__(receiver)
    def ExcuteCommand(self):
        self.receiver.BakeChickenWing()

class Waiter(object):
    def __init__(self):
        self.orders=[]
    def SetOrder(self,command):
        if (isinstance(command,BakeChickenWingCommand)):
            print('服务员：鸡翅没有了，请点别的烧烤')
        else:
            self.orders.append(command)
            print("增加订单:"+str(command)+' 时间:'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    def CancelOrder(self,command):
        self.orders.remove(command)
        print("取消订单:"+str(command)+'时间:'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    def Notify(self):
        for cmd in (self.orders):
            cmd.ExcuteCommand()

