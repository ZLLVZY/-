class SubSystemOne(object):
    """docstring for SubSystem"""
    def __init__(self):
        super(SubSystemOne, self).__init__()
        pass
    def MethodOne(self):
        """docstring for Methodone"""
        print("子系统方法一")

class SubSystemTwo(object):
    """docstring for SubSystem"""
    def __init__(self):
        super(SubSystemTwo, self).__init__()
        pass
    def MethodTwo(self):
        """docstring for Methodone"""
        print("子系统方法二")

class SubSystemThree(object):
    """docstring for SubSystem"""
    def __init__(self):
        super(SubSystemThree, self).__init__()
        pass
    def MethodThree(self):
        """docstring for Methodone"""
        print("子系统方法三")

class SubSystemFour(object):
    """docstring for SubSystem"""
    def __init__(self):
        super(SubSystemFour, self).__init__()
        pass
    def MethodFour(self):
        """docstring for Methodone"""
        print("子系统方法四")

class Facade(object):
    """docstring for Facade"""
    def __init__(self):
        super(Facade, self).__init__()
        self.one=SubSystemOne()
        self.two=SubSystemTwo()
        self.three=SubSystemThree()
        self.four=SubSystemFour()
    
    def MethodA(self):
        print('方法组A() ----')
        self.one.MethodOne()
        self.two.MethodTwo()
        self.four.MethodFour()
    
    def MethodB(self):
        print('方法组B() ----')
        self.two.MethodTwo()
        self.three.MethodThree()
