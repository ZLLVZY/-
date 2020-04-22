class HandsetSoft(object):
    def __init__(self):
        pass

class HandsetGame(HandsetSoft):
    def __init__(self):
        pass
    def Run(self):
        print("运行手机游戏")

class HandsetAddressList(HandsetSoft):
    def __init__(self):
        pass
    def Run(self):
        print("运行手机通讯录")

class HandsetBrand(object):
    def __init__(self):
        pass
    def SetHandsetSoft(self,soft):
        self.soft=soft
    def Run(self):
        pass

class HandsetBrandN(HandsetBrand):
    def Run(self):
        self.soft.Run()

class HandsetBrandM(HandsetBrand):
    def Run(self):
        self.soft.Run()
