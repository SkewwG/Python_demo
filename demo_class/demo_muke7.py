#类的魔法方法
'''
    转换为字符串

        __str__(self)           转换给人看
        __repr__(self)          转换给电脑看
        __unicode__(self)

    展现对象属性

        __dir__                 展现属性

'''

class demo_Class():
    def __init__(self,name,age):
        self.name = name
        if isinstance(age,int):
            self.age = age
        else:
            print('age must be int!')

    def __str__(self):
        return '{0} is {1} years old'.format(self.name,self.age)

    def __dir__(self):
        return self.__dict__.keys()                                                 #self.__dict.keys()获取构造函数里的属性

A = demo_Class('demo1',25)
B = demo_Class('demo2',30)
print(A)                                                                            #自动调用了__str__
print(dir(A))                                                                       #__dir__被重写了。所以返回的是构造函数里的属性