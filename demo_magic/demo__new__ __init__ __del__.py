# __new__ 是对象实例化时第一个调用的方法，它只取下 cls 参数，并把其他参数传给 __init__ 。
# __new__(cls,arg)是对象实例化的时候调用的第一个方法
# __init__(self)是实例化对象的时候调用的第一个方法
# __del__ 是对象的销毁器

class Person:
    def __new__(cls, *args, **kwargs):
        print("__new__() is called")
        return object.__new__(cls)

    def __init__(self):
        print("__init__() is called")

    def __del__(self):
        print("__del__() is called")

p = Person()        # __new__() is called       __init__() is called        __del__() is called


