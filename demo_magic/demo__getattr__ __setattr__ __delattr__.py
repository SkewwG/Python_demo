# __getattr__ __setattr__ __delattr__
# __getattr__   当用户访问一个不存在的属性时调用
# __setattr__   设置属性时调用
# __delattr__   删除一个属性时调用
class Person:
    def __init__(self):
        self.name = 'ske'

    def __getattr__(self, item):
        print('__getattr__() called')
        return '__getattr__ item={}'.format(item)

    def __setattr__(self, key, value):
        print('__setattr__() called. key={}, value={}'.format(key, value))
        return object.__setattr__(self, key, value)     # 一定要return object.__setattr__(self, key, value)，否则不会成功赋值

    def __delattr__(self, item):
        print('__delete__() called. item={}'.format(item))
        return object.__delattr__(self, item)

p = Person()            # __setattr__() called. key=name, value=ske
print(p.name)           # ske                                               先从__dict__里面取寻找，找到了就不调用__getattr__
print(p.age)            # __getattr__() called      __getattr__ item=age    如果从__dict__找不到，则调用__getattr__
p.name = 'admin'        # __setattr__() called. key=name, value=admin
del p.name              # __delete__() called. item=name