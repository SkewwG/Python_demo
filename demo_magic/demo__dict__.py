# __dict__
# 类和实例对象(实际上，Python中一切都是对象，类是type的实例)都有__dict__属性，里面存放它们的自定义属性

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        print('func1')

p = Person('ske', 22)
print(p.__dict__)               # {'age': 22, 'name': 'ske'}