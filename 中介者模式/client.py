from server import *
UNSC=UnitedNationsSecurityCouncil()
c1=USA(UNSC)
c2=Iraq(UNSC)
UNSC.colleague1=c1
UNSC.colleague2=c2

c1.Declare("不准研制核武器，否则要发动战争!")
c2.Declare("我们没有核武器，也不怕侵略。")