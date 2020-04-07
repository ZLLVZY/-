import toml
path='/mnt/d/Design-pattern/抽象工厂模式/'
config='appconfig.toml'

class User(object):
    def __init__(self):
        pass

class Department(object):
    def __init__(self):
        pass

class IUser(object):
    def __init__(self):
        pass
    def Insert(self,user):
        pass
    def GetUser(self,id):
        pass

class IDepartment(object):
    def __init__(self):
        pass
    def Insert(self,department):
        pass
    def GetUser(self,id):
        pass

class SqlserverUser(IUser):
    def Insert(self,user):
        print("在SQL Server中给User表增加一条记录")
    def GetUser(self,id):
        print("在SQL Server中根据ID得到User表一条记录")
        return None

class AccessUser(IUser):
    def Insert(self,user):
        print("在Access中给User表增加一条记录")
    def GetUser(self,id):
        print("在Access中根据ID得到User表一条记录")
        return None

class SqlserverDepartment(IDepartment):
    def Insert(self,user):
        print("在SQL Server中给Department表增加一条记录")
    def GetUser(self,id):
        print("在SQL Server中根据ID得到Department表一条记录")
        return None

class AccessDepartment(IDepartment):
    def Insert(self,user):
        print("在Access中给Department表增加一条记录")
    def GetUser(self,id):
        print("在Access中根据ID得到Department表一条记录")
        return None

'''
class IFactory(object):
    def __init__(self):
        pass
    def CreateUser(self):
        pass
    def CreateDepartment(self):
        pass

class SqlserverFactory(IFactory):
    def CreateUser(self):
        return SqlserverUser()
    def CreateDepartment(self):
        return SqlserverDepartment()

class AccessFactory(IFactory):
    def CreateUser(self):
        return AccessUser()    
    def CreateDepartment(self):
        return AccessDepartment()
'''

class DataAccess(object):
    def __init__(self):
        #self.db='Sqlserver'
        self.db=toml.load(path+config)['database']['db']
    def CreatUser(self):
        return globals()[self.db+'User']()
    def CreateDepartment(self):
        return globals()[self.db+'Department']()
