class LeiFeng(object):
    def __init__(self):
        pass
    def Sweep(self):
        print('扫地')
    def Wash(self):
        print('洗衣')
    def BuyRice(self):
        print('买米')

class UnderGraduate(LeiFeng):
    def __init__(self):
        pass

class Volunteer(LeiFeng):
    def __init__(self):
        pass

class IFactory(object):
    def __init__(self):
        pass
    def CreateLeiFeng(self):
        pass

class UnderGraduateFactory(IFactory):
    def __init__(self):
        pass
    def CreateLeiFeng(self):
        leifeng=UnderGraduate()
        return leifeng

class VolunteerFactory(IFactory):
    def __init__(self):
        pass
    def CreateLeiFeng(self):
        leifeng=Volunteer()
        return leifeng