from server import *
'''boy=Barbecuer()
boy.BakeMutton()
boy.BakeMutton()
boy.BakeMutton()
boy.BakeChickenWing()
boy.BakeMutton()
boy.BakeMutton()
boy.BakeChickenWing()'''

#开店前的准备
boy=Barbecuer()
BakeMuttonCommand1=BakeMuttonCommand(boy)
BakeMuttonCommand2=BakeMuttonCommand(boy)
BakeChickenWingCommand1=BakeChickenWingCommand(boy)
girl=Waiter()

#开门营业
girl.SetOrder(BakeMuttonCommand1)
girl.SetOrder(BakeMuttonCommand2)
girl.SetOrder(BakeChickenWingCommand1)
girl.CancelOrder(BakeMuttonCommand1)
girl.Notify()