#公有、私有、部分私有属性
class Program():
    hobby = 'Play program'

    def __init__(self,name,age,weight):         #name，age，weight是类的属性
        self.name = name                        #公有属性       编程规范的约束，而不是python的语法约束
        self._age = age                         #私有属性       编程规范的约束，而不是python的语法约束
        self.__weight = weight                  #部分私有属性     在类里面可以访问该属性，但是生成的对象不能访问该属性          编程规范的约束，而不是python的语法约束

    def get_weight(self):
        return self.__weight


p = Program('admin','18','96')

print('p的所有属性:{0}'.format(dir(p)))                                                   #打印p的所有属性
print('p的构造函数里的属性:{0}'.format(p.__dict__))                                        #打印p的构造函数里的属性
print('对象的公有属性和私有属性:name={0};age={1}'.format(p.name,p._age))                    #公有和私有属性都可以打印
print('部分私有属性的变量名已经发生改变：{0}'.format(p._Program__weight))                     #部分私有属性的变量名则变成了_Program__weight
print('调用方法：{0}'.format(p.get_weight()))
