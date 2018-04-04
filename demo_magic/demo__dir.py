# 定义对类的实例调用 dir() 时的行为，这个方法应该向调用者返回一个属性列表
# dir()函数会自动寻找一个对象的所有属性，包括__dict__中的属性。

class Person1:
    pass

p1 = Person1()
print(dir(p1))                  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


class Person2:
    def __dir__(self):
        return [1, 2, 3]

p2 = Person2()
print(dir(p2))                  # [1, 2, 3]
