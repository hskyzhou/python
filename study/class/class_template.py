class AClass:
    """定义一个A类"""
    def __init__(self):
        """
        定义一个初始化方法
        双下划线代表的是python中特有的方法
        """
        self.class_name = "A"
    def __showName(self):
        """
        定义一个私有方法
        但下划线代表的是私有方法
        """
        print self.class_name
        
    def sun(self):
        """
        定义一般的方法
        """
        print "this is a simple function"
        
class BClass(Aclass):
    """
    定义一个B类，继承自A类
    """
    def __init__(self):
        """
        定义初始化方法，相当于java中的构造方法
        """

    