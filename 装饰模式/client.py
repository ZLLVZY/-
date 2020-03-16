import server as s
xc=s.Person('ZL')
dtx=s.Tshirts()
dpx=s.Shoes()
dtx.Decorate(xc)
dpx.Decorate(dtx)
dpx.show()