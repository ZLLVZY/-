import server as s
import copy
a=s.Resume('ZL')
a.SetPersonalInfo("男","29")
a.SetWorkExperience('1998','cmcc')
b=copy.deepcopy(a)#数值和引用都copy为新的
c=copy.copy(a)#数值copy为新的,引用仍指向原来的引用

'''改变b，只改变b自己的值和引用'''
b.SetPersonalInfo('女',"29")
b.SetWorkExperience('2015','chinanet')
a.dispaly()
b.dispaly()
c.dispaly()

'''改变c,a的值不变,但引用变了'''
c.SetPersonalInfo('女',"29")
c.SetWorkExperience('2016','chinatower')
a.dispaly()
b.dispaly()
c.dispaly()
