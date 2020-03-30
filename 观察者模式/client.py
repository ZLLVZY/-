from server import *

huhansan=Boss()

tongshi1=StockObserver('狗子',huhansan)
tongshi2=NBAObserver('村花',huhansan)

huhansan.Attach(tongshi1)
huhansan.Attach(tongshi2)
huhansan.Detach(tongshi1)

huhansan.SubjectState("我胡汉三回来了")
huhansan.Notify()
