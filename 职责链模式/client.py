from server import *

jinli=CommonManager('经理')
zongjian=Majordomo('总监')
zongjingli=GeneralManager('总经理')
jinli.SetSuperior(zongjian)
zongjian.SetSuperior(zongjingli)

request=Request()
request.RequestType("请假")
request.RequestContent("小菜请假")
request.Number(1)
jinli.RequestApplication(request)

request2=Request()
request2.RequestType("请假")
request2.RequestContent("小菜请假")
request2.Number(4)
jinli.RequestApplication(request2)

request3=Request()
request3.RequestType("加薪")
request3.RequestContent("小菜请求加薪")
request3.Number(500)
jinli.RequestApplication(request3)

request4=Request()
request4.RequestType("加薪")
request4.RequestContent("小菜请求加薪")
request4.Number(1000)
jinli.RequestApplication(request4)