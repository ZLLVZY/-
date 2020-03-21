class WorkExperience(object):
    """docstring for WorkExperience"""
    def __init__(self):
        super(WorkExperience, self).__init__()
        pass

class Resume(object):
    """docstring for Resume"""
    def __init__(self,name):
        self.name=name
        self.work=WorkExperience()

    def SetPersonalInfo(self,sex,age):
        self.sex=sex
        self.age=age

    def SetWorkExperience(self,timeArea,company):
        """docstring for SetWorkExperience"""
        self.work.workDate=timeArea,
        self.work.company=company

    def dispaly(self):
        """docstring for dispaly"""
        print(self.name+' '+self.sex+' '+self.age)
        print('工作经历: %s %s' % (self.work.workDate,self.work.company))
