from server import *
root=ConcreteCompany("北京总公司")
root.Add(HRDepartment("总公司人力资源部"))
root.Add(FinaceDepartment("总公司财务部"))

comp=ConcreteCompany("上海华东分公司")
comp.Add(HRDepartment("上海华东分公司人力资源部"))
comp.Add(FinaceDepartment("上海华东分公司财务部"))
root.Add(comp)

comp1=ConcreteCompany("南京办事处")
comp1.Add(HRDepartment("南京办事处人力资源部"))
comp1.Add(FinaceDepartment("南京办事处财务部"))
comp.Add(comp1)

comp2=ConcreteCompany("杭州办事处")
comp2.Add(HRDepartment("杭州办事处人力资源部"))
comp2.Add(FinaceDepartment("杭州办事处财务部"))
comp.Add(comp2)

print("结构图:")
root.Display(1)

print("职责:")
root.LineOfDuty()