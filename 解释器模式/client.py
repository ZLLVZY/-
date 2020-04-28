from server import *
context=PlayContext()
print("上海滩：")
context.text="T 500 O 2 E 0.5 G 0.5 A 3 E 0.5 G 0.5 D 3 E 0.5 G 0.5 A 0.5 O 3 C 1 O 2 A 0.5 G 1 C 0.5 E 0.5 D 3"
context.text=context.text.split(' ')
while(len(context.text)>0):
    l=context.text[0]
    #print(l)
    if l=="O":
        expression=Scale()
    elif l in "CDEFGABP":
        expression=Note()
    elif l=="T":
        expression=Speed()
    else:
        print("输入错误")
    expression.Interpret(context)
    