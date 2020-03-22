class TestPaper(object):
    """docstring for TestPaper"""
    def __init__(self):
        super(TestPaper, self).__init__()
        pass

    def TestQuestion1(self):
        """docstring for TestQuestion1"""
        print('杨过得到后来给了郭靖,炼成倚天剑、屠龙刀的玄铁可能是[ ]\
                a.球磨铸铁 b.马口铁 c.高速合金钢 d.碳素纤维')
        print('答案:'+self.Answer1())

    def Answer1(self):
        """docstring for Answer1"""
        pass
   
    def TestQuestion2(self):
        """docstring for TestQuestion1"""
        print('杨过、程英、陆无双铲除了情花造成[ ]\
                a.使这种植物不再害人 b.使一种珍惜物种灭绝 c.破坏了那个生物圈的生态平衡 d.造成了该地区沙漠化')
        print('答案:'+self.Answer2())

    def Answer2(self):
        """docstring for Answer1"""
        pass
    
    def TestQuestion3(self):
        """docstring for TestQuestion1"""
        print('蓝凤凰致使华山师徒、桃谷六仙呕吐不止如果你是大夫，会给他们开什么药[ ]\
                a.阿斯匹林 b.牛黄解毒片 c.氟哌酸 d.让他们喝大量的生牛奶 e.以上全不对')
        print('答案:'+self.Answer3())

    def Answer3(self):
        """docstring for Answer1"""
        pass

class TestPaperA(TestPaper):
    """docstring for TestPaperA"""
    def __init__(self):
        super(TestPaperA, self).__init__()
        pass
    def Answer1(self):
        return  'a'
    def Answer2(self):
        return  'b'
    def Answer3(self):
        return  'c'
class TestPaperB(TestPaper):
    """docstring for TestPaperA"""
    def __init__(self):
        super(TestPaperB, self).__init__()
        pass
    def Answer1(self):
        return  'b'
    def Answer2(self):
        return  'b'
    def Answer3(self):
        return  'c'
class TestPaperC(TestPaper):
    """docstring for TestPaperA"""
    def __init__(self):
        super(TestPaperC, self).__init__()
        pass
    def Answer1(self):
        return  'c'
    def Answer2(self):
        return  'b'
    def Answer3(self):
        return  'c'
