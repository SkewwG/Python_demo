#设置对象属性、查询对象属性、删除对象属性
'''
    设置对象属性
        def __setattr__(self,name,value):
            self.__dict__[name] = value                         防止递归

    查询对象属性
        def __getattr__(self,name):                             没有访问name属性时调用

        def __getattribute__(self,name):                        访问name属性时调用

    删除对象属性
        def __delattr(self,name):
'''


class demo_Class():
    def __init__(self,name,age):
        self.name = name
        if isinstance(age,int):
            self.age = age
        else:
            print('age must be int!')

    def __setattr__(self, key, value):
        #setattr(self,key,value)                                                         #错误代码1
        self.__dict__[key] = value                                                     #正确代码

    def __getattribute__(self, item):
        #return getattr(self,item)                                                       #错误代码1
        return self.__dict__[item]                                                     #错误代码2
        #return super(demo_Class,self).__getattribute__(item)                           #正确代码

A = demo_Class('demo','25')
print(A.name)