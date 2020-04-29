from server import *

o=ObjectStructure()
o.Attach(Man())
o.Attach(Woman())

v1=Success()
o.Display(v1)
v2=Failing()
o.Display(v2)
v3=Amativeness()
o.Display(v3)
v4=Marriage()
o.Display(v4)