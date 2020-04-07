from server import *

user=User()
dept=Department()
'''
factory=SqlserverFactory()
factory=AccessFactory()
iu=factory.CreateUser()
iu.Insert(user)
iu.GetUser(1)

id=factory.CreateDepartment()
id.Insert(dept)
id.GetUser(1)
'''
iu=DataAccess().CreatUser()
iu.Insert(user)
iu.GetUser(1)
id=DataAccess().CreateDepartment()
id.Insert(dept)
id.GetUser(1)
