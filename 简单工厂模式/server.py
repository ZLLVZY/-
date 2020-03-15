class Operation(object):
    def __init__(self):
        pass
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def GetResult(self):
        result =self.NumberA+self.NumberB
        return result

class OperationSub(Operation):
    def GetResult(self):
        result =self.NumberA-self.NumberB
        return result

class OperationMul(Operation):
    def GetResult(self):
        result =self.NumberA*self.NumberB
        return result

class OperationDiv(Operation):
    def GetResult(self):
        try:
            result =self.NumberA/self.NumberB
            return result
        except:
            print('请输入正确的数字')

class OperationFactory(object):
    def __init__(self):
        operation={}
        operation['+']=OperationAdd()
        operation['-']=OperationSub()
        operation['*']=OperationMul()
        operation['/']=OperationDiv()
        self.operation=operation
    def createOperation(self,operate):
        oper=self.operation[operate]
        return oper
