#装饰器


class Program():
    hobby = 'Play program'

    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        return 'My name is {0},I am {1} years old!'.format(self.name,self._age)

p = Program('admin','18','96')
print('p的所有属性:{0}'.format(dir(p)))                                                                       #打印p的所有属性
print('类方法Program.get_hobby()：{0}'.format(Program.get_hobby()))                                           #类方法
print('类的方法变为对象的属性p.get_weight:{0}'.format(p.get_weight))                                             #方法转变为属性
print('正常的方法:{0}'.format(p.self_introduction()))                                                          #put的方法


