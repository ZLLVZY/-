from server import *
f=WebSiteFactory()

fx=f.GetWebSiteCategory("产品展示")
fx.Use(User("小菜"))
fy=f.GetWebSiteCategory("产品展示")
fy.Use(User("大鸟"))
fz=f.GetWebSiteCategory("产品展示")
fz.Use(User("狗子"))
fl=f.GetWebSiteCategory("博客")
fl.Use(User("time"))
fm=f.GetWebSiteCategory("博客")
fm.Use(User("zy"))
fn=f.GetWebSiteCategory("博客")
fn.Use(User("zl"))

f.GetWebSiteCount()