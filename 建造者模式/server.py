class PersonBuilder(object):
    """docstring for PersonBuilder"""
    def __init__(self):
        super(PersonBuilder, self).__init__()
        pass

    def BuildHead(self):
        """docstring for BuildHead"""
        pass
        
    def BuildBody(self):
        """docstring for BuildHead"""
        pass

    def BuildArmLeft(self):
        """docstring for BuildHead"""
        pass

    def BuildArmRight(self):
        """docstring for BuildHead"""
        pass

    def BuildLegLeft(self):
        """docstring for BuildHead"""
        pass
    def BuildLegRight(self):
        """docstring for BuildHead"""
        pass

class PersonThinBuilder(PersonBuilder):
    """docstring for PersonThinBuilder"""
    def __init__(self,):
        super(PersonThinBuilder, self).__init__()
        pass

    def BuildHead(self):
        """docstring for BuiledHead"""
        print('thin head')
        
    def BuildBody(self):
        """docstring for BuiledHead"""
        print('thin body')
        
    def BuildArmLeft(self):
        """docstring for BuiledHead"""
        print('thin armleft')
        
    def BuildArmRight(self):
        """docstring for BuiledHead"""
        print('thin armright')
        
    def BuildLegLeft(self):
        """docstring for BuiledHead"""
        print('thin legleft')
        
    def BuildLegRight(self):
        """docstring for BuiledHead"""
        print('thin legright')
        
class PersonFatBuilder(PersonBuilder):
    """docstring for PersonThinBuilder"""
    def __init__(self,):
        super(PersonFatBuilder, self).__init__()
        pass

    def BuildHead(self):
        """docstring for BuiledHead"""
        print('fat head')
        
    def BuildBody(self):
        """docstring for BuiledHead"""
        print('fat body')
        
    def BuildArmLeft(self):
        """docstring for BuiledHead"""
        print('fat armleft')
        
    def BuildArmRight(self):
        """docstring for BuiledHead"""
        print('fat armright')
        
    def BuildLegLeft(self):
        """docstring for BuiledHead"""
        print('fat legleft')
        
    def BuildLegRight(self):
        """docstring for BuiledHead"""
        print('fat legright')
        
class PersonDirector(object):
    """docstring for PersonDirector"""
    def __init__(self, pb):
        super(PersonDirector, self).__init__()
        self.pb = pb
    
    def CreatePerson(self):
        """docstring for CreatePerson"""
        self.pb.BuildHead()
        self.pb.BuildBody()
        self.pb.BuildArmLeft()
        self.pb.BuildArmRight()
        self.pb.BuildLegLeft()
        self.pb.BuildLegRight()
