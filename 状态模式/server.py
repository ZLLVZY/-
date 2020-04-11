class State(object):
    """docstring for State"""
    def __init__(self):
        pass
    def WriteProgram(self,w):
        pass

class ForenoonState(State):
    def __init__(self):
        pass
    def WriteProgram(self,w):
        if (w.Hour<12):
            print("当前时间：%s点 上午工作，精神百倍" % w.Hour)
        else:
            w.SetState(NoonState())
            w.WriteProgram()
class NoonState(State):
    def __init__(self):
        pass
    def WriteProgram(self,w):
        if (w.Hour<13):
            print("当前时间：%s点 饿了，午饭；犯困；午休" % w.Hour)
        else:
            w.SetState(AfternoonState())
            w.WriteProgram()
class AfternoonState(State):
    def __init__(self):
        pass
    def WriteProgram(self,w):
        if (w.Hour<17):
            print("当前时间：%s点 下午状态还不错，继续努力" % w.Hour)
        else:
            w.SetState(EveningState())
            w.WriteProgram()
class EveningState(State):
    def __init__(self):
        pass
    def WriteProgram(self,w):
        if (w.finish):
            w.SetState(RestState())
            w.WriteProgram()
        else:
            if (w.Hour<21):
                print("当前时间：%s点 加班哦，疲累之极" % w.Hour)
            else:
                w.SetState(SleepingState())
                w.WriteProgram()
class SleepingState(State):
    def __init__(self):
        pass
    def WriteProgram(self,w):
        print("当前时间：%s点 不行了,睡着了。" % w.Hour)
class RestState(State):
    def __init__(self):
        pass
    def WriteProgram(self,w):
        print("当前时间：%s点 下班回家了。" % w.Hour)

class Work(object):
    """docstring for Work"""
    def __init__(self):
        self.current=ForenoonState()
        self.Hour=None
        self.finish=False
    def TaskFinished(self,finish):
        self.finish=finish
        return self.finish
    def SetState(self,s):
        self.current=s
    def WriteProgram(self):
        self.current.WriteProgram(self)
