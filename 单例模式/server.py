def singleton(cls,*args,**kw):
    isinstance={}
    def _singleton():
        if cls not in isinstance:
            isinstance[cls]=cls(*args,**kw)
        return isinstance[cls]
    return _singleton

@singleton
class Myclass(object):
    def __init__(slef):
        pass
