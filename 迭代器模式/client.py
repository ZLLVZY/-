a=[]
a.append("大鸟")
a.append("小菜")
a.append("行李")
a.append("老外")
a.append("公交内部员工")
a.append("小偷")

for i in a:
    print(i+" 请买车票")

for i in range(len(a)-1,-1,-1):
    print(a[i]+" 请买车票")