# __get__  如果class定义了它，则这个class就可以称为descriptor
# descriptor作为其他类的属性身份出现的时候，会调用descriptor的__get__
# descriptor实例作为函数调用的时候，触发__call__
class Person:
    def __get__(self, instance, owner):
        print("__get__() is called", instance, owner)
        return '__get__()'

    def __call__(self, *args, **kwargs):
        print("__call__() is called")
        return '__call__()'

class Teacher:
    t = Person()

pt = Teacher()
print(pt.t)                 # __get__() is called <__main__.Teacher object at 0x0000000005AEE4E0> <class '__main__.Teacher'>    __get__()
print(Person()())           # __call__() is called      __call__()
