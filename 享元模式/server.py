class User(object):
    def __init__(self,name):
        self.name=name
    def Name(self):
        return self.name

class WebSite(object):
    def __init__(self,name):
        pass
    def Use(self):
        pass

class ConcreteWebSite(WebSite):
    def __init__(self,name):
        self.name=name
    def Use(self,user):
        print("网站分类:"+self.name+",用户:"+user.Name())

class WebSiteFactory(object):
    def __init__(self):
        self.webtype={}
        self.count={}
    def GetWebSiteCategory(self,key):
        if (key not in self.webtype):
            tmp=ConcreteWebSite(key)
            self.webtype[key]=tmp
            self.count[key]=1
        else:
            tmp=self.webtype[key]
            self.count[key]+=1
        return tmp
    def GetWebSiteCount(self):
        for key in self.webtype:
            print('type:%s,count:%d' % (key,self.count[key]))