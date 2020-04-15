class GameRole(object):
    def __init__(self):
        pass
    def GetInitState(self):
        self.vit=100
        self.atk=100
        self.de=100

    def StateDisplay(self):
        print("角色当前状态：")
        print("体力：%s" % self.vit)
        print("攻击力：%s" % self.atk)
        print("防御力：%s" % self.de)

    def Fight(self):
        self.vit=0
        self.atk=0
        self.de=0

    def SaveState(self):
        return RoleStateMemento(self.vit,self.atk,self.de)

    def RecoveryState(self,memento):
        self.vit=memento.vit
        self.atk=memento.atk
        self.de=memento.de

class RoleStateMemento(object):
    def __init__(self,vit,atk,de):
        self.vit=vit
        self.atk=atk
        self.de=de

class RoleStateCaretaker(object):
    def __init__(self):
        self.memento=None
    