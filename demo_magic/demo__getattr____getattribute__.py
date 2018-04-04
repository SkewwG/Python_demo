# 1、如果同时定义了__getattr__ 和 __getattribute__，
#     1.1、但__getattribute__没有显示调用。如没有这句话：return object.__getattribute__(self, name)
#         那么无论属性存在还是不存在，都只调用__getattribute__而不调用__getattr__
#     1.2、但如果__getattribute__显示调用。如： return object.__getattribute__(self, name)
#         1.2.1 属性存在，就只调用__getattribute__
#         1.2.2 属性不存在 先调用__getattribute__，接着调用__getattr__
# 总结：
# __getattribute__    访问存在的属性时调用
# __getattr__         访问不存在的属性时调用
class Person:
    name = 'ske'

    def __getattribute__(self, name):
        print("__getattribute__() is called")
        return object.__getattribute__(self, name)  # 显示调用

    def __getattr__(self, name):
        print("__getattr__() is called")
        return name + ' from __getattr__()'

p = Person()
print(p.name)           # __getattribute__() is called   ske
print(p.age)            # __getattribute__() is called   __getattr__() is called    age from __getattr__()

class Teacher:
    name = 'ske'

    def __getattribute__(self, name):
        print("__getattribute__() is called")
        # return object.__getattribute__(self, name)  # 显示调用

    def __getattr__(self, name):
        print("__getattr__() is called")
        return name + ' from __getattr__()'

t = Teacher()
print(t.name)           # __getattribute__() is called   None
print(t.age)            # __getattribute__() is called   None
