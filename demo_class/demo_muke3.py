#继承
class Program():
    hobby = 'Play program'

    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight

class son_Program(Program):
    def __init__(self,name,age,weight,language):
        super(son_Program,self).__init__(name,age,weight)
        self.language = language

p = son_Program('admin','18','96','python')
print('p的所有属性:{0}'.format(dir(p)))                                                                       #打印p的所有属性
print('p的构造函数里的属性：{0}'.format(p.__dict__))                                                            #p的构造函数里的属性
print('p的类型:{0}'.format(type(p)))                                                                         #p的类型
print('son_Program是Program的子类嘛？:{0}'.format(isinstance(p,Program)))                                     #son_Program是Program的子类

