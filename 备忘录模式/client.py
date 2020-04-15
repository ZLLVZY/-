from server import *
lixiaoyao=GameRole()
lixiaoyao.GetInitState()
lixiaoyao.StateDisplay()

stateAdmin=RoleStateCaretaker()
stateAdmin.Memento=lixiaoyao.SaveState()

lixiaoyao.Fight()
lixiaoyao.StateDisplay()

lixiaoyao.RecoveryState(stateAdmin.Memento)
lixiaoyao.StateDisplay()
