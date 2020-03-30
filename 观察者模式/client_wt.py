from server_wt import *

huhansan=Boss()

tongshi1=StockObserver('狗子',huhansan)
tongshi2=NBAObserver('村花',huhansan)

huhansan.Event(tongshi1.CloseStockMarket)
huhansan.Event(tongshi2.CloseNBADirectSeeding)

huhansan.SubjectState("我胡汉三回来了")
huhansan.Notify()
