class Player(object):
    def __init__(self,name):
        self.name=name
    def Attack(self):
        pass
    def Defense(self):
        pass

class Forwards(Player):
    def Attack(self):
        print("前锋 %s进攻" % self.name)
    def Defense(self):
        print("前锋 %s防守" % self.name)

class Center(Player):
    def Attack(self):
        print("中锋 %s进攻" % self.name)
    def Defense(self):
        print("中锋 %s防守" % self.name)

class Guards(Player):
    def Attack(self):
        print("后卫 %s进攻" % self.name)
    def Defense(self):
        print("后卫 %s防守" % self.name)

class ForeignCenter(object):
    def __init__(self,name):
        self.name=name
    def 进攻(self):
        print("外籍中锋 %s进攻" % self.name)
    def 防守(self):
        print("外籍中锋 %s防守" % self.name)

class Translator(Player):
    def __init__(self,name):
        super(Translator,self).__init__(name)
        self.wjzf=ForeignCenter(self.name)
    def Attack(self):
        self.wjzf.进攻()
    def Defense(self):
        self.wjzf.防守()
