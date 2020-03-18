class GiveGift(object):
    def __init__(self):
        pass
    def GiveDolls(self):
        pass
    def GiveFlowers(self):
        pass
    def GiveChocolate(self):
        pass

class Persuit(GiveGift):
    def __init__(self,mm):
        self.mm=mm
    def GiveDolls(self):
        print(self.mm.name+"送你洋娃娃")
    def GiveFlowers(self):
        print(self.mm.name+"送你鲜花")
    def GiveChocolate(self):
        print(self.mm.name+"送你巧克力")

class Proxy(GiveGift):
    def __init__(self,mm):
        self.gg=Persuit(mm)
    def GiveDolls(self):
        self.gg.GiveDolls()
    def GiveFlowers(self):
        self.gg.GiveFlowers()
    def GiveChocolate(self):
        self.gg.GiveChocolate()

class SchoolGirl(object):
    def __init__(self,name):
        self.name=name

