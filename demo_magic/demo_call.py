# __call__
# 所有的函数都是可调用对象。
# 一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
# 单看 p() 你无法确定 p 是一个函数还是一个类实例，所以，在Python中，函数也是对象，对象和函数的区别并不显著。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('My name is {}'.format(self.name))
        print('My age is {}'.format(self.age))

    def __call__(self, year):
        print('My birthday is {}'.format(year))

p = Person('ske', '20')     # My name is ske    My age is 20
p(2017)                     # My birthday is 2017