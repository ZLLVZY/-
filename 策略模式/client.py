import server as s
money=input('请输入总额:')
typelx=input('请输入收费模式:')
#cs=s.CashFactory().createCashAccept(typelx)
#result=cs.acceptCash(float(money))

cs=s.CashContext(typelx)
result=cs.GetResult(float(money))
print(result)
