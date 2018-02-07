#类的魔法方法  运算符
'''
    比较运算符

        __cmp__(self,other)     比较
        __eq__(self,other)      等于
        __lt__(self,other)      小于
        __gt__(self,other)      大于

    数字运算符

        __add__(self,other)     加
        __sub__(self,other)     减
        __mul__(self,other)     乘
        __div__(self,other)     除

    逻辑运算符

        __or__(self,other)      或
        __and__(self,other)     与
'''


class demo_Class():
    def __init__(self,name,age):
        if isinstance(age,int):
            self.age = age
        else:
            print('age must be int!')

    def __eq__(self,other):
        if isinstance(other,demo_Class):
            return True if self.age == other.age else False

    def __add__(self,other):
        if isinstance(other,demo_Class):
            return self.age + other.age

A = demo_Class('demo1',25)
B = demo_Class('demo2',30)
print(A+B)
print(A==B)