from server import *
ptb=PersonThinBuilder()
pdThin=PersonDirector(ptb)
pdThin.CreatePerson()

pfb=PersonFatBuilder()
pdFat=PersonDirector(pfb)
pdFat.CreatePerson()
