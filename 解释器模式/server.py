class PlayContext(object):
    def __init__(self):
        self.text=None

class Expression(object):
    def __init__(self):
        pass
    def Interpret(self,context):
        if len(context.text)==0:
            return None
        else:
            playKey=context.text[0]
            playValue=context.text[1]
            context.text.pop(0)
            context.text.pop(0)
            self.Excute(playKey,playValue)
    def Excute(self,key,value):
        pass

class Note(Expression):
    def Excute(self,key,value):
        tmp={}
        tmp['C']="1"
        tmp['D']="2"
        tmp['E']="3"
        tmp['F']="4"
        tmp['G']="5"
        tmp['A']="6"
        tmp['B']="7"
        print(tmp[key],end='')

class Scale(Expression):
    def Excute(self,key,value):
        tmp={}
        tmp['1']="低音"
        tmp['2']="中音"
        tmp['3']="高音"
        print(tmp[value],end='')

class Speed(Expression):
    def Excute(self,key,value):
        if int(value)<500:
            speed="快速"
        elif int(value)>=1000:
            speed="慢速"
        else:
            speed="中速"
        print(speed,end=' ')