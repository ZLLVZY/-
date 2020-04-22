from server import *
ab=HandsetBrandN()
ab.SetHandsetSoft(HandsetGame())
ab.Run()

ab.SetHandsetSoft(HandsetAddressList())
ab.Run()

ab=HandsetBrandM()
ab.SetHandsetSoft(HandsetGame())
ab.Run()

ab.SetHandsetSoft(HandsetAddressList())
ab.Run()
