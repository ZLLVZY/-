class CashSuper(object):
    def __init__(self):
        pass
    def acceptCash(self,money):
        pass

class CashNormal(CashSuper):
    def acceptCash(self,money):
        return money

class CashRebate(CashSuper):
    def __init__(self,moneyRebate=0.8):
        self.moneyRebate=moneyRebate

    def acceptCash(self,money):
        return money*self.moneyRebate

class CashReturn(CashSuper):
    def __init__(self,moneyCondition=300,moneyReturn=100):
        self.moneyCondition=moneyCondition
        self.moneyReturn=moneyReturn
    
    def acceptCash(self,money):
        if (money>=self.moneyCondition):
            result=money-(money/self.moneyCondition)*self.moneyReturn
        return result
    
class CashFactory(object):
    def __init__(self):
        CashAcception={}
        CashAcception['1']=CashNormal()
        CashAcception['2']=CashRebate()
        CashAcception['3']=CashReturn()
        self.CashAcception=CashAcception

    def createCashAccept(self,typelx):
        cs=self.CashAcception[typelx]
        return cs

class CashContext(object):
    def __init__(self,typelx):
        CashAcception={}
        CashAcception['1']=CashNormal()
        CashAcception['2']=CashRebate()
        CashAcception['3']=CashReturn()
        self.cs=CashAcception[typelx]
        
    def GetResult(self,money):
        return self.cs.acceptCash(money)
