import server as s
NumberA=input('请输入数字A:')
operate=input('请输入运算符:')
NumberB=input('请输入数字B:')

oper=s.OperationFactory().createOperation(operate)
oper.NumberA=float(NumberA)
oper.NumberB=float(NumberB)
result=oper.GetResult()
print(str(result))
